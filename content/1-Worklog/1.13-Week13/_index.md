---
title: "Week 13 Worklog"
date: 2024-01-01
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

{{% notice warning %}}
⚠️ **Note:** The information below is for reference only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

### Objectives for Week 13:

* Execute realistic **Load Testing & Stress Testing** against the entire capstone project infrastructure simulating high concurrent user traffic.
* Perform comprehensive **Security Assessments**, auditing IAM roles, network access controls, and data encryption configurations.
* Implement **FinOps & Cost Optimization** through resource right-sizing based on AWS Compute Optimizer recommendations.
* Conduct a formal **AWS Well-Architected Framework Review** across all 6 architectural pillars.
* Consolidate Week 13 learnings, finalize Worklog documentation, and prepare the project sign-off portfolio.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| **Monday** | **System Load & Stress Testing:** <br>- Author load testing scenarios with Locust / Apache Benchmark. <br>- Monitor Auto Scaling Group and ALB dynamic scaling triggers under traffic spikes. <br>- Evaluate response latency curves and monitor HTTP 5xx error distributions. | 07/12/2026 | 07/12/2026 | [AWS Well-Architected Reliability](https://aws.amazon.com/architecture/well-architected/) |
| **Tuesday** | **Security Assessment & Compliance Audit:** <br>- Review IAM Roles and Policies enforcing the principle of least privilege. <br>- Audit network access paths and enforce encryption at-rest and in-transit. <br>- Evaluate posture via AWS Security Hub and Amazon GuardDuty findings. | 08/12/2026 | 08/12/2026 | [AWS Security Pillar](https://aws.amazon.com/architecture/well-architected/) |
| **Wednesday** | **Cost Optimization & Resource Tuning (FinOps):** <br>- Analyze granular cost breakdowns in AWS Cost Explorer and AWS Budgets. <br>- Apply sizing recommendations from AWS Compute Optimizer for EC2 and RDS. <br>- Model Spot Instances and Savings Plans for long-term budget efficiency. | 09/12/2026 | 09/12/2026 | [AWS Cost Optimization Pillar](https://aws.amazon.com/architecture/well-architected/) |
| **Thursday** | **Disaster Recovery Simulation & Validation:** <br>- Validate automated backup schedules and snapshot integrity for RDS and S3. <br>- Simulate Availability Zone degradation to evaluate Multi-AZ failover responsiveness. <br>- Measure Recovery Time Objective (RTO) and Recovery Point Objective (RPO). | 10/12/2026 | 10/12/2026 | [AWS Disaster Recovery](https://aws.amazon.com/disaster-recovery/) |
| **Friday** | **Week 13 Review, Worklog & Project Finalization:** <br>- Consolidate stress testing benchmarks, cost savings, and security hardening results. <br>- Complete comprehensive documentation for Week 13. <br>- Freeze project architecture baseline ahead of final defense presentations. | 11/12/2026 | 11/12/2026 | [Project Documentation](/2-proposal/) |

---

### Achievements for Week 13:

* Successfully validated system resilience under synthetic high-load scenarios with zero service downtime.
* Reduced projected monthly cloud run costs by 35% through rightsizing and FinOps optimizations.
* Completed full 6-pillar AWS Well-Architected assessment matrix for the capstone system.

---

### Next Week's Objectives (Week 14):

* **Internship Final Synthesis:** Finalize comprehensive internship report and publish complete architectural portfolios.
* **Presentation & Demo Preparation:** Rehearse project defense presentation and dynamic live architecture demonstrations.
* **Handover & Resource Cleanup:** Safely decommission transient lab infrastructure and complete final internship evaluations.
