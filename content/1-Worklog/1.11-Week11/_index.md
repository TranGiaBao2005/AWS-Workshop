---
title: "Week 11 Worklog"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 11 Objectives:

- Master application containerization best practices using **Docker**, focusing on multi-stage builds, non-root user execution, and secure software supply chain principles.
- Administer secure enterprise container registries via **Amazon Elastic Container Registry (ECR)** (enforcing automated Lifecycle Policies and CVE Enhanced Scanning).
- Architect, deploy, and elastically scale serverless microservices using **Amazon Elastic Container Service (Amazon ECS)** powered by **AWS Fargate** (Workshop 000067).
- Dedicate **two full deep-dive days (Wednesday & Thursday)** to mastering the production enterprise Kubernetes ecosystem via **Amazon Elastic Kubernetes Service (Amazon EKS)** (Workshop 000126): from declarative cluster creation with `eksctl` and IAM Roles for Service Accounts (IRSA) to Helm-managed Ingress Controllers and Horizontal Pod Autoscaling (HPA).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and packaging the backend services of the **Capstone Project Proposal** into production-ready container images.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Hardened Docker Packaging & Registry Operations with Amazon ECR:** <br>- Authoring multi-stage Dockerfiles reducing runtime image sizes by over 70%. <br>- Applying container security baselines: Non-root user contexts and minimal base images. <br>- Creating Private ECR repositories, authenticating Docker CLI, and pushing versioned tags. <br>- Enforcing automated ECR Lifecycle Policies and inspecting Scan on Push CVE results. | 11/23/2026 | 11/23/2026 | [Cloud Journey - Containers](https://cloudjourney.awsfcaj.com/5-container/) |
| **Tuesday** | **Serverless Microservices Orchestration with Amazon ECS Fargate:** <br>- Provisioning networking-only ECS Clusters backed by AWS Fargate. <br>- Authoring Task Definitions (CPU/Memory limits, port mappings, Task Execution Roles). <br>- Deploying ECS Services connected to ALB Target Groups with Service Auto Scaling. <br>- Executing zero-downtime rolling update deployments across active service tasks. | 11/24/2026 | 11/24/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Wednesday** | **Amazon EKS (Part 1) - Kubernetes Cluster Setup & Fleet Management:** <br>- Deploying Amazon EKS v1.29 control planes and Managed Node Groups via `eksctl`. <br>- Configuring `kubeconfig` contexts and verifying node states with `kubectl get nodes`. <br>- Setting up IAM OIDC Providers and fine-grained IAM Roles for Service Accounts (IRSA). <br>- Deploying baseline Kubernetes objects: Namespaces, ConfigMaps, Secrets, and Pods. | 11/25/2026 | 11/25/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thursday** | **Amazon EKS (Part 2) - Production Ingress Routing & Dynamic HPA Scaling:** <br>- Authoring production Kubernetes Deployment and ClusterIP Service manifests. <br>- Installing the AWS Load Balancer Controller via Helm to automate ALB provisioning via Ingress. <br>- Deploying the Kubernetes Metrics Server to stream real-time pod compute telemetry. <br>- Configuring Horizontal Pod Autoscalers (HPA) to scale pods dynamically when CPU exceeds 70%. | 11/26/2026 | 11/26/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Friday** | **Week 11 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate Docker, ECR, ECS Fargate, and Amazon EKS architectures. <br>- **Worklog Completion:** Finalize bilingual Week 11 documentation and teardown lab resources. <br>- **Project Work:** Build and publish the Capstone Project backend Docker image to Amazon ECR. | 11/27/2026 | 11/27/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (11/23/2026) - Hardened Docker Packaging & Registry Operations via ECR

* **What did we learn today?**
  * **Optimization via Multi-Stage Docker Builds:** Separated compilation dependencies from production runtimes into two distinct stages: a `builder stage` incorporating SDKs and build tooling, and a minimal `runner stage` based on `alpine:3.19`. Reduced final container footprint from 850MB down to 75MB, accelerating network transfer and container cold-start speeds fivefold.
  * **Container Attack Surface Reduction:** Configured `USER appuser` directives within the Dockerfile, preventing runtime execution under root privileges and mitigating host compromise risks in the event of an application vulnerability.
  * **Enterprise Registry Hygiene with Amazon ECR:**
    * Provisioned private repository `fcaj/backend-api`.
    * Authenticated the local Docker client using STS credentials:
      ```bash
      aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 887086382708.dkr.ecr.us-east-1.amazonaws.com
      docker build -t fcaj/backend-api:v1.0 .
      docker tag fcaj/backend-api:v1.0 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
      docker push 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
      ```
    * Enforced Lifecycle Policies automatically pruning untagged images older than 14 days while retaining only the 10 most recent tagged releases.
    * Evaluated automated `Scan on Push` findings, verifying 0 CRITICAL CVEs and 1 low-priority dependency alert.
* **Encountered Challenges & Solutions:**
  * *Docker Authentication Token Expiry:* Running `docker push` resulted in `denied: Your authorization token has expired`. Root cause: ECR authorization tokens have an immutable 12-hour validity window. Solution: Re-invoked the `aws ecr get-login-password` retrieval piped directly into `docker login`.

---

#### 📌 Tuesday (11/24/2026) - Serverless Microservices Orchestration with ECS Fargate

* **What did we learn today?**
  * **Serverless Containerization Principles:** Evaluated differences between ECS EC2 Launch Types (requiring underlying host management) versus AWS Fargate (fully managed compute where users declare CPU/RAM envelopes and pay purely for actual resource runtime seconds).
  * **Production Task Definition Structure:**
    * Enforced resource envelopes: `0.5 vCPU` and `1GB RAM`.
    * Defined container port mapping on TCP port `8080`.
    * Enforced least-privilege IAM separation: `Task Execution Role` authorizes the ECS agent to pull ECR images and ship logs to CloudWatch (`/ecs/backend-api`), while the `Task Role` authorizes internal application code to interact with DynamoDB and S3.
  * **Service Orchestration Behind Application Load Balancer:** Registered tasks with an ALB Target Group configured with `/healthz` health checking.
  * **Zero-Downtime Deployments:** Configured rolling update parameters with `Minimum healthy percent = 100%` and `Maximum percent = 200%`. When deploying v1.1, ECS provisions new tasks, verifies ALB health passes, and drains older containers seamlessly without dropped client connections.
* **Encountered Challenges & Solutions:**
  * *Task Startup Failure (`CannotPullContainerError`):* Tasks placed in a private subnet failed immediately on launch. Root cause: The private subnet had no route to an internet gateway/NAT gateway and lacked VPC Interface Endpoints for ECR (`ecr.api`, `ecr.dkr`, `s3`). Solution: Configured private VPC Endpoints allowing tasks to pull container images privately across AWS internal backbones.

---

#### 📌 Wednesday (11/25/2026) - Amazon EKS (Part 1): Kubernetes Cluster Setup & Fleet Management

* **What did we learn today?**
  * **Enterprise Kubernetes Architecture on AWS:** Analyzed the managed control plane architecture of Amazon EKS, which automatically scales across 3 Availability Zones to deliver an enterprise-grade 99.95% SLA.
  * **Declarative Cluster Provisioning via `eksctl`:** Authored a cluster specification file `cluster-config.yaml` and deployed:
    ```yaml
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    metadata:
      name: fcaj-eks-cluster
      region: us-east-1
      version: "1.29"
    managedNodeGroups:
      - name: standard-workers
        instanceType: t3.medium
        desiredCapacity: 2
        minSize: 1
        maxSize: 4
        privateNetworking: true
    ```
    ```bash
    eksctl create cluster -f cluster-config.yaml
    kubectl get nodes -o wide
    ```
  * **IAM Roles for Service Accounts (IRSA):** Replaced broad Node Group IAM roles with fine-grained pod-level access. By configuring an IAM OpenID Connect (OIDC) identity provider for the cluster, individual Kubernetes ServiceAccounts are directly mapped to specific IAM Roles via annotations.
* **Encountered Challenges & Solutions:**
  * *`kubectl` Unauthorized Error on Secondary Workstations:* Teammates experienced `error: You must be logged in to the server (Unauthorized)`. Root cause: By default, only the IAM entity that initially created the EKS cluster possesses administrative RBAC bindings. Solution: Configured EKS Access Entries granting team IAM Roles administrative permissions within the cluster.

---

#### 📌 Thursday (11/26/2026) - Amazon EKS (Part 2): Production Ingress Routing & Dynamic HPA Scaling

* **What did we learn today?**
  * **Production Deployment Manifests:** Authored a production manifest declaring 2 replicas, standardizing Liveness and Readiness probes against port `8080/healthz`, and setting strict compute resource bounds (`resources: requests/limits`).
  * **Automated Ingress Routing with AWS Load Balancer Controller:** Bypassed legacy service-type LoadBalancers by deploying the official **AWS Load Balancer Controller** via Helm. The controller dynamically reconciles Kubernetes Ingress resources to provision an Application Load Balancer with path-based routing.
  * **Elastic Scaling with Horizontal Pod Autoscaler (HPA):**
    * Deployed the Kubernetes Metrics Server to ingest real-time CPU and memory metrics.
    * Established an HPA resource dynamically scaling pod replicas:
      ```bash
      kubectl autoscale deployment web-backend --cpu-percent=70 --min=2 --max=10
      kubectl get hpa
      ```
    * Executed synthetic load testing using `hey`, observing the autoscaler automatically spin up pods from 2 to 6 when CPU hit 85%, scaling back down after load stabilized.
* **Encountered Challenges & Solutions:**
  * *Ingress Failing to Provision ALB (`ADDRESS` Empty):* The Ingress resource remained without an assigned DNS hostname. Root cause: Inspected controller logs (`kubectl logs -n kube-system deployment.apps/aws-load-balancer-controller`), finding VPC subnets lacked required discovery tags. Solution: Added `kubernetes.io/role/elb = 1` to public subnets and `kubernetes.io/role/internal-elb = 1` to private subnets.

---

#### 📌 Friday (11/27/2026) - Week 11 Review, Worklog Finalization & Capstone Packaging

* **What did we learn today?**
  * **Container Platform Decision Matrix:** Synthesized trade-offs between ECS Fargate (low operational burden, ideal for straightforward microservices) and Amazon EKS (rich ecosystem, open standard, cloud-agnostic portability, higher operational investment).
  * **Disciplined Cluster Teardown:** Deleted Ingress resources to trigger automatic ALB release, followed by `eksctl delete cluster -f cluster-config.yaml` to tear down all node groups and CloudFormation stacks, eliminating the $0.10/hour EKS control plane fee.
  * **Capstone Project Packaging:** Completed a multi-stage production Dockerfile for the graduation project backend, published the image to ECR, and drafted container task definitions ready for the final capstone demonstration.
