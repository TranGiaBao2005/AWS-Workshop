---
title : "Cấu hình 4 Ngưỡng Cảnh báo Ngân sách"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.7.2. </b> "
---

#### Thiết lập & Xác nhận 4 Ngưỡng Cảnh báo (`Alert thresholds`)

Gắn **4 ngưỡng cảnh báo tự động gửi email** cho đội vận hành để phát hiện sớm mọi dấu hiệu tăng chi phí bất thường:

1. **Actual cost > `50%`** (`$100.00`) — trạng thái `Not exceeded`
2. **Actual cost > `80%`** (`$160.00`) — trạng thái `Not exceeded`
3. **Actual cost > `100%`** (`$200.00`) — trạng thái `Not exceeded`
4. **Forecasted cost > `80%`** (`$160.00`) — trạng thái `Not exceeded`

![Xác nhận 4 ngưỡng cảnh báo trên exammaker-200usd-budget ở trạng thái Not exceeded](/images/5-Workshop/5.7-AWS-Budgets/17.png)
