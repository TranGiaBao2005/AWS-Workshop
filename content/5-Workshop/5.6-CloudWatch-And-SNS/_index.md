---
title : "CloudWatch & SNS Monitoring Setup"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

Trong phần này, chúng ta thiết lập kênh cảnh báo qua email **Amazon SNS** (exammaker-dev-alerts), nhóm nhật ký ứng dụng **CloudWatch Log Group** (/exammaker/dev/app lưu trữ 7 ngày), **4 Metric Filters** và **10 CloudWatch Alarms** nằm trọn trong hạn mức Free Tier ().

#### Nội dung thực hiện

1. [5.6.1. Tạo SNS Topic & Đăng ký Email Nhận Cảnh báo (Hình 13 & 13.2)](5.6.1-SNS-Topic-Subscription/)
2. [5.6.2. Tạo CloudWatch Log Group 7 Ngày & Metric Filters (Hình 14 & 14.2)](5.6.2-Log-Group-Metric-Filters/)
3. [5.6.3. Thiết lập & Kiểm tra 10 CloudWatch Alarms Free Tier (Hình 15)](5.6.3-CloudWatch-10-Alarms/)