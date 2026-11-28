---
title : "Chọn Engine PostgreSQL 16, Single-AZ & Tài khoản"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

#### Bước 1: Chọn phương thức khởi tạo & Template

1. Vào **Aurora and RDS → Databases → Create database**.
2. Chọn:
  * *Database creation method:* `Full configuration`
  * *Engine type:* `PostgreSQL`
  * *Templates:* `Dev/Test`

![Chọn Full configuration, PostgreSQL và Dev/Test template](/images/5-Workshop/5.3-RDS-PostgreSQL/5.png)

#### Bước 2: Chọn chế độ Single-AZ tối ưu chi phí

Tại mục **Availability and durability**, chọn `Single-AZ DB instance deployment (1 instance)` (độ sẵn sàng **99.5% uptime**, `MultiAZ = false`) để tránh nhân đôi chi phí vận hành trong giai đoạn dev/demo.

![Chọn Single-AZ DB instance deployment](/images/5-Workshop/5.3-RDS-PostgreSQL/5.2.png)

#### Bước 3: Chọn phiên bản PostgreSQL 16 & Thông tin quản trị

* *Engine version:* `PostgreSQL 16.13-R2` (Tắt **RDS Extended Support** để không phát sinh phí gia hạn ngầm).
* *DB instance identifier:* `exammaker-dev-pg`
* *Master username:* `exammaker_admin`
* *Credentials management:* `Self managed` (mật khẩu được lưu bảo mật dưới dạng `SecureString` tại SSM Parameter Store).

![Cấu hình PostgreSQL 16.13-R2, exammaker-dev-pg và exammaker_admin](/images/5-Workshop/5.3-RDS-PostgreSQL/5.4.png)
