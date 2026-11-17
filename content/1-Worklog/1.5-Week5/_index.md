---
title: "Week 5"
date: 2026-10-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 5 Objectives:

- Architect and deploy a bidirectional **Hybrid DNS** resolution topology connecting on-premises enterprise networks with AWS via **Amazon Route 53 Resolver**.
- Master the **AWS Command Line Interface (AWS CLI v2)** and configure **Multiple Named Profiles** to automate foundational infrastructure (S3, SNS, VPC, EC2).
- Administer non-relational database tables via **Amazon DynamoDB**, optimize access patterns with **Global Secondary Indexes (GSI)**, and implement SDK automation via **Python Boto3**.
- Deploy distributed in-memory caching clusters with **Amazon ElastiCache - Redis** (Cluster Mode Disabled & Enabled), enforce TLS/RBAC security, and develop client code.
- Synthesize all Week 5 knowledge, finalize comprehensive Worklog documentation, and advance the internship capstone project (**Project Proposal**).

---

### Tasks to be Carried Out This Week:

| Day           | Tasks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Start Date | Completion Date | Reference Sources                                                |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :-------------- | :--------------------------------------------------------------- |
| **Monday**    | **Set up Hybrid DNS with Route 53 Resolver:** <br>- Deploy multi-VPC CloudFormation stack & configure Security Groups. <br>- Deploy AWS Managed Microsoft AD acting as on-premises enterprise DNS. <br>- Build Route 53 Outbound Endpoints & Resolver Rules. <br>- Build Inbound Endpoints & validate bidirectional resolution via `nslookup`.                                                                                                                                                                                                                      | 12/10/2026 | 12/10/2026      | [Hybrid DNS Workshop](https://000010.awsfcaj.com/)         |
| **Tuesday**   | **Command Line Operations with AWS CLI:** <br>- Set up IAM Groups, Users & CLI Access Keys. <br>- Launch EC2 Management Workstation & connect via MobaXterm. <br>- Install AWS CLI v2 & configure multiple profiles (`default`, `devops`). <br>- Administer Amazon S3, Amazon SNS & IAM via CLI. <br>- Construct VPC Network & automate EC2 lifecycle.                                                                                                                                                                                                                       | 13/10/2026 | 13/10/2026      | [AWS CLI Workshop](https://000011.awsfcaj.com/)            |
| **Wednesday** | **Work with Amazon DynamoDB:** <br>- Administer NoSQL database tables via AWS Management Console. <br>- Execute command-line CRUD operations and manage GSIs using AWS CloudShell. <br>- Master DynamoDB Partition Key distribution and GSI Backfilling mechanisms. <br>- Programmatic SDK automation using Python 3 and Boto3. <br>- Ingest benchmark payload of 4,609 movies (`moviedata.json`), Query & Scan.                                                                                                                                                             | 14/10/2026 | 14/10/2026      | [DynamoDB Workshop](https://000060.awsfcaj.com/)           |
| **Thursday**  | **Deploy Amazon ElastiCache - Redis:** <br>- Design VPC 3 AZs network topology & create Subnet Group. <br>- Provision Cluster Mode Disabled & Enabled on Web Console. <br>- Automate cluster deployment using Python Boto3 SDK. <br>- Configure TLS Transit Encryption & RBAC Users/Groups. <br>- Programmatic Python operations (Strings TTL, Hash, Pub/Sub).                                                                                                                                                                                                               | 15/10/2026 | 15/10/2026      | [ElastiCache Workshop](https://000061.awsfcaj.com/)        |
| **Friday**    | **Week 5 Review, Worklog & Project:** <br>- Synthesize concepts across Route 53 Resolver, AWS CLI, DynamoDB, and ElastiCache Redis. <br>- Finalize technical details and evidence screenshots for Worklogs 1.5.1 through 1.5.4. <br>- Research cloud architectural patterns and advance internship project proposal deliverables.                                                                                                                                                                                                                                        | 16/10/2026 | 16/10/2026      | [Internal Review & Project Documentation](/2-proposal/)          |

---

### Week 5 Achievements:

#### 📌 Monday (12/10/2026) - Set up Hybrid DNS with Route 53 Resolver:

{{% notice tip %}}
👉 **Detailed Lab Report:** Full configuration parameters, step-by-step procedures, and all 11 verification screenshots are neatly organized at: **[1.5.1. Hybrid DNS with Route 53 Resolver](1.5.1-hybrid-dns/)**.
{{% /notice %}}

- **Hybrid Cloud Networking Architecture:** Understood the DNS resolution challenge when bridging traditional on-premises enterprise data centers with AWS Cloud environments.
- **Bidirectional DNS Routing:** Mastered the core principles of Route 53 Resolver Inbound and Outbound Endpoints to enable seamless domain lookup across both networks.
- **Validation & Troubleshooting:** Verified low-latency domain lookup and end-to-end name resolution accuracy using `nslookup` across multi-VPC enterprise topologies.

---

#### 📌 Tuesday (13/10/2026) - Command Line Operations with AWS CLI:

{{% notice tip %}}
👉 **Detailed Lab Report:** All technical configurations, command line procedures, 12 resolved technical issues, and the complete collection of 38 screenshots are documented at: **[1.5.2. Command Line Operations with AWS CLI](1.5.2-aws-cli/)**.
{{% /notice %}}

- **Mastering the AWS CLI Interface:** Understood the power of command-line automation in managing cloud infrastructure compared to manual Web Console actions.
- **Identity Management & Access Control:** Learned best practices for IAM permissions, secure credential management, and configuring multiple environment profiles on a Linux management host.
- **Infrastructure Automation via Scripting:** Practiced provisioning and managing foundational services—including S3 buckets, SNS notification topics, custom VPC networks, and EC2 instances—entirely via terminal commands.
- **Practical Troubleshooting Skills:** Gained hands-on experience identifying and fixing common operational issues related to SSH keys, network routing, and permission constraints.

---

#### 📌 Wednesday (14/10/2026) - Work with Amazon DynamoDB:

{{% notice tip %}}
👉 **Detailed Lab Report:** All technical configurations, operational procedures, 10 resolved troubleshooting scenarios, and the complete collection of 32 screenshots are documented at: **[1.5.3. Work with Amazon DynamoDB](1.5.3-amazon-dynamodb/)**.
{{% /notice %}}

- **NoSQL Database Concepts:** Grasped key differences between non-relational (NoSQL) and relational (SQL) databases, focusing on document schema flexibility and performance.
- **Multi-Interface Operations:** Mastered CRUD operations across both the AWS Management Console and command-line environments (AWS CloudShell).
- **Query Optimization & Secondary Indexes:** Understood primary key design (Partition Key & Sort Key) and the strategic use of Global Secondary Indexes (GSI) for multidimensional queries.
- **Automation with Python SDK (Boto3):** Learned how to write Python scripts to programmatically create tables, ingest large datasets in bulk, and run filtered scans and queries.

---

#### 📌 Thursday (15/10/2026) - Deploy Amazon ElastiCache - Redis:

{{% notice tip %}}
👉 **Detailed Lab Report:** All technical configurations, operational procedures, 12 resolved troubleshooting scenarios, and the complete collection of 27 screenshots are documented at: **[1.5.4. Deploy Amazon ElastiCache - Redis](1.5.4-amazon-elasticache/)**.
{{% /notice %}}

- **In-Memory Caching Architecture:** Learned how in-memory caching dramatically speeds up application response times and offloads traffic from primary relational databases.
- **Distributed Cluster Topologies:** Explored and deployed both primary-replica failover setups (Cluster Mode Disabled) and horizontally sharded architectures (Cluster Mode Enabled).
- **Enterprise Security & Application Integration:** Configured in-transit encryption (TLS), role-based access control (RBAC), and wrote client code utilizing key expiration (TTL) and real-time Pub/Sub messaging.
- **SDK Automation & Operational Insights:** Automated cluster deployments using Python Boto3 and gained valuable experience resolving multi-AZ networking constraints.

---

#### 📌 Friday (16/10/2026) - Week 5 Review, Worklog & Project:

{{% notice tip %}}
👉 **Friday Milestone Focus:** Every Friday is systematically dedicated to three pillars: (1) Synthesizing hands-on technical skills; (2) Perfecting worklog entries with evidence screenshots; (3) Researching and advancing the internship capstone (**[Project Proposal](/2-proposal/)**).
{{% /notice %}}

* **1. Weekly Knowledge Synthesis:**
  * Consolidated hybrid networking patterns with Route 53 Resolver bridging AWS VPCs and on-premises directory services.
  * Mastered command-line operations and multi-profile scripting workflows with AWS CLI v2.
  * Mastered modern database paradigms: NoSQL persistence with Amazon DynamoDB and high-throughput caching with Amazon ElastiCache Redis.
* **2. Worklog Documentation & Quality Audit:**
  * Rigorously reviewed and polished lab documentation across **1.5.1 to 1.5.4**, incorporating full parameter specifications and over 100 verification screenshots.
  * Maintained strict bilingual parity (Vietnamese and English), correct markdown standards, and unbroken internal cross-references.
* **3. Project Proposal Research & Design:**
  * Investigated caching integration and DynamoDB session store architectures for e-commerce workloads in the internship project.
  * Updated proposed architecture schematics and documentation within **[Project Proposal](/2-proposal/)**.

---

### Next Week's Objectives (Week 6):

* **Resource Limit Governance with AWS Service Quotas (1.6.1):**
  * Understand AWS account protection quotas, rate limiting, and governance models.
  * Practice real-world quota increase requests for Spot Instance vCPUs and coordinate with AWS Support Center.
  * Automate quota tracking with AWS CLI and configure proactive CloudWatch metric alarms.
* **Optimize Amazon EC2 Costs with AWS Lambda & Slack Notifications (1.6.2):**
  * Build a serverless automated start/stop solution for non-production EC2 instances outside working hours.
  * Program Python Boto3 Lambda functions and integrate ChatOps notifications via Slack Incoming Webhooks.
  * Automate scheduling using Amazon EventBridge Scheduler cron expressions.
* **Monitoring with Grafana & CloudWatch (1.6.3):**
  * Deploy a centralized monitoring and dashboard solution using Grafana integrated with Amazon CloudWatch metrics (Workshop 000029 - Getting started with Grafana basic).
  * Build real-time dashboards to track compute health, network throughput, and infrastructure performance.
* **Week 6 Review, Worklog & Project:** Consolidate observability and cost optimization knowledge, polish weekly worklogs, and advance internship project milestones.

