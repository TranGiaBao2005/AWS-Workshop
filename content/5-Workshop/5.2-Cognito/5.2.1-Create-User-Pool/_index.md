---
title : "Create User Pool & SPA Application"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.2.1. </b> "
---

#### Bước 1: Chọn Loại Ứng dụng SPA & Định danh Đăng nhập Email (Hình 1)

1. Mở **Amazon Cognito Console** tại vùng **Asia Pacific (Singapore) ap-southeast-1** → chọn **User pools** → bấm **Create user pool**.
2. Tại khung **Define your application**:
   - **Application type:** Chọn **Single-page application (SPA)** *(tự động tắt Client Secret và áp dụng luồng OAuth 2.0 PKCE cho ứng dụng chạy trên trình duyệt)*.
   - **Name your application:** Điền **exammaker-dev-spa**.
3. Tại khung **Configure options**:
   - **Options for sign-in identifiers:** Tích chọn **Email** (đăng nhập bằng địa chỉ email không phân biệt chữ hoa/thường).

![Hình 1 — Chọn Single-page application (SPA), đặt tên exammaker-dev-spa và chọn đăng nhập bằng Email](/images/5-Workshop/5.2-Cognito/1.png)

---

#### Bước 2: Tắt Tự đăng ký (Self-registration) & Khai báo Return URL (Hình 1.2)

1. Kéo xuống mục **Self-registration**:
   - **Bỏ tích (Uncheck)** ô **Enable self-registration** (AllowAdminCreateUserOnly = true — chỉ cho phép Admin trường học cấp tài khoản cho giáo viên, chống đăng ký tự do làm tiêu hao hạn ngạch gọi AI).
2. Tại mục **Required attributes for sign-up**:
   - Chọn thuộc tính bắt buộc **email**.
3. Tại mục **Add a return URL**:
   - **Return URL:** Điền **http://localhost:3000/auth/callback/** (có dấu / ở cuối để khớp cấu hình 	railingSlash: true của Next.js static export).
4. Bấm **Create user directory** để hoàn tất tạo User Pool **exammaker-dev-users**.

![Hình 1.2 — Bỏ tích Enable self-registration, chọn thuộc tính email và điền Return URL](/images/5-Workshop/5.2-Cognito/1.2.png)