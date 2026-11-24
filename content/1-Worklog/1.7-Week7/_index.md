---
title: "Week 7"
date: 2026-10-26
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Objectives for Week 7:

- Master advanced infrastructure observability techniques with the **Amazon CloudWatch Advanced Workshop**: dynamic calculations with **Metric Math**, automated discovery via **Search Expressions**, and legend formatting with **Dynamic Labels**.
- Utilize **AWS Systems Manager Session Manager** for secure, credential-less instance access, deploy synthetic log generation scripts, and conduct deep-dive telemetry diagnostics with **CloudWatch Logs Insights**.
- Establish quantitative metric extraction from unstructured logs using **Metric Filters**, trigger real-time multi-channel incident notifications via **Amazon SNS**, and construct a unified **Custom Operations Dashboard**.
- Synthesize the harvest report for the **First Cloud AI Journey Meetup (24/10/2026)** and publish technical **Blog 1: Introducing AWS Continuum for Code Vulnerabilities**.
- Systematically dedicate Friday to synthesizing technical skills, perfecting Worklog documentation, and advancing the internship capstone project (**Project Proposal**).

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Advanced Observability with Amazon CloudWatch (CloudWatch Advanced Workshop):** <br>- Provision multi-instance lab cluster automatically with CloudFormation (`AwsWorkshopStack`). <br>- Configure Metric Math formulas and automated dynamic `SEARCH()` expressions. <br>- Standardize graph legends utilizing Dynamic Labels `${PROP('Dim.DimName')}`. <br>- Connect via SSM Session Manager and launch background synthetic logger (`logger.py`). <br>- Run advanced log queries with CloudWatch Logs Insights and save reusable queries. <br>- Create Metric Filter `PythonAppErrors`, alarm thresholds, and integrate into `ssmDashboard`. | 26/10/2026 | 26/10/2026 | [Amazon CloudWatch Observability Workshop](https://catalog.workshops.aws/observability/en-US/) |
| **Tuesday** | **Workload Monitoring & Automated Incident Response with CloudWatch & SNS:** <br>- Design server stress-testing scenarios to simulate compute resource saturation. <br>- Configure multi-threshold composite alarms tracking correlated CPU and memory spikes. <br>- Route real-time alerts to operations team email and ChatOps channels via Amazon SNS. <br>- Benchmark Mean Time to Detect (MTTD) and optimize telemetry collection intervals. | 27/10/2026 | 27/10/2026 | [AWS Observability Best Practices](https://aws.amazon.com/cloudwatch/) |
| **Wednesday** | **First Cloud AI Journey Meetup Synthesis (24/10/2026):** <br>- Consolidate five enterprise sessions: Vietnamese Voice AI, AWS RAM, AI Pentest, Bedrock AgentCore, and Kiro Crew. <br>- Document key architectural takeaways on Latency Budgets, Shift-Left Security, and Context Window management. <br>- Publish the full bilingual event report with verification photos. | 28/10/2026 | 28/10/2026 | [Events Participated](/4-eventparticipated/) |
| **Thursday** | **Author & Publish Blog 1: AWS Continuum for Code Vulnerabilities:** <br>- Study the October 22, 2026 AWS News Blog GA announcement for AWS Continuum. <br>- Analyze bidirectional Context Graphs, isolated sandbox exploit validation, and automated remediation Pull Requests. <br>- Publish to the Facebook AWS Study Group - First Cloud Journey community and integrate bilingually. | 29/10/2026 | 29/10/2026 | [Blog 1 - AWS Continuum](/3-blogsposted/3.1-blog1/) |
| **Friday** | **Week 7 Review, Worklog & Project:** <br>- Consolidate knowledge across CloudWatch Advanced, Logs Insights, Metric Math & SNS Alarms. <br>- Review and polish technical specifications and screenshot evidence for Worklog 1.7.1. <br>- Advance architecture design research and documentation for the internship Project Proposal. | 30/10/2026 | 30/10/2026 | [Internal Review & Project Documentation](/2-proposal/) |

---

### Achievements for Week 7:

#### 📌 Results for Monday (26/10/2026) - Advanced Observability with Amazon CloudWatch:

{{% notice tip %}}
👉 **Detailed Lab Report:** All CloudFormation stack specifications, Metric Math formulas, Logs Insights query commands, Metric Filter configurations, and the full collection of 20 hands-on screenshots are documented at: **[1.7.1. Advanced Observability with Amazon CloudWatch (CloudWatch Advanced Workshop)](1.7.1-cloudwatch-advanced/)**.
{{% /notice %}}

- **Automated Infrastructure Provisioning with CloudFormation:** Successfully deployed an isolated multi-instance test fleet (Instance-A through Instance-E) reaching `CREATE_COMPLETE` status using `AwsWorkshopStack`.
- **Dynamic Telemetry Discovery with Metric Math & Search Expressions:** Built resilient monitoring panels that scale dynamically without manual intervention using `SEARCH('used', 'Average', 300)` and `SEARCH('disk_used_percent', 'Average')`.
- **Sanitized Visual Dashboards with Dynamic Labels:** Extracted logical names using `${PROP('Dim.DimName')}` to replace uninformative instance identifiers with clear, human-readable legends.
- **Deep-Dive Diagnostics via CloudWatch Logs Insights:** Executed regex-based error isolation (`/ERROR/`, `/WARN/`), grouped event occurrences across log streams (`@logStream`), and rendered time-bucketed event trends using `bin(5m)`.
- **Automated Alerting & Executive Dashboards:** Extracted structured metrics via Metric Filter `PythonAppErrors`, routed breach notifications to Amazon SNS, and assembled a comprehensive operations view in `ssmDashboard`.

---

#### 📌 Results for Tuesday (27/10/2026) - Workload Monitoring & Automated Incident Response with CloudWatch & SNS:

- **Simulated Workload Stress Testing:** Executed high-load synthetic traffic simulations evaluating system resilience under sustained compute spikes.
- **Multi-Channel Incident Dispatch:** Configured Amazon SNS topics to deliver actionable event notifications to on-call engineers instantaneously.
- **MTTD Optimization:** Reduced incident identification latency through fine-tuned evaluation periods and proactive metric thresholds.

---

#### 📌 Results for Wednesday & Thursday (28/10 – 29/10/2026) - FCAJ Meetup Synthesis & Blog 1 Publication:

- **Completed First Cloud AI Journey Meetup Report:** Synthesized practical lessons from five industry speakers covering Voice AI, AWS RAM, Frontier Security Agent, Bedrock AgentCore, and Kiro Crew, complete with event photography at Bitexco Level 26.
- **Published Technical Blog 1 (AWS Continuum for Code Vulnerabilities):** Analyzed AWS's autonomous DevSecOps architecture—bidirectional Context Graphs, isolated sandbox proof-of-concept verification, and human-in-the-loop remediation Pull Requests.

---

#### 📌 Results for Friday (30/10/2026) - Week 7 Review, Worklog & Project:

{{% notice tip %}}
👉 **Friday Milestone Focus:** Every Friday is systematically dedicated to three pillars: (1) Synthesizing hands-on technical skills; (2) Perfecting worklog entries with evidence screenshots; (3) Researching and advancing the internship capstone (**[Project Proposal](/2-proposal/)**).
{{% /notice %}}

- **1. Weekly Knowledge Synthesis:**
  - Consolidated operational proficiency in **Metric Math**, **Search Expressions**, **Dynamic Labels**, **Logs Insights**, and **Metric Filters**.
  - Solidified zero-trust remote administration workflows eliminating traditional SSH ports via **AWS Systems Manager Session Manager**.
  - Mastered automated event-driven incident alerting utilizing **CloudWatch Alarms** and **Amazon SNS**.
- **2. Worklog Documentation & Quality Audit:**
  - Conducted an exhaustive audit of lab **1.7.1**, verifying that all 20 screenshot artifacts render with high fidelity and accurate technical annotations.
  - Preserved strict bilingual parity (Vietnamese and English) and guaranteed zero broken internal links.
- **3. Project Proposal Research & Design:**
  - Embedded CloudWatch Advanced telemetry architectures, structured log filters, and automated alarm pipelines into the internship capstone (**[Project Proposal](/2-proposal/)**).
  - Outlined production observability SLOs/SLAs to be presented in the final internship defense.

---

### Next Week's Objectives (Week 8):

- **Infrastructure as Code with AWS CloudFormation (000037) & AWS CDK:**
  - Master declarative YAML templates, intrinsic functions, Nested Stacks, Change Sets, Drift Detection, and software-defined infrastructure using AWS CDK (TypeScript, L1/L2/L3 Constructs).
- **Centralized Fleet Operations with AWS Systems Manager (000024) & AWS Backup (000038):**
  - Zero-inbound-port access via Session Manager, fleet automation with Run Command, encrypted secrets in Parameter Store, and ransomware-resistant Backup Vault Lock (WORM).
- **Week 8 Review, Worklog & Project:** Consolidate IaC patterns and package automated infrastructure templates for the Capstone Project.
