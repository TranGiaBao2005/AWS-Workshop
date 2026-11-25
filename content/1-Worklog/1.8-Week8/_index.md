---
title: "Week 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---


### Objectives for Week 8:

- Adopt **Infrastructure as Code (IaC)** workflows to automate provisioning, version-control infrastructure definitions, and guarantee repeatable cloud environments on AWS.
- Master **AWS CloudFormation** (Workshop 000037): YAML template anatomy, intrinsic functions, Nested Stacks, Change Sets, Drift Detection, and Termination Protection.
- Model modern cloud infrastructure using **AWS Cloud Development Kit (AWS CDK)** in TypeScript across L1, L2, and L3 Constructs.
- Perform zero-SSH fleet administration with **AWS Systems Manager (SSM)** (Workshop 000024) and enforce ransomware-resistant backup policies using **AWS Backup** (Workshop 000038).
- Dedicate Friday to consolidating weekly learnings, updating bilingual Worklogs, cleaning up test stacks, and codifying the Capstone Project infrastructure.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Infrastructure as Code with AWS CloudFormation:** <br>- Author YAML templates with Parameters, Mappings, Conditions, Resources, Outputs, and intrinsic functions (`!Ref`, `!Sub`, `!GetAtt`). <br>- Modularize multi-tier workloads using Nested Stacks (Network, DB, App). <br>- Govern updates safely with Change Sets, detect manual edits via Drift Detection, and enable Termination Protection. | 02/11/2026 | 02/11/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Tuesday** | **Software-Defined Infrastructure with AWS CDK:** <br>- Install CDK CLI, initialize a TypeScript project (`cdk init app --language typescript`), and run `cdk bootstrap`. <br>- Differentiate and apply L1 (`Cfn*`), L2 (AWS best-practice defaults), and L3 (architectural pattern) Constructs. <br>- Execute end-to-end `cdk synth`, `cdk diff`, `cdk deploy`, and `cdk destroy`. | 03/11/2026 | 03/11/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Wednesday** | **Zero-SSH Fleet Operations with AWS Systems Manager (SSM):** <br>- Access EC2 instances in private subnets securely via SSM Session Manager with S3/CloudWatch Session Logging. <br>- Run automated maintenance scripts across tagged instances using SSM Run Command. <br>- Store encrypted configuration parameters and secrets via SSM Parameter Store (`SecureString` + KMS). | 04/11/2026 | 04/11/2026 | [AWS Systems Manager (000024)](https://000024.awsfcaj.com/) |
| **Thursday** | **Centralized Backup & Disaster Recovery with AWS Backup:** <br>- Create Backup Vaults protected by WORM (`Vault Lock`) against premature deletion or ransomware. <br>- Configure tag-driven Backup Plans for daily Amazon EBS and Amazon RDS snapshots. <br>- Execute a restore drill to validate data integrity and measure RTO/RPO. | 05/11/2026 | 05/11/2026 | [AWS Backup (000038)](https://000038.awsfcaj.com/) |
| **Friday** | **Week 8 Review, Worklog & Project:** <br>- **Knowledge Synthesis:** Consolidate CloudFormation, CDK, SSM, and AWS Backup patterns. <br>- **Worklog & Cleanup:** Complete bilingual Week 8 documentation and tear down test stacks. <br>- **Capstone Project:** Package core network and compute infrastructure into reusable IaC templates. | 06/11/2026 | 06/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily Learning Details & Results:

#### 📌 Monday (02/11/2026) - Comprehensive Infrastructure as Code with AWS CloudFormation

* **What did I learn today?**
  * **YAML Template Anatomy & Intrinsic Functions:** Authored `network-foundation.yaml` provisioning a Multi-AZ VPC (`10.0.0.0/16`), public/private subnets, Internet Gateway, and Route Tables, linking resources dynamically via `!Ref`, `!Sub`, `!GetAtt`, and `!Join`.
  * **Nested Stacks & Safe Change Governance:** Split a root stack referencing modular child templates (`network`, `database`, `compute`) hosted in S3. Used **Change Sets** to preview `Add / Modify / Replace` impacts before applying updates, ran **Drift Detection** to catch console-level configuration drift, and enabled **Termination Protection**.
  * **AWS CLI Workflow:**
    ```bash
    aws cloudformation create-stack \
      --stack-name fcaj-network-stack \
      --template-body file://network-foundation.yaml \
      --parameters ParameterKey=EnvironmentName,ParameterValue=Development
    aws cloudformation detect-stack-drift --stack-name fcaj-network-stack
    ```
* **Challenges & Resolutions:**
  * *IGW Route race condition & `UPDATE_ROLLBACK_FAILED`:* Added explicit `DependsOn: AttachGateway` on `AWS::EC2::Route` to guarantee attachment order, and used `Continue Update Rollback` with resource skipping to recover a stuck Subnet Group update.

---

#### 📌 Tuesday (03/11/2026) - Software-Defined Infrastructure with AWS CDK

* **What did I learn today?**
  * **Programming Cloud Infrastructure:** Leveraged TypeScript loops, conditionals, and compile-time type safety to eliminate repetitive boilerplate YAML.
  * **Construct Abstraction Tiers:**
    * *L1 (`Cfn*`):* Direct 1:1 mappings to raw CloudFormation resource specifications.
    * *L2 (Curated AWS Constructs):* Pre-wired security defaults and automated subnetting (e.g., `new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 })`).
    * *L3 (Patterns):* Turnkey multi-service architectures such as `ApplicationLoadBalancedFargateService`.
  * **CDK CLI Lifecycle:**
    ```bash
    cdk bootstrap aws://887086382708/us-east-1
    cdk synth && cdk diff && cdk deploy
    ```
* **Challenges & Resolutions:**
  * *Missing Bootstrap Toolkit & v1/v2 package conflicts:* Executed `cdk bootstrap` once per account/region to provision `CDKToolkit`, and standardized all dependencies on the unified `aws-cdk-lib` v2 package.

---

#### 📌 Wednesday (04/11/2026) - Zero-SSH Fleet Operations with AWS Systems Manager

* **What did I learn today?**
  * **Zero-Trust Access with SSM Session Manager:** Eliminated inbound SSH port 22 completely, connecting to private-subnet EC2 terminals directly over AWS APIs while streaming full audit logs to S3 and CloudWatch Logs.
  * **Fleet Automation & Secrets Management:** Executed batch maintenance scripts across tagged instances with SSM Run Command and stored KMS-encrypted application secrets as `SecureString` entries in Parameter Store.
* **Challenges & Resolutions:**
  * *EC2 instances missing from SSM Managed Nodes:* Attached an IAM Instance Profile with `AmazonSSMManagedInstanceCore` and provisioned VPC Interface Endpoints (`ssm`, `ssmmessages`, `ec2messages`) for isolated private subnets.

---

#### 📌 Thursday (05/11/2026) - Centralized Backup & Disaster Recovery with AWS Backup

* **What did I learn today?**
  * **Policy-Driven Protection with AWS Backup:** Configured tag-based Backup Plans (`Backup=Daily`) automating snapshots across EBS Volumes and Amazon RDS with 30-day retention lifecycles.
  * **Ransomware Resilience via Vault Lock (WORM):** Enforced *Write Once, Read Many* immutability on the Backup Vault so recovery points cannot be deleted prematurely even by compromised admin credentials.
  * **Restore Verification Drill:** Restored a test EBS volume from an AWS Backup recovery point to validate data integrity and measure operational RTO.
* **Challenges & Resolutions:**
  * *Tag-based Backup Selection missed target resources:* Resolved case-sensitive tag key mismatches and ensured the backup service role attached `AWSBackupServiceRolePolicyForBackup`.

---

#### 📌 Friday (06/11/2026) - Week 8 Review, Worklog & Capstone IaC Packaging

* **What did I learn today?**
  * **End-to-End IaC & Operations Loop:** Connected declarative provisioning (CloudFormation/CDK), port-less fleet administration (SSM), and immutable data protection (AWS Backup) into a cohesive operational baseline.
  * **Cost Hygiene Audit:** Executed `cdk destroy` and `aws cloudformation delete-stack`, verifying zero lingering billable resources in Cost Explorer.
  * **Capstone Project Advancement:** Codified the core network and compute foundation of the Capstone Project into modular IaC templates.

---

### Next Week's Objectives (Week 9):

- **Cloud Migration & Database Replication:** Apply the 7Rs framework, execute VM Import/Export (000027), AWS MGN, AWS DMS (000031), and AWS SCT.
- **Extended Hybrid Networking & Bulk Data Transfer:** Deploy AWS Transit Gateway (Hub-and-Spoke), AWS DataSync, and AWS Storage Gateway.

