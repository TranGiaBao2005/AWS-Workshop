---
title : "Thiết lập Amazon Cognito"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

Trong phần này, chúng ta thiết lập dịch vụ định danh **Amazon Cognito User Pool** (`exammaker-dev-users`) ở phân tầng **Essentials** (miễn phí ≤ 10.000 MAU), cấu hình ứng dụng trình duyệt **Single-page application (SPA)** (`exammaker-dev-spa`) sử dụng luồng OAuth 2.0 Authorization Code + PKCE và khởi tạo 3 nhóm phân quyền RBAC (`admin`, `head`, `teacher`).

#### Nội dung thực hiện

1. [5.2.1. Khởi tạo User Pool & Ứng dụng SPA (Hình 1 & 1.2)](5.2.1-Create-User-Pool/)
2. [5.2.2. Cấu hình Managed Login, PKCE & OIDC Scopes (Hình 2 & 2.2)](5.2.2-App-Client-PKCE/)
3. [5.2.3. Khởi tạo & Kiểm tra 3 Nhóm Phân quyền Người dùng (Hình 3 & 3.2)](5.2.3-User-Groups/)
