---
title : "Thiết lập Amazon RDS PostgreSQL 16"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

Trong phần này, chúng ta thiết lập cơ sở dữ liệu quan hệ **Amazon RDS PostgreSQL 16.13** (exammaker-dev-pg) sử dụng dòng máy chủ ARM64 Graviton **db.t4g.micro**, triển khai **Single-AZ** bên trong **Private Subnets** (em-private-a, em-private-b), ổ cứng **gp3 20 GiB** mã hóa KMS và tự động sao lưu 3 ngày.

#### Nội dung thực hiện

1. [5.3.1. Khởi tạo DB Subnet Group trên 2 Private Subnets (Hình 4 & 4.2)](5.3.1-DB-Subnet-Group/)
2. [5.3.2. Chọn Engine PostgreSQL 16.13-R2, Single-AZ & Tài khoản Quản trị (Hình 5, 5.2 & 5.4)](5.3.2-Engine-And-Credentials/)
3. [5.3.3. Cấu hình Instance db.t4g.micro, Storage gp3 20 GiB & Mạng Private VPC (Hình 6 & 6.2)](5.3.3-Instance-Storage-Network/)
4. [5.3.4. Cấu hình Database exammaker, Mã hóa KMS & Automated Backup 3 Ngày (Hình 7)](5.3.4-Database-Encryption-Backup/)