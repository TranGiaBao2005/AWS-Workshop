---
title : "Workshop"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

# Deploying AWS Infrastructure for the AI Exam Maker Platform

#### Overview

In this workshop, we provision and configure the core AWS infrastructure in **`ap-southeast-1` (Singapore)** for the **AI Exam Maker** platform, following **Least Privilege** security principles and strict FinOps cost optimization within a **$200.00/Quarterly** budget ceiling.

The implementation is organized cleanly by AWS service and console walkthrough screen (`Figure 1` through `Figure 19.2`), concluding with a complete post-demo teardown guide.

#### Workshop Contents

1. [5.1. Workshop Overview](5.1-Workshop-overview/)
2. [5.2. Amazon Cognito User Pool, App Client & Groups Setup](5.2-Cognito/)
3. [5.3. Amazon RDS PostgreSQL 16 Database Setup](5.3-RDS-PostgreSQL/)
4. [5.4. Amazon SQS & Dead-Letter Queue Setup](5.4-SQS-And-DLQ/)
5. [5.5. Centralized Configuration with SSM Parameter Store](5.5-SSM-Parameter-Store/)
6. [5.6. Amazon SNS Alerts & CloudWatch Monitoring Setup](5.6-CloudWatch-And-SNS/)
7. [5.7. Cost Control with AWS Budgets ($200/Quarter)](5.7-AWS-Budgets/)
8. [5.8. IAM Roles & S3 Artifact Bucket Setup for CI/CD](5.8-IAM-And-S3-CD/)
9. [5.9. Clean up](5.9-Cleanup/)
