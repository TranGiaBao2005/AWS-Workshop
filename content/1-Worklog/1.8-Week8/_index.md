---
title: "Week 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 8 Objectives:

- Embrace the **Infrastructure as Code (IaC)** paradigm to automate resource provisioning, enforce version control, and enable reproducible cloud environments on AWS.
- Dedicate **two full deep-dive days (Monday & Tuesday)** to thoroughly mastering **AWS CloudFormation** (Workshop 000037): from core YAML syntax, parameters, intrinsic functions, and stack orchestration to advanced production patterns like Nested Stacks, Change Sets, and Drift Detection.
- Adopt modern software-defined infrastructure via the **AWS Cloud Development Kit (AWS CDK)**, defining cloud topology with familiar object-oriented programming languages across L1, L2, and L3 construct abstractions.
- Administer secure, zero-inbound-port fleet operations using **AWS Systems Manager (SSM)** (Workshop 000024) and manage sensitive configuration variables via Parameter Store.
- Implement centralized enterprise data protection policies and ransomware safeguards using **AWS Backup** (Workshop 000038).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and refactoring manual architecture designs from the **Capstone Project Proposal** into reusable IaC templates.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **AWS CloudFormation (Part 1) - Template Anatomy & Stack Provisioning:** <br>- Mastering core template sections: AWSTemplateFormatVersion, Parameters, Resources, Outputs. <br>- Utilizing intrinsic functions: `!Ref`, `!Sub`, `!GetAtt`, `!Join` for dynamic resource binding. <br>- Fully automating a resilient multi-tier networking stack (VPC 2 AZs, 4 subnets, route tables). | 11/02/2026 | 11/02/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Tuesday** | **AWS CloudFormation (Part 2) - Nested Stacks, Change Sets & Drift Detection:** <br>- Designing modular architectures using Nested Stacks (Network, Database, Compute tiers). <br>- Mitigating deployment risk on production stacks using Change Sets preview workflows. <br>- Scanning for out-of-band manual configuration drift using CloudFormation Drift Detection. <br>- Enforcing Stack Termination Protection to prevent catastrophic accidental deletions. | 11/03/2026 | 11/03/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Wednesday** | **Modern Software-Defined Infrastructure with AWS CDK:** <br>- Setting up AWS CDK CLI environment and initializing TypeScript projects (`cdk init app`). <br>- Exploring construct hierarchies: L1 (CfnResource), L2 (AWS-managed best practices), L3 (Architectural Patterns). <br>- Executing development workflows: template synthesis (`cdk synth`), diff inspection (`cdk diff`), and deployment (`cdk deploy`). | 11/04/2026 | 11/04/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Thursday** | **Fleet Operations with AWS Systems Manager & Protection with AWS Backup:** <br>- Zero-inbound-port instance connectivity without SSH (port 22) via SSM Session Manager. <br>- Fleet-wide script execution across distributed instances via SSM Run Command. <br>- Encrypted configuration and database credential storage via SSM Parameter Store (`SecureString`). <br>- Establishing automated backup policies with AWS Backup Vaults (WORM lock) for EBS and RDS. | 11/05/2026 | 11/05/2026 | [SSM (000024)](https://000024.awsfcaj.com/) & [Backup (000038)](https://000038.awsfcaj.com/) |
| **Friday** | **Week 8 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate IaC principles (CloudFormation, CDK), SSM operations, and AWS Backup. <br>- **Worklog Completion:** Finalize bilingual Week 8 documentation and teardown lab resources. <br>- **Project Work:** Convert manual architecture specifications in the Capstone Proposal into modular CloudFormation templates. | 11/06/2026 | 11/06/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (11/02/2026) - AWS CloudFormation (Part 1): Template Anatomy & Stack Provisioning

* **What did we learn today?**
  * **Anatomy of a Production CloudFormation Template:** Mastered the standard declarative YAML sections: `AWSTemplateFormatVersion: '2010-09-09'`, `Description`, `Parameters` (accepting runtime variables such as CIDR blocks and environment tiers), `Mappings` (region-to-AMI lookups), `Conditions` (conditional resource activation), `Resources` (mandatory cloud primitives), and `Outputs` (cross-stack reference exports).
  * **Mastery of Intrinsic Functions:**
    * `!Ref`: Referencing user parameters or extracting physical resource IDs.
    * `!Sub`: Dynamic variable string interpolation (e.g., `${AWS::StackName}-public-subnet-1`).
    * `!GetAtt`: Deep attribute extraction (e.g., `!GetAtt MyVPC.Arn` or `!GetAtt MyEC2.PrivateIp`).
    * `!Join`: Concatenating strings with specific delimiters.
  * **Hands-on Network Stack Provisioning:** Authored a 180-line `network-foundation.yaml` template declaring an isolated VPC (`10.0.0.0/16`), Internet Gateway, 2 Public Subnets, 2 Private Subnets, Route Tables, and Route Table Associations.
  * **AWS CLI Orchestration:**
    ```bash
    aws cloudformation create-stack \
      --stack-name fcaj-network-stack \
      --template-body file://network-foundation.yaml \
      --parameters ParameterKey=EnvironmentName,ParameterValue=Development
    aws cloudformation describe-stacks --stack-name fcaj-network-stack --query "Stacks[0].StackStatus"
    ```
* **Encountered Challenges & Solutions:**
  * *YAML Indentation Formatting Errors:* Encountered `Template format error: YAML not well-formed`. Root cause: Inconsistent white-space indentation under `Properties` blocks. Solution: Integrated `cfn-lint` and the VS Code CloudFormation extension to lint templates prior to CLI execution.
  * *Circular Dependency Hangs:* When declaring an Internet Gateway attachment alongside route creation, the default route failed because the IGW was not fully attached. Solution: Added an explicit `DependsOn: AttachGateway` directive on the `AWS::EC2::Route` resource.

---

#### 📌 Tuesday (11/03/2026) - AWS CloudFormation (Part 2): Nested Stacks, Change Sets & Drift Detection

* **What did we learn today?**
  * **Modular Architecture with Nested Stacks:** Overcame single-template resource limits and enforced separation of concerns by creating a Root Stack (`master.yaml`) that references three S3-staged child templates: `network-stack.yaml`, `database-stack.yaml` (RDS), and `compute-stack.yaml` (EC2 & ALB) using `AWS::CloudFormation::Stack`.
  * **Safe Deployment with Change Sets:** Avoided direct in-place updates on production stacks. Change Sets allow visual pre-flight inspection of additions (`Add`), modifications (`Modify`), and deletions (`Remove`), specifically highlighting potential stateful replacements (`Replacement: True/False`).
  * **Configuration Auditing with Drift Detection:** Mastered the Drift Detection engine to verify live AWS resource configurations against the template state, immediately spotting unmanaged manual changes (such as rogue security group inbound rules added via console).
  * **Accidental Deletion Protection:** Enabled `Termination Protection` on critical stacks, preventing human error from deleting production infrastructure.
* **Encountered Challenges & Solutions:**
  * *Handling the `UPDATE_ROLLBACK_FAILED` State:* An incompatible DB subnet group modification caused stack rollback to fail, locking the stack in `UPDATE_ROLLBACK_FAILED`. Solution: Inspected CloudFormation Stack Events, triggered `Continue Update Rollback` with `Skip Resources` on the stuck resource, restoring the stack to `UPDATE_ROLLBACK_COMPLETE`.

---

#### 📌 Wednesday (11/04/2026) - Modern Software-Defined Infrastructure with AWS CDK

* **What did we learn today?**
  * **Software-Defined Cloud Engineering:** Replaced lengthy declarative templates with TypeScript, applying Object-Oriented Programming (OOP) paradigms, compile-time type safety, automated code completion (IntelliSense), and unit testing frameworks.
  * **Construct Abstraction Levels:**
    * *Level 1 (L1 - Cfn Resources):* 1-to-1 direct mapping to CloudFormation resource types (e.g., `CfnVPC`).
    * *Level 2 (L2 - AWS Managed):* Opinionated AWS best-practice constructs that configure subnets, route tables, and security groups with sensible defaults in minimal code lines (e.g., `new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 })`).
    * *Level 3 (L3 - Architectural Patterns):* Multi-service composite patterns (e.g., `ApplicationLoadBalancedFargateService`).
  * **Core CDK CLI Lifecycle:**
    ```bash
    cdk bootstrap aws://887086382708/us-east-1  # Provisions S3 buckets & IAM Roles for CDK
    cdk synth                                    # Compiles TypeScript into synthesized CloudFormation
    cdk diff                                     # Compares local construct code against deployed AWS state
    cdk deploy                                   # Deploys synthesized CloudFormation stacks automatically
    ```
* **Encountered Challenges & Solutions:**
  * *Missing Bootstrap Environment:* Running `cdk deploy` failed with `This stack uses assets, so the toolkit stack must be deployed to the environment`. Solution: Executed `cdk bootstrap` once for the target account/region to provision the `CDKToolkit` assets stack.
  * *Library Version Mismatches:* Encountered dependency conflicts between legacy `@aws-cdk` packages and the consolidated `aws-cdk-lib`. Solution: Standardized the package manifest to AWS CDK v2 with exclusive references to `aws-cdk-lib`.

---

#### 📌 Thursday (11/05/2026) - Centralized Fleet Operations via Systems Manager & AWS Backup

* **What did we learn today?**
  * **Zero Inbound Port Security with SSM Session Manager:** Completely removed port 22 (SSH) from all Security Groups. Enabled credential-less terminal sessions into private subnet instances via browser console and CLI, with full keystroke auditing recorded into S3 and CloudWatch Logs.
  * **Fleet-Scale Automation with SSM Run Command:** Executed shell scripts and package upgrade commands simultaneously across 50 EC2 instances without requiring direct interactive login.
  * **Secure Secrets Management via SSM Parameter Store:** Stored database connection strings and API credentials as `SecureString` parameters encrypted with AWS KMS, allowing applications to retrieve runtime credentials securely without hardcoding secrets in configuration files.
  * **Centralized Data Protection with AWS Backup:** Configured an immutable Backup Vault protected by `Vault Lock` (WORM compliance), preventing snapshot deletion even by the AWS account root user. Configured an automated daily Backup Plan for EBS and RDS with a 30-day retention cycle.
* **Encountered Challenges & Solutions:**
  * *EC2 Instance Not Showing in SSM Managed Nodes:* New instance showed `Target Not Connected` in Session Manager. Root cause: Missing the `AmazonSSMManagedInstanceCore` IAM role, and the private subnet lacked either an internet NAT gateway or VPC Interface Endpoints for SSM (`ssm`, `ssmmessages`, `ec2messages`). Solution: Attached the instance profile and provisioned VPC Endpoints for private SSM communication.

---

#### 📌 Friday (11/06/2026) - Week 8 Review, Worklog Finalization & Capstone Project Development

* **What did we learn today?**
  * **IaC Lifecycle Synthesis:** Successfully bridged the entire infrastructure automation pipeline: programmatic provisioning (CloudFormation/CDK) ➔ secure instance administration (SSM) ➔ automated data protection and disaster recovery (AWS Backup).
  * **FinOps Resource Hygiene:** Ran `cdk destroy` and `aws cloudformation delete-stack` to tear down all transient experimental infrastructure created during the week, ensuring zero ongoing idle charges in AWS Cost Explorer.
  * **Capstone Project Architecture Packaging:** Refactored the manual architecture designs of the graduation proposal into modular, version-controlled AWS CloudFormation templates ready for automated deployment.

