---
title : "Cấu hình db.t4g.micro, gp3 20 GiB & Mạng Private"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3.3. </b> "
---

#### Bước 1: Chọn cấu hình máy chủ `db.t4g.micro` & Ổ cứng `gp3`

1. **DB instance class:** chọn `Burstable classes (includes t classes)` → `db.t4g.micro` (**2 vCPUs, 1 GiB RAM**, EBS Bandwidth lên đến **2,085 Mbps**, Network lên đến **5 Gbps**, chi phí chỉ ~$0.020/giờ).
2. **Storage type & Capacity:** `General Purpose SSD (gp3)`, **Allocated storage = `20` GiB** (Baseline **3,000 IOPS**, **125 MiBps**).
3. **Storage autoscaling:** `Enabled`, khóa trần **Maximum storage threshold = `40` GiB** để phòng tránh phình dung lượng ngoài kiểm soát.

![Cấu hình instance db.t4g.micro và ổ cứng gp3 20 GiB](/images/5-Workshop/5.3-RDS-PostgreSQL/6.png)

#### Bước 2: Thiết lập kết nối Private & Security Group

* *VPC:* `aem-demo-vpc`
* *DB subnet group:* `exammaker-dev-db-subnets`
* *Public access:* `No` (tuyệt đối không gán Public IP cho cơ sở dữ liệu).
* *VPC security group:* chọn `aem-rds-sg` (chỉ mở duy nhất cổng TCP `5432` cho Security Group của máy chủ EC2 backend).

![Cấu hình mạng Private, Public access No và Security Group aem-rds-sg](/images/5-Workshop/5.3-RDS-PostgreSQL/6.2.png)
