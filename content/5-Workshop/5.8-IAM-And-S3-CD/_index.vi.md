---
title : "Thiết lập IAM Roles & S3 Artifact Bucket"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

Trong phần này, chúng ta thiết lập nền tảng bảo mật không dùng cổng SSH (port 22) và không dùng Access Key dài hạn cho vận hành & CI/CD: gồm **3 IAM Roles** (`aem-*`) theo chuẩn **Least Privilege / GitHub OIDC** và **S3 Artifact Bucket riêng tư** (`aem-dev-backend-artifacts-9d07a0f131`) kèm Lifecycle 30 ngày.

#### Nội dung thực hiện

1. [5.8.1. Thiết lập 3 IAM Roles & Permissions Policies (Hình 18)](5.8.1-IAM-Roles-Policies/)
2. [5.8.2. Khởi tạo S3 Artifact Bucket Riêng tư & Lifecycle 30 Ngày (Hình 19 & 19.2)](5.8.2-S3-Artifact-Bucket/)
