---
title : "IAM Roles & S3 Artifact Bucket Setup"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

In this section, we establish a keyless, SSH-free security foundation for operations and CI/CD: **3 IAM Roles** (`aem-*`) enforcing **Least Privilege / GitHub OIDC** and a **private S3 Artifact Bucket** (`aem-dev-backend-artifacts-9d07a0f131`) with a 30-day automatic expiration lifecycle rule.

#### Section Contents

1. [5.8.1. Configure 3 IAM Roles & Permissions Policies (Figure 18)](5.8.1-IAM-Roles-Policies/)
2. [5.8.2. Create Private S3 Artifact Bucket & 30-Day Lifecycle (Figures 19 & 19.2)](5.8.2-S3-Artifact-Bucket/)
