# Customer Accounts Microservice

[![CI Build](https://github.com/PruthviChaudharii/customer-accounts/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/PruthviChaudharii/customer-accounts/actions/workflows/ci-build.yaml)

Customer Accounts capstone for the IBM DevOps and Software Engineering course.
Maintainer: PruthviChaudharii.

Based on the [official IBM starter template](https://github.com/ibm-developer-skills-network/aolwx-devops-capstone-template),
with the original Apache 2.0 license and attribution preserved.

## Run with Docker

```sh
docker compose up --build -d
curl http://localhost:8080/
curl http://localhost:8080/health
```

PostgreSQL persists in the `accounts-data` volume. Compose credentials are local development defaults.
For an external deployment, supply database credentials through your secret manager.

## REST API

| Method | Endpoint | Result |
| --- | --- | --- |
| POST | /accounts | Create; 201 with Location header |
| GET | /accounts | List; 200, optional `?name=` filter |
| GET | /accounts/{id} | Read; 200 or 404 |
| PUT | /accounts/{id} | Replace; 200 or 404 |
| DELETE | /accounts/{id} | Delete; 204, idempotent |
| GET | /health | Health; 200 |

Account fields: integer `id` (server assigned), required strings `name`, `email`,
`address`, optional `phone_number`, and ISO `date_joined` (defaults to today's date).
JSON request bodies are validated; malformed data returns 400 and unsupported media returns 415.

## Development and tests

Use Python 3.11. Set `DATABASE_URI` to a disposable PostgreSQL database before importing the service.
Tests clear account data in this database.

```sh
python -m venv .venv
# Activate .venv for your shell
pip install -r requirements-dev.txt
export DATABASE_URI=postgresql://postgres:postgres@localhost:5432/accounts_test
flake8 service tests
pylint service --fail-under=9
nosetests
```

`pynose` provides the maintained `nosetests` command on modern Python. The suite enforces
at least 95% service coverage. GitHub Actions performs checkout, dependency installation,
lint, nosetests, and Docker build against PostgreSQL.

## Security

Flask-Talisman sets CSP, frame, and content-type security headers. Set `FORCE_HTTPS=true`
when using HTTPS; local HTTP is supported by default. `CORS_ORIGINS` is a comma-separated
allowlist, defaulting to `http://localhost:8080`. The runtime container runs as UID 10001.

## Kubernetes and Tekton

See [deployment instructions](docs/deployment.md). The manifests are configuration;
successful deployment and pipeline logs must be collected from a real cluster.

## Submission evidence

See [submission guide](docs/submission.md). Only evidence collected from actual runs is
included in `evidence/`. Planning screenshots must come from the real GitHub project board.

## Original template author

John Rofrano, IBM Research, instructor for the IBM DevOps course.
