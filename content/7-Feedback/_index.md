---
title: "Sharing and Feedback"
date: 2026-12-04
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

After completing 12 weeks in the **Workforce Bootcamp - First Cloud AI Journey (FCAJ)** program, I would like to share my honest reflections and practical suggestions to help make the program even stronger for future cohorts.

---

### Overall Evaluation

**1. Learning & Working Environment**  
The learning atmosphere across the FCAJ community and the in-person workshops at the AWS Vietnam Office (Level 26, Bitexco Financial Tower) is open, focused, and technically energizing. Hearing directly from AWS Solutions Architects, enterprise Tech Leads, and fellow interns from different universities created far stronger momentum than studying video courses alone.

**2. Support from Mentors and the Admin Team**  
The Mentors and Admin team provided clear structure from onboarding onto `cloudjourney.awsfcaj.com` and enforcing account security/budget controls to reviewing technical documentation. What I valued most was that Mentors encouraged us to read official documentation, inspect logs, and reason through failures ourselves rather than handing out ready-made answers.

**3. Alignment with My Information Technology Major**  
The 12-week curriculum connected directly with core university subjects (Computer Networks, Operating Systems, Databases, Software Architecture) while putting them into real AWS production contexts: multi-AZ CIDR/subnet design, chained Security Groups for RDS Multi-AZ, CLI/Boto3 automation, CloudWatch/Grafana observability, and enterprise AI Agent security with Bedrock AgentCore.

**4. Practical Skill Development**  
Beyond configuring individual AWS services, I built three lasting engineering habits:
- **FinOps Cost Awareness:** Setting AWS Budgets early, automating non-production EC2 stop/start schedules via Lambda & Slack, and auditing regions for lingering billable resources.
- **Rigorous Bilingual Documentation:** Structuring technical reports with architecture diagrams, parameter tables, and reproducible root-cause troubleshooting notes.
- **Early Exposure to Modern Cloud Security & AI Agents:** Analyzing **AWS Continuum** and attending deep-dive sessions on production **AgentCore** memory and two-door authentication.

**5. Community Culture & Knowledge Sharing**  
The *"Learn and Be Curious"* spirit within the AWS Study Group Vietnam community is genuine. From the Fireside Chat with **Dr. Werner Vogels** (CTO of Amazon) to weekend technical meetups, speakers candidly shared both production architectures and hard-earned lessons from real outages and cost pitfalls.

**6. Lab Curriculum & In-Person Technical Events**  
The hands-on lab portal (`cloudjourney.awsfcaj.com`) progresses logically from foundational services to advanced architectures, and having access to in-person events at the AWS Vietnam Office was one of the most rewarding privileges of the internship.

---

### Additional Questions

- **What did you find most satisfying during your internship?**  
  Two things stood out: first, deploying and debugging dozens of real hands-on labs on a live AWS account (spanning Auto Scaling, Hybrid DNS, DynamoDB, ElastiCache, CloudWatch Advanced, and S3 VPC Endpoints); second, attending the Fireside Chat with **Dr. Werner Vogels** and the **Enterprise AI Agent Architecture & Security** deep-dive sessions in person at Bitexco Level 26.

- **What do you think the program should improve for future interns?**  
  A few workshop guides reference older AWS Console layouts or legacy Python packages (such as `redis-py-cluster` on Python 3.12 or minor UI shifts in VPC/CloudWatch). While adapting to those differences was great troubleshooting practice, adding brief version-compatibility notes at the top of those labs would save new interns initial confusion.

- **If recommending to a friend, would you suggest they intern here? Why?**  
  **Definitely yes.** The program goes beyond passive theory—it builds self-learning discipline, real cloud deployment habits, cost accountability, and clear bilingual technical writing, all of which map directly to junior Cloud, DevOps, and Backend Engineer roles.

---

### Suggestions & Expectations

- **Do you have any suggestions to improve the internship experience?**  
  1. Introduce a **"5-Minute Post-Lab FinOps & Teardown Checklist"** in Week 1 highlighting common hidden cost traps (unassociated Elastic IPs, NAT Gateways, AWS WAF Web ACLs left on disabled CloudFront distributions, unattached EBS volumes, and OpenSearch Serverless collections).
  2. Host short **Architecture & Worklog Review Clinics (30–45 minutes)** every 3–4 weeks so intern teams can compare architectural trade-offs and learn from one another's troubleshooting logs.

- **Would you like to stay involved with the community in the future?**  
  Yes—I look forward to remaining an active member of the **AWS Study Group - First Cloud Journey** community, contributing future technical blog posts, and helping mentor upcoming student cohorts.

- **Closing Note:**  
  My sincere thanks to the **First Cloud AI Journey** Mentors, Admin team, and AWS Community Builders for their guidance, support, and inspiration throughout these 12 weeks.
