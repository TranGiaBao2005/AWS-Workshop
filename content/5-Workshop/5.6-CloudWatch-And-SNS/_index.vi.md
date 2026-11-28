---
title : "Thiết lập Giám sát CloudWatch & SNS"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

Trong phần này, chúng ta thiết lập hệ thống giám sát và cảnh báo chủ động với chi phí **$0/tháng** (nằm trọn trong hạn mức AWS Free Tier): gồm SNS Topic `exammaker-dev-alerts`, CloudWatch Log Group `/exammaker/dev/app` lưu 7 ngày kèm 4 Metric Filters, và đúng **10/10 Standard CloudWatch Alarms**.

#### Nội dung thực hiện

1. [5.6.1. Tạo SNS Topic & Email Subscription (Hình 13 & 13.2)](5.6.1-SNS-Topic-Subscription/)
2. [5.6.2. Tạo Log Group 7 Ngày & 4 Metric Filters (Hình 14 & 14.2)](5.6.2-Log-Group-Metric-Filters/)
3. [5.6.3. Thiết lập & Kiểm tra 10 CloudWatch Alarms (Hình 15)](5.6.3-CloudWatch-10-Alarms/)
