"""
Account API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from tests.factories import AccountFactory
from service.common import status  # HTTP Status Codes
from service.models import db, Account, init_db
from service.routes import app

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

BASE_URL = "/accounts"


######################################################################
#  T E S T   C A S E S
######################################################################
class TestAccountService(TestCase):
    """Account Service Tests"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db(app)

    @classmethod
    def tearDownClass(cls):
        """Runs once before test suite"""

    def setUp(self):
        """Runs before each test"""
        db.session.query(Account).delete()  # clean up the last tests
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Runs once after each test case"""
        db.session.remove()

    ######################################################################
    #  H E L P E R   M E T H O D S
    ######################################################################

    def _create_accounts(self, count):
        """Factory method to create accounts in bulk"""
        accounts = []
        for _ in range(count):
            account = AccountFactory()
            response = self.client.post(BASE_URL, json=account.serialize())
            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED,
                "Could not create test Account",
            )
            new_account = response.get_json()
            account.id = new_account["id"]
            accounts.append(account)
        return accounts

    ######################################################################
    #  A C C O U N T   T E S T   C A S E S
    ######################################################################

    def test_index(self):
        """It should get 200_OK from the Home Page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health(self):
        """It should be healthy"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")

    def test_create_account(self):
        """It should Create a new Account"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Make sure location header is set
        location = response.headers.get("Location", None)
        self.assertIsNotNone(location)

        # Check the data is correct
        new_account = response.get_json()
        self.assertEqual(new_account["name"], account.name)
        self.assertEqual(new_account["email"], account.email)
        self.assertEqual(new_account["address"], account.address)
        self.assertEqual(new_account["phone_number"], account.phone_number)
        self.assertEqual(new_account["date_joined"], str(account.date_joined))

    def test_bad_request(self):
        """It should not Create an Account when sending the wrong data"""
        response = self.client.post(BASE_URL, json={"name": "not enough data"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsupported_media_type(self):
        """It should not Create an Account when sending the wrong media type"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="test/html"
        )
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    def test_list_accounts(self):
        """It should list all accounts and return an empty list when absent."""
        self.assertEqual(self.client.get(BASE_URL).get_json(), [])
        self._create_accounts(3)
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 3)

    def test_filter_accounts(self):
        """It should filter accounts by name."""
        account = self._create_accounts(1)[0]
        response = self.client.get(BASE_URL, query_string={"name": account.name})
        self.assertEqual(len(response.get_json()), 1)
        self.assertEqual(response.get_json()[0]["id"], account.id)
        self.assertEqual(self.client.get(BASE_URL, query_string={"name": "missing"}).get_json(), [])

    def test_read_account(self):
        """It should read a created account using its Location header."""
        data = AccountFactory().serialize()
        created = self.client.post(BASE_URL, json=data)
        response = self.client.get(created.headers["Location"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), created.get_json())

    def test_read_missing(self):
        """It should return 404 when an account is absent."""
        self.assertEqual(self.client.get(f"{BASE_URL}/99999").status_code, 404)

    def test_update_account(self):
        """It should update an account and preserve its identifier."""
        account = self._create_accounts(1)[0]
        data = account.serialize()
        data.update(name="Updated Customer", id=99999)
        response = self.client.put(f"{BASE_URL}/{account.id}", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], account.id)
        self.assertEqual(self.client.get(f"{BASE_URL}/{account.id}").get_json()["name"], "Updated Customer")

    def test_update_missing(self):
        """It should return 404 when replacing an absent account."""
        response = self.client.put(f"{BASE_URL}/99999", json=AccountFactory().serialize())
        self.assertEqual(response.status_code, 404)

    def test_update_bad_data(self):
        """It should reject incomplete updates and leave stored data unchanged."""
        account = self._create_accounts(1)[0]
        response = self.client.put(f"{BASE_URL}/{account.id}", json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.get(f"{BASE_URL}/{account.id}").get_json()["name"], account.name)

    def test_delete_account(self):
        """It should delete an account and allow repeated deletion."""
        account = self._create_accounts(1)[0]
        url = f"{BASE_URL}/{account.id}"
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)
        self.assertEqual(self.client.delete(url).status_code, 204)

    def test_optional_fields(self):
        """It should default the join date and allow a missing phone."""
        data = {"name": "Customer", "email": "customer@example.com", "address": "123 Example Street"}
        response = self.client.post(BASE_URL, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIsNone(response.get_json()["phone_number"])
        self.assertIsNotNone(response.get_json()["date_joined"])

    def test_invalid_values(self):
        """It should reject invalid types, lengths, dates and JSON shapes."""
        for invalid in ({"name": ""}, {"email": None}, {"address": "x" * 257},
                        {"phone_number": 42}, {"date_joined": "not-a-date"}):
            data = AccountFactory().serialize()
            data.update(invalid)
            self.assertEqual(self.client.post(BASE_URL, json=data).status_code, 400)
        for data in ([], "text", 42):
            self.assertEqual(self.client.post(BASE_URL, json=data).status_code, 400)

    def test_security_headers(self):
        """It should set Talisman security headers."""
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(response.headers["X-Frame-Options"], "SAMEORIGIN")
        self.assertIn("default-src", response.headers["Content-Security-Policy"])
        secure = self.client.get("/", base_url="https://localhost")
        self.assertIn("max-age", secure.headers["Strict-Transport-Security"])

    def test_cors_allowlist(self):
        """It should allow configured origins and reject other origins."""
        allowed = self.client.get(BASE_URL, headers={"Origin": "http://localhost:8080"})
        self.assertEqual(allowed.headers["Access-Control-Allow-Origin"], "http://localhost:8080")
        denied = self.client.get(BASE_URL, headers={"Origin": "https://untrusted.example"})
        self.assertNotIn("Access-Control-Allow-Origin", denied.headers)
        preflight = self.client.options(BASE_URL, headers={
            "Origin": "http://localhost:8080", "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "Content-Type",
        })
        self.assertEqual(preflight.status_code, 200)
        self.assertIn("POST", preflight.headers["Access-Control-Allow-Methods"])

    def test_method_not_allowed(self):
        """It should respond with a JSON 405 for unsupported methods."""
        response = self.client.patch(BASE_URL, json={})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.get_json()["status"], 405)

    def test_malformed_json(self):
        """It should reject malformed JSON."""
        response = self.client.post(BASE_URL, data="{bad", content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_internal_error_handler(self):
        """It should return a structured response for an internal error."""
        from service.common.error_handlers import internal_server_error
        with app.app_context():
            response, code = internal_server_error("test failure")
            self.assertEqual(code, 500)
            self.assertEqual(response.get_json()["error"], "Internal Server Error")
