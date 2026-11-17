---
title: "Week 4 Worklog"
date: 2026-10-05
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

{{% notice warning %}}
⚠️ **Note:** The information below is for reference only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

### Objectives for Week 4:

* Familiarize and practice on **Amazon Lightsail** (Deploy Managed Database, WordPress, Prestashop, Snapshot, and Migration).
* Practice running containerized workloads rapidly using **Amazon Lightsail Container**.
* Design and implement elastic scaling and traffic balancing using **Amazon EC2 Auto Scaling** and **Application Load Balancer**.
* Establish comprehensive observability, deep log analytics, and automated threshold alerts with **Amazon CloudWatch**.
* Consolidate Week 4 knowledge, finalize all Worklog entries, and dedicate time to internship project research (**Project Proposal**).

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| **Monday** | **Amazon Lightsail Deployment:** <br>- Managed MySQL Database & WordPress Instance. <br>- Ubuntu Configuration, Static IP & Networking. <br>- Prestashop E-Commerce Platform. <br>- Snapshots Backup & Hardware Migration. | 05/10/2026 | 05/10/2026 | [Lightsail Workshop](https://000045.awsfcaj.com/) |
| **Tuesday** | **Run Applications on Amazon Lightsail Container:** <br>- Setup AWS CLI & Resolve IAM Policy Restrictions. <br>- Provision Lightsail Container Service. <br>- Deploy Public Nginx Container Image. <br>- Package & Push Custom Image via Build-Instance. | 06/10/2026 | 06/10/2026 | [Lightsail Container](https://000046.awsfcaj.com/) |
| **Wednesday** | **Scaling Applications with EC2 Auto Scaling:** <br>- Package Custom AMI & Build Launch Template. <br>- Establish Target Group & Application Load Balancer. <br>- Configure Auto Scaling Group & Scaling Policies. <br>- Execute Stress Testing & Validate Scale Out/In. | 07/10/2026 | 07/10/2026 | [Auto Scaling Workshop](https://000006.awsfcaj.com/) |
| **Thursday** | **Monitoring with Amazon CloudWatch:** <br>- Install CloudWatch Agent & Stream EC2 Metrics/Logs. <br>- Telemetry plotting with Search Expressions & Math Expressions. <br>- Query log data with CloudWatch Logs Insights. <br>- Configure Metric Filters and automated CloudWatch Alarms. | 08/10/2026 | 08/10/2026 | [CloudWatch Workshop](https://000008.awsfcaj.com/) |
| **Friday** | **Week 4 Review, Worklog & Project:** <br>- Synthesize concepts across Lightsail, Auto Scaling, and CloudWatch. <br>- Finalize technical details and screenshots for Worklogs 1.4.1 through 1.4.4. <br>- Research AWS architectural patterns and advance internship project proposal. | 09/10/2026 | 09/10/2026 | [Internal Review & Project Documentation](/2-proposal/) |

---

### Achievements for Week 4:

#### 📌 Results for Monday (05/10/2026) - Amazon Lightsail Deployment:

{{% notice tip %}}
👉 **Detailed Lab Report:** Full configuration parameters, step-by-step procedures, and all 13 verification screenshots are neatly organized at: **[1.4.1. Amazon Lightsail Deployment](1.4.1-amazon-lightsail/)**.
{{% /notice %}}

* **Introduction to Amazon Lightsail:** Understood AWS's simplified cloud platform designed for rapidly launching small-to-medium applications with predictable monthly costs.
* **Web Application & Database Setup:** Mastered deploying popular web platforms (WordPress and PrestaShop e-commerce) connected to an isolated managed database.
* **Networking & Data Protection:** Learned how to attach static IPs, manage basic firewall rules, create backup snapshots, and scale instances seamlessly as workloads grow.

---

#### 📌 Results for Tuesday (06/10/2026) - Run Applications on Amazon Lightsail Container:

{{% notice tip %}}
👉 **Detailed Lab Report:** Full configuration parameters, step-by-step procedures, and all 11 verification screenshots are neatly organized at: **[1.4.2. Run Applications on Amazon Lightsail Container](1.4.2-lightsail-container/)**.
{{% /notice %}}

* **Container Services on Lightsail:** Understood running containerized workloads in the cloud without the complexity of managing underlying server orchestration clusters.
* **Deploying Container Workloads:** Learned how to launch standard public container images from Docker Hub, as well as build and push custom application containers to private cloud repositories.
* **Secure Application Access:** Experienced automatic HTTPS/SSL certificate provisioning and verified public accessibility of running container services.

---

#### 📌 Results for Wednesday (07/10/2026) - Scaling Applications with EC2 Auto Scaling:

{{% notice tip %}}
👉 **Detailed Lab Report:** Full configuration parameters, step-by-step procedures, and all 44 verification screenshots are neatly organized at: **[1.4.3. Scaling Applications with EC2 Auto Scaling](1.4.3-ec2-auto-scaling/)**.
{{% /notice %}}

* **Standardizing Server Templates:** Understood how to capture golden server images (AMIs) and standardize deployment configurations via Launch Templates.
* **Traffic Distribution via Load Balancers:** Mastered load balancing principles by distributing incoming user traffic across multiple availability zones to ensure high availability.
* **Elastic Auto Scaling:** Experienced dynamic scaling firsthand—observing automatic scale-out during high demand and scale-in when demand subsides to optimize infrastructure costs.

---

#### 📌 Results for Thursday (08/10/2026) - Monitoring with Amazon CloudWatch:

{{% notice tip %}}
👉 **Detailed Lab Report:** Full configuration parameters, step-by-step procedures, and all 33 verification screenshots are neatly organized at: **[1.4.4. Monitoring with Amazon CloudWatch](1.4.4-amazon-cloudwatch/)**.
{{% /notice %}}

* **System Telemetry Collection:** Learned to deploy agents to track compute health metrics (CPU, memory, disk) and centralize application logs into cloud repositories.
* **Metric Visualization & Log Analytics:** Practiced building dynamic dashboards and running advanced log queries to quickly detect and diagnose system anomalies.
* **Automated Alerting:** Configured threshold-based alarms integrated with notification services to instantly alert engineers when performance thresholds are breached.

---

#### 📌 Results for Friday (09/10/2026) - Week 4 Review, Worklog & Project:

{{% notice tip %}}
👉 **Friday Milestone Focus:** Every Friday is systematically dedicated to three pillars: (1) Synthesizing hands-on technical skills; (2) Perfecting worklog entries with evidence screenshots; (3) Researching and advancing the internship capstone (**[Project Proposal](/2-proposal/)**).
{{% /notice %}}

* **1. Weekly Knowledge Synthesis:**
  * Consolidated operational workflows for rapid application deployment using **Amazon Lightsail** and **Lightsail Containers**.
  * Mastered high-availability scaling patterns with **EC2 Auto Scaling** coordinated behind **Application Load Balancers**.
  * Solidified system observability, custom telemetry ingestion, and proactive operational monitoring using **Amazon CloudWatch**.
* **2. Worklog Documentation & Quality Audit:**
  * Rigorously reviewed and polished lab documentation across **1.4.1 to 1.4.4**, ensuring comprehensive parameter matrices and validated screenshots.
  * Verified bilingual parity (Vietnamese and English), correct markdown typography, and seamless internal cross-linking.
* **3. Project Proposal Research & Design:**
  * Dedicated focused research on AWS Well-Architected Framework design principles applicable to enterprise cloud migrations.
  * Refined baseline architectural diagrams and workload specifications in **[Project Proposal](/2-proposal/)**.

---

### Next Week's Objectives (Week 5):

* **Hybrid DNS with Route 53 Resolver (1.5.1):**
  * Automated deployment of multi-VPC simulation topology using AWS CloudFormation.
  * Deploy AWS Managed Microsoft AD as an authoritative on-premises enterprise DNS domain controller.
  * Configure Route 53 Resolver Inbound and Outbound Endpoints with conditional forwarding rules for bidirectional DNS resolution.
* **Command Line Operations with AWS CLI (1.5.2):**
  * Centralized administration of IAM User Groups, Users, and secure programmatic Access Keys.
  * Launch an EC2 Linux management bastion and establish remote SSH access via MobaXterm.
  * Install AWS CLI v2 on Linux and configure multiple credential profiles (`default`, `devops`).
  * Administer Amazon S3 object storage and Amazon SNS notification distribution channels exclusively via the command line.
  * Fully automate the construction of an isolated Amazon VPC network topology and manage compute lifecycles of Amazon EC2 instances.
* **Work with Amazon DynamoDB (1.5.3):**
  * Administer NoSQL databases, provision the `Music` table, and manage dynamic documents via the AWS Management Console.
  * Execute comprehensive command-line operations using AWS CloudShell (atomic CRUD operations, Global Secondary Index creation, and queries).
  * Programmatic automation with Python 3 and Boto3 SDK: provision the `Movies` table, ingest a 4,609-movie benchmark dataset (`moviedata.json`), execute primary key lookups, and perform conditional scans.
* **Deploy Amazon ElastiCache - Redis (1.5.4):**
  * Design a resilient VPC network with 3 Subnets distributed across 3 distinct Availability Zones (`us-east-1a`, `1b`, `1c`) and configure an ElastiCache Subnet Group.
  * Provision Redis clusters across both architectures: Cluster Mode Disabled and Cluster Mode Enabled via AWS Console and Python Boto3 SDK.
  * Implement enterprise security controls: Transit Encryption (TLS) combined with Role-Based Access Control (RBAC) using Users and User Groups.
  * Develop client-side Python scripts executed from an in-VPC EC2 client: verify TLS RBAC connections, perform string operations with 60s TTL, manage hash maps with collision mitigation, and stream real-time Pub/Sub messages.
* **Week 5 Review, Worklog & Project:** Consolidate weekly learnings, document root cause analyses for technical edge cases, and advance internship project deliverables.
