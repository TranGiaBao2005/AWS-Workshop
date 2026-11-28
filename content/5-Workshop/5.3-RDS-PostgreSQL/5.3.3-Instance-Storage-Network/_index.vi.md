---
title : "Cấu hình db.t4g.micro, gp3 20 GiB & Mạng Private"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3.3. </b> "
---

#### Bước 1: Chọn Instance Class db.t4g.micro & Ổ cứng gp3 20 GiB (Hình 6)

1. Tại mục **Instance configuration**:
   - **DB instance class:** Tích chọn **Burstable classes (includes t classes)**.
   - **Instance type:** Chọn **db.t4g.micro** (2 vCPUs, 1 GiB RAM — vi xử lý ARM64 Graviton).
2. Tại mục **Storage**:
   - **Storage type:** Chọn **General Purpose SSD (gp3)**.
   - **Allocated storage:** Điền **20** GiB.
   - Mở mục **Additional storage configuration** → tích chọn **Enable storage autoscaling** (giới hạn trần Maximum storage threshold = **40** GiB).

![Hình 6 — Chọn Burstable classes (db.t4g.micro), ổ cứng gp3 20 GiB và bật Enable storage autoscaling](/images/5-Workshop/5.3-RDS-PostgreSQL/6.png)

---

#### Bước 2: Cấu hình Kết nối VPC, Private Subnet Group & Security Group em-rds-sg (Hình 6.2)

Tại mục **Connectivity**:
- **Compute resource:** Chọn **Don't connect to an EC2 compute resource**.
- **Virtual private cloud (VPC):** Chọn **em-demo-vpc**.
- **DB subnet group:** Chọn **exammaker-dev-db-subnets**.
- **Public access:** Tích chọn **No** (PubliclyAccessible = false — cô lập hoàn toàn Database trong Private Subnets).
- **VPC security group (firewall):** Chọn **Choose existing** → chọn **em-rds-sg** (chỉ nhận kết nối TCP 5432 từ Security Group em-ec2-sg).

![Hình 6.2 — Cấu hình VPC aem-demo-vpc, DB subnet group exammaker-dev-db-subnets, Public access = No và Security Group aem-rds-sg](/images/5-Workshop/5.3-RDS-PostgreSQL/6.2.png)