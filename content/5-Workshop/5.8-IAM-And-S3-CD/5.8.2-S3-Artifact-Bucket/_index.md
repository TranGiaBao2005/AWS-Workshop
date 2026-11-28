---
title : "Create Private S3 Artifact Bucket"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.8.2. </b> "
---

#### Step 1: Create the Backend Release Artifact S3 Bucket

1. Open **Amazon S3 → Create bucket**.
2. Configure the bucket identity:
  * *AWS Region:* `Asia Pacific (Singapore) ap-southeast-1`
  * *Bucket type:* `General purpose` · **Namespace:** `Global namespace`
  * *Bucket name:* `aem-dev-backend-artifacts-9d07a0f131`

![Create S3 bucket aem-dev-backend-artifacts-9d07a0f131 in ap-southeast-1](/images/5-Workshop/5.8-IAM-And-S3-CD/19.png)

#### Step 2: Enforce Block All Public Access, SSE-S3 & 30-Day Lifecycle

* *Object Ownership:* `ACLs disabled (recommended)` (`Bucket owner enforced`).
* *Block Public Access:* enforce `Block all public access = Enabled` (100% private).
* *Default encryption:* `SSE-S3 (AES-256)` (**$0**).
* *Lifecycle rule:* automatically expire old build artifacts after `30 days` to avoid unnecessary storage accumulation.

![Configure ACLs disabled, Block all public access, and SSE-S3](/images/5-Workshop/5.8-IAM-And-S3-CD/19.2.png)
