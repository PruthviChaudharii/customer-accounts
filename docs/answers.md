# Submission answers and evidence

Links below are real repository file URLs. Paste actual contents of the named evidence files for text questions.
Missing screenshots, deployment results, and pipeline logs are pending; do not submit placeholders.

| Question | Answer or evidence |
| --- | --- |
| 1 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/README.md |
| 2 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/user-story.md |
| 3 | PENDING: capture actual GitHub board as `planning-userstories-done.png` |
| 4 | PENDING: capture actual GitHub board as `planning-productbacklog-done.png` |
| 5 | PENDING: capture actual GitHub board as `planning-labels-done.png` |
| 6 | PENDING: capture actual GitHub board as `planning-kanban-done.png` |
| 7 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/setup.cfg |
| 8 | PENDING: capture actual GitHub board as `rest-techdebt-done.png` |
| 9 | PENDING: capture actual GitHub board as `read-accounts.png` |
| 10 | PENDING: capture actual GitHub board as `list-accounts.png` |
| 11 | PENDING: capture actual GitHub board as `update-accounts.png` |
| 12 | PENDING: capture actual GitHub board as `delete-accounts.png` |
| 13 | Paste `evidence/rest-create-done` |
| 14 | Paste `evidence/rest-list-done` |
| 15 | Paste `evidence/rest-read-done` |
| 16 | Paste `evidence/rest-update-done` |
| 17 | Paste `evidence/rest-delete-done` |
| 18 | PENDING: capture actual GitHub board as `sprint2-plan.png` |
| 19 | Paste `evidence/ci-workflow-done` |
| 20 | PENDING: capture actual GitHub board as `ci-kanban-done.png` |
| 21 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/.github/workflows/ci-build.yaml |
| 22 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/service/__init__.py |
| 23 | Paste `evidence/security-headers-done` |
| 24 | PENDING: capture actual GitHub board as `security-kanban-done.png` |
| 25 | PENDING: capture actual GitHub board as `sprint3-plan.png` |
| 26 | PENDING: collect actual `kube-app-output` |
| 27 | PENDING: capture actual GitHub board as `kube-docker-done.png` |
| 28 | PENDING: capture actual GitHub board as `kube-kubernetes-done.png` |
| 29 | https://github.com/PruthviChaudharii/customer-accounts/blob/main/Dockerfile |
| 30 | Paste `evidence/kube-images` |
| 31 | PENDING: collect actual `kube-deploy-accounts` |
| 32 | PENDING: collect actual `pipelinerun.txt` |
| 33 | PENDING: capture actual GitHub board as `cd-pipeline-done.png` |

The output in `docker-app-output` is from local Docker and is not proof of Kubernetes deployment.
CI passed: https://github.com/PruthviChaudharii/customer-accounts/actions/runs/40069532939
GitHub Projects access needs the `project` scope; the current CLI token lacks it.


# Text answers ready to paste


## Question 13

```text

curl.exe --silent --show-error --include -X POST http://localhost:8080/accounts -H "Content-Type: application/json" --data-binary @evidence/create-account.json

HTTP/1.1 201 CREATED
Server: gunicorn
Date: Sat, 24 Oct 2026 06:16:11 GMT
Connection: close
Content-Type: application/json
Content-Length: 156
Location: http://localhost:8080/accounts/1
Access-Control-Allow-Origin: http://localhost:8080
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; object-src 'none'
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Example Street","date_joined":"2026-10-24","email":"pruthvi.demo@example.com","id":1,"name":"Pruthvi Demo","phone_number":"+91-9000000000"}


```


## Question 14

```text

curl.exe --silent --show-error --include http://localhost:8080/accounts

HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 24 Oct 2026 06:16:11 GMT
Connection: close
Content-Type: application/json
Content-Length: 158
Access-Control-Allow-Origin: http://localhost:8080
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; object-src 'none'
Referrer-Policy: strict-origin-when-cross-origin

[{"address":"123 Example Street","date_joined":"2026-10-24","email":"pruthvi.demo@example.com","id":1,"name":"Pruthvi Demo","phone_number":"+91-9000000000"}]


```


## Question 15

```text

curl.exe --silent --show-error --include http://localhost:8080/accounts/1

HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 24 Oct 2026 06:16:11 GMT
Connection: close
Content-Type: application/json
Content-Length: 156
Access-Control-Allow-Origin: http://localhost:8080
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; object-src 'none'
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Example Street","date_joined":"2026-10-24","email":"pruthvi.demo@example.com","id":1,"name":"Pruthvi Demo","phone_number":"+91-9000000000"}


```


## Question 16

```text

curl.exe --silent --show-error --include -X PUT http://localhost:8080/accounts/1 -H "Content-Type: application/json" --data-binary @evidence/update-account.json

HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 24 Oct 2026 06:16:11 GMT
Connection: close
Content-Type: application/json
Content-Length: 159
Access-Control-Allow-Origin: http://localhost:8080
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; object-src 'none'
Referrer-Policy: strict-origin-when-cross-origin

{"address":"123 Example Street","date_joined":"2026-10-24","email":"pruthvi.demo@example.com","id":1,"name":"Pruthvi Updated","phone_number":"+91-9000000000"}


```


## Question 17

```text

curl.exe --silent --show-error --include -X DELETE http://localhost:8080/accounts/1

HTTP/1.1 204 NO CONTENT
Server: gunicorn
Date: Sat, 24 Oct 2026 06:16:11 GMT
Connection: close
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Origin: http://localhost:8080
Permissions-Policy: browsing-topics=()
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'; object-src 'none'
Referrer-Policy: strict-origin-when-cross-origin


```


## Question 19

```text

test	Set up job	﻿2026-10-24T06:16:15.0407450Z Current runner version: '2.338.0'
test	Set up job	2026-10-24T06:16:15.0423645Z ##[group]Runner Image Provisioner
test	Set up job	2026-10-24T06:16:15.0424216Z Hosted Compute Agent
test	Set up job	2026-10-24T06:16:15.0424559Z Version: 20261021.618
test	Set up job	2026-10-24T06:16:15.0424982Z Commit: 21505ad2541d5be6135ed84fc33697146cf75b8e
test	Set up job	2026-10-24T06:16:15.0425409Z Build Date: 2026-10-21T00:45:21Z
test	Set up job	2026-10-24T06:16:15.0425841Z Worker ID: {10c362fc-49f9-48cd-942b-93ea9e013feb}
test	Set up job	2026-10-24T06:16:15.0426327Z Region: centralus
test	Set up job	2026-10-24T06:16:15.0426652Z Cloud: Azure
test	Set up job	2026-10-24T06:16:15.0427026Z ##[endgroup]
test	Set up job	2026-10-24T06:16:15.0427989Z ##[group]Operating System
test	Set up job	2026-10-24T06:16:15.0428394Z Ubuntu
test	Set up job	2026-10-24T06:16:15.0428752Z 24.04.5
test	Set up job	2026-10-24T06:16:15.0429061Z LTS
test	Set up job	2026-10-24T06:16:15.0429407Z ##[endgroup]
test	Set up job	2026-10-24T06:16:15.0429739Z ##[group]Runner Image
test	Set up job	2026-10-24T06:16:15.0430153Z Image: ubuntu-24.04
test	Set up job	2026-10-24T06:16:15.0430539Z Version: 20261012.334.1
test	Set up job	2026-10-24T06:16:15.0431149Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20261012.334/images/ubuntu/Ubuntu2404-Readme.md
test	Set up job	2026-10-24T06:16:15.0432170Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20261012.334
test	Set up job	2026-10-24T06:16:15.0432779Z ##[endgroup]
test	Set up job	2026-10-24T06:16:15.0433453Z ##[group]GITHUB_TOKEN Permissions
test	Set up job	2026-10-24T06:16:15.0434681Z Contents: read
test	Set up job	2026-10-24T06:16:15.0435037Z Metadata: read
test	Set up job	2026-10-24T06:16:15.0435374Z ##[endgroup]
test	Set up job	2026-10-24T06:16:15.0436674Z Secret source: Actions
test	Set up job	2026-10-24T06:16:15.0437223Z Cache mode: write
test	Set up job	2026-10-24T06:16:15.0438069Z Prepare workflow directory
test	Set up job	2026-10-24T06:16:15.0703399Z Prepare all required actions
test	Set up job	2026-10-24T06:16:15.0736032Z Getting action download info
test	Set up job	2026-10-24T06:16:15.2892364Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
test	Set up job	2026-10-24T06:16:15.4292656Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
test	Set up job	2026-10-24T06:16:15.6312133Z Complete job name: test
test	Initialize containers	﻿2026-10-24T06:16:15.6692022Z ##[group]Checking docker version
test	Initialize containers	2026-10-24T06:16:15.6699942Z ##[command]/usr/bin/docker version --format '{{.Server.APIVersion}}'
test	Initialize containers	2026-10-24T06:16:16.7545158Z '1.48'
test	Initialize containers	2026-10-24T06:16:16.7553863Z Docker daemon API version: '1.48'
test	Initialize containers	2026-10-24T06:16:16.7554824Z ##[command]/usr/bin/docker version --format '{{.Client.APIVersion}}'
test	Initialize containers	2026-10-24T06:16:16.7671373Z '1.48'
test	Initialize containers	2026-10-24T06:16:16.7682838Z Docker client API version: '1.48'
test	Initialize containers	2026-10-24T06:16:16.7686893Z ##[endgroup]
test	Initialize containers	2026-10-24T06:16:16.7688867Z ##[group]Clean up resources from previous jobs
test	Initialize containers	2026-10-24T06:16:16.7692909Z ##[command]/usr/bin/docker ps --all --quiet --no-trunc --filter "label=69ec33"
test	Initialize containers	2026-10-24T06:16:16.7912147Z ##[command]/usr/bin/docker network prune --force --filter "label=69ec33"
test	Initialize containers	2026-10-24T06:16:16.8005088Z ##[endgroup]
test	Initialize containers	2026-10-24T06:16:16.8005863Z ##[group]Create local container network
test	Initialize containers	2026-10-24T06:16:16.8013247Z ##[command]/usr/bin/docker network create --label 69ec33 github_network_d40593f89f804a2680838a0e96681556
test	Initialize containers	2026-10-24T06:16:16.8373860Z e78e0490d93bbdad87c312a78ca419f3ef8fc8a11d50856bdf2ccd0944075dd3
test	Initialize containers	2026-10-24T06:16:16.8387468Z ##[endgroup]
test	Initialize containers	2026-10-24T06:16:16.8406669Z ##[group]Starting postgres service container
test	Initialize containers	2026-10-24T06:16:16.8422004Z ##[command]/usr/bin/docker pull postgres:16-alpine
test	Initialize containers	2026-10-24T06:16:17.4724277Z 16-alpine: Pulling from library/postgres
test	Initialize containers	2026-10-24T06:16:17.6721088Z 7b229517ed22: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6721542Z 768bbab50810: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6721723Z d982e6c592c4: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6722000Z a735dce41235: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6722284Z 42065dcfea93: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6722534Z f121f7f3dec1: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6722800Z 7ea8819886f9: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6723053Z d3f6cab92edc: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6723311Z 911527e7800c: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6723577Z 22df74fd5323: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6723836Z 9f477227db48: Pulling fs layer
test	Initialize containers	2026-10-24T06:16:17.6724210Z a735dce41235: Waiting
test	Initialize containers	2026-10-24T06:16:17.6724914Z 42065dcfea93: Waiting
test	Initialize containers	2026-10-24T06:16:17.6725275Z f121f7f3dec1: Waiting
test	Initialize containers	2026-10-24T06:16:17.6725536Z 7ea8819886f9: Waiting
test	Initialize containers	2026-10-24T06:16:17.6725680Z d3f6cab92edc: Waiting
test	Initialize containers	2026-10-24T06:16:17.6725823Z 22df74fd5323: Waiting
test	Initialize containers	2026-10-24T06:16:17.6725972Z 911527e7800c: Waiting
test	Initialize containers	2026-10-24T06:16:17.6726112Z 9f477227db48: Waiting
test	Initialize containers	2026-10-24T06:16:17.7998318Z 768bbab50810: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:17.7998799Z 768bbab50810: Download complete
test	Initialize containers	2026-10-24T06:16:17.8785174Z d982e6c592c4: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:17.8785909Z d982e6c592c4: Download complete
test	Initialize containers	2026-10-24T06:16:17.9286560Z a735dce41235: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:17.9287135Z a735dce41235: Download complete
test	Initialize containers	2026-10-24T06:16:18.0094253Z 7b229517ed22: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.0094684Z 7b229517ed22: Download complete
test	Initialize containers	2026-10-24T06:16:18.0098022Z 42065dcfea93: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.0098287Z 42065dcfea93: Download complete
test	Initialize containers	2026-10-24T06:16:18.0950834Z 7b229517ed22: Pull complete
test	Initialize containers	2026-10-24T06:16:18.1476874Z 7ea8819886f9: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.1477409Z 7ea8819886f9: Download complete
test	Initialize containers	2026-10-24T06:16:18.1753386Z d3f6cab92edc: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.1753968Z d3f6cab92edc: Download complete
test	Initialize containers	2026-10-24T06:16:18.2209017Z 768bbab50810: Pull complete
test	Initialize containers	2026-10-24T06:16:18.2823996Z 911527e7800c: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.2825199Z 911527e7800c: Download complete
test	Initialize containers	2026-10-24T06:16:18.3296000Z 22df74fd5323: Download complete
test	Initialize containers	2026-10-24T06:16:18.4094713Z 9f477227db48: Download complete
test	Initialize containers	2026-10-24T06:16:18.4111939Z d982e6c592c4: Pull complete
test	Initialize containers	2026-10-24T06:16:18.5149685Z f121f7f3dec1: Verifying Checksum
test	Initialize containers	2026-10-24T06:16:18.5150010Z f121f7f3dec1: Download complete
test	Initialize containers	2026-10-24T06:16:18.8518657Z a735dce41235: Pull complete
test	Initialize containers	2026-10-24T06:16:18.8601379Z 42065dcfea93: Pull complete
test	Initialize containers	2026-10-24T06:16:21.5997852Z f121f7f3dec1: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6100397Z 7ea8819886f9: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6170122Z d3f6cab92edc: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6253327Z 911527e7800c: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6322074Z 22df74fd5323: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6391417Z 9f477227db48: Pull complete
test	Initialize containers	2026-10-24T06:16:21.6424507Z Digest: sha256:f4610795587492cd4fb887c2dc3de301b813278bb6f616992061141b5f15ac36
test	Initialize containers	2026-10-24T06:16:21.6434841Z Status: Downloaded newer image for postgres:16-alpine
test	Initialize containers	2026-10-24T06:16:21.6441179Z docker.io/library/postgres:16-alpine
test	Initialize containers	2026-10-24T06:16:21.6486214Z ##[command]/usr/bin/docker create --name a83b267ba1864d9998aa2c51aa0681ec_postgres16alpine_d28be4 --label 69ec33 --network github_network_d40593f89f804a2680838a0e96681556 --network-alias postgres -p 5432:5432 --health-cmd pg_isready --health-interval 5s --health-timeout 5s --health-retries 10 -e "POSTGRES_USER=postgres" -e "POSTGRES_PASSWORD=postgres" -e "POSTGRES_DB=accounts" -e GITHUB_ACTIONS=true -e CI=true postgres:16-alpine
test	Initialize containers	2026-10-24T06:16:21.6712867Z 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:21.6729532Z ##[command]/usr/bin/docker start 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:22.4203682Z 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:22.4228902Z ##[command]/usr/bin/docker ps --all --filter id=0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd --filter status=running --no-trunc --format "{{.ID}} {{.Status}}"
test	Initialize containers	2026-10-24T06:16:22.4381615Z 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd Up Less than a second (health: starting)
test	Initialize containers	2026-10-24T06:16:22.4399898Z ##[command]/usr/bin/docker port 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:22.4584595Z 5432/tcp -> 0.0.0.0:5432
test	Initialize containers	2026-10-24T06:16:22.4584886Z 5432/tcp -> [::]:5432
test	Initialize containers	2026-10-24T06:16:22.4649570Z ##[endgroup]
test	Initialize containers	2026-10-24T06:16:22.4657212Z ##[group]Waiting for all services to be ready
test	Initialize containers	2026-10-24T06:16:22.4668475Z ##[command]/usr/bin/docker inspect --format="{{if .Config.Healthcheck}}{{print .State.Health.Status}}{{end}}" 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:22.4805239Z starting
test	Initialize containers	2026-10-24T06:16:22.4823914Z postgres service is starting, waiting 2 seconds before checking again.
test	Initialize containers	2026-10-24T06:16:24.4820106Z ##[command]/usr/bin/docker inspect --format="{{if .Config.Healthcheck}}{{print .State.Health.Status}}{{end}}" 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:24.4913910Z starting
test	Initialize containers	2026-10-24T06:16:24.4924920Z postgres service is starting, waiting 3 seconds before checking again.
test	Initialize containers	2026-10-24T06:16:28.1724778Z ##[command]/usr/bin/docker inspect --format="{{if .Config.Healthcheck}}{{print .State.Health.Status}}{{end}}" 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Initialize containers	2026-10-24T06:16:28.1820269Z healthy
test	Initialize containers	2026-10-24T06:16:28.1834324Z postgres service is healthy.
test	Initialize containers	2026-10-24T06:16:28.1834924Z ##[endgroup]
test	Checkout	﻿2026-10-24T06:16:28.2065704Z ##[group]Run actions/checkout@v4
test	Checkout	2026-10-24T06:16:28.2066215Z with:
test	Checkout	2026-10-24T06:16:28.2066364Z   repository: PruthviChaudharii/customer-accounts
test	Checkout	2026-10-24T06:16:28.2068033Z   token: ***
test	Checkout	2026-10-24T06:16:28.2068150Z   ssh-strict: true
test	Checkout	2026-10-24T06:16:28.2068267Z   ssh-user: git
test	Checkout	2026-10-24T06:16:28.2068386Z   persist-credentials: true
test	Checkout	2026-10-24T06:16:28.2068516Z   clean: true
test	Checkout	2026-10-24T06:16:28.2068636Z   sparse-checkout-cone-mode: true
test	Checkout	2026-10-24T06:16:28.2068775Z   fetch-depth: 1
test	Checkout	2026-10-24T06:16:28.2068886Z   fetch-tags: false
test	Checkout	2026-10-24T06:16:28.2069002Z   show-progress: true
test	Checkout	2026-10-24T06:16:28.2069116Z   lfs: false
test	Checkout	2026-10-24T06:16:28.2069218Z   submodules: false
test	Checkout	2026-10-24T06:16:28.2069332Z   set-safe-directory: true
test	Checkout	2026-10-24T06:16:28.2069466Z   allow-unsafe-pr-checkout: false
test	Checkout	2026-10-24T06:16:28.2069703Z env:
test	Checkout	2026-10-24T06:16:28.2069935Z   DATABASE_URI: ***localhost:5432/accounts
test	Checkout	2026-10-24T06:16:28.2070083Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.2714512Z Syncing repository: PruthviChaudharii/customer-accounts
test	Checkout	2026-10-24T06:16:28.2715535Z ##[group]Getting Git version info
test	Checkout	2026-10-24T06:16:28.2715775Z Working directory is '/home/runner/work/customer-accounts/customer-accounts'
test	Checkout	2026-10-24T06:16:28.2716229Z [command]/usr/bin/git version
test	Checkout	2026-10-24T06:16:28.2758417Z git version 2.55.0
test	Checkout	2026-10-24T06:16:28.2771599Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.2781591Z Temporarily overriding HOME='/home/runner/work/_temp/94b744ee-f289-428c-ae6f-a7d1297fec67' before making global git config changes
test	Checkout	2026-10-24T06:16:28.2782263Z Adding repository directory to the temporary git global config as a safe directory
test	Checkout	2026-10-24T06:16:28.2785892Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/customer-accounts/customer-accounts
test	Checkout	2026-10-24T06:16:28.2826873Z Deleting the contents of '/home/runner/work/customer-accounts/customer-accounts'
test	Checkout	2026-10-24T06:16:28.2828864Z ##[group]Initializing the repository
test	Checkout	2026-10-24T06:16:28.2832192Z [command]/usr/bin/git init /home/runner/work/customer-accounts/customer-accounts
test	Checkout	2026-10-24T06:16:28.2906054Z hint: Using 'master' as the name for the initial branch. This default branch name
test	Checkout	2026-10-24T06:16:28.2906540Z hint: will change to "main" in Git 3.0. To configure the initial branch name
test	Checkout	2026-10-24T06:16:28.2906987Z hint: to use in all of your new repositories, which will suppress this warning,
test	Checkout	2026-10-24T06:16:28.2907328Z hint: call:
test	Checkout	2026-10-24T06:16:28.2907506Z hint:
test	Checkout	2026-10-24T06:16:28.2907848Z hint: 	git config --global init.defaultBranch <name>
test	Checkout	2026-10-24T06:16:28.2908127Z hint:
test	Checkout	2026-10-24T06:16:28.2908377Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
test	Checkout	2026-10-24T06:16:28.2908812Z hint: 'development'. The just-created branch can be renamed via this command:
test	Checkout	2026-10-24T06:16:28.2909154Z hint:
test	Checkout	2026-10-24T06:16:28.2909333Z hint: 	git branch -m <name>
test	Checkout	2026-10-24T06:16:28.2909537Z hint:
test	Checkout	2026-10-24T06:16:28.2909819Z hint: Disable this message with "git config set advice.defaultBranchName false"
test	Checkout	2026-10-24T06:16:28.2910368Z Initialized empty Git repository in /home/runner/work/customer-accounts/customer-accounts/.git/
test	Checkout	2026-10-24T06:16:28.2917881Z [command]/usr/bin/git remote add origin https://github.com/PruthviChaudharii/customer-accounts
test	Checkout	2026-10-24T06:16:28.2970569Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.2970977Z ##[group]Disabling automatic garbage collection
test	Checkout	2026-10-24T06:16:28.2973289Z [command]/usr/bin/git config --local gc.auto 0
test	Checkout	2026-10-24T06:16:28.3009394Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.3009805Z ##[group]Setting up auth
test	Checkout	2026-10-24T06:16:28.3010160Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
test	Checkout	2026-10-24T06:16:28.3037077Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
test	Checkout	2026-10-24T06:16:28.3314074Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
test	Checkout	2026-10-24T06:16:28.3345019Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
test	Checkout	2026-10-24T06:16:28.3514929Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
test	Checkout	2026-10-24T06:16:28.3542345Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
test	Checkout	2026-10-24T06:16:28.3716596Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
test	Checkout	2026-10-24T06:16:28.3870653Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.3870999Z ##[group]Fetching the repository
test	Checkout	2026-10-24T06:16:28.3876823Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +e9415db1d1f97ce5f54808daf8bd71db6c4f303b:refs/remotes/origin/main
test	Checkout	2026-10-24T06:16:28.7123108Z From https://github.com/PruthviChaudharii/customer-accounts
test	Checkout	2026-10-24T06:16:28.7123969Z  * [new ref]         e9415db1d1f97ce5f54808daf8bd71db6c4f303b -> origin/main
test	Checkout	2026-10-24T06:16:28.7125793Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.7126138Z ##[group]Determining the checkout info
test	Checkout	2026-10-24T06:16:28.7128697Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.7133288Z [command]/usr/bin/git sparse-checkout disable
test	Checkout	2026-10-24T06:16:28.7175911Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
test	Checkout	2026-10-24T06:16:28.7204362Z ##[group]Checking out the ref
test	Checkout	2026-10-24T06:16:28.7206584Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
test	Checkout	2026-10-24T06:16:28.7270604Z Switched to a new branch 'main'
test	Checkout	2026-10-24T06:16:28.7274356Z branch 'main' set up to track 'origin/main'.
test	Checkout	2026-10-24T06:16:28.7278509Z ##[endgroup]
test	Checkout	2026-10-24T06:16:28.7311577Z [command]/usr/bin/git log -1 --format=%H
test	Checkout	2026-10-24T06:16:28.7333804Z e9415db1d1f97ce5f54808daf8bd71db6c4f303b
test	Set up Python	﻿2026-10-24T06:16:28.7517047Z ##[group]Run actions/setup-python@v5
test	Set up Python	2026-10-24T06:16:28.7517213Z with:
test	Set up Python	2026-10-24T06:16:28.7517325Z   python-version: 3.11
test	Set up Python	2026-10-24T06:16:28.7517444Z   cache: pip
test	Set up Python	2026-10-24T06:16:28.7517552Z   check-latest: false
test	Set up Python	2026-10-24T06:16:28.7519088Z   token: ***
test	Set up Python	2026-10-24T06:16:28.7519215Z   update-environment: true
test	Set up Python	2026-10-24T06:16:28.7519348Z   allow-prereleases: false
test	Set up Python	2026-10-24T06:16:28.7519472Z   freethreaded: false
test	Set up Python	2026-10-24T06:16:28.7519586Z env:
test	Set up Python	2026-10-24T06:16:28.7519806Z   DATABASE_URI: ***localhost:5432/accounts
test	Set up Python	2026-10-24T06:16:28.7519955Z ##[endgroup]
test	Set up Python	2026-10-24T06:16:28.8366720Z ##[group]Installed versions
test	Set up Python	2026-10-24T06:16:28.8874988Z (node:2429) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
test	Set up Python	2026-10-24T06:16:28.8875670Z (Use `node --trace-deprecation ...` to show where the warning was created)
test	Set up Python	2026-10-24T06:16:28.8876048Z Successfully set up CPython (3.11.17)
test	Set up Python	2026-10-24T06:16:28.8876473Z ##[endgroup]
test	Set up Python	2026-10-24T06:16:28.9340633Z [command]/opt/hostedtoolcache/Python/3.11.17/x64/bin/pip cache dir
test	Set up Python	2026-10-24T06:16:30.3773410Z /home/runner/.cache/pip
test	Set up Python	2026-10-24T06:16:30.5317047Z pip cache is not found
test	Install dependencies	﻿2026-10-24T06:16:30.5439935Z ##[group]Run pip install -r requirements-dev.txt
test	Install dependencies	2026-10-24T06:16:30.5440378Z ^[[36;1mpip install -r requirements-dev.txt^[[0m
test	Install dependencies	2026-10-24T06:16:30.5594289Z shell: /usr/bin/bash -e {0}
test	Install dependencies	2026-10-24T06:16:30.5594448Z env:
test	Install dependencies	2026-10-24T06:16:30.5594783Z   DATABASE_URI: ***localhost:5432/accounts
test	Install dependencies	2026-10-24T06:16:30.5594982Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
test	Install dependencies	2026-10-24T06:16:30.5595220Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
test	Install dependencies	2026-10-24T06:16:30.5595450Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Install dependencies	2026-10-24T06:16:30.5595657Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Install dependencies	2026-10-24T06:16:30.5595868Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Install dependencies	2026-10-24T06:16:30.5596077Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
test	Install dependencies	2026-10-24T06:16:30.5596264Z ##[endgroup]
test	Install dependencies	2026-10-24T06:16:32.0017877Z Collecting Flask==2.2.5 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 1))
test	Install dependencies	2026-10-24T06:16:32.0735789Z   Downloading Flask-2.2.5-py3-none-any.whl.metadata (3.9 kB)
test	Install dependencies	2026-10-24T06:16:32.1038848Z Collecting Werkzeug==2.3.8 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 2))
test	Install dependencies	2026-10-24T06:16:32.1171110Z   Downloading werkzeug-2.3.8-py3-none-any.whl.metadata (4.1 kB)
test	Install dependencies	2026-10-24T06:16:32.1394220Z Collecting Flask-SQLAlchemy==2.5.1 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 3))
test	Install dependencies	2026-10-24T06:16:32.1492065Z   Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl.metadata (3.1 kB)
test	Install dependencies	2026-10-24T06:16:32.3690398Z Collecting SQLAlchemy==1.4.54 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 4))
test	Install dependencies	2026-10-24T06:16:32.3794560Z   Downloading SQLAlchemy-1.4.54-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
test	Install dependencies	2026-10-24T06:16:32.4286771Z Collecting psycopg2-binary==2.9.10 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 5))
test	Install dependencies	2026-10-24T06:16:32.4386537Z   Downloading psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
test	Install dependencies	2026-10-24T06:16:32.4811450Z Collecting gunicorn==23.0.0 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 6))
test	Install dependencies	2026-10-24T06:16:32.4913506Z   Downloading gunicorn-23.0.0-py3-none-any.whl.metadata (4.4 kB)
test	Install dependencies	2026-10-24T06:16:32.5128846Z Collecting flask-talisman==1.1.0 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 7))
test	Install dependencies	2026-10-24T06:16:32.5236947Z   Downloading flask_talisman-1.1.0-py2.py3-none-any.whl.metadata (18 kB)
test	Install dependencies	2026-10-24T06:16:32.5494381Z Collecting Flask-Cors==6.0.1 (from -r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 8))
test	Install dependencies	2026-10-24T06:16:32.5595086Z   Downloading flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)
test	Install dependencies	2026-10-24T06:16:32.5803434Z Collecting pynose==1.5.5 (from -r requirements-dev.txt (line 2))
test	Install dependencies	2026-10-24T06:16:32.5901580Z   Downloading pynose-1.5.5-py3-none-any.whl.metadata (19 kB)
test	Install dependencies	2026-10-24T06:16:32.8227794Z Collecting coverage==7.6.12 (from -r requirements-dev.txt (line 3))
test	Install dependencies	2026-10-24T06:16:32.8331591Z   Downloading coverage-7.6.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.5 kB)
test	Install dependencies	2026-10-24T06:16:32.8557267Z Collecting factory-boy==3.3.3 (from -r requirements-dev.txt (line 4))
test	Install dependencies	2026-10-24T06:16:32.8658000Z   Downloading factory_boy-3.3.3-py2.py3-none-any.whl.metadata (15 kB)
test	Install dependencies	2026-10-24T06:16:32.8913498Z Collecting flake8==7.1.2 (from -r requirements-dev.txt (line 5))
test	Install dependencies	2026-10-24T06:16:32.9014025Z   Downloading flake8-7.1.2-py2.py3-none-any.whl.metadata (3.8 kB)
test	Install dependencies	2026-10-24T06:16:32.9292312Z Collecting pylint==3.3.4 (from -r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:32.9399144Z   Downloading pylint-3.3.4-py3-none-any.whl.metadata (12 kB)
test	Install dependencies	2026-10-24T06:16:32.9628178Z Collecting Jinja2>=3.0 (from Flask==2.2.5->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 1))
test	Install dependencies	2026-10-24T06:16:32.9726248Z   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
test	Install dependencies	2026-10-24T06:16:32.9982009Z Collecting itsdangerous>=2.0 (from Flask==2.2.5->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 1))
test	Install dependencies	2026-10-24T06:16:33.0079482Z   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
test	Install dependencies	2026-10-24T06:16:33.0297118Z Collecting click>=8.0 (from Flask==2.2.5->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 1))
test	Install dependencies	2026-10-24T06:16:33.0393919Z   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
test	Install dependencies	2026-10-24T06:16:33.0935235Z Collecting MarkupSafe>=2.1.1 (from Werkzeug==2.3.8->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 2))
test	Install dependencies	2026-10-24T06:16:33.1036326Z   Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
test	Install dependencies	2026-10-24T06:16:33.1831795Z Collecting greenlet!=0.4.17 (from SQLAlchemy==1.4.54->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 4))
test	Install dependencies	2026-10-24T06:16:33.1946165Z   Downloading greenlet-3.5.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
test	Install dependencies	2026-10-24T06:16:33.2168921Z Collecting packaging (from gunicorn==23.0.0->-r /home/runner/work/customer-accounts/customer-accounts/requirements.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.2266289Z   Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
test	Install dependencies	2026-10-24T06:16:33.2744112Z Collecting Faker>=0.7.0 (from factory-boy==3.3.3->-r requirements-dev.txt (line 4))
test	Install dependencies	2026-10-24T06:16:33.2851678Z   Downloading faker-40.43.0-py3-none-any.whl.metadata (16 kB)
test	Install dependencies	2026-10-24T06:16:33.3066247Z Collecting mccabe<0.8.0,>=0.7.0 (from flake8==7.1.2->-r requirements-dev.txt (line 5))
test	Install dependencies	2026-10-24T06:16:33.3163643Z   Downloading mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
test	Install dependencies	2026-10-24T06:16:33.3364933Z Collecting pycodestyle<2.13.0,>=2.12.0 (from flake8==7.1.2->-r requirements-dev.txt (line 5))
test	Install dependencies	2026-10-24T06:16:33.3463940Z   Downloading pycodestyle-2.12.1-py2.py3-none-any.whl.metadata (4.5 kB)
test	Install dependencies	2026-10-24T06:16:33.3740703Z Collecting pyflakes<3.3.0,>=3.2.0 (from flake8==7.1.2->-r requirements-dev.txt (line 5))
test	Install dependencies	2026-10-24T06:16:33.3837476Z   Downloading pyflakes-3.2.0-py2.py3-none-any.whl.metadata (3.5 kB)
test	Install dependencies	2026-10-24T06:16:33.4040853Z Collecting dill>=0.3.6 (from pylint==3.3.4->-r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.4145415Z   Downloading dill-0.4.1-py3-none-any.whl.metadata (10 kB)
test	Install dependencies	2026-10-24T06:16:33.4389564Z Collecting platformdirs>=2.2.0 (from pylint==3.3.4->-r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.4490467Z   Downloading platformdirs-4.13.5-py3-none-any.whl.metadata (5.5 kB)
test	Install dependencies	2026-10-24T06:16:33.4780120Z Collecting astroid<=3.4.0-dev0,>=3.3.8 (from pylint==3.3.4->-r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.4880994Z   Downloading astroid-3.3.11-py3-none-any.whl.metadata (4.4 kB)
test	Install dependencies	2026-10-24T06:16:33.5212416Z Collecting isort!=5.13.0,<7,>=4.2.5 (from pylint==3.3.4->-r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.5311395Z   Downloading isort-6.1.0-py3-none-any.whl.metadata (12 kB)
test	Install dependencies	2026-10-24T06:16:33.5546081Z Collecting tomlkit>=0.10.1 (from pylint==3.3.4->-r requirements-dev.txt (line 6))
test	Install dependencies	2026-10-24T06:16:33.5644827Z   Downloading tomlkit-0.15.2-py3-none-any.whl.metadata (3.4 kB)
test	Install dependencies	2026-10-24T06:16:33.5796368Z Downloading Flask-2.2.5-py3-none-any.whl (101 kB)
test	Install dependencies	2026-10-24T06:16:33.6040328Z Downloading werkzeug-2.3.8-py3-none-any.whl (242 kB)
test	Install dependencies	2026-10-24T06:16:33.6256795Z Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
test	Install dependencies	2026-10-24T06:16:33.6371225Z Downloading SQLAlchemy-1.4.54-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
test	Install dependencies	2026-10-24T06:16:33.6700682Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 46.6 MB/s  0:00:00
test	Install dependencies	2026-10-24T06:16:33.6802625Z Downloading psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
test	Install dependencies	2026-10-24T06:16:33.7084667Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 104.2 MB/s  0:00:00
test	Install dependencies	2026-10-24T06:16:33.7184998Z Downloading gunicorn-23.0.0-py3-none-any.whl (85 kB)
test	Install dependencies	2026-10-24T06:16:33.7299303Z Downloading flask_talisman-1.1.0-py2.py3-none-any.whl (18 kB)
test	Install dependencies	2026-10-24T06:16:33.7410679Z Downloading flask_cors-6.0.1-py3-none-any.whl (13 kB)
test	Install dependencies	2026-10-24T06:16:33.7522355Z Downloading pynose-1.5.5-py3-none-any.whl (130 kB)
test	Install dependencies	2026-10-24T06:16:33.7643724Z Downloading coverage-7.6.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (241 kB)
test	Install dependencies	2026-10-24T06:16:33.7761827Z Downloading factory_boy-3.3.3-py2.py3-none-any.whl (37 kB)
test	Install dependencies	2026-10-24T06:16:33.7873806Z Downloading flake8-7.1.2-py2.py3-none-any.whl (57 kB)
test	Install dependencies	2026-10-24T06:16:33.7998364Z Downloading pylint-3.3.4-py3-none-any.whl (522 kB)
test	Install dependencies	2026-10-24T06:16:33.8279493Z Downloading astroid-3.3.11-py3-none-any.whl (275 kB)
test	Install dependencies	2026-10-24T06:16:33.8397413Z Downloading isort-6.1.0-py3-none-any.whl (94 kB)
test	Install dependencies	2026-10-24T06:16:33.8515437Z Downloading mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
test	Install dependencies	2026-10-24T06:16:33.8626605Z Downloading pycodestyle-2.12.1-py2.py3-none-any.whl (31 kB)
test	Install dependencies	2026-10-24T06:16:33.8738338Z Downloading pyflakes-3.2.0-py2.py3-none-any.whl (62 kB)
test	Install dependencies	2026-10-24T06:16:33.8851152Z Downloading click-8.5.0-py3-none-any.whl (125 kB)
test	Install dependencies	2026-10-24T06:16:33.8963284Z Downloading dill-0.4.1-py3-none-any.whl (120 kB)
test	Install dependencies	2026-10-24T06:16:33.9076120Z Downloading faker-40.43.0-py3-none-any.whl (2.1 MB)
test	Install dependencies	2026-10-24T06:16:33.9154338Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 294.0 MB/s  0:00:00
test	Install dependencies	2026-10-24T06:16:33.9254089Z Downloading greenlet-3.5.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (624 kB)
test	Install dependencies	2026-10-24T06:16:33.9287375Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 624.4/624.4 kB 183.8 MB/s  0:00:00
test	Install dependencies	2026-10-24T06:16:33.9384730Z Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
test	Install dependencies	2026-10-24T06:16:33.9495844Z Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
test	Install dependencies	2026-10-24T06:16:33.9609684Z Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
test	Install dependencies	2026-10-24T06:16:33.9721646Z Downloading platformdirs-4.13.5-py3-none-any.whl (32 kB)
test	Install dependencies	2026-10-24T06:16:33.9832281Z Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
test	Install dependencies	2026-10-24T06:16:33.9943244Z Downloading packaging-26.3-py3-none-any.whl (129 kB)
test	Install dependencies	2026-10-24T06:16:34.1806190Z Installing collected packages: flask-talisman, tomlkit, pynose, pyflakes, pycodestyle, psycopg2-binary, platformdirs, packaging, mccabe, MarkupSafe, itsdangerous, isort, greenlet, Faker, dill, coverage, click, astroid, Werkzeug, SQLAlchemy, pylint, Jinja2, gunicorn, flake8, factory-boy, Flask, Flask-SQLAlchemy, Flask-Cors
test	Install dependencies	2026-10-24T06:16:36.3660545Z 
test	Install dependencies	2026-10-24T06:16:36.3671921Z Successfully installed Faker-40.43.0 Flask-2.2.5 Flask-Cors-6.0.1 Flask-SQLAlchemy-2.5.1 Jinja2-3.1.6 MarkupSafe-3.0.4 SQLAlchemy-1.4.54 Werkzeug-2.3.8 astroid-3.3.11 click-8.5.0 coverage-7.6.12 dill-0.4.1 factory-boy-3.3.3 flake8-7.1.2 flask-talisman-1.1.0 greenlet-3.5.6 gunicorn-23.0.0 isort-6.1.0 itsdangerous-2.2.0 mccabe-0.7.0 packaging-26.3 platformdirs-4.13.5 psycopg2-binary-2.9.10 pycodestyle-2.12.1 pyflakes-3.2.0 pylint-3.3.4 pynose-1.5.5 tomlkit-0.15.2
test	Install dependencies	2026-10-24T06:16:36.3677843Z 
test	Install dependencies	2026-10-24T06:16:36.3678103Z [notice] A new release of pip is available: 26.2.1 -> 26.2.2
test	Install dependencies	2026-10-24T06:16:36.3678467Z [notice] To update, run: pip install --upgrade pip
test	Lint	﻿2026-10-24T06:16:36.4544292Z ##[group]Run flake8 service tests
test	Lint	2026-10-24T06:16:36.4544516Z ^[[36;1mflake8 service tests^[[0m
test	Lint	2026-10-24T06:16:36.4544669Z ^[[36;1mpylint service --fail-under=9^[[0m
test	Lint	2026-10-24T06:16:36.4602015Z shell: /usr/bin/bash -e {0}
test	Lint	2026-10-24T06:16:36.4602176Z env:
test	Lint	2026-10-24T06:16:36.4602493Z   DATABASE_URI: ***localhost:5432/accounts
test	Lint	2026-10-24T06:16:36.4602692Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
test	Lint	2026-10-24T06:16:36.4602932Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
test	Lint	2026-10-24T06:16:36.4603172Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Lint	2026-10-24T06:16:36.4603385Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Lint	2026-10-24T06:16:36.4603734Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Lint	2026-10-24T06:16:36.4603956Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
test	Lint	2026-10-24T06:16:36.4604140Z ##[endgroup]
test	Lint	2026-10-24T06:16:41.6078910Z 
test	Lint	2026-10-24T06:16:41.6079461Z ------------------------------------
test	Lint	2026-10-24T06:16:41.6079891Z Your code has been rated at 10.00/10
test	Lint	2026-10-24T06:16:41.6080044Z 
test	Unit tests with nosetests	﻿2026-10-24T06:16:43.3025283Z ##[group]Run nosetests
test	Unit tests with nosetests	2026-10-24T06:16:43.3025451Z ^[[36;1mnosetests^[[0m
test	Unit tests with nosetests	2026-10-24T06:16:43.3078150Z shell: /usr/bin/bash -e {0}
test	Unit tests with nosetests	2026-10-24T06:16:43.3078290Z env:
test	Unit tests with nosetests	2026-10-24T06:16:43.3078662Z   DATABASE_URI: ***localhost:5432/accounts
test	Unit tests with nosetests	2026-10-24T06:16:43.3078904Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
test	Unit tests with nosetests	2026-10-24T06:16:43.3079254Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
test	Unit tests with nosetests	2026-10-24T06:16:43.3079604Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Unit tests with nosetests	2026-10-24T06:16:43.3079829Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Unit tests with nosetests	2026-10-24T06:16:43.3080046Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Unit tests with nosetests	2026-10-24T06:16:43.3080257Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
test	Unit tests with nosetests	2026-10-24T06:16:43.3080434Z ##[endgroup]
test	Unit tests with nosetests	2026-10-24T06:16:44.0535709Z It should Create an account and add it to the database ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0550437Z It should Create an Account and assert that it exists ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0602033Z It should Delete an account from the database ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0630818Z It should Deserialize an account ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0639564Z It should not Deserialize an account with a KeyError ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0646249Z It should not Deserialize an account with a TypeError ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0696025Z It should Find an Account by name ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0770347Z It should List all Accounts in the database ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0801533Z It should Read an account ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0814017Z It should Serialize an account ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0858210Z It should Update an account ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.0984590Z It should not Create an Account when sending the wrong data ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1022696Z It should allow configured origins and reject other origins. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1067386Z It should Create a new Account ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1148582Z It should delete an account and allow repeated deletion. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1216167Z It should filter accounts by name. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1230028Z It should be healthy ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1241843Z It should get 200_OK from the Home Page ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1250041Z It should return a structured response for an internal error. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1311606Z It should reject invalid types, lengths, dates and JSON shapes. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1409918Z It should list all accounts and return an empty list when absent. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1423049Z It should reject malformed JSON. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1434359Z It should respond with a JSON 405 for unsupported methods. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1463202Z It should default the join date and allow a missing phone. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1506145Z It should read a created account using its Location header. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1526358Z It should return 404 when an account is absent. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1541112Z It should set Talisman security headers. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1557206Z It should not Create an Account when sending the wrong media type ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1625009Z It should update an account and preserve its identifier. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1677353Z It should reject incomplete updates and leave stored data unchanged. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1701768Z It should return 404 when replacing an absent account. ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1735457Z It should call the db-create command ... ok
test	Unit tests with nosetests	2026-10-24T06:16:44.1736109Z 
test	Unit tests with nosetests	2026-10-24T06:16:44.1910033Z Name                               Stmts   Miss  Cover   Missing
test	Unit tests with nosetests	2026-10-24T06:16:44.1910720Z ----------------------------------------------------------------
test	Unit tests with nosetests	2026-10-24T06:16:44.1911066Z service/__init__.py                   20      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1911384Z service/common/__init__.py             0      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1911690Z service/common/cli_commands.py         7      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1911986Z service/common/error_handlers.py      32      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1912587Z service/common/log_handlers.py        10      1    90%   21
test	Unit tests with nosetests	2026-10-24T06:16:44.1912911Z service/common/status.py              45      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1913234Z service/config.py                     11      5    55%   12-16
test	Unit tests with nosetests	2026-10-24T06:16:44.1913575Z service/models.py                     77      2    97%   32, 98
test	Unit tests with nosetests	2026-10-24T06:16:44.1913891Z service/routes.py                     51      0   100%
test	Unit tests with nosetests	2026-10-24T06:16:44.1914196Z ----------------------------------------------------------------
test	Unit tests with nosetests	2026-10-24T06:16:44.1914488Z TOTAL                                253      8    97%
test	Unit tests with nosetests	2026-10-24T06:16:44.2018907Z ----------------------------------------
test	Unit tests with nosetests	2026-10-24T06:16:44.2019190Z Ran 32 tests in 0.162s
test	Unit tests with nosetests	2026-10-24T06:16:44.2019317Z 
test	Unit tests with nosetests	2026-10-24T06:16:44.2019394Z OK
test	Build Docker image	﻿2026-10-24T06:16:44.2753045Z ##[group]Run docker build -t customer-accounts:ci .
test	Build Docker image	2026-10-24T06:16:44.2753288Z ^[[36;1mdocker build -t customer-accounts:ci .^[[0m
test	Build Docker image	2026-10-24T06:16:44.2806434Z shell: /usr/bin/bash -e {0}
test	Build Docker image	2026-10-24T06:16:44.2806572Z env:
test	Build Docker image	2026-10-24T06:16:44.2807044Z   DATABASE_URI: ***localhost:5432/accounts
test	Build Docker image	2026-10-24T06:16:44.2807235Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64
test	Build Docker image	2026-10-24T06:16:44.2807466Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib/pkgconfig
test	Build Docker image	2026-10-24T06:16:44.2807766Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Build Docker image	2026-10-24T06:16:44.2807973Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Build Docker image	2026-10-24T06:16:44.2808178Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.17/x64
test	Build Docker image	2026-10-24T06:16:44.2808404Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.17/x64/lib
test	Build Docker image	2026-10-24T06:16:44.2808587Z ##[endgroup]
test	Build Docker image	2026-10-24T06:16:47.0414195Z #0 building with "default" instance using docker driver
test	Build Docker image	2026-10-24T06:16:47.0414441Z 
test	Build Docker image	2026-10-24T06:16:47.0414611Z #1 [internal] load build definition from Dockerfile
test	Build Docker image	2026-10-24T06:16:47.0414797Z #1 transferring dockerfile: 619B 0.0s done
test	Build Docker image	2026-10-24T06:16:47.0414946Z #1 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:47.0415014Z 
test	Build Docker image	2026-10-24T06:16:47.0415105Z #2 [auth] library/python:pull token for registry-1.docker.io
test	Build Docker image	2026-10-24T06:16:47.1921500Z #2 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:47.1921711Z 
test	Build Docker image	2026-10-24T06:16:47.1921902Z #3 [internal] load metadata for docker.io/library/python:3.11-slim
test	Build Docker image	2026-10-24T06:16:47.5658572Z #3 DONE 0.6s
test	Build Docker image	2026-10-24T06:16:47.6884216Z 
test	Build Docker image	2026-10-24T06:16:47.6884894Z #4 [internal] load .dockerignore
test	Build Docker image	2026-10-24T06:16:47.6885282Z #4 transferring context: 100B done
test	Build Docker image	2026-10-24T06:16:47.6885464Z #4 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:47.6885535Z 
test	Build Docker image	2026-10-24T06:16:47.6885599Z #5 [internal] load build context
test	Build Docker image	2026-10-24T06:16:47.6885844Z #5 transferring context: 45.19kB done
test	Build Docker image	2026-10-24T06:16:47.6886023Z #5 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:47.6886089Z 
test	Build Docker image	2026-10-24T06:16:47.6886324Z #6 [1/5] FROM docker.io/library/python:3.11-slim@sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377
test	Build Docker image	2026-10-24T06:16:47.6886907Z #6 resolve docker.io/library/python:3.11-slim@sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377 done
test	Build Docker image	2026-10-24T06:16:47.6887397Z #6 sha256:90d47cf54851a8d83f33db71f0025a8ba367c12fb24817259dd9736098cb305b 0B / 1.29MB 0.1s
test	Build Docker image	2026-10-24T06:16:47.6888110Z #6 sha256:6d9af71a343efe2a00fdfc9507db3bdf3530bf3f8cf2975eb1be235a7eb70128 0B / 14.46MB 0.1s
test	Build Docker image	2026-10-24T06:16:47.6888687Z #6 sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377 10.37kB / 10.37kB done
test	Build Docker image	2026-10-24T06:16:47.6889253Z #6 sha256:b95327ce1439e687237841b0210677aeadd62d55a060a5f6bcb9c15bf6251dd3 1.75kB / 1.75kB done
test	Build Docker image	2026-10-24T06:16:47.6889681Z #6 sha256:b4403f3b7acf5e0700a5dd4e7ab01456d62b557a208a04f8a42d3470d93b5730 5.49kB / 5.49kB done
test	Build Docker image	2026-10-24T06:16:47.6890518Z #6 sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 0B / 29.84MB 0.1s
test	Build Docker image	2026-10-24T06:16:47.8924811Z #6 sha256:90d47cf54851a8d83f33db71f0025a8ba367c12fb24817259dd9736098cb305b 1.29MB / 1.29MB 0.3s
test	Build Docker image	2026-10-24T06:16:47.8925329Z #6 sha256:6d9af71a343efe2a00fdfc9507db3bdf3530bf3f8cf2975eb1be235a7eb70128 13.63MB / 14.46MB 0.3s
test	Build Docker image	2026-10-24T06:16:48.0885570Z #6 sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 29.84MB / 29.84MB 0.3s
test	Build Docker image	2026-10-24T06:16:48.0886238Z #6 sha256:90d47cf54851a8d83f33db71f0025a8ba367c12fb24817259dd9736098cb305b 1.29MB / 1.29MB 0.3s done
test	Build Docker image	2026-10-24T06:16:48.0886809Z #6 sha256:6d9af71a343efe2a00fdfc9507db3bdf3530bf3f8cf2975eb1be235a7eb70128 14.46MB / 14.46MB 0.5s done
test	Build Docker image	2026-10-24T06:16:48.0887252Z #6 sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 29.84MB / 29.84MB 0.5s done
test	Build Docker image	2026-10-24T06:16:48.0887907Z #6 sha256:b0aec4a98ced1e92f1d50c37aa89c78d60e3dc6a52d61f8134afda24b185ad06 0B / 249B 0.5s
test	Build Docker image	2026-10-24T06:16:48.1958813Z #6 sha256:b0aec4a98ced1e92f1d50c37aa89c78d60e3dc6a52d61f8134afda24b185ad06 249B / 249B 0.5s done
test	Build Docker image	2026-10-24T06:16:48.1959446Z #6 extracting sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 0.1s
test	Build Docker image	2026-10-24T06:16:48.7258055Z #6 extracting sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 0.5s done
test	Build Docker image	2026-10-24T06:16:48.7258606Z #6 extracting sha256:90d47cf54851a8d83f33db71f0025a8ba367c12fb24817259dd9736098cb305b 0.1s done
test	Build Docker image	2026-10-24T06:16:49.7020949Z #6 extracting sha256:6d9af71a343efe2a00fdfc9507db3bdf3530bf3f8cf2975eb1be235a7eb70128
test	Build Docker image	2026-10-24T06:16:50.2483879Z #6 extracting sha256:6d9af71a343efe2a00fdfc9507db3bdf3530bf3f8cf2975eb1be235a7eb70128 0.4s done
test	Build Docker image	2026-10-24T06:16:50.4020507Z #6 extracting sha256:b0aec4a98ced1e92f1d50c37aa89c78d60e3dc6a52d61f8134afda24b185ad06
test	Build Docker image	2026-10-24T06:16:50.5851685Z #6 extracting sha256:b0aec4a98ced1e92f1d50c37aa89c78d60e3dc6a52d61f8134afda24b185ad06 done
test	Build Docker image	2026-10-24T06:16:50.5852018Z #6 DONE 2.8s
test	Build Docker image	2026-10-24T06:16:50.5852098Z 
test	Build Docker image	2026-10-24T06:16:50.5852154Z #7 [2/5] WORKDIR /app
test	Build Docker image	2026-10-24T06:16:50.5852282Z #7 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:50.5852347Z 
test	Build Docker image	2026-10-24T06:16:50.5852408Z #8 [3/5] COPY requirements.txt .
test	Build Docker image	2026-10-24T06:16:50.5852559Z #8 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:50.5852619Z 
test	Build Docker image	2026-10-24T06:16:50.5852802Z #9 [4/5] RUN pip install --no-cache-dir -r requirements.txt     && useradd --create-home --uid 10001 appuser
test	Build Docker image	2026-10-24T06:16:51.3611947Z #9 0.926 Collecting Flask==2.2.5 (from -r requirements.txt (line 1))
test	Build Docker image	2026-10-24T06:16:51.4680524Z #9 0.965   Downloading Flask-2.2.5-py3-none-any.whl.metadata (3.9 kB)
test	Build Docker image	2026-10-24T06:16:51.4680946Z #9 0.998 Collecting Werkzeug==2.3.8 (from -r requirements.txt (line 2))
test	Build Docker image	2026-10-24T06:16:51.4681194Z #9 1.008   Downloading werkzeug-2.3.8-py3-none-any.whl.metadata (4.1 kB)
test	Build Docker image	2026-10-24T06:16:51.4681448Z #9 1.033 Collecting Flask-SQLAlchemy==2.5.1 (from -r requirements.txt (line 3))
test	Build Docker image	2026-10-24T06:16:51.6289854Z #9 1.044   Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl.metadata (3.1 kB)
test	Build Docker image	2026-10-24T06:16:51.7558461Z #9 1.321 Collecting SQLAlchemy==1.4.54 (from -r requirements.txt (line 4))
test	Build Docker image	2026-10-24T06:16:51.8563177Z #9 1.332   Downloading SQLAlchemy-1.4.54-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
test	Build Docker image	2026-10-24T06:16:51.8563928Z #9 1.385 Collecting psycopg2-binary==2.9.10 (from -r requirements.txt (line 5))
test	Build Docker image	2026-10-24T06:16:51.8564476Z #9 1.395   Downloading psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
test	Build Docker image	2026-10-24T06:16:51.8564989Z #9 1.422 Collecting gunicorn==23.0.0 (from -r requirements.txt (line 6))
test	Build Docker image	2026-10-24T06:16:51.9630576Z #9 1.431   Downloading gunicorn-23.0.0-py3-none-any.whl.metadata (4.4 kB)
test	Build Docker image	2026-10-24T06:16:51.9631201Z #9 1.454 Collecting flask-talisman==1.1.0 (from -r requirements.txt (line 7))
test	Build Docker image	2026-10-24T06:16:51.9631666Z #9 1.465   Downloading flask_talisman-1.1.0-py2.py3-none-any.whl.metadata (18 kB)
test	Build Docker image	2026-10-24T06:16:51.9632410Z #9 1.491 Collecting Flask-Cors==6.0.1 (from -r requirements.txt (line 8))
test	Build Docker image	2026-10-24T06:16:51.9632829Z #9 1.500   Downloading flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)
test	Build Docker image	2026-10-24T06:16:51.9633290Z #9 1.528 Collecting Jinja2>=3.0 (from Flask==2.2.5->-r requirements.txt (line 1))
test	Build Docker image	2026-10-24T06:16:52.0958569Z #9 1.538   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
test	Build Docker image	2026-10-24T06:16:52.0959147Z #9 1.563 Collecting itsdangerous>=2.0 (from Flask==2.2.5->-r requirements.txt (line 1))
test	Build Docker image	2026-10-24T06:16:52.0959639Z #9 1.574   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
test	Build Docker image	2026-10-24T06:16:52.0960088Z #9 1.603 Collecting click>=8.0 (from Flask==2.2.5->-r requirements.txt (line 1))
test	Build Docker image	2026-10-24T06:16:52.0960511Z #9 1.613   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
test	Build Docker image	2026-10-24T06:16:52.0960932Z #9 1.661 Collecting MarkupSafe>=2.1.1 (from Werkzeug==2.3.8->-r requirements.txt (line 2))
test	Build Docker image	2026-10-24T06:16:52.2562950Z #9 1.671   Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
test	Build Docker image	2026-10-24T06:16:52.2899287Z #9 1.855 Collecting greenlet!=0.4.17 (from SQLAlchemy==1.4.54->-r requirements.txt (line 4))
test	Build Docker image	2026-10-24T06:16:52.3961939Z #9 1.865   Downloading greenlet-3.5.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
test	Build Docker image	2026-10-24T06:16:52.3962820Z #9 1.872 Requirement already satisfied: packaging in /usr/local/lib/python3.11/site-packages (from gunicorn==23.0.0->-r requirements.txt (line 6)) (26.3)
test	Build Docker image	2026-10-24T06:16:52.3963403Z #9 1.904 Downloading Flask-2.2.5-py3-none-any.whl (101 kB)
test	Build Docker image	2026-10-24T06:16:52.3964023Z #9 1.918    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.8/101.8 kB 8.4 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.3964384Z #9 1.928 Downloading werkzeug-2.3.8-py3-none-any.whl (242 kB)
test	Build Docker image	2026-10-24T06:16:52.3964853Z #9 1.939    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.3/242.3 kB 23.0 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.3965236Z #9 1.950 Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
test	Build Docker image	2026-10-24T06:16:52.3965900Z #9 1.961 Downloading SQLAlchemy-1.4.54-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.6 MB)
test	Build Docker image	2026-10-24T06:16:52.4973724Z #9 1.991    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 57.5 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.4974170Z #9 2.001 Downloading psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
test	Build Docker image	2026-10-24T06:16:52.4974545Z #9 2.021    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 166.4 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.4974775Z #9 2.031 Downloading gunicorn-23.0.0-py3-none-any.whl (85 kB)
test	Build Docker image	2026-10-24T06:16:52.4975049Z #9 2.032    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.0/85.0 kB 565.9 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.4975296Z #9 2.043 Downloading flask_talisman-1.1.0-py2.py3-none-any.whl (18 kB)
test	Build Docker image	2026-10-24T06:16:52.4975533Z #9 2.053 Downloading flask_cors-6.0.1-py3-none-any.whl (13 kB)
test	Build Docker image	2026-10-24T06:16:52.6124506Z #9 2.063 Downloading click-8.5.0-py3-none-any.whl (125 kB)
test	Build Docker image	2026-10-24T06:16:52.6125430Z #9 2.064    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.3/125.3 kB 534.6 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.6126017Z #9 2.074 Downloading greenlet-3.5.6-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (624 kB)
test	Build Docker image	2026-10-24T06:16:52.6126728Z #9 2.077    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 624.4/624.4 kB 660.3 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.6127163Z #9 2.086 Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
test	Build Docker image	2026-10-24T06:16:52.6127459Z #9 2.096 Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
test	Build Docker image	2026-10-24T06:16:52.6128056Z #9 2.098    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 586.1 MB/s eta 0:00:00
test	Build Docker image	2026-10-24T06:16:52.6128488Z #9 2.107 Downloading markupsafe-3.0.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
test	Build Docker image	2026-10-24T06:16:52.6129161Z #9 2.178 Installing collected packages: flask-talisman, psycopg2-binary, MarkupSafe, itsdangerous, gunicorn, greenlet, click, Werkzeug, SQLAlchemy, Jinja2, Flask, Flask-SQLAlchemy, Flask-Cors
test	Build Docker image	2026-10-24T06:16:53.3696213Z #9 2.935 Successfully installed Flask-2.2.5 Flask-Cors-6.0.1 Flask-SQLAlchemy-2.5.1 Jinja2-3.1.6 MarkupSafe-3.0.4 SQLAlchemy-1.4.54 Werkzeug-2.3.8 click-8.5.0 flask-talisman-1.1.0 greenlet-3.5.6 gunicorn-23.0.0 itsdangerous-2.2.0 psycopg2-binary-2.9.10
test	Build Docker image	2026-10-24T06:16:53.5906256Z #9 2.935 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
test	Build Docker image	2026-10-24T06:16:53.5906901Z #9 3.005 
test	Build Docker image	2026-10-24T06:16:53.5907073Z #9 3.005 [notice] A new release of pip is available: 24.0 -> 26.2.2
test	Build Docker image	2026-10-24T06:16:53.5907303Z #9 3.005 [notice] To update, run: pip install --upgrade pip
test	Build Docker image	2026-10-24T06:16:53.8892757Z #9 DONE 3.5s
test	Build Docker image	2026-10-24T06:16:54.0539165Z 
test	Build Docker image	2026-10-24T06:16:54.0540134Z #10 [5/5] COPY --chown=appuser:appuser service ./service
test	Build Docker image	2026-10-24T06:16:54.0540989Z #10 DONE 0.0s
test	Build Docker image	2026-10-24T06:16:54.0541298Z 
test	Build Docker image	2026-10-24T06:16:54.0541563Z #11 exporting to image
test	Build Docker image	2026-10-24T06:16:54.0541942Z #11 exporting layers
test	Build Docker image	2026-10-24T06:16:54.2640525Z #11 exporting layers 0.4s done
test	Build Docker image	2026-10-24T06:16:54.2827266Z #11 writing image sha256:350af9c26d7044b4163a0b9d56ec5b2e812f79ef224c3c9c3e12ec424c6c8873 done
test	Build Docker image	2026-10-24T06:16:54.2827933Z #11 naming to docker.io/library/customer-accounts:ci done
test	Build Docker image	2026-10-24T06:16:54.2828450Z #11 DONE 0.4s
test	Post Set up Python	﻿2026-10-24T06:16:54.2981103Z Post job cleanup.
test	Post Set up Python	2026-10-24T06:16:54.3749094Z (node:2774) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
test	Post Set up Python	2026-10-24T06:16:54.3749664Z (Use `node --trace-deprecation ...` to show where the warning was created)
test	Post Set up Python	2026-10-24T06:16:54.3930468Z [command]/usr/bin/tar --posix -cf cache.tzst --exclude cache.tzst -P -C /home/runner/work/customer-accounts/customer-accounts --files-from manifest.txt --use-compress-program zstdmt
test	Post Set up Python	2026-10-24T06:16:54.6248806Z (node:2774) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
test	Post Set up Python	2026-10-24T06:16:55.3142091Z Sent 12646882 of 12646882 (100.0%), 17.4 MBs/sec
test	Post Set up Python	2026-10-24T06:16:55.5035001Z Cache saved with the key: setup-python-Linux-x64-24.04-Ubuntu-python-3.11.17-pip-4f9a00a44e0961ad88e89db919f72ed35abe46070469b010b8869955aba9ebc3
test	Post Checkout	﻿2026-10-24T06:16:55.5161422Z Post job cleanup.
test	Post Checkout	2026-10-24T06:16:55.5743512Z [command]/usr/bin/git version
test	Post Checkout	2026-10-24T06:16:55.5778042Z git version 2.55.0
test	Post Checkout	2026-10-24T06:16:55.5804611Z Temporarily overriding HOME='/home/runner/work/_temp/a9906894-7c37-4d80-9878-0370225e3058' before making global git config changes
test	Post Checkout	2026-10-24T06:16:55.5805390Z Adding repository directory to the temporary git global config as a safe directory
test	Post Checkout	2026-10-24T06:16:55.5808330Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/customer-accounts/customer-accounts
test	Post Checkout	2026-10-24T06:16:55.5845621Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
test	Post Checkout	2026-10-24T06:16:55.5875842Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
test	Post Checkout	2026-10-24T06:16:55.6100771Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
test	Post Checkout	2026-10-24T06:16:55.6127109Z http.https://github.com/.extraheader
test	Post Checkout	2026-10-24T06:16:55.6139766Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
test	Post Checkout	2026-10-24T06:16:55.6181369Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
test	Post Checkout	2026-10-24T06:16:55.6393397Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
test	Post Checkout	2026-10-24T06:16:55.6424851Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
test	Stop containers	﻿2026-10-24T06:16:55.6713311Z Print service container logs: a83b267ba1864d9998aa2c51aa0681ec_postgres16alpine_d28be4
test	Stop containers	2026-10-24T06:16:55.6716347Z ##[command]/usr/bin/docker logs --details 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Stop containers	2026-10-24T06:16:55.6815443Z  sh: locale: not found
test	Stop containers	2026-10-24T06:16:55.6815864Z  The files belonging to this database system will be owned by user "postgres".
test	Stop containers	2026-10-24T06:16:55.6816321Z  2026-10-24 06:16:22.718 UTC [35] WARNING:  no usable system locales were found
test	Stop containers	2026-10-24T06:16:55.6816733Z  initdb: warning: enabling "trust" authentication for local connections
test	Stop containers	2026-10-24T06:16:55.6817331Z  initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
test	Stop containers	2026-10-24T06:16:55.6818099Z  2026-10-24 06:16:23.620 UTC [1] LOG:  starting PostgreSQL 16.15 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
test	Stop containers	2026-10-24T06:16:55.6818492Z  2026-10-24 06:16:23.620 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
test	Stop containers	2026-10-24T06:16:55.6818830Z  2026-10-24 06:16:23.620 UTC [1] LOG:  listening on IPv6 address "::", port 5432
test	Stop containers	2026-10-24T06:16:55.6819119Z  2026-10-24 06:16:23.621 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
test	Stop containers	2026-10-24T06:16:55.6819433Z  2026-10-24 06:16:23.623 UTC [57] LOG:  database system was shut down at 2026-10-24 06:16:23 UTC
test	Stop containers	2026-10-24T06:16:55.6819721Z  2026-10-24 06:16:23.626 UTC [1] LOG:  database system is ready to accept connections
test	Stop containers	2026-10-24T06:16:55.6819969Z  2026-10-24 06:16:27.449 UTC [67] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6820194Z  2026-10-24 06:16:32.479 UTC [74] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6820418Z  2026-10-24 06:16:37.506 UTC [81] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6820633Z  2026-10-24 06:16:42.533 UTC [88] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6820850Z  2026-10-24 06:16:47.558 UTC [98] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6821072Z  2026-10-24 06:16:52.589 UTC [105] FATAL:  role "root" does not exist
test	Stop containers	2026-10-24T06:16:55.6830666Z  This user must also own the server process.
test	Stop containers	2026-10-24T06:16:55.6831080Z  
test	Stop containers	2026-10-24T06:16:55.6831325Z  The database cluster will be initialized with locale "en_US.utf8".
test	Stop containers	2026-10-24T06:16:55.6831715Z  The default database encoding has accordingly been set to "UTF8".
test	Stop containers	2026-10-24T06:16:55.6832082Z  The default text search configuration will be set to "english".
test	Stop containers	2026-10-24T06:16:55.6832369Z  
test	Stop containers	2026-10-24T06:16:55.6832545Z  Data page checksums are disabled.
test	Stop containers	2026-10-24T06:16:55.6832762Z  
test	Stop containers	2026-10-24T06:16:55.6833021Z  fixing permissions on existing directory /var/lib/postgresql/data ... ok
test	Stop containers	2026-10-24T06:16:55.6833359Z  creating subdirectories ... ok
test	Stop containers	2026-10-24T06:16:55.6833634Z  selecting dynamic shared memory implementation ... posix
test	Stop containers	2026-10-24T06:16:55.6833948Z  selecting default max_connections ... 100
test	Stop containers	2026-10-24T06:16:55.6834208Z  selecting default shared_buffers ... 128MB
test	Stop containers	2026-10-24T06:16:55.6834461Z  selecting default time zone ... UTC
test	Stop containers	2026-10-24T06:16:55.6834703Z  creating configuration files ... ok
test	Stop containers	2026-10-24T06:16:55.6834945Z  running bootstrap script ... ok
test	Stop containers	2026-10-24T06:16:55.6835204Z  performing post-bootstrap initialization ... ok
test	Stop containers	2026-10-24T06:16:55.6835472Z  syncing data to disk ... ok
test	Stop containers	2026-10-24T06:16:55.6835677Z  
test	Stop containers	2026-10-24T06:16:55.6835827Z  
test	Stop containers	2026-10-24T06:16:55.6836030Z  Success. You can now start the database server using:
test	Stop containers	2026-10-24T06:16:55.6836293Z  
test	Stop containers	2026-10-24T06:16:55.6836497Z      pg_ctl -D /var/lib/postgresql/data -l logfile start
test	Stop containers	2026-10-24T06:16:55.6836756Z  
test	Stop containers	2026-10-24T06:16:55.6837135Z  waiting for server to start....2026-10-24 06:16:23.363 UTC [41] LOG:  starting PostgreSQL 16.15 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
test	Stop containers	2026-10-24T06:16:55.6837730Z  2026-10-24 06:16:23.363 UTC [41] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
test	Stop containers	2026-10-24T06:16:55.6838278Z  2026-10-24 06:16:23.365 UTC [44] LOG:  database system was shut down at 2026-10-24 06:16:23 UTC
test	Stop containers	2026-10-24T06:16:55.6838733Z  2026-10-24 06:16:23.369 UTC [41] LOG:  database system is ready to accept connections
test	Stop containers	2026-10-24T06:16:55.6838939Z   done
test	Stop containers	2026-10-24T06:16:55.6839050Z  server started
test	Stop containers	2026-10-24T06:16:55.6839167Z  CREATE DATABASE
test	Stop containers	2026-10-24T06:16:55.6839281Z  
test	Stop containers	2026-10-24T06:16:55.6839376Z  
test	Stop containers	2026-10-24T06:16:55.6839687Z  /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
test	Stop containers	2026-10-24T06:16:55.6839913Z  
test	Stop containers	2026-10-24T06:16:55.6840120Z  waiting for server to shut down....2026-10-24 06:16:23.505 UTC [41] LOG:  received fast shutdown request
test	Stop containers	2026-10-24T06:16:55.6840410Z  2026-10-24 06:16:23.505 UTC [41] LOG:  aborting any active transactions
test	Stop containers	2026-10-24T06:16:55.6840726Z  2026-10-24 06:16:23.507 UTC [41] LOG:  background worker "logical replication launcher" (PID 47) exited with exit code 1
test	Stop containers	2026-10-24T06:16:55.6841031Z  2026-10-24 06:16:23.508 UTC [42] LOG:  shutting down
test	Stop containers	2026-10-24T06:16:55.6841248Z  2026-10-24 06:16:23.508 UTC [42] LOG:  checkpoint starting: shutdown immediate
test	Stop containers	2026-10-24T06:16:55.6841861Z  2026-10-24 06:16:23.585 UTC [42] LOG:  checkpoint complete: wrote 926 buffers (5.7%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.059 s, sync=0.018 s, total=0.078 s; sync files=301, longest=0.017 s, average=0.001 s; distance=4283 kB, estimate=4283 kB; lsn=0/1925D68, redo lsn=0/1925D68
test	Stop containers	2026-10-24T06:16:55.6842454Z  2026-10-24 06:16:23.591 UTC [41] LOG:  database system is shut down
test	Stop containers	2026-10-24T06:16:55.6842635Z   done
test	Stop containers	2026-10-24T06:16:55.6842741Z  server stopped
test	Stop containers	2026-10-24T06:16:55.6842855Z  
test	Stop containers	2026-10-24T06:16:55.6842988Z  PostgreSQL init process complete; ready for start up.
test	Stop containers	2026-10-24T06:16:55.6843165Z  
test	Stop containers	2026-10-24T06:16:55.6846812Z Stop and remove container: a83b267ba1864d9998aa2c51aa0681ec_postgres16alpine_d28be4
test	Stop containers	2026-10-24T06:16:55.6850905Z ##[command]/usr/bin/docker rm --force 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Stop containers	2026-10-24T06:16:55.8286666Z 0fc7c578dbc5f0b4112388176e362aecc2a789fd48af755a03b619d691da9fdd
test	Stop containers	2026-10-24T06:16:55.8311719Z Remove container network: github_network_d40593f89f804a2680838a0e96681556
test	Stop containers	2026-10-24T06:16:55.8314259Z ##[command]/usr/bin/docker network rm github_network_d40593f89f804a2680838a0e96681556
test	Stop containers	2026-10-24T06:16:55.9127058Z github_network_d40593f89f804a2680838a0e96681556
test	Complete job	﻿2026-10-24T06:16:55.9184317Z Cleaning up orphan processes
test	Complete job	2026-10-24T06:16:55.9464094Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/


```


## Question 23

```text

It should Create an account and add it to the database ... ok
It should Create an Account and assert that it exists ... ok
It should Delete an account from the database ... ok
It should Deserialize an account ... ok
It should not Deserialize an account with a KeyError ... ok
It should not Deserialize an account with a TypeError ... ok
It should Find an Account by name ... ok
It should List all Accounts in the database ... ok
It should Read an account ... ok
It should Serialize an account ... ok
It should Update an account ... ok
It should not Create an Account when sending the wrong data ... ok
It should allow configured origins and reject other origins. ... ok
It should Create a new Account ... ok
It should delete an account and allow repeated deletion. ... ok
It should filter accounts by name. ... ok
It should be healthy ... ok
It should get 200_OK from the Home Page ... ok
It should return a structured response for an internal error. ... ok
It should reject invalid types, lengths, dates and JSON shapes. ... ok
It should list all accounts and return an empty list when absent. ... ok
It should reject malformed JSON. ... ok
It should respond with a JSON 405 for unsupported methods. ... ok
It should default the join date and allow a missing phone. ... ok
It should read a created account using its Location header. ... ok
It should return 404 when an account is absent. ... ok
It should set Talisman security headers. ... ok
It should not Create an Account when sending the wrong media type ... ok
It should update an account and preserve its identifier. ... ok
It should reject incomplete updates and leave stored data unchanged. ... ok
It should return 404 when replacing an absent account. ... ok
It should call the db-create command ... ok

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
service\__init__.py                   20      0   100%
service\common\__init__.py             0      0   100%
service\common\cli_commands.py         7      0   100%
service\common\error_handlers.py      32      0   100%
service\common\log_handlers.py        10      1    90%   21
service\common\status.py              45      0   100%
service\config.py                     11      5    55%   12-16
service\models.py                     77      2    97%   32, 98
service\routes.py                     51      0   100%
----------------------------------------------------------------
TOTAL                                253      8    97%
----------------------------------------
Ran 32 tests in 5.128s

OK


```


## Question 30

```text

REPOSITORY          TAG       IMAGE ID       CREATED AT                      SIZE
customer-accounts   1.0       fa552051eb3d   2026-10-24 11:45:52 +0530 IST   231MB


```
