---
title: "Week 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---


### Objectives for Week 9:

- Master the **AWS 7Rs Migration Strategies** framework and server rehosting workflows using **VM Import/Export** (Workshop 000027) and **AWS Application Migration Service (AWS MGN)**.
- Execute near-zero-downtime database migrations via **AWS Database Migration Service (DMS)** (Workshop 000031) and **AWS Schema Conversion Tool (SCT)**.
- Architect scalable multi-VPC **Hub-and-Spoke** enterprise networks using **AWS Transit Gateway (TGW)**.
- Explore hybrid storage and high-throughput data transfers with **AWS DataSync** and **AWS Storage Gateway**.
- Dedicate Friday to consolidating learnings, updating bilingual Worklogs, cleaning up hourly network/migration resources, and drafting a Migration Runbook for the Capstone Project.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **7Rs Framework, VM Import/Export & Continuous Replication with AWS MGN:** <br>- Classify workloads across the 7Rs (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate). <br>- Convert VMDK/OVA virtual disk images into Custom AMIs using `aws ec2 import-image`. <br>- Study Replication Agent setup, continuous block-level replication, Test Cutover, and Cutover on AWS MGN. | 09/11/2026 | 09/11/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) & [Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Tuesday** | **Database Migration with AWS DMS & AWS SCT:** <br>- Convert heterogeneous database schemas, views, and constraints using AWS Schema Conversion Tool (SCT). <br>- Provision a DMS Replication Instance and validate Source/Target Endpoints (Amazon RDS MySQL). <br>- Run Full Load plus real-time Change Data Capture (CDC) replication tasks. | 10/11/2026 | 10/11/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Wednesday** | **Enterprise Hub-and-Spoke Networking with AWS Transit Gateway:** <br>- Contrast Full-Mesh VPC Peering limitations against centralized Transit Gateway topologies. <br>- Provision a Transit Gateway and attach Dev, Prod, and Shared Services VPCs. <br>- Enforce environment isolation through dedicated TGW Route Tables. | 11/11/2026 | 11/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thursday** | **Hybrid Storage & Bulk Transfers with AWS DataSync & Storage Gateway:** <br>- Configure accelerated, TLS-encrypted, checksum-verified file transfers from on-premises NAS to S3 via AWS DataSync. <br>- Compare AWS Storage Gateway modes: S3 File Gateway, Volume Gateway, and Tape Gateway. <br>- Apply bandwidth throttling policies to protect corporate WAN links. | 12/11/2026 | 12/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Friday** | **Week 9 Review, Worklog & Project:** <br>- **Knowledge Synthesis:** Consolidate 7Rs, MGN, DMS/SCT, Transit Gateway, and DataSync patterns. <br>- **Worklog & Cleanup:** Finalize bilingual Week 9 entries and delete DMS/TGW lab resources. <br>- **Capstone Project:** Document a structured data and application migration runbook. | 13/11/2026 | 13/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily Learning Details & Results:

#### 📌 Monday (09/11/2026) - 7Rs Framework, VM Import/Export & AWS MGN

* **What did I learn today?**
  * **AWS 7Rs Decision Framework:** Distinguished *Rehost* (lift-and-shift), *Replatform* (managed service adoption like RDS), *Refactor* (cloud-native/serverless re-architecture), *Repurchase* (SaaS), *Retain*, *Retire*, and *Relocate* (VMware Cloud on AWS).
  * **Offline Conversion via VM Import/Export:** Configured the `vmimport` IAM Role for `vmie.amazonaws.com`, uploaded a `.vmdk` image to S3, and triggered AMI conversion via CLI:
    ```bash
    aws ec2 import-image \
      --description "Ubuntu Server Migration Lab" \
      --disk-containers "Format=vmdk,UserBucket={S3Bucket=fcaj-migration-staging,S3Key=ubuntu-server.vmdk}"
    ```
  * **Continuous Rehosting with AWS MGN:** Installed the lightweight Replication Agent for continuous block-level replication into a Staging Area Subnet, running non-disruptive **Test Cutovers** prior to final **Cutover** with minimal downtime.
* **Challenges & Resolutions:**
  * *Missing ENA/NVMe drivers on boot & blocked TCP 1500:* Updated the source Linux kernel with ENA support prior to VMDK export, and opened outbound firewall rules for TCP port 1500 to allow MGN replication traffic.

---

#### 📌 Tuesday (10/11/2026) - Database Migration & CDC with AWS DMS & SCT

* **What did I learn today?**
  * **Schema Conversion with AWS SCT:** Assessed source-to-target compatibility and translated table DDL, views, and constraints for heterogeneous migrations.
  * **Near-Zero-Downtime Replication with AWS DMS:** Provisioned a `dms.t3.medium` Replication Instance, verified endpoint connectivity, and ran `Migrate existing data and replicate ongoing changes` (Full Load + MySQL `binlog` CDC) to keep the target Amazon RDS instance synchronized up to cutover.
* **Challenges & Resolutions:**
  * *CDC failed with `Binary logging not enabled on source database`:* Updated `my.cnf` on the source MySQL server with `log-bin=mysql-bin`, `binlog_format=ROW`, and `binlog_row_image=FULL`, then restarted the service.

---

#### 📌 Wednesday (11/11/2026) - Hub-and-Spoke Multi-VPC Networking with AWS Transit Gateway

* **What did I learn today?**
  * **Overcoming VPC Peering Complexity:** Eliminated the $N(N-1)/2$ full-mesh peering problem and lack of transitive routing by centralizing connectivity through a single AWS Transit Gateway cloud router.
  * **Segmented Routing via TGW Route Tables:** Configured separate `Prod-Route-Table` and `Dev-Route-Table` associations so both environments reach Shared Services while remaining strictly isolated from each other.
* **Challenges & Resolutions:**
  * *Asymmetric routing blocked cross-VPC pings:* Updated both the TGW Route Tables and each VPC's local Subnet Route Tables to direct remote CIDR ranges toward `tgw-xxxx`.

---

#### 📌 Thursday (12/11/2026) - Hybrid Cloud Storage with AWS DataSync & Storage Gateway

* **What did I learn today?**
  * **High-Throughput Transfers with AWS DataSync:** Connected DataSync Agents to NFS/SMB shares for accelerated, TLS-encrypted transfers to S3/EFS with built-in end-to-end checksum verification.
  * **Hybrid Storage Modes with AWS Storage Gateway:**
    * *S3 File Gateway:* Exposes S3 buckets over NFS/SMB with local low-latency caching.
    * *Volume Gateway:* Presents iSCSI block storage (Cached/Stored Volumes) backed asynchronously by EBS snapshots.
    * *Tape Gateway:* Replaces physical tape libraries with a Virtual Tape Library (VTL) archived in S3 Glacier.
* **Challenges & Resolutions:**
  * *Office WAN link saturation during bulk sync:* Applied `BytesPerSecond` bandwidth throttling on the DataSync Task during business hours.

---

#### 📌 Friday (13/11/2026) - Week 9 Review, Worklog & Migration Runbook

* **What did I learn today?**
  * **End-to-End Migration Architecture:** Synthesized server rehosting (MGN/VM Import), continuous database replication (DMS/SCT), centralized routing (TGW), and bulk hybrid transfers (DataSync).
  * **FinOps Cleanup:** Deleted DMS Replication Instances, Transit Gateway Attachments, and the Transit Gateway itself immediately after testing to eliminate hourly charges.
  * **Capstone Project Deliverable:** Authored a step-by-step cutover runbook detailing how legacy application data transitions safely to Multi-AZ AWS services.

---

### Next Week's Objectives (Week 10):

- **Serverless & Event-Driven Architecture:** Amazon API Gateway, Amazon SQS (000078), Amazon SNS, EventBridge, and AWS Step Functions.
- **Enterprise Container Orchestration:** Docker Multi-Stage builds, Amazon ECR, Amazon ECS Fargate (000067), and Amazon EKS Kubernetes (000126).

