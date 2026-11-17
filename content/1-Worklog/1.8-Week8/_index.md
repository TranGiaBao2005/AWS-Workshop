---
title: "Week 8 Worklog"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 8 Objectives:

- Master the **Infrastructure as Code (IaC)** paradigm to automate resource provisioning, version control, and multi-environment reproducibility on AWS.
- Implement declarative resource stacks using **AWS CloudFormation** (Workshop 000037) with standardized YAML/JSON templates.
- Explore modern software-defined infrastructure via the **AWS Cloud Development Kit (AWS CDK)**, defining cloud topology with familiar object-oriented programming languages.
- Execute secure, credential-less server fleet operations and automated patch management with **AWS Systems Manager (SSM)** (Workshop 000024).
- Establish centralized enterprise data protection policies and ransomware safeguards using **AWS Backup** (Workshop 000038).
- Dedicate Friday to synthesizing technical knowledge, perfecting Worklog documentation, and refactoring manual resources in the internship **Capstone Project Proposal** into reusable IaC templates.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Automated Infrastructure Provisioning with AWS CloudFormation:** <br>- Template anatomy (AWSTemplateFormatVersion, Parameters, Resources, Outputs). <br>- Provisioning and managing stacks and nested stacks. <br>- Change Sets validation prior to deployment and Drift Detection. | 11/02/2026 | 11/02/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Tuesday** | **Modern Software-Defined Infrastructure with AWS CDK:** <br>- Setting up AWS CDK CLI environment and project structure (`cdk init app`). <br>- Constructing VPC, Subnets, and Security Groups using higher-level L2/L3 Constructs. <br>- Synthesizing templates (`cdk synth`), diff checking (`cdk diff`), and deploying (`cdk deploy`). | 11/03/2026 | 11/03/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Wednesday** | **Centralized Operations Management with AWS Systems Manager (SSM):** <br>- Secure instance connectivity without inbound SSH/RDP ports via SSM Session Manager. <br>- Fleet-wide command execution at scale using SSM Run Command. <br>- Centralized secret and configuration management via SSM Parameter Store (SecureString). | 11/04/2026 | 11/04/2026 | [AWS Systems Manager (000024)](https://000024.awsfcaj.com/) |
| **Thursday** | **Centralized Data Protection & Disaster Recovery with AWS Backup:** <br>- Creating Backup Vaults with WORM (Write Once, Read Many) Vault Lock protection. <br>- Establishing automated daily Backup Plans for Amazon EBS, RDS, and EFS volumes. <br>- Performing restore drills and configuring Cross-Region Backup replication. | 11/05/2026 | 11/05/2026 | [AWS Backup Workshop (000038)](https://000038.awsfcaj.com/) |
| **Friday** | **Week 8 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate IaC principles (CloudFormation, CDK), SSM, and AWS Backup. <br>- **Worklog Completion:** Finalize bilingual Week 8 documentation and teardown lab resources. <br>- **Project Work:** Convert manual architecture specifications in the Capstone Proposal into CloudFormation templates. | 11/06/2026 | 11/06/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 8 Achievements:

#### 📌 Monday (11/02/2026) - Infrastructure as Code with AWS CloudFormation:
* **Automated Lifecycle Management:** Defined a multi-tier networking stack (2 AZs, 4 subnets, route tables) within a single declarative YAML template, eliminating human configuration errors and reducing provisioning time from 45 minutes to under 5 minutes.
* **Controlled Pipeline Updates:** Implemented **Change Sets** to preview resource modifications and impacts before executing stack updates; deployed **Drift Detection** to monitor unmanaged manual console alterations.

#### 📌 Tuesday (11/03/2026) - Modern Cloud Engineering with AWS CDK:
* **High-Level Abstractions:** Leveraged AWS CDK L2 constructs to generate compliant infrastructure with built-in AWS Well-Architected guardrails, type safety, and unit testing capabilities.
* **Code Efficiency:** Provisioned an Auto Scaling Group behind an Application Load Balancer in less than 50 lines of TypeScript, compared to over 400 lines in raw CloudFormation YAML.

#### 📌 Wednesday (11/04/2026) - Fleet Operations via AWS Systems Manager:
* **Zero Inbound Port Security:** Terminated public SSH (port 22) and RDP access on all Security Groups. All operational interaction is now channeled securely through IAM-authenticated SSM Session Manager with full CloudTrail audit logging.
* **Decoupled Secrets Configuration:** Separated database credentials and third-party API keys from application codebases by storing them in **SSM Parameter Store** with KMS encryption.

#### 📌 Thursday (11/05/2026) - Centralized Data Protection with AWS Backup:
* **Automated Compliance:** Configured automated backup policies for Amazon RDS database instances and EC2 instances with a 30-day retention schedule and automatic transition to cold storage after 7 days.
* **Disaster Recovery Readiness:** Successfully validated data restoration workflows from the primary region (`ap-southeast-1`) to a secondary region (`ap-southeast-2`), achieving an RPO of under 15 minutes and RTO of under 30 minutes.
