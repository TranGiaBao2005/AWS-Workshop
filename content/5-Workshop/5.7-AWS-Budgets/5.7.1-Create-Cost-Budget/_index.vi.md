---
title : "Khởi tạo Cost Budget $200.00/Quý"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.7.1. </b> "
---

#### Bước 1: Chọn loại ngân sách Cost Budget nâng cao

1. Mở **AWS Billing and Cost Management → Budgets → Create budget**.
2. Chọn `Customize (advanced)` → `Cost budget - Recommended`.

![Chọn Customize advanced và Cost budget](/images/5-Workshop/5.7-AWS-Budgets/16.png)

#### Bước 2: Thiết lập tên ngân sách & Định mức $200.00/Quý

* *Budget name:* `exammaker-200usd-budget`
* *Period:* `Quarterly` (Theo quý)
* *Budget renewal type:* `Recurring budget`
* *Budgeting method:* `Fixed`
* *Budgeted amount:* `$200.00`

![Thiết lập tên exammaker-200usd-budget và định mức $200.00/Quý](/images/5-Workshop/5.7-AWS-Budgets/16.2.png)

#### Bước 3: Phạm vi toàn bộ dịch vụ & Tổng hợp theo `Unblended costs`

* *Budget scope:* `All AWS services (Recommended)`
* *Aggregate costs by:* `Unblended costs` (đo lường trực tiếp trên chi phí gốc phát sinh trước khi trừ AWS Credit để theo dõi chính xác tốc độ tiêu thụ thực tế).

![Chọn phạm vi All AWS services và Unblended costs](/images/5-Workshop/5.7-AWS-Budgets/16.3.png)
