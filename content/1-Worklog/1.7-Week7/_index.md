---
title: "Week 7 Worklog"
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
- Participate in AWS Cloud Community technical events and author an in-depth technical article (**Blog 1**) covering enterprise cloud migration patterns.
- Systematically dedicate Friday to synthesizing technical skills, perfecting Worklog documentation, and advancing the internship capstone project (**Project Proposal**).

---

### Tasks to be implemented this week:

| Day           | Task                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Start Date | Completion Date | Reference Material                                                                             |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------- | :-------------- | :--------------------------------------------------------------------------------------------- |
| **Monday**    | **Advanced Observability with Amazon CloudWatch (CloudWatch Advanced Workshop):** <br>- Provision multi-instance lab cluster automatically with CloudFormation (`AwsWorkshopStack`). <br>- Configure Metric Math formulas and automated dynamic `SEARCH()` expressions. <br>- Standardize graph legends utilizing Dynamic Labels `${PROP('Dim.DimName')}`. <br>- Connect via SSM Session Manager and launch background synthetic logger (`logger.py`). <br>- Run advanced log queries with CloudWatch Logs Insights and save reusable queries. <br>- Create Metric Filter `PythonAppErrors`, alarm thresholds, and integrate into `ssmDashboard`. | 26/10/2026 | 26/10/2026      | [Amazon CloudWatch Observability Workshop](https://catalog.workshops.aws/observability/en-US/) |
| **Tuesday**   | **Workload Monitoring & Automated Incident Response with CloudWatch & SNS:** <br>- Design server stress-testing scenarios to simulate compute resource saturation. <br>- Configure multi-threshold composite alarms tracking correlated CPU and memory spikes. <br>- Route real-time alerts to operations team email and ChatOps channels via Amazon SNS. <br>- Benchmark Mean Time to Detect (MTTD) and optimize telemetry collection intervals.                                                                                                                                                                                                 | 27/10/2026 | 27/10/2026      | [AWS Observability Best Practices](https://aws.amazon.com/cloudwatch/)                         |
| **Wednesday** | **AWS Community Tech Event & Architecture Deep-Dive:** <br>- Attend AWS Cloud Practitioner & Solutions Day technical sessions. <br>- Engage with AWS Solutions Architects regarding enterprise observability and telemetry pipelines. <br>- Synthesize centralized observability architectural blueprints for distributed workloads.                                                                                                                                                                                                                                                                                                              | 28/10/2026 | 28/10/2026      | [AWS Community Events](https://aws.amazon.com/events/)                                         |
| **Thursday**  | **Author Technical Deep-Dive Article Blog 1 (Cloud Migration Journey):** <br>- Research end-to-end workload migration frameworks targeting AWS public cloud. <br>- Analyze AWS Well-Architected Framework pillars applied to practical enterprise migrations. <br>- Draft, review, and finalize technical publication Blog 1 for community sharing.                                                                                                                                                                                                                                                                                               | 29/10/2026 | 29/10/2026      | [AWS Architecture Center](https://aws.amazon.com/architecture/)                                |
| **Friday**    | **Week 7 Review, Worklog & Project:** <br>- Consolidate knowledge across CloudWatch Advanced, Logs Insights, Metric Math & SNS Alarms. <br>- Review and polish technical specifications and screenshot evidence for Worklog 1.7.1. <br>- Advance architecture design research and documentation for the internship Project Proposal.                                                                                                                                                                                                                                                                                                              | 30/10/2026 | 30/10/2026      | [Internal Review & Project Documentation](/2-proposal/)                                        |

---

### Achievements for Week 7:

#### 📌 Results for Monday (26/10/2026) - Advanced Observability with Amazon CloudWatch:

{{% notice tip %}}
👉 **Detailed Lab Report:** All CloudFormation stack specifications, Metric Math formulas, Logs Insights query commands, Metric Filter configurations, and the full collection of 24 hands-on screenshots are documented at: **[1.7.1. Advanced Observability with Amazon CloudWatch (CloudWatch Advanced Workshop)](1.7.1-cloudwatch-advanced/)**.
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

#### 📌 Results for Wednesday & Thursday (28/10 - 29/10/2026) - Tech Community Event & Technical Blog 1:

- **AWS Cloud Community Engagement:** Learned modern architectural paradigms, FinOps practices, and security governance frameworks from AWS technical leaders.
- **Completed Technical Deep-Dive Blog 1:** Published an exhaustive analysis detailing the end-to-end cloud migration lifecycle, grounded in AWS Well-Architected Framework principles.

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
  - Conducted an exhaustive audit of lab **1.7.1**, verifying that all 24 screenshot artifacts render with high fidelity and accurate technical annotations.
  - Preserved strict bilingual parity (Vietnamese and English) and guaranteed zero broken internal links.
- **3. Project Proposal Research & Design:**
  - Embedded CloudWatch Advanced telemetry architectures, structured log filters, and automated alarm pipelines into the internship capstone (**[Project Proposal](/2-proposal/)**).
  - Outlined production observability SLOs/SLAs to be presented in the final internship defense.

---

### Next Week's Objectives (Week 8):

- **Automated Infrastructure Deployment with AWS CloudFormation (Workshop 000037):**
  - Design modular CloudFormation templates (YAML/JSON) automating multi-tier VPC architectures.
  - Deploy Nested Stacks, integrate Systems Manager Parameter Store, and execute Drift Detection audits.
- **Configuration Governance and Compliance Auditing with AWS Config & CloudTrail:**
  - Enable AWS CloudTrail capturing immutable multi-region audit trails.
  - Implement AWS Config Rules for continuous security posture evaluation and automated non-compliance remediation.
- **Week 8 Review, Worklog & Project:** Consolidate automated governance workflows, polish worklogs, and advance internship project deliverables.
