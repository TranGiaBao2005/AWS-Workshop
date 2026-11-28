---
title : "Thiết lập IAM Roles & S3 Artifact Bucket"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

Trong phần này, chúng ta thiết lập **3 IAM Roles cốt lõi (em-*)** tuân thủ nguyên tắc quyền tối thiểu (Least Privilege, không dùng AWS access key dài hạn) và khởi tạo **S3 Artifact Bucket riêng tư** (em-dev-backend-artifacts-9d07a0f131) phục vụ pipeline CI/CD Backend.

#### Nội dung thực hiện

1. [5.8.1. Thiết lập 3 IAM Roles (em-*) & Chi tiết Permissions Policies (Hình 18)](5.8.1-IAM-Roles-Policies/)
2. [5.8.2. Khởi tạo S3 Artifact Bucket Riêng tư cho Backend CI/CD (Hình 19 & 19.2)](5.8.2-S3-Artifact-Bucket/)