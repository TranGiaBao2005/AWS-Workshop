---
title : "Khởi tạo S3 Artifact Bucket Riêng tư"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.8.2. </b> "
---

#### Bước 1: Tạo S3 Bucket lưu trữ gói release backend

1. Mở **Amazon S3 → Create bucket**.
2. Cấu hình thông tin định danh:
  * *AWS Region:* `Asia Pacific (Singapore) ap-southeast-1`
  * *Bucket type:* `General purpose` · **Namespace:** `Global namespace`
  * *Bucket name:* `aem-dev-backend-artifacts-9d07a0f131`

![Khởi tạo S3 Bucket aem-dev-backend-artifacts-9d07a0f131 tại ap-southeast-1](/images/5-Workshop/5.8-IAM-And-S3-CD/19.png)

#### Bước 2: Bật Block All Public Access, SSE-S3 & Lifecycle 30 Ngày

* *Object Ownership:* `ACLs disabled (recommended)` (`Bucket owner enforced`).
* *Block Public Access:* bật `Block all public access = Enabled` 100%.
* *Default encryption:* `SSE-S3 (AES-256)` (**$0**).
* *Lifecycle rule:* tự động xóa các gói artifact bản build cũ sau `30 days` để tránh tích lũy dung lượng lưu trữ không cần thiết.

![Cấu hình ACLs disabled, Block all public access và SSE-S3](/images/5-Workshop/5.8-IAM-And-S3-CD/19.2.png)
