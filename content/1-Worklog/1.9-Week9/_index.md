---
title: "Week 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 9 Objectives:

- Analyze and evaluate enterprise cloud migration strategies according to the formal **AWS 7Rs Migration Framework** (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate).
- Dedicate **two full deep-dive days (Monday & Tuesday)** to mastering server migration techniques: from offline VMDK image conversions with **VM Import/Export** (Workshop 000027) to continuous block-level data replication via **AWS Application Migration Service (AWS MGN)**.
- Implement homogenous and heterogeneous database migrations with near-zero downtime utilizing **AWS Database Migration Service (DMS)** (Workshop 000031) coupled with the **AWS Schema Conversion Tool (SCT)**.
- Architect scalable, enterprise-grade multi-VPC hub-and-spoke networking topologies utilizing **AWS Transit Gateway (TGW)** to eliminate full-mesh peering complexity.
- Explore hybrid cloud storage architectures and accelerated bulk data transfers using **AWS DataSync** and **AWS Storage Gateway**.
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and formulating an end-to-end migration runbook for the internship **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Server Migration (Part 1) - 7Rs Strategies & VM Import/Export:** <br>- Evaluating infrastructure inventory and classifying workloads via the 7Rs Framework. <br>- Exporting on-premises VMDK/OVA disk images and staging on Amazon S3. <br>- Executing `aws ec2 import-image` CLI workflows to generate production Custom AMIs. <br>- Launching EC2 instances from converted AMIs and validating operating system integrity. | 11/09/2026 | 11/09/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) |
| **Tuesday** | **Server Migration (Part 2) - Real-Time Block Replication with AWS MGN:** <br>- Installing the lightweight AWS Replication Agent on Linux/Windows source servers. <br>- Configuring Replication Settings Templates (Staging Subnets, EBS volume types, KMS keys). <br>- Monitoring continuous block-level data synchronization over TLS channels. <br>- Executing non-disruptive Test Cutover instances and performing the final Cutover. | 11/10/2026 | 11/10/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Wednesday** | **Continuous Database Migration with AWS DMS & AWS SCT:** <br>- Converting database schemas across heterogeneous engines using the Schema Conversion Tool. <br>- Provisioning DMS Replication Instances, Source Endpoints, and Target RDS Endpoints. <br>- Executing Full Load migrations combined with continuous Change Data Capture (CDC). | 11/11/2026 | 11/11/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Thursday** | **Enterprise Hub-and-Spoke Networking with AWS Transit Gateway & DataSync:** <br>- Provisioning a centralized Transit Gateway router to interconnect multi-account VPCs. <br>- Creating VPC Attachments across functional tiers (Dev, Prod, Shared Services). <br>- Implementing isolated route tables within TGW to enforce strict environment segregation. <br>- Accelerating large-scale on-premises NAS data synchronization into S3 using AWS DataSync. | 11/12/2026 | 12/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Friday** | **Week 9 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate 7Rs methodology, server migration tooling, DMS CDC, and TGW routing. <br>- **Worklog Completion:** Finalize bilingual Week 9 documentation and teardown lab resources. <br>- **Project Work:** Develop an end-to-end migration and cutover plan for the internship Capstone Project. | 11/13/2026 | 11/13/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (11/09/2026) - Server Migration (Part 1): 7Rs Strategies & VM Import/Export

* **What did we learn today?**
  * **Systematic Evaluation via the AWS 7Rs Framework:** Evaluated the architectural rationale behind each migration path:
    * *Rehost (Lift-and-shift):* Migrating existing virtual machine disks directly into EC2 without code modifications.
    * *Replatform (Lift-tinker-and-shift):* Substituting self-managed components with managed equivalents (e.g., self-hosted MySQL to Amazon RDS).
    * *Refactor / Re-architect:* Redesigning monolithic applications into cloud-native microservices or serverless architectures.
    * *Repurchase:* Transitioning to commercial SaaS solutions.
    * *Retain:* Keeping sensitive workloads on-premises due to compliance or legacy coupling.
    * *Retire:* Decommissioning redundant applications identified during discovery.
    * *Relocate:* Rapidly moving VMware infrastructure to VMware Cloud on AWS without hardware conversion.
  * **End-to-End Execution of VM Import/Export:**
    1. Built a baseline Ubuntu Linux web server on a local hypervisor environment.
    2. Exported the virtual machine hard disk image into `.vmdk` format.
    3. Created an Amazon S3 staging bucket `fcaj-migration-staging-887086382708` and uploaded the `.vmdk` image.
    4. Configured the `vmimport` IAM Role with a trust policy for `vmie.amazonaws.com` granting S3 get and EC2 write access.
    5. Executed image conversion via the AWS CLI:
       ```bash
       aws ec2 import-image \
         --description "Ubuntu Web Server Migration" \
         --disk-containers "Format=vmdk,UserBucket={S3Bucket=fcaj-migration-staging-887086382708,S3Key=ubuntu-server.vmdk}"
       aws ec2 describe-import-image-tasks --import-task-ids import-ami-0abc123def456
       ```
    6. Launched an EC2 instance from the generated Custom AMI, validating that the web daemon, local files, and network configurations remained intact.
* **Encountered Challenges & Solutions:**
  * *Missing Kernel Virtualization Drivers on Boot:* The converted EC2 instance stalled during initialization due to missing Elastic Network Adapter (ENA) and NVMe storage drivers. Solution: Booted into the source VM prior to export, updated the Linux kernel to install official AWS Nitro driver packages, and successfully re-imported the VMDK.

---

#### 📌 Tuesday (11/10/2026) - Server Migration (Part 2): Continuous Block Replication with AWS MGN

* **What did we learn today?**
  * **Architecture of AWS Application Migration Service (MGN):** Mastered how AWS MGN provides non-disruptive, block-level background replication directly from live operating systems, decoupling replication throughput from OS filesystem locks.
  * **Step-by-Step Production Migration Workflow:**
    1. Configured the Replication Settings Template: Selected dedicated staging subnets, cost-efficient replication storage volumes (gp3/sc1), and KMS customer-managed encryption keys.
    2. Installed the lightweight AWS Replication Agent on the running host:
       ```bash
       wget -O ./aws-replication-installer-init.py https://aws-application-migration-service-us-east-1.s3.amazonaws.com/latest/linux/aws-replication-installer-init.py
       python3 ./aws-replication-installer-init.py --region us-east-1 --aws-access-key-id <KEY> --aws-secret-access-key <SECRET>
       ```
    3. Monitored initial block synchronization until the agent entered steady-state `Continuous Data Replication`.
    4. Launched non-disruptive Test Instances inside a staging VPC to validate application boot sequences, network routes, and database connectivity.
    5. Conducted the final Cutover: Changed instance state to `Ready for Cutover`, stopped source server processes, and launched the final production instance, achieving a business cutover window under 3 minutes.
* **Encountered Challenges & Solutions:**
  * *Firewall Block on Replication Port (TCP 1500):* The source agent reported `Failed to connect to replication server`. Root cause: Outbound firewall policies on the local perimeter blocked outbound TCP port 1500 traffic. Solution: Opened outbound TCP 1500 to the regional AWS MGN replication endpoints, enabling real-time TLS data streaming.

---

#### 📌 Wednesday (11/11/2026) - Database Migration & Continuous CDC with AWS DMS & SCT

* **What did we learn today?**
  * **Automated Schema Translation with AWS SCT:** Utilized the AWS Schema Conversion Tool to analyze source database structures, automatically transforming DDL scripts, constraints, sequences, and indexes into Amazon RDS MySQL specifications.
  * **Core Components of AWS Database Migration Service:**
    * *DMS Replication Instance:* Deployed a dedicated `dms.t3.medium` replication instance to manage transactional memory buffers and apply schema transformations.
    * *Source & Target Endpoints:* Configured secure credentials and verified database connectivity with end-to-end connection tests.
    * *DMS Migration Task:* Configured a task combining initial Full Load with continuous Change Data Capture (CDC) utilizing MySQL binary logging (`binlog`).
  * **Zero-Downtime Cutover Mechanics:** Monitored the initial full copy reaching 100% completion while continuous write mutations (inserts/updates/deletes) streamed real-time. Verified that replica lag remained under 1 second before promoting the Amazon RDS instance to production primary.
* **Encountered Challenges & Solutions:**
  * *CDC Failing to Capture Live Transactions:* The DMS task threw an error stating `Binary logging not enabled on source database`. Solution: Updated the source MySQL `my.cnf` configuration with mandatory binary log directives (`log-bin=mysql-bin`, `binlog_format=ROW`, `binlog_row_image=FULL`) and restarted the service.

---

#### 📌 Thursday (11/12/2026) - Enterprise Networking with AWS Transit Gateway & DataSync

* **What did we learn today?**
  * **Hub-and-Spoke Topology via AWS Transit Gateway:** Solved the combinatorial complexity of full-mesh VPC Peering ($N(N-1)/2$ connection pairs) by establishing a central cloud router. Each VPC connects to Transit Gateway through a single elastic network attachment.
  * **Segmented Traffic Routing via Dedicated Route Tables:**
    * Created `Prod-Route-Table` within TGW routing production traffic exclusively to the Shared Services VPC and explicitly dropping routes to development networks.
    * Created `Dev-Route-Table` restricting development network packets within their isolated perimeter.
  * **High-Throughput File Migration with AWS DataSync:** Deployed a local DataSync agent reading directly from on-premises NFS/SMB shares. Achieved accelerated, encrypted parallel transfers into S3 buckets with automatic SHA256 integrity checksum validations.
* **Encountered Challenges & Solutions:**
  * *Asymmetric Routing Packet Drops:* Connected VPCs were unable to ping one another across the Transit Gateway. Root cause: While routes were declared within the TGW route tables, the VPC subnet route tables lacked a static route sending destination CIDRs to the `tgw-xxxx` target. Solution: Updated local subnet route tables on both VPCs to route target ranges to the Transit Gateway.

---

#### 📌 Friday (11/13/2026) - Week 9 Review, Worklog Finalization & Migration Runbook Engineering

* **What did we learn today?**
  * **Enterprise Migration Lifecycle Synthesis:** Seamlessly unified server rehosting (AWS MGN), zero-downtime relational data migration (AWS DMS), centralized hub-and-spoke networking (Transit Gateway), and bulk file synchronization (DataSync).
  * **Disciplined Decommissioning Protocol:** Decommissioned DMS replication instances, removed cutover test nodes, detached VPC attachments, and deleted Transit Gateway resources to prevent idle hourly billing.
  * **Production Cutover Runbook for the Capstone Project:** Authored an exhaustive minute-by-minute migration runbook detailing database schema extraction, continuous replication steps, rollback procedures, and DNS switchovers for the graduation project.

