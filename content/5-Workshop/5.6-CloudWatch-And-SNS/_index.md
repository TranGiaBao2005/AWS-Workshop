---
title : "CloudWatch & SNS Monitoring Setup"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

In this section, we build a proactive monitoring and alerting stack at **$0/month** (100% within AWS Free Tier): an SNS Topic (`exammaker-dev-alerts`), a 7-day CloudWatch Log Group (`/exammaker/dev/app`) with 4 Metric Filters, and exactly **10/10 Standard CloudWatch Alarms**.

#### Section Contents

1. [5.6.1. Create SNS Topic & Email Subscription (Figures 13 & 13.2)](5.6.1-SNS-Topic-Subscription/)
2. [5.6.2. Create 7-Day Log Group & 4 Metric Filters (Figures 14 & 14.2)](5.6.2-Log-Group-Metric-Filters/)
3. [5.6.3. Configure & Verify 10 CloudWatch Alarms (Figure 15)](5.6.3-CloudWatch-10-Alarms/)
