---
title: "Week 10"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Objectives for Week 10:

- Master **Serverless & Event-Driven Architecture (EDA)** with **Amazon API Gateway**, **Amazon SQS** (Workshop 000078), **Amazon SNS**, **Amazon EventBridge**, and **AWS Step Functions**.
- Standardize container packaging using **Docker Multi-Stage Builds**, secure private registries in **Amazon ECR**, and run serverless microservices on **Amazon ECS Fargate** (Workshop 000067).
- Provision and autoscale enterprise Kubernetes workloads on **Amazon EKS** (Workshop 000126) with `eksctl`, IRSA, AWS Load Balancer Controller, and Horizontal Pod Autoscaler (HPA).
- Dedicate Friday to consolidating weekly learnings, updating bilingual Worklogs, tearing down test clusters, and integrating decoupled messaging and containerization into the Capstone Project.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Amazon API Gateway & Workload Decoupling with Amazon SQS:** <br>- Compare REST API vs HTTP API; configure CORS, Lambda JWT Authorizers, and Token Bucket Throttling. <br>- Deploy Standard vs FIFO SQS queues and reduce polling costs using Long Polling (`20s`). <br>- Configure Visibility Timeout and Dead-Letter Queues (DLQ) with Redrive Policies. | 16/11/2026 | 16/11/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Tuesday** | **Pub/Sub Routing (SNS/EventBridge) & AWS Step Functions:** <br>- Build a Fanout architecture fanning one SNS Topic to multiple independent SQS Queues. <br>- Configure Amazon EventBridge Event Buses with JSON Event Pattern Filtering rules. <br>- Design State Machines in Workflow Studio combining Task, Choice, Parallel, and Retry/Catch logic. | 17/11/2026 | 17/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Wednesday** | **Docker Multi-Stage, Amazon ECR & Amazon ECS Fargate:** <br>- Author optimized Multi-Stage Dockerfiles running under a non-root user. <br>- Push images to private Amazon ECR with Lifecycle Policies and CVE Scan on Push. <br>- Deploy ECS Fargate Services behind an ALB and verify Zero-Downtime Rolling Updates. | 18/11/2026 | 18/11/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Thursday** | **Enterprise Kubernetes Orchestration with Amazon EKS:** <br>- Provision an Amazon EKS cluster and Managed Node Groups via `eksctl` and configure `kubeconfig`. <br>- Enable IAM OIDC Provider for pod-level least-privilege permissions (IRSA). <br>- Install AWS Load Balancer Controller (ALB Ingress), Metrics Server, and configure HPA pod scaling. | 19/11/2026 | 19/11/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Friday** | **Week 10 Review, Worklog & Project:** <br>- **Knowledge Synthesis:** Consolidate Serverless EDA and Container Orchestration (ECS/EKS) patterns. <br>- **Worklog & Cleanup:** Finalize bilingual Week 10 entries and delete EKS/ECS test clusters. <br>- **Capstone Project:** Integrate async SQS decoupling and containerize backend services in ECR. | 20/11/2026 | 20/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily Learning Details & Results:

#### 📌 Monday (16/11/2026) - Hardening Amazon API Gateway & Decoupling with Amazon SQS

* **What did I learn today?**
  * **Amazon API Gateway (REST vs HTTP API):** HTTP API delivers lower latency and >70% cost savings for lightweight microservices, while REST API provides Usage Plans, API Keys, WAF integration, and Private Endpoints. Implemented a Lambda Custom Authorizer for JWT validation and configured Rate/Burst Throttling.
  * **Asynchronous Decoupling with Amazon SQS:** Contrasted Standard Queues (*at-least-once*, near-unlimited throughput) with FIFO Queues (*exactly-once*, ordered per `MessageGroupId`). Configured Long Polling (`ReceiveMessageWaitTimeSeconds = 20`), `VisibilityTimeout = 30s`, and a DLQ Redrive Policy (`maxReceiveCount = 3`).
* **Challenges & Resolutions:**
  * *Browser CORS rejections & duplicate worker processing:* Enabled `OPTIONS` preflight methods with explicit `Access-Control-Allow-*` headers on API Gateway, and called `change_message_visibility` dynamically for long-running jobs exceeding 30s.

---

#### 📌 Tuesday (17/11/2026) - Amazon SNS Fanout, EventBridge & AWS Step Functions

* **What did I learn today?**
  * **SNS Fanout & EventBridge Content Filtering:** Subscribed multiple SQS queues to a single SNS Topic for parallel downstream processing, and configured JSON content-based EventBridge routing rules:
    ```json
    {
      "source": ["app.events"],
      "detail-type": ["JobSubmitted"],
      "detail": { "priority": ["HIGH"] }
    }
    ```
  * **Workflow Orchestration with AWS Step Functions:** Built Amazon States Language (ASL) workflows combining `Task`, `Choice`, and `Parallel` states with exponential backoff `Retry` (`BackoffRate = 2.0`) and `Catch` compensating branches.
* **Challenges & Resolutions:**
  * *Empty SQS queues after SNS publish & state payload mismatches:* Granted `sqs:SendMessage` to the SNS Topic ARN in the SQS Access Policy, and applied `InputPath`, `ResultPath`, and `OutputPath` JSONPath filters between Step Functions states.

---

#### 📌 Wednesday (18/11/2026) - Docker Multi-Stage, Amazon ECR & Amazon ECS Fargate

* **What did I learn today?**
  * **Lean Container Builds & Amazon ECR:** Separated compile-time dependencies (`builder` stage) from minimal runtime images (`alpine`/`distroless`) with `USER appuser` (non-root), shrinking image size and attack surface while enabling ECR Lifecycle Policies and `Scan on Push`.
    ```bash
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 887086382708.dkr.ecr.us-east-1.amazonaws.com
    docker build -t fcaj/backend-api:v1.0 .
    docker tag fcaj/backend-api:v1.0 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
    docker push 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
    ```
  * **Serverless Containers on Amazon ECS Fargate:** Strictly separated the `Task Execution Role` (ECR pulls & CloudWatch log delivery) from the `Task Role` (application AWS permissions), deploying behind an ALB with `Minimum healthy percent = 100%` and `Maximum percent = 200%` for zero-downtime rolling updates.
* **Challenges & Resolutions:**
  * *`CannotPullContainerError` inside Private Subnets:* Verified NAT Gateway routes or provisioned VPC Interface/Gateway Endpoints (`ecr.api`, `ecr.dkr`, `s3`) so Fargate tasks pull private images reliably.

---

#### 📌 Thursday (19/11/2026) - Enterprise Kubernetes Orchestration with Amazon EKS

* **What did I learn today?**
  * **EKS Provisioning & IRSA Least Privilege:** Provisioned an EKS cluster with Managed Node Groups via `eksctl` and enabled IAM OIDC Provider to bind scoped IAM Roles directly to Kubernetes `ServiceAccount` objects (IRSA) instead of over-privileged node roles.
    ```bash
    eksctl create cluster --name fcaj-eks-cluster --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2
    kubectl autoscale deployment web-backend --cpu-percent=70 --min=2 --max=10
    ```
  * **ALB Ingress & Horizontal Pod Autoscaler (HPA):** Installed the **AWS Load Balancer Controller** via Helm to reconcile Kubernetes Ingress resources into ALBs, paired with Metrics Server and HPA to scale pods dynamically based on CPU thresholds.
* **Challenges & Resolutions:**
  * *Ingress remained without an external ALB `ADDRESS`:* Added mandatory discovery tags `kubernetes.io/role/elb = 1` on public subnets and `kubernetes.io/role/internal-elb = 1` on private subnets.

---

#### 📌 Friday (20/11/2026) - Week 10 Review, Worklog & Capstone Containerization

* **What did I learn today?**
  * **Modern Distributed Architecture Synthesis:** Bridged asynchronous event-driven patterns (API Gateway, SQS, SNS, EventBridge, Step Functions) with portable container platforms (ECR, ECS Fargate, EKS).
  * **High-Cost Cluster Teardown:** Executed `eksctl delete cluster` immediately after lab verification to avoid ongoing EKS Control Plane charges ($0.10/hour) and removed test ALBs/ECS services.
  * **Capstone Project Progress:** Designed asynchronous queue decoupling and packaged backend application images for Amazon ECR.

---

### Next Week's Objectives (Week 11):

- **Big Data Analytics & Data Lakes:** AWS Lake Formation (000035), AWS Glue ETL (Parquet), Amazon Athena (000106), Kinesis, QuickSight (000073), and Redshift.
- **Generative AI & MLOps on AWS:** Amazon Bedrock Foundation Models, RAG Knowledge Bases, Bedrock Agents, and Amazon SageMaker.
