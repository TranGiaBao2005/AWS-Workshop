---
title: "Week 6 Worklog"
date: 2026-10-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

{{% notice warning %}}
⚠️ **Note:** The information below is for reference only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

### Objectives for Week 6:

* Master account ceiling governance and compute vCPU thresholds via **AWS Service Quotas** and collaborate with the **AWS Support Center**.
* Design and implement a serverless cost optimization architecture for EC2 instances utilizing **AWS Lambda**, **Amazon EventBridge Scheduler**, and ChatOps integration through **Slack Incoming Webhooks**.
* Standardize resource tagging strategies and centralized management utilizing **AWS Tags** (console-based & automated via AWS CLI) and **AWS Resource Groups**.
* Deploy advanced visualization and infrastructure observability using **Grafana** integrated with **Amazon CloudWatch** data sources (Workshop 000029 - Getting started with Grafana basic).
* Consolidate Week 6 learnings, finalize comprehensive Worklog entries, and advance the internship capstone project (**Project Proposal**).

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| **Monday** | **Resource Limit Governance with AWS Service Quotas:** <br>- Explore the Service Quotas system & audit EC2 Spot vCPU limits. <br>- Test interactive console input validation rules. <br>- Submit request increasing Spot vCPU ceiling from 32 to 64 (`L-34B43A08`). <br>- Monitor and verify AWS Support approval (Case ID: `179257232100832`). <br>- Automate quota queries via AWS CLI & configure CloudWatch alarms. | 19/10/2026 | 19/10/2026 | [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/) |
| **Tuesday** | **Optimize Amazon EC2 Costs with AWS Lambda & Slack Notifications:** <br>- Tag target EC2 instances with `environment_auto: true` for automated governance. <br>- Establish ChatOps incoming webhook integration with Slack. <br>- Configure IAM Execution Role granting EC2 lifecycle management privileges. <br>- Develop and deploy automated stop/start functions (`dc-common-lambda-auto-stop`, `dc-common-lambda-auto-start`). <br>- Configure recurring EventBridge schedules aligned with business operating hours. <br>- Execute real-time verification tests and receive instantaneous Slack notifications. | 20/10/2026 | 20/10/2026 | [Optimize EC2 Cost with Lambda](https://000022.awsfcaj.com/) |
| **Wednesday** | **Resource Governance with AWS Tags & Resource Groups:** <br>- Launch test EC2 instances and manage resource tags via the AWS Management Console. <br>- Create IAM Access Keys and automate tagging with the AWS CLI (`create-tags`). <br>- Perform multi-attribute resource queries using advanced CLI filters (`describe-instances --filters`). <br>- Create an AWS Resource Group (`EnvTest`) to automatically aggregate resources matching environment tags. <br>- Document troubleshooting lessons on case-sensitivity, tag limits, and regional scope constraints. | 21/10/2026 | 21/10/2026 | [AWS Tagging & Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) |
| **Thursday** | **Infrastructure Observability with Grafana & CloudWatch (Workshop 000029):** <br>- Provision VPC, public subnet with auto-assign public IPv4, and security group for port 3000 & 22. <br>- Launch an Amazon Linux 2023 EC2 host and configure an IAM Role granting CloudWatch read access. <br>- Install and enable the `grafana-server` background daemon using YUM repository and systemd. <br>- Connect CloudWatch Data Source and validate telemetry APIs (Metrics and Logs). <br>- Construct time-series dashboards for CPUUtilization and perform ad-hoc exploration with Bar charts. | 22/10/2026 | 22/10/2026 | [Getting started with Grafana basic](https://000029.awsfcaj.com/) |
| **Friday** | **Week 6 Review, Worklog & Project:** <br>- Synthesize concepts across Service Quotas, Lambda FinOps, AWS Tagging & Grafana CloudWatch. <br>- Finalize technical details and evidence screenshots for Worklogs 1.6.1 through 1.6.4. <br>- Dedicate time to AWS architecture research and develop the internship Project Proposal. | 23/10/2026 | 23/10/2026 | [Internal Review & Project Documentation](/2-proposal/) |

---

### Achievements for Week 6:

#### 📌 Results for Monday (19/10/2026) - Resource Limit Governance with AWS Service Quotas:

{{% notice tip %}}
👉 **Detailed Lab Report:** All technical configurations, operational procedures, cloud economics analysis (zero-cost quota increases), real-world lessons, and the complete collection of screenshots are documented at: **[1.6.1. Resource Limit Governance with AWS Service Quotas](1.6.1-service-quotas/)**.
{{% /notice %}}

- **Resource Ceiling Governance (Service Quotas):** Understood how AWS safeguards accounts against accidental budget overruns, misconfigurations, and credential compromise.
- **Hands-On Limit Increase Lifecycles:** Gained real-world experience doubling compute capacity from 32 to 64 vCPUs for standard Spot instances via the AWS Management Console while adhering to input validation rules.
- **Technical Support Case Integration (AWS Support Center):** Experienced case management lifecycle, support notifications, and official email confirmations under the Basic Support tier.
- **CLI Automation & Proactive Monitoring:** Practiced command-line quota auditing and planned CloudWatch alarm thresholds to prevent compute exhaustion before reaching capacity limits.

---

#### 📌 Results for Tuesday (20/10/2026) - Optimize Amazon EC2 Costs with AWS Lambda & Slack Notifications:

{{% notice tip %}}
👉 **Detailed Lab Report:** Complete technical parameters, optimized Python Boto3 code, 10 resolved troubleshooting scenarios, and the complete collection of 18 hands-on screenshots are documented at: **[1.6.2. Optimize Amazon EC2 Costs with AWS Lambda & Slack Notifications](1.6.2-aws-lambda/)**.
{{% /notice %}}

- **Automated EC2 Instance Lifecycle Management:** Implemented scheduled automatic shutdown of development/staging instances outside business hours and automatic morning restarts, cutting idle compute costs by 65% - 70%.
- **Serverless Architecture with AWS Lambda & Boto3:** Built resilient Lambda automation using resource tags (`tag:environment_auto = true`) and enhanced state filtering (`instance-state-name`) to gracefully bypass terminated instances.
- **Real-Time ChatOps via Slack Incoming Webhooks:** Integrated instant event delivery directly to DevOps chat channels (`#notification`), visualizing instance IDs and execution status upon each trigger.
- **Scheduled Event Orchestration with EventBridge Scheduler:** Configured serverless Cron/Rate schedules providing zero-maintenance, highly reliable periodic execution.

---

#### 📌 Results for Wednesday (21/10/2026) - Resource Governance with AWS Tags & Resource Groups:

{{% notice tip %}}
👉 **Detailed Lab Report:** Complete technical specifications, CLI commands, ABAC architecture analysis, and the full collection of 14 hands-on screenshots are documented at: **[1.6.3. Resource Governance with AWS Tags & Resource Groups](1.6.3-tags-and-resource-groups/)**.
{{% /notice %}}

- **AWS Tagging Strategy Standardization:** Mastered the foundational role of metadata tags in multi-account governance, FinOps cost allocation (Cost Allocation Tags), and Attribute-Based Access Control (ABAC).
- **Multi-Interface Tag Administration:** Seamlessly combined interactive management via the AWS Console with batch automation using `aws ec2 create-tags` and filtered lookups via `aws ec2 describe-instances --filters`.
- **Centralized Management via AWS Resource Groups:** Constructed query-driven resource group `EnvTest` to dynamically bundle, audit, and operate upon EC2 workloads belonging to identical environments.
- **Real-World Operational Bank:** Documented strict case-sensitivity rules, 50-tag per-resource boundaries, and region-scoped isolation inherent to AWS Resource Groups.

---

#### 📌 Results for Thursday (22/10/2026) - Infrastructure Observability with Grafana & CloudWatch:

{{% notice tip %}}
👉 **Detailed Lab Report:** Complete networking topology, IAM Role/Policy least-privilege configurations, AL2023 YUM repository commands, CloudWatch Data Source setup, and the full collection of 18 hands-on screenshots are documented at: **[1.6.4. Infrastructure Observability with Grafana & CloudWatch](1.6.4-grafana-basic/)**.
{{% /notice %}}

- **Grafana Server Deployment on AL2023:** Provisioned open-source Grafana v13.3.0 on Amazon Linux 2023, configuring official RPM repositories and managing services with systemd.
- **Credential-less CloudWatch Integration:** Utilized EC2 Instance Profile (`GrafanaAccessRole`) adhering to AWS Zero-Trust guidelines without embedding static API keys.
- **Interactive Dashboards & Multi-Dimensional Telemetry:** Designed real-time Time Series panels tracking `CPUUtilization` and leveraged the Explore tool for bar-chart anomaly investigation.
- **Troubleshooting Bank:** Documented security group port 3000 rules, IAM 403 authorization remedies, and complete resource cleanup procedures.

---

#### 📌 Results for Friday (23/10/2026) - Week 6 Review, Worklog & Project:

{{% notice tip %}}
👉 **Friday Milestone Focus:** Every Friday is systematically dedicated to three pillars: (1) Synthesizing hands-on technical skills; (2) Perfecting worklog entries with evidence screenshots; (3) Researching and advancing the internship capstone (**[Project Proposal](/2-proposal/)**).
{{% /notice %}}

* **1. Weekly Knowledge Synthesis:**
  * Consolidated operational understanding of **AWS Service Quotas** limit management and AWS Support collaboration.
  * Mastered FinOps automated cost-control architecture using **AWS Lambda**, **EventBridge Scheduler**, and **Slack ChatOps**.
  * Solidified best practices for metadata tagging and centralized management with **AWS Tags** and **AWS Resource Groups**.
  * Solidified skills in modern centralized observability combining the metrics backbone of **CloudWatch** with the powerful visualization of **Grafana**.
* **2. Worklog Documentation & Quality Audit:**
  * Rigorously reviewed and polished lab documentation across **1.6.1 to 1.6.4**, incorporating complete parameter specifications and evidence screenshots.
  * Maintained strict bilingual parity (Vietnamese and English), correct markdown standards, and unbroken internal cross-references.
* **3. Project Proposal Research & Design:**
  * Incorporated Grafana/CloudWatch telemetry monitoring, resource tagging conventions, and serverless cost optimization patterns into the internship capstone (**[Project Proposal](/2-proposal/)**).
  * Refined system architecture diagrams and detailed cost projections for the final proposal presentation.

---

### Next Week's Objectives (Week 7):

* **Advanced Observability with CloudWatch Advanced Workshop:**
  * Master advanced telemetry queries, Metric Math, dynamic search expressions, and dimension properties.
  * Construct multi-channel alerting workflows and analyze complex infrastructure workloads.
* **Technology Community Event & Deep-Dive Technical Blog:**
  * Attend the AWS Cloud Practitioner / Solution Day (24/10/2026).
  * Research and publish Deep-Dive Technical Blog 1 detailing cloud migration and operational optimization.
* **Week 7 Review, Worklog & Project:** Consolidate advanced observability workflows, polish worklogs, and advance internship project deliverables.
