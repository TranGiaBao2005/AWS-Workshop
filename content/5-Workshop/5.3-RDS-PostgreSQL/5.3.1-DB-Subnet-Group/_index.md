---
title : "Create DB Subnet Group"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

#### Bước 1: Khai báo Tên DB Subnet Group, VPC & 2 Availability Zones (Hình 4)

1. Mở **Aurora and RDS Console** tại vùng **p-southeast-1 (Singapore)** → menu trái chọn **Subnet groups** → bấm **Create DB subnet group**.
2. Tại khung **Subnet group details**:
   - **Name:** Điền **exammaker-dev-db-subnets**.
   - **Description:** Điền **Private DB subnet group for AI Exam Maker (dev)**.
   - **VPC:** Chọn **em-demo-vpc**.
3. Tại khung **Add subnets**:
   - **Availability Zones:** Chọn 2 AZ là **p-southeast-1b** và **p-southeast-1c**.

![Hình 4 — Điền tên exammaker-dev-db-subnets, chọn VPC aem-demo-vpc và 2 Availability Zones ap-southeast-1b, ap-southeast-1c](/images/5-Workshop/5.3-RDS-PostgreSQL/4.png)

---

#### Bước 2: Chọn 2 Private Subnets (em-private-a, em-private-b) & Bấm Create (Hình 4.2)

1. Tại mục **Subnets**, chọn 2 Private Subnets của dự án:
   - **em-private-a** (CIDR: 10.20.11.0/24 tại p-southeast-1b)
   - **em-private-b** (CIDR: 10.20.12.0/24 tại p-southeast-1c)
2. Kiểm tra danh sách tại bảng **Subnets selected (2)** và bấm **Create**.

![Hình 4.2 — Chọn 2 Private Subnets aem-private-a, aem-private-b và bấm Create](/images/5-Workshop/5.3-RDS-PostgreSQL/4.2.png)