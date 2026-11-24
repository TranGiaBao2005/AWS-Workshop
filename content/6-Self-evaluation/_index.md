---
title: "Self-Assessment"
date: 2026-12-04
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Throughout my 12-week internship at **Amazon Web Services Vietnam Company Limited** (**Workforce Bootcamp - First Cloud AI Journey**) from **September 14, 2026** to **December 04, 2026**, I had the opportunity to build and troubleshoot workloads directly on AWS and connect the theoretical coursework from **FPT University** with practical cloud engineering workflows.

During the program, I completed a structured **12-week hands-on curriculum** (covering VPC networking, EC2 Auto Scaling, RDS Multi-AZ, DynamoDB, ElastiCache Redis, Route 53 Hybrid DNS, Service Quotas governance, serverless EC2 cost optimization with AWS Lambda & Slack, Grafana & CloudWatch Advanced observability, IaC with CloudFormation/CDK, workload migration, ECS/EKS containers, Data Lakes, and Amazon Bedrock), published a community technical analysis on **AWS Continuum for Code Vulnerabilities**, attended three technical events at the AWS Vietnam Office (Bitexco Financial Tower), and implemented the **Secure Hybrid Access to Amazon S3 via VPC Endpoints** workshop. Through this work, I strengthened my practical capabilities in network isolation, CLI/Boto3 automation, FinOps cost control, systematic troubleshooting, and bilingual technical documentation.

Below is my self-assessment based on my actual performance during the internship:

| No. | Criteria | Description | Good | Fair | Average |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | **Professional knowledge & skills** | Solid grasp of core AWS services; able to deploy multi-tier networks, databases, CLI/Boto3 automation, and observability pipelines | ✅ | ☐ | ☐ |
| 2 | **Ability to learn** | Quickly picked up new services and patterns (Hybrid DNS, CloudWatch Metric Math, AgentCore, AWS Continuum) through labs and docs | ✅ | ☐ | ☐ |
| 3 | **Proactiveness** | Built test environments independently, inspected logs before escalating issues, and actively attended in-person sessions at AWS Vietnam | ✅ | ☐ | ☐ |
| 4 | **Sense of responsibility** | Completed all 12 weekly worklogs on schedule with verifiable screenshots and audited account costs after lab sessions | ✅ | ☐ | ☐ |
| 5 | **Discipline** | Followed the Monday–Friday study cadence, resource tagging conventions, and post-lab teardown checklists | ☐ | ✅ | ☐ |
| 6 | **Progressive mindset** | Acted on Mentor and peer feedback to streamline report structure and keep technical writing concise and accurate | ✅ | ☐ | ☐ |
| 7 | **Communication** | Authored clear bilingual (VI/EN) technical reports and engaged effectively with peers and speakers during community meetups | ☐ | ✅ | ☐ |
| 8 | **Teamwork** | Collaborated well with fellow FCAJ interns when discussing architectures, sharing debugging tips, and attending workshops | ✅ | ☐ | ☐ |
| 9 | **Professional conduct** | Respected Mentors, organizers, and community members; adhered to account security baselines and office rules | ✅ | ☐ | ☐ |
| 10 | **Problem-solving skills** | Isolated faults layer by layer (IAM policies, Security Groups, Route Tables, DNS, CloudWatch Logs) and documented fixes | ✅ | ☐ | ☐ |
| 11 | **Contribution to project/team** | Published a technical article on the AWS Study Group Facebook community and produced detailed, reproducible lab documentation | ✅ | ☐ | ☐ |
| 12 | **Overall** | Overall completion of internship milestones and growth in cloud engineering maturity across the 12 weeks | ✅ | ☐ | ☐ |

---

### Areas for Improvement

* **Stricter Post-Lab Resource Teardown Discipline:** Earlier in the internship, I accidentally left an unassociated Elastic IP in Singapore (`ap-southeast-1`) and an AWS WAF Web ACL attached to a disabled CloudFront distribution in `us-east-1`, which generated small recurring daily charges. After auditing all 17 regions via AWS CLI and Cost Explorer to remove them, I established a strict habit of checking Elastic IPs, WAF Web ACLs, Snapshots, and orphaned ENIs immediately after every lab.
* **Time Management During Complex Infrastructure Debugging:** When troubleshooting cross-service permission issues (IAM/KMS/Lake Formation) or multi-VPC hybrid routing, I sometimes spent too long testing changes manually in the Console before switching to structured CLI queries and CloudWatch Logs.
* **Technical Presentation & Architectural Trade-Off Defense:** I want to further sharpen my ability to explain service trade-offs (cost vs. latency vs. operational overhead) concisely in English during live technical reviews.
