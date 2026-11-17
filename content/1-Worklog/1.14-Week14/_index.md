---
title: "Week 14 Worklog"
date: 2026-12-14
weight: 14
chapter: false
pre: " <b> 1.14. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 14 Objectives:

- Synthesize the end-to-end **14-week internship journey** under the **First Cloud AI Journey (FCAJ)** program (September 14, 2026 – December 18, 2026).
- Finalize and publish the formal **Final Capstone Project Report** alongside comprehensive bilingual technical documentation.
- Design an executive presentation deck, author live system demonstration scripts, and defend the project before the FCAJ Evaluation Panel.
- Execute a disciplined **Cloud Resource Teardown** workflow following strict reverse-dependency hierarchies to eliminate post-internship operational costs.
- Complete official internship self-evaluations, process mentor feedback, and chart future career development milestones in Cloud and DevOps Engineering.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Internship Portfolio Consolidation & Code Archival:** <br>- Auditing and organizing all hands-on workshops across Weeks 1 through 13. <br>- Finalizing bilingual documentation quality and publishing project deliverables. <br>- Archiving infrastructure-as-code templates and project source code to GitHub. | 12/14/2026 | 12/14/2026 | [Final Report Review](/2-proposal/) |
| **Tuesday** | **Presentation Deck & Demonstration Rehearsal:** <br>- Authoring the 25-slide deck (Business Context, AWS Architecture, Validation, FinOps). <br>- Scripting live demo workflows: Auto Scaling, RDS Multi-AZ Failover, and CloudWatch telemetry. <br>- Rehearsing presentation pacing, speaker transitions, and Q&A timing. | 12/15/2026 | 12/15/2026 | [Presentation Deck](/2-proposal/) |
| **Wednesday** | **Capstone Project Defense Session:** <br>- Delivering the formal capstone project presentation before FCAJ Mentors and evaluators. <br>- Conducting a live demonstration of cloud infrastructure operating on AWS. <br>- Defending architectural trade-offs regarding security posture, resilience, and operational efficiency. | 12/16/2026 | 12/16/2026 | [Capstone Defense Session](https://cloudjourney.awsfcaj.com/) |
| **Thursday** | **Cloud Resource Teardown & Account Sanitization:** <br>- Following strict reverse-dependency deletion order to prevent `DependencyViolation` blocks. <br>- Terminating EC2 instances, deleting RDS databases, ElastiCache nodes, and VPC Endpoints. <br>- Securing persistent snapshots and archiving project artifacts into encrypted cold storage. | 12/17/2026 | 12/17/2026 | [AWS Resource Cleanup Guide](https://cloudjourney.awsfcaj.com/) |
| **Friday** | **Internship Wrap-up & Retrospective Evaluation:** <br>- Completing formal self-assessments and receiving official mentor evaluations. <br>- Synthesizing technical feedback and architectural insights. <br>- Successfully concluding the First Cloud AI Journey internship program! | 12/18/2026 | 12/18/2026 | [Self-Evaluation & Feedback](/6-self-evaluation/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (12/14/2026) - Portfolio Packaging & Source Archival

* **What did we learn today?**
  * **Professional Technical Documentation Packaging:** Audited the entire body of work spanning Weeks 1 through 13, verifying strict parameter accuracy, image link integrity, and specification consistency. Ensured 100% bilingual parity across both Vietnamese (`.vi.md`) and English (`.md`) documentation trees.
  * **Open-Source Delivery via GitHub:** Staged modular CloudFormation YAML templates, AWS CDK TypeScript constructs, Python Boto3 automation scripts, and multi-stage Dockerfiles within the official GitHub repository. Authored a comprehensive `README.md` Quick Start guide with architectural flowcharts.
* **Encountered Challenges & Solutions:**
  * *Broken Markdown Hyperlink Paths:* Found several legacy relative links with invalid path prefixes during documentation cross-checks. Solution: Deployed automated `markdown-link-check` scripts across the `content/` hierarchy to sanitize and validate all internal links.

---

#### 📌 Tuesday (12/15/2026) - Presentation Deck & Live Demo Scripting

* **What did we learn today?**
  * **Communicating Cloud Architecture Solutions:** Built a 25-slide executive deck structured around the STAR (Situation, Task, Action, Result) framework. Emphasized quantitative business metrics: 99.99% system availability, sub-minute recovery times (RTO < 1 min), and 42% cost reduction compared to on-premises baseline projections.
  * **Resilience Demonstration Scripting:**
    1. Scenario 1: Generated synthetic CPU load (85%+), observing CloudWatch Alarms trigger and EC2 Auto Scaling scale out 2 new instances in under 3 minutes.
    2. Scenario 2: Initiated forced primary database reboot with failover, verifying that Amazon RDS Multi-AZ shifted traffic to the standby instance within 45 seconds without dropped HTTP connections.
    3. Scenario 3: Real-time interactive session querying live operational telemetry via the Amazon Bedrock conversational assistant.
* **Encountered Challenges & Solutions:**
  * *Demonstration Overrunning Allotted Time:* The dry-run rehearsal clocked 28 minutes against a strict 20-minute presentation ceiling. Solution: Pruned granular console walkthroughs, focusing exclusively on architectural diagrams and live dashboard telemetry graphs.

---

#### 📌 Wednesday (12/16/2026) - Capstone Project Defense Session

* **What did we learn today?**
  * **Technical Defense Before Solutions Architects:** Confidently presented architectural decisions before the FCAJ evaluation panel and AWS Solutions Architects.
  * **Key Insights from Technical Q&A:**
    * *Security Question:* How does the system guarantee zero data exfiltration between EC2 and S3? ➔ Articulated the private VPC Gateway Endpoint architecture combined with strict bucket endpoint policies implemented in Week 7.
    * *Cost Governance Question:* Why adopt EC2 Auto Scaling and RDS Multi-AZ over a pure serverless approach? ➔ Explained that predictable baseline enterprise traffic combined with 1-year Savings Plans yields substantially lower unit economics than high-concurrency serverless executions running 24/7.
* **Encountered Challenges & Solutions:**
  * *Intermittent Network Latency During Live Demo:* WiFi instability threatened live console access. Having prepared an offline fallback demonstration video recording, the panel commended the disciplined risk-mitigation mindset and thorough operational preparation.

---

#### 📌 Thursday (12/17/2026) - Disciplined Cloud Resource Teardown

* **What did we learn today?**
  * **Reverse-Dependency Decommissioning Hierarchy:** Systematically prevented `DependencyViolation` deadlocks by dismantling resources from the edge application layer down to core networking primitives:
    1. Deleted Auto Scaling Groups and removed Launch Templates.
    2. Deregistered Application Load Balancer Target Groups and released Elastic IPs.
    3. Captured final DB Snapshots and terminated the Amazon RDS Multi-AZ cluster.
    4. Flushed and deleted ElastiCache Redis clusters and OpenSearch Serverless collections.
    5. Deleted VPC Endpoints, NAT Gateways, Internet Gateways, and Route Tables.
    6. Finally, deleted the root Amazon VPC.
  * **FinOps Clean Slate Verification:** Inspected the AWS Billing Console and Cost Explorer across both `us-east-1` and `ap-southeast-1` regions, confirming that all hourly metered resources were completely purged, returning prospective account run rates to exactly $0.
* **Encountered Challenges & Solutions:**
  * *VPC Refusing Deletion Due to `DependencyViolation`:* The console reported active network interfaces attached to the VPC. Root cause: Lingering Elastic Network Interfaces (ENIs) provisioned by Lambda VPC access had not yet released. Solution: Inspected the Network Interfaces panel under EC2, detached dangling ENIs manually, and completed VPC deletion cleanly.

---

#### 📌 Friday (12/18/2026) - Internship Conclusion & Retrospective Evaluation

* **What did we learn today?**
  * **Self-Assessment & Professional Retrospective:** Completed the formal self-assessment report ([Self-Evaluation Report](/6-self-evaluation/)), reflecting on the remarkable trajectory from cloud novice to an engineer capable of designing and automating resilient systems against the AWS Well-Architected Framework.
  * **Synthesizing Mentor Feedback:** Received valuable praise regarding disciplined FinOps awareness, documentation rigor, and proactive incident response skills.
  * **Next Career Milestones:** Defined actionable future objectives: sitting for the AWS Certified Solutions Architect - Associate (SAA-C03) examination and pursuing professional Cloud & DevOps engineering career opportunities.
