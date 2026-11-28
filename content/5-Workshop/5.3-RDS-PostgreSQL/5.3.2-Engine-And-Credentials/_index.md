---
title : "Select PostgreSQL 16 Engine, Single-AZ & Credentials"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

#### Step 1: Choose Creation Method & Template

1. Open **Aurora and RDS → Databases → Create database**.
2. Select:
  * *Database creation method:* `Full configuration`
  * *Engine type:* `PostgreSQL`
  * *Templates:* `Dev/Test`

![Select Full configuration, PostgreSQL, and Dev/Test template](/images/5-Workshop/5.3-RDS-PostgreSQL/5.png)

#### Step 2: Select Single-AZ Deployment for Cost Efficiency

Under **Availability and durability**, select `Single-AZ DB instance deployment (1 instance)` (**99.5% uptime**, `MultiAZ = false`) to avoid doubling hourly compute costs during dev/demo.

![Select Single-AZ DB instance deployment](/images/5-Workshop/5.3-RDS-PostgreSQL/5.2.png)

#### Step 3: Select PostgreSQL 16 Version & Master Credentials

* *Engine version:* `PostgreSQL 16.13-R2` (Disable **RDS Extended Support** to avoid extra extended-support fees).
* *DB instance identifier:* `exammaker-dev-pg`
* *Master username:* `exammaker_admin`
* *Credentials management:* `Self managed` (master password stored securely as a `SecureString` in SSM Parameter Store).

![Configure PostgreSQL 16.13-R2, exammaker-dev-pg, and exammaker_admin](/images/5-Workshop/5.3-RDS-PostgreSQL/5.4.png)
