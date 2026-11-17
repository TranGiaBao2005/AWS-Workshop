---
title: "Week 2 Worklog"
date: 2026-09-21
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 2 Objectives:

- Master workload optimization principles according to the **AWS Well-Architected Framework** under the [Optimizing the System on AWS](https://cloudjourney.awsfcaj.com/3-optimize/) curriculum.
- Explore event-driven serverless operational automation (**AWS Lambda**), centralized observability, and Infrastructure as Code foundations.
- Implement cryptographic data protection (**AWS KMS**), web application perimeter defense (**AWS WAF**), and continuous threat detection (**Amazon GuardDuty**).
- Deploy serverless microservices container packaging (**Amazon ECS Fargate**) alongside automated Continuous Integration and Continuous Deployment pipelines (**CI/CD**).
- Formulate long-term cost governance strategies (**Savings Plans**) and serverless expense telemetry analytics via **AWS Glue & Amazon Athena**.
- Dedicate Friday to synthesizing weekly technical knowledge, finalizing comprehensive Worklog documentation, and advancing the internship **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Operational Excellence & Serverless Automation:** <br>- Automating administrative tasks with [AWS Lambda (000022)](https://000022.awsfcaj.com). <br>- Advanced observability with [CloudWatch & Grafana (000029)](https://000029.awsfcaj.com). <br>- Infrastructure as Code concepts with [AWS CloudFormation (000037)](https://000037.awsfcaj.com). | 09/21/2026 | 09/21/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Tuesday** | **Security & Cryptographic Data Protection:** <br>- Centralized encryption key management with [AWS KMS (000033)](https://000033.awsfcaj.com). <br>- Web layer perimeter defense using [AWS WAF (000026)](https://000026.awsfcaj.com). <br>- Intelligent threat detection with [Amazon GuardDuty (000098)](https://000098.awsfcaj.com). | 09/22/2026 | 09/22/2026 | [Cloud Journey - Security](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Wednesday** | **Reliability & Serverless Containers:** <br>- Microservices containerization via [Docker & Amazon ECS Fargate (000016)](https://000016.awsfcaj.com). <br>- Automated software delivery pipelines via [AWS CodePipeline (000017)](https://000017.awsfcaj.com). | 09/23/2026 | 09/23/2026 | [Cloud Journey - Reliability](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Thursday** | **Cost Optimization & Telemetry Analytics:** <br>- Long-term financial commitments via [Savings Plans & Reserved Instances (000042)](https://000042.awsfcaj.com). <br>- Serverless cost analytics with [AWS Glue & Athena (000040)](https://000040.awsfcaj.com). | 09/24/2026 | 09/24/2026 | [Cloud Journey - Cost](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Friday** | **Week 2 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate the 4 Well-Architected pillars mastered (Operations, Security, Reliability, Cost). <br>- **Worklog Completion:** Finalize bilingual Week 2 documentation and execute clean resource teardowns. <br>- **Project Work:** Refine architectural schematics and compute monthly budget models for the Capstone Proposal. | 09/25/2026 | 09/25/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (09/21/2026) - Operational Excellence & Serverless Automation

* **What did we learn today?**
  * **Event-Driven Serverless Compute with AWS Lambda:**
    * Mastered serverless compute abstraction: Eliminating OS patching and capacity management, executing code only in response to discrete triggers.
    * Developed an automated maintenance function `ec2-nightly-stop` in Python using Boto3 to discover development instances matching `Environment = Development` and issue termination signals at 20:00 daily.
  * **Automated Event Scheduling via EventBridge & CloudWatch:**
    * Established an **Amazon EventBridge Scheduler** cron expression `cron(0 20 ? * MON-FRI *)` invoking the Lambda handler automatically.
    * Streamed execution telemetry into CloudWatch Logs Group `/aws/lambda/ec2-nightly-stop`, measuring cold-start durations of 1.2 seconds and memory allocations under 64MB.

![Lambda Serverless Automation](/images/1-Worklog/1.2-Week2/lambda-serverless-automation.png)
*Figure 1.2.1: Automated serverless EC2 operational management triggered by EventBridge and AWS Lambda.*

* **Encountered Challenges & Solutions:**
  * *`AccessDeniedException` on Function Execution:* The Lambda handler failed with unauthorized API call errors when invoking EC2 APIs. Root cause: Default basic execution roles only permit writing CloudWatch Logs. Solution: Created an IAM customer-managed policy authorizing `ec2:DescribeInstances` and `ec2:StopInstances` attached to the function execution role.

---

#### 📌 Tuesday (09/22/2026) - Security Hardening & Cryptographic Key Management

* **What did we learn today?**
  * **Envelope Encryption & Lifecycle Governance with AWS KMS:**
    * Differentiated between AWS Managed Keys and Customer Managed Keys (CMK).
    * Created symmetric CMK `fcaj-data-encryption-key`, defining granular Key Policies controlling which IAM principals can invoke `kms:Encrypt` and `kms:Decrypt`.
    * Enabled Automatic Annual Key Rotation without changing key ARNs.
    * Applied CMK encryption across Amazon EBS storage volumes and Amazon S3 objects (SSE-KMS) with full audit logging in CloudTrail.
  * **Web Application Defense via AWS WAF:**
    * Created and deployed a regional Web ACL protecting Application Load Balancers.
    * Configured pre-packaged AWS Managed Rules: `Core rule set (CRS)` for OWASP Top 10 vulnerabilities, `Amazon IP reputation list` blocking malicious scanners, and a Rate-based rule capping traffic at 100 requests per 5 minutes per IP.
  * **Intelligent Threat Detection with Amazon GuardDuty:**
    * Activated GuardDuty to passively analyze VPC Flow Logs, DNS logs, and CloudTrail management events using machine learning to detect port scans and compromised credentials.

![KMS Encryption Architecture](/images/1-Worklog/1.2-Week2/kms-encryption-architecture.png)
*Figure 1.2.2: S3 data-at-rest encryption control model governed by AWS KMS and audited via CloudTrail.*

![AWS WAF Security Shield](/images/1-Worklog/1.2-Week2/waf-security-shield.png)
*Figure 1.2.3: Perimeter defense shield protecting application entry points against web threats using AWS WAF.*

* **Encountered Challenges & Solutions:**
  * *False-Positive Block on Legitimate API Payloads:* Valid client requests were blocked with HTTP 403 by the `GenericRFI_BODY` rule. Solution: Inspected CloudWatch WAF metrics to identify the specific rule ID, toggled the rule to `Count` mode to log telemetry without dropping packets, and configured path-specific rule exclusions.

---

#### 📌 Wednesday (09/23/2026) - Resilience & Serverless Microservices Containers

* **What did we learn today?**
  * **Serverless Container Orchestration with Amazon ECS Fargate:**
    * Packaged microservice application code into Docker images and published versioned artifacts to Amazon Elastic Container Registry (ECR).
    * Authored ECS Task Definitions specifying container compute footprints (`0.25 vCPU`, `512MB RAM`), eliminating underlying host OS administration.
    * Launched an ECS Service running on **AWS Fargate** behind an Application Load Balancer with dynamic health checking and self-healing task replacement.
  * **Continuous Delivery Automation via AWS CodePipeline:**
    * Engineered an automated CI/CD pipeline: Pulling source updates from GitHub ➔ Triggering **AWS CodeBuild** to compile Docker images and execute unit tests ➔ Executing rolling deployments to ECS Fargate tasks with zero downtime.

![ECS Fargate Cluster Architecture](/images/1-Worklog/1.2-Week2/ecs-fargate-cluster-arch.png)
*Figure 1.2.4: Multi-container service orchestration architecture on Amazon ECS elastically scaled via AWS Fargate.*

![CI/CD Pipeline Succeeded](/images/1-Worklog/1.2-Week2/cicd-codebuild-succeeded.png)
*Figure 1.2.5: Successful automated build and deployment report in AWS CodeBuild.*

* **Encountered Challenges & Solutions:**
  * *Docker Hub Pull Rate Limiting in CodeBuild:* Builds failed during base image acquisition. Solution: Updated Dockerfiles to pull official base images from the Amazon ECR Public Gallery (`public.ecr.aws/docker/library/`), bypassing third-party rate limits and improving download speeds over AWS internal networks.

---

#### 📌 Thursday (09/24/2026) - Cost Optimization & Telemetry Analytics

* **What did we learn today?**
  * **Strategic Cloud Financial Management:**
    * Analyzed cost structures across On-Demand, Spot instances (up to 90% discount for fault-tolerant workloads), and 1- to 3-year commitments (**Savings Plans** & **Reserved Instances**).
    * For steady-state 24/7 database and backend tiers, Compute Savings Plans yield 45% to 66% sustained cost reductions compared to standard On-Demand pricing.
  * **Serverless Telemetry Analytics with AWS Glue & Athena:**
    * Configured **AWS Cost and Usage Reports (CUR)** delivering granular hourly billing manifests into an S3 bucket.
    * Deployed an **AWS Glue Crawler** to discover report schemas and generate partition metadata in the AWS Glue Data Catalog.
    * Executed serverless SQL queries in **Amazon Athena** to identify spending spikes per service, peak regional usage hours, and unattached idle EBS volumes.

![Glue Athena Cost Analytics](/images/1-Worklog/1.2-Week2/glue-athena-cost-analytics.png)
*Figure 1.2.6: Cloud cost data extraction, cataloging, and analytical query workflow utilizing AWS Glue and Amazon Athena.*

* **Encountered Challenges & Solutions:**
  * *Athena Syntax Errors Reading Compressed CUR Manifests:* Direct queries threw syntax errors on gzipped micro-batch files. Solution: Deployed the automated CloudFormation integration template provided by AWS CUR, configuring standardized month-based partition indexing for Athena.

---

#### 📌 Friday (09/25/2026) - Week 2 Review, Worklog Finalization & Proposal Formulation

* **What did we learn today?**
  * **AWS Well-Architected Pillar Synthesis:**
    * **Operational Excellence:** Event-driven automation with Lambda and observability via CloudWatch.
    * **Security:** Envelope encryption via KMS and perimeter defense via WAF.
    * **Reliability:** Microservices containerization via ECS Fargate and automated CI/CD deployments.
    * **Cost Optimization:** Strategic commitment models and serverless billing audits with Athena.
  * **Resource Hygiene:** Decommissioned test ECS services, halted crawler jobs, and detached staging Web ACLs to preserve financial guardrails.
  * **Capstone Proposal Development:** Finalized full system architecture blueprints and drafted detailed monthly operational cost projections utilizing the official **AWS Pricing Calculator**.
