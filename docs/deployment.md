# Kubernetes and Tekton deployment

Use a namespace dedicated to this capstone. Never use a production database for tests.
Install Tekton Pipelines v1 in your cluster before applying `tekton/` resources.

## Kubernetes

Build and push the Docker image to a registry your cluster can access, or load
`customer-accounts:1.0` into a local cluster. Provision PostgreSQL separately.

```sh
kubectl create namespace customer-accounts
kubectl -n customer-accounts create secret generic accounts-db \
  --from-literal=uri='postgresql://USER:PASSWORD@DATABASE_HOST:5432/accounts'
kubectl -n customer-accounts apply -f k8s/accounts.yaml
kubectl -n customer-accounts set image deployment/accounts accounts=YOUR_REGISTRY/accounts:1.0
kubectl -n customer-accounts rollout status deployment/accounts --timeout=180s
kubectl -n customer-accounts get deployments,pods,replicasets,services > evidence/kube-deploy-accounts
kubectl -n customer-accounts port-forward service/accounts 8080:8080
# In a second terminal:
curl http://localhost:8080/ > evidence/kube-app-output
```

The values in uppercase are deployment-specific inputs. Do not submit placeholder values.
For a cloud cluster, configure an ingress and enable `FORCE_HTTPS` when appropriate.

## Tekton

The pipeline clones the repository, lints, runs nosetests, builds and pushes an image,
then applies the Kubernetes deployment and waits for rollout. It uses a dedicated
test database and a registry secret; it does not run tests against the application database.

Create `accounts-test-db` with key `uri` pointing to a separate, disposable PostgreSQL
database. Create a `registry-credentials` secret with a Docker `config.json` key
containing credentials for the image registry. Never commit either secret.

```sh
kubectl -n customer-accounts apply -f tekton/rbac.yaml
kubectl -n customer-accounts apply -f tekton/tasks.yaml
kubectl -n customer-accounts apply -f tekton/pipeline.yaml
```

Edit `tekton/pipelinerun.yaml` to set the actual registry/image destination, then:

```sh
kubectl -n customer-accounts create -f tekton/pipelinerun.yaml
tkn -n customer-accounts pipelinerun logs --last -f > evidence/pipelinerun.txt
```

Verify the PipelineRun's `Succeeded` condition and the deployment rollout before
marking the CD story complete. Buildah requires a namespace that permits its privileged
build container. Check your cluster's policy before running this pipeline.

## Verified local execution

On 24 October 2026, the service was deployed to the `accounts-capstone` k3d cluster
(Kubernetes v1.35.5+k3s1), namespace `customer-accounts`. Tekton Pipelines v1.17.1
completed PipelineRun `accounts-cd-gpd2m` with all four tasks successful and none failed.
The pipeline built and pushed `accounts-registry:5000/customer-accounts:cd-1`, then
rolled out the accounts deployment. The app and PostgreSQL each had one ready replica.

Local configuration is in `k8s/postgres-local.yaml` and `tekton/pipelinerun-local.yaml`.
The database password was randomly generated and is held only in Kubernetes Secrets.
The local Docker registry does not use authentication or TLS and is intended only for
this local development environment. Remote registries should use the default TLS verification.

Captured evidence: `evidence/kube-app-output`, `evidence/kube-deploy-accounts`, and
`evidence/pipelinerun.txt`. The latter contains logs from every container in all four
Tekton task pods, with task and container prefixes.
