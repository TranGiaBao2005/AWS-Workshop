---
title: "Week 12"
date: 2026-11-30
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Objectives for Week 12:

- Synthesize the end-to-end **12-week internship journey** under the **First Cloud AI Journey (FCAJ)** program (September 14, 2026 – December 04, 2026).
- Finalize and publish the **Final Capstone Project Report**, bilingual documentation website, and clean GitHub source repositories.
- Build the presentation slide deck, rehearse live demos, and defend the Capstone Project before the FCAJ Mentor panel.
- Execute dependency-ordered **Cloud Resource Teardown** across all AWS regions, confirming a $0 ongoing spend baseline.
- Complete the **Self-Evaluation** (`6-Self-evaluation`), absorb Mentor feedback, and map out the next AWS certification roadmap.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **11-Week Synthesis, Final Packaging & GitHub Release:** <br>- Audit Weeks 1–11 for bilingual EN/VI parity, accurate image paths, and unbroken internal links. <br>- Publish IaC templates (CloudFormation/CDK), Python Boto3 scripts, and Dockerfiles with a clear `README.md`. <br>- Verify a zero-error static site build (`hugo --minify`) across both languages. | 30/11/2026 | 30/11/2026 | [Final Report Review](/2-proposal/) |
| **Tuesday** | **Slide Deck Preparation & Live Demo Rehearsal:** <br>- Design a concise STAR-structured presentation deck (Problem, AWS Architecture, Benchmarks, FinOps). <br>- Rehearse the end-to-end live demo workflow and record a fallback backup video. <br>- Time-box the presentation strictly within the defense slot. | 01/12/2026 | 01/12/2026 | [Presentation Deck](/2-proposal/) |
| **Wednesday** | **Capstone Project Defense before FCAJ Mentor Panel:** <br>- Present the cloud architecture design and implementation outcomes on AWS. <br>- Perform a live demonstration of running workloads and observability dashboards. <br>- Defend architectural trade-offs across security, high availability, and cost optimization. | 02/12/2026 | 02/12/2026 | [Capstone Defense](https://cloudjourney.awsfcaj.com/) |
| **Thursday** | **Disciplined Cloud Resource Teardown ($0 Audit):** <br>- Terminate resources in dependency order (Compute/ALB ➔ DB/Cache ➔ NAT/EIP/Endpoints ➔ VPC) to avoid `DependencyViolation`. <br>- Audit all AWS regions (`us-east-1`, `ap-southeast-1`) via AWS CLI and Cost Explorer. <br>- Verify zero lingering hourly or daily charges on the AWS account. | 03/12/2026 | 03/12/2026 | [AWS Resource Cleanup](https://cloudjourney.awsfcaj.com/) |
| **Friday** | **Self-Evaluation & Internship Completion:** <br>- Finalize Self-Assessment (`6-Self-evaluation`) and Sharing & Feedback (`7-Feedback`). <br>- Capture constructive technical feedback from FCAJ Mentors. <br>- Establish a preparation roadmap for **AWS Certified Solutions Architect - Associate (SAA-C03)**. | 04/12/2026 | 04/12/2026 | [Self-Evaluation](/6-self-evaluation/) |

---

### Daily Focus & Deliverables:

#### 📌 Monday (30/11/2026) - Final Documentation Packaging & GitHub Release

* **Core Focus:**
  * **Report-Wide Quality Audit:** Cross-check all 12 Worklog weeks, Proposal, Blogs, Events, and Workshop sections to guarantee valid image rendering and unbroken links across English and Vietnamese builds.
  * **GitHub Repository Standardization:** Package CloudFormation/CDK templates, Boto3 automation scripts, and Dockerfiles with an actionable `README.md` architecture overview.
* **Key Safeguard:**
  * Audit `.gitignore` and commit history before pushing to ensure zero AWS Access Keys, Secret Keys, or hardcoded credentials ever reach GitHub.

---

#### 📌 Tuesday (01/12/2026) - Slide Deck Design & Live Demo Rehearsal

* **Core Focus:**
  * **STAR-Structured Architecture Deck:** Highlight business problem framing, Well-Architected service selection, architectural diagrams, validation metrics, and AWS Pricing Calculator cost estimates.
  * **Demo Dry-Run & Fail-Safe:** Walk through live demonstration checkpoints under time constraints and capture a clean backup screen recording in case of venue network instability.

---

#### 📌 Wednesday (02/12/2026) - Capstone Project Defense before FCAJ Mentors

* **Core Focus:**
  * **Technical Presentation & Live Demo:** Walk the panel through the architecture blueprint and live AWS telemetry dashboards.
  * **Q&A Defense:** Articulate concrete architectural trade-offs regarding Zero-Trust security (Least Privilege, Private Subnets, VPC Endpoints), resilience (Multi-AZ, Auto Scaling), and FinOps cost efficiency.

---

#### 📌 Thursday (03/12/2026) - Disciplined Cloud Resource Teardown

* **Core Focus:**
  * **Dependency-Ordered Teardown Checklist:**
    1. Delete Auto Scaling Groups, ECS/EKS Clusters, and Launch Templates.
    2. Delete Application Load Balancers, Target Groups, and release all idle Elastic IPs.
    3. Terminate Amazon RDS, ElastiCache, OpenSearch/SageMaker endpoints, and unused CloudFront/WAF Web ACLs.
    4. Remove VPC Endpoints, NAT Gateways, Internet Gateways, and finally custom VPCs.
  * **Multi-Region FinOps Audit:** Sweep all 17 AWS regions via AWS CLI and review AWS Cost Explorer/Budgets to guarantee $0 recurring hourly/daily charges.
* **Troubleshooting Tip:**
  * If VPC deletion raises `DependencyViolation`, inspect **EC2 Network Interfaces (ENIs)** to detach orphaned Lambda or VPC Endpoint interfaces before retrying.

---

#### 📌 Friday (04/12/2026) - Self-Evaluation & 12-Week Internship Completion

* **Core Focus:**
  * **Objective Self-Assessment ([Self-Evaluation](/6-self-evaluation/)):** Reflect on technical progression across 12 weeks—from foundational IAM/VPC/EC2 labs to IaC automation, deep observability, container orchestration, data lakes, and Generative AI on AWS.
  * **Mentor Feedback & Career Roadmap:** Incorporate Mentor recommendations, complete internship closeout formalities, and transition into preparation for **AWS Certified Solutions Architect - Associate (SAA-C03)**.
