---
title : "Khởi tạo 3 Nhóm Phân quyền Người dùng"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.2.3. </b> "
---

#### Bước 1: Tạo Nhóm Phân quyền trên Form Create group (Hình 3)

1. Trong User Pool **exammaker-dev-users** → menu trái chọn **User management** → **Groups** → bấm **Create group**.
2. Tại màn hình **Create group**, điền thông tin cho nhóm quản trị viên:
   - **Group name:** Điền **dmin** *(chữ thường 100% để khớp enum Role trong OpenAPI contract)*.
   - **Description - optional:** Điền **System administrators (publish, user/catalog management, fallback review)**.
   - **Precedence - optional:** Điền **1** (mức độ ưu tiên cao nhất).
   - **IAM permissions:** Để trống *(Backend .NET đọc trực tiếp claim cognito:groups trong JWT token để phân quyền RBAC)*.
3. Bấm **Create group**.

![Hình 3 — Điền thông số tạo nhóm quyền admin với Precedence = 1 trên màn hình Create group](/images/5-Workshop/5.2-Cognito/3.png)

---

#### Bước 2: Kiểm tra Kết quả 3 Nhóm Phân quyền (dmin, head, 	eacher) (Hình 3.2)

Thực hiện tương tự cho 2 nhóm còn lại (head và 	eacher). Tại màn hình **Groups (3)**, xác nhận đủ 3 nhóm quyền với thứ tự ưu tiên chuẩn:
- **dmin** — Precedence: **1** — System administrators (publish, user/catalog management, fallback review)
- **head** — Precedence: **2** — Department heads (teacher permissions plus department review)
- **	eacher** — Precedence: **3** — Teachers (generate AI questions, manage own questions and exams)

![Hình 3.2 — Bảng kết quả 3 nhóm quyền admin, head, teacher đã được khởi tạo](/images/5-Workshop/5.2-Cognito/3.2.png)