---
title: "Week 9 Worklog"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 9 Objectives:

- Analyze and evaluate enterprise workload migration strategies using the **AWS 7Rs Migration Framework** (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate).
- Execute physical and virtual server migrations from on-premises environments (VMware, Hyper-V, VirtualBox) to AWS using **VM Import/Export** (Workshop 000027) and **AWS Application Migration Service (AWS MGN)**.
- Implement homogenous and heterogeneous database migrations with near-zero downtime utilizing **AWS Database Migration Service (DMS)** (Workshop 000031) and the **AWS Schema Conversion Tool (SCT)**.
- Design scalable, enterprise-grade multi-VPC networking topologies utilizing **AWS Transit Gateway (TGW)** to eliminate full-mesh peering complexity.
- Explore hybrid cloud storage architectures and accelerated bulk data transfers using **AWS DataSync** and **AWS Storage Gateway**.
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and formulating a robust database migration plan for the internship **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Server Migration with VM Import/Export & AWS MGN:** <br>- Exporting on-premises VMDK/OVA disk images and uploading to Amazon S3. <br>- Executing `aws ec2 import-image` to convert virtual disks into custom AMIs. <br>- Analyzing continuous block-level data replication mechanisms via AWS MGN. | 11/09/2026 | 11/09/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) |
| **Tuesday** | **Database Migration & Continuous Replication with AWS DMS & SCT:** <br>- Converting database schemas across heterogeneous database engines using AWS SCT. <br>- Configuring DMS Replication Instances, Source Endpoints, and Target RDS MySQL Endpoints. <br>- Executing Full Load migrations combined with continuous Change Data Capture (CDC). | 11/10/2026 | 11/10/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Wednesday** | **Scalable Enterprise Networking with AWS Transit Gateway (TGW):** <br>- Provisioning a centralized Transit Gateway router to interconnect multiple isolated VPCs. <br>- Creating VPC Attachments across functional tiers (Shared Services VPC, Web VPC, DB VPC). <br>- Designing dedicated Transit Gateway Route Tables and validating cross-VPC routing. | 11/11/2026 | 11/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thursday** | **Accelerated Data Transfer & Hybrid Storage with DataSync & Storage Gateway:** <br>- Deploying DataSync Agents to automate high-throughput data synchronization into Amazon S3. <br>- Evaluating AWS Storage Gateway architectures: File Gateway (NFS/SMB), Volume Gateway, and Tape Gateway. <br>- Analyzing transfer bandwidth optimization and hybrid storage cost models. | 11/12/2026 | 11/12/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Friday** | **Week 9 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate 7Rs migration patterns, DMS/MGN mechanics, and Transit Gateway routing. <br>- **Worklog Completion:** Finalize bilingual Week 9 documentation and teardown lab resources. <br>- **Project Work:** Develop an end-to-end migration and cutover plan for the internship Capstone Project. | 11/13/2026 | 11/13/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 9 Achievements:

#### 📌 Monday (11/09/2026) - Virtual Machine Migration via VM Import/Export:
* **Seamless Server Rehosting:** Packaged an on-premises virtual machine disk into VMDK format, staged the artifacts on Amazon S3, and converted the images into an EC2 Custom AMI via the AWS CLI. Validated server launch, kernel integrity, and network connectivity without data loss.
* **Continuous Block-Level Replication:** Analyzed how AWS MGN utilizes lightweight client agents to stream block-level changes over TLS, enabling minimal business downtime cutovers in enterprise migration initiatives.

#### 📌 Tuesday (11/10/2026) - Database Migration with AWS DMS & SCT:
* **Automated Heterogeneous Conversion:** Evaluated source relational schemas, converting legacy constraints, table definitions, and indexes into Amazon RDS-compatible DDL using the AWS Schema Conversion Tool.
* **Zero-Downtime Synchronization (CDC):** Configured an AWS DMS task combining initial full data load with Change Data Capture (CDC), maintaining continuous replication between the primary transactional source and the AWS target until cutover verification.

#### 📌 Wednesday (11/11/2026) - Hub-and-Spoke Topology with AWS Transit Gateway:
* **Architecture Simplification:** Replaced point-to-point VPC Peering mesh networks with a centralized Transit Gateway router, drastically reducing operational overhead as the VPC count scales.
* **Network Segmentation & Isolation:** Built segregated route tables within the Transit Gateway to enforce strict traffic isolation between development and production environments, while maintaining governed shared-access paths to administrative services.

#### 📌 Thursday (11/12/2026) - Hybrid Storage Integration with DataSync:
* **High-Throughput Ingestion:** Validated automated data transfers into Amazon S3 at speeds up to 10x faster than legacy open-source utilities (e.g., rsync, scp) by taking advantage of multi-threaded parallel transfers with built-in checksum verification.
* **On-Premises Cloud Storage Extension:** Reviewed AWS Storage Gateway File Gateway deployments, enabling existing enterprise applications to mount cloud-backed S3 buckets as local network shares via NFS and SMB protocols.
