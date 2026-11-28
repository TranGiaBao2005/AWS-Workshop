---
title : "Configure Managed Login, PKCE & Scopes"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2.2. </b> "
---

#### Bước 1: Cấu hình Callback URLs, Sign-out URLs & Identity Provider (Hình 2)

1. Mở User Pool **exammaker-dev-users** → menu trái chọn **Applications** → **App clients** → bấm vào **exammaker-dev-spa**.
2. Chuyển sang tab **Login pages** → bấm **Edit**.
3. Tại khung **Managed login pages**:
   - **Allowed callback URLs:** Khai báo http://localhost:3000/auth/callback/ (môi trường dev) và https://app.khaothiai.xyz/auth/callback/ (môi trường production).
   - **Allowed sign-out URLs:** Khai báo http://localhost:3000/ và https://app.khaothiai.xyz/.
   - **Identity providers:** Chọn **Cognito user pool**.

![Hình 2 — Cấu hình Allowed callback URLs, Allowed sign-out URLs và Identity provider trên App Client](/images/5-Workshop/5.2-Cognito/2.png)

---

#### Bước 2: Cấu hình OAuth 2.0 Authorization Code Grant & OpenID Connect Scopes (Hình 2.2)

1. Kéo xuống mục **OAuth 2.0 grant types**:
   - Chỉ chọn **Authorization code grant** (luồng code kết hợp PKCE, tuyệt đối không bật Implicit grant).
2. Tại mục **OpenID Connect scopes**:
   - Chọn đủ 3 scopes chuẩn: **Email**, **OpenID**, **Profile**.
3. Bấm **Save changes**.

![Hình 2.2 — Chọn Authorization code grant và 3 OpenID Connect scopes (Email, OpenID, Profile)](/images/5-Workshop/5.2-Cognito/2.2.png)