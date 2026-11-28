---
title : "Create .00 Quarterly Cost Budget"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.7.1. </b> "
---

#### Bước 1: Chọn Loại Ngân sách Tùy chỉnh (Customize (advanced) & Cost budget) (Hình 16)

1. Mở **Billing and Cost Management Console** → menu trái chọn **Budgets** → bấm **Create budget**.
2. Tại **Step 1 (Choose budget type)**:
   - **Budget setup:** Tích chọn **Customize (advanced)**.
   - **Budget types:** Tích chọn **Cost budget - Recommended** → bấm **Next**.

![Hình 16 — Chọn Customize (advanced) và Cost budget - Recommended tại Step 1](/images/5-Workshop/5.7-AWS-Budgets/16.png)

---

#### Bước 2: Thiết lập Tên Ngân sách exammaker-200usd-budget & Định mức $200.00/Quý (Hình 16.2)

Tại **Step 2 (Set your budget)**:
- **Budget name:** Điền **exammaker-200usd-budget**.
- **Period:** Chọn **Quarterly** (Theo quý).
- **Budget renewal type:** Tích chọn **Recurring budget**.
- **Budgeting method:** Chọn **Fixed**.
- **Enter your budgeted amount ($):** Điền **200.00**.

![Hình 16.2 — Đặt tên exammaker-200usd-budget, chu kỳ Quarterly, Recurring budget, Fixed và số tiền .00](/images/5-Workshop/5.7-AWS-Budgets/16.2.png)

---

#### Bước 3: Chọn Phạm vi All AWS services & Phương thức Tính Unblended costs (Hình 16.3)

Kéo xuống mục **Budget scope** ở cuối Step 2:
- **Scope options:** Tích chọn **All AWS services (Recommended)**.
- **Advanced options → Aggregate costs by:** Giữ **Unblended costs** (đo lường tổng chi phí thực tế phát sinh trước khi áp dụng credit khuyến mãi để cảnh báo chính xác mức tiêu thụ tài nguyên) → bấm **Next**.

![Hình 16.3 — Chọn All AWS services (Recommended) và Aggregate costs by Unblended costs](/images/5-Workshop/5.7-AWS-Budgets/16.3.png)