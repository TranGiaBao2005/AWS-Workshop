---
title : "Amazon RDS PostgreSQL 16 Setup"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

In this section, we deploy an **Amazon RDS PostgreSQL 16.13-R2** database (`exammaker-dev-pg`) isolated inside **2 Private Subnets** (`aem-private-a` and `aem-private-b`) of `aem-demo-vpc`, using the ARM64 Graviton `db.t4g.micro` instance class, `20 GiB gp3` storage, `aws/rds` encryption ($0), and 3-day automated backups.

#### Section Contents

1. [5.3.1. Create DB Subnet Group (Figures 4 & 4.2)](5.3.1-DB-Subnet-Group/)
2. [5.3.2. Select PostgreSQL 16 Engine, Single-AZ & Credentials (Figures 5, 5.2 & 5.4)](5.3.2-Engine-And-Credentials/)
3. [5.3.3. Configure db.t4g.micro, gp3 20 GiB & Private Network (Figures 6 & 6.2)](5.3.3-Instance-Storage-Network/)
4. [5.3.4. Configure Database exammaker, Encryption & Backup (Figure 7)](5.3.4-Database-Encryption-Backup/)
