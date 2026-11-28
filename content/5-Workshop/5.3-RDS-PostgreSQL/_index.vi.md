---
title : "Thiết lập Amazon RDS PostgreSQL 16"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

Trong phần này, chúng ta triển khai cơ sở dữ liệu **Amazon RDS PostgreSQL 16.13-R2** (`exammaker-dev-pg`) nằm hoàn toàn trong **2 Private Subnets** (`aem-private-a` và `aem-private-b`) thuộc VPC `aem-demo-vpc`, sử dụng dòng chip ARM64 Graviton `db.t4g.micro`, ổ đĩa `gp3` 20 GiB, mã hóa `aws/rds` ($0) và sao lưu tự động 3 ngày.

#### Nội dung thực hiện

1. [5.3.1. Khởi tạo DB Subnet Group (Hình 4 & 4.2)](5.3.1-DB-Subnet-Group/)
2. [5.3.2. Chọn Engine PostgreSQL 16, Single-AZ & Tài khoản (Hình 5, 5.2 & 5.4)](5.3.2-Engine-And-Credentials/)
3. [5.3.3. Cấu hình db.t4g.micro, gp3 20 GiB & Mạng Private (Hình 6 & 6.2)](5.3.3-Instance-Storage-Network/)
4. [5.3.4. Cấu hình Database exammaker, Mã hóa & Backup (Hình 7)](5.3.4-Database-Encryption-Backup/)
