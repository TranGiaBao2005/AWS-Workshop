---
title: "Week 11 Worklog"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 11 Objectives:

- Master containerization best practices using **Docker**, focusing on multi-stage builds, minimal attack surfaces, and non-root execution contexts.
- Manage secure enterprise container artifact repositories via **Amazon Elastic Container Registry (ECR)** (Lifecycle Policies and automated CVE vulnerability scanning).
- Architect, deploy, and scale serverless microservices utilizing **Amazon Elastic Container Service (Amazon ECS)** powered by **AWS Fargate** (Workshop 000067) fronted by an Application Load Balancer.
- Deploy and administer enterprise Kubernetes clusters utilizing **Amazon Elastic Kubernetes Service (Amazon EKS)** (Workshop 000126) managed via `eksctl` and `kubectl`.
- Evaluate developer-friendly managed container deployment options with **AWS App Runner** and hybrid enterprise platforms via **Red Hat OpenShift on AWS (ROSA)** (Workshop 000071).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and packaging the backend microservices of the **Capstone Project Proposal** into production-ready ECR images.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Docker Image Hardening & Registry Management with Amazon ECR:** <br>- Authoring multi-stage Dockerfiles to reduce final image footprints by over 70%. <br>- Provisioning private Amazon ECR repositories with IAM-governed access policies. <br>- Authenticating local Docker daemons, tagging artifacts, and pushing images to ECR. | 11/23/2026 | 11/23/2026 | [Cloud Journey - Containers](https://cloudjourney.awsfcaj.com/5-container/) |
| **Tuesday** | **Serverless Microservices Orchestration with Amazon ECS Fargate:** <br>- Creating a networking-only ECS Cluster backed by AWS Fargate. <br>- Designing Task Definitions (CPU/Memory allocations, port mappings, Execution Roles). <br>- Provisioning ECS Services linked to ALB target groups with Target Tracking Auto Scaling. | 11/24/2026 | 11/24/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Wednesday** | **Managed Kubernetes Cluster Deployment with Amazon EKS:** <br>- Provisioning an Amazon EKS control plane and managed node groups via `eksctl`. <br>- Configuring `kubeconfig` contexts and verifying node states with `kubectl`. <br>- Deploying Kubernetes primitives: Deployments, ClusterIP Services, Ingress, and HPA. | 11/25/2026 | 11/25/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thursday** | **Streamlined Container Deployment with AWS App Runner & ROSA:** <br>- Deploying containerized web services directly from source code and ECR via AWS App Runner. <br>- Analyzing Red Hat OpenShift on AWS (ROSA) deep infrastructure integration patterns. <br>- Evaluating cost, management complexity, and runtime ergonomics across ECS, EKS, and App Runner. | 11/26/2026 | 11/26/2026 | [ROSA Workshop (000071)](https://000071.awsfcaj.com/) |
| **Friday** | **Week 11 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate ECR, ECS Fargate, Amazon EKS, and App Runner architectures. <br>- **Worklog Completion:** Finalize bilingual Week 11 documentation and teardown lab resources. <br>- **Project Work:** Push the Capstone Project backend Docker image to Amazon ECR and configure ECS Tasks. | 11/27/2026 | 11/27/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 11 Achievements:

#### 📌 Monday (11/23/2026) - Container Hardening & Registry Management:
* **Footprint Optimization:** Implemented multi-stage Docker builds separating compile-time dependencies from lightweight production runtimes, slashing image sizes from 850MB to 75MB.
* **Supply Chain Security:** Configured automated Amazon ECR "Scan on Push" to inspect container images for known vulnerabilities, establishing continuous security baselines against public CVE databases.

#### 📌 Tuesday (11/24/2026) - Serverless Containers on ECS Fargate:
* **Zero Host Management:** Deployed microservice tasks onto AWS Fargate, abstracting away underlying EC2 instances, OS maintenance, and node cluster provisioning.
* **Zero-Downtime Rolling Upgrades:** Configured rolling deployments with minimum healthy capacity at 100% and maximum at 200%, verifying that user traffic routed uninterrupted during service upgrades.

#### 📌 Wednesday (11/25/2026) - Managed Kubernetes on Amazon EKS:
* **Standardized Orchestration:** Provisioned an enterprise-grade Kubernetes cluster using `eksctl` with automated IAM OIDC provider integration for granular service account role binding (IRSA).
* **Dynamic Workload Scaling:** Deployed Horizontal Pod Autoscalers (HPA) responding dynamically to CPU metrics, scaling replica counts from 2 to 10 pods during simulated load tests.

#### 📌 Thursday (11/26/2026) - Rapid App Delivery with AWS App Runner:
* **Accelerated Time to Market:** Demonstrated end-to-end container deployment to a public HTTPS endpoint in under 3 minutes using AWS App Runner, bypassing manual load balancer and certificate setup.
* **Cost-Effective Auto Scaling:** Validated automatic request-based scaling to zero when idle, minimizing compute costs for low-traffic staging environments.
