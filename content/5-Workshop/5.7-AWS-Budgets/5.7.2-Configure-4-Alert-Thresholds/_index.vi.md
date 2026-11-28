---
title : "Cấu hình 4 Ngưỡng Cảnh báo Ngân sách"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.7.2. </b> "
---

#### Bước 1: Kiểm tra 4 Ngưỡng Cảnh báo Ngân sách (50%, 80%, 100% Actual & 80% Forecasted) (Hình 17)

Tại **Step 3 (Configure alerts)**, thiết lập **4 ngưỡng cảnh báo tự động gửi email** tới đội kỹ thuật và kiểm tra tại màn hình **Budget details**:
1. **Actual cost > 50%** ($100.00 trên $200.00) — Trạng thái: **Not exceeded**.
2. **Actual cost > 80%** ($160.00 trên $200.00) — Trạng thái: **Not exceeded**.
3. **Actual cost > 100%** ($200.00 trên $200.00) — Trạng thái: **Not exceeded**.
4. **Forecasted cost > 80%** ($160.00 dự phóng trên $200.00) — Trạng thái: **Not exceeded**.

![Hình 17 — Cả 4 ngưỡng cảnh báo trên ngân sách exammaker-200usd-budget đều hoạt động ở trạng thái Not exceeded](/images/5-Workshop/5.7-AWS-Budgets/17.png)