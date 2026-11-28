---
title : "Tạo SNS Topic & Email Subscription"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.6.1. </b> "
---

#### Bước 1: Tạo SNS Topic `exammaker-dev-alerts`

1. Mở **Amazon SNS** tại region `ap-southeast-1` → chọn **Topics → Create topic**.
2. Cấu hình:
  * *Type:* `Standard`
  * *Name:* `exammaker-dev-alerts`
  * *Display name:* `ExamMakerAlert` (Max message size: `256` KiB)
3. Bấm **Create topic**.

![Tạo Amazon SNS Topic exammaker-dev-alerts](/images/5-Workshop/5.6-CloudWatch-And-SNS/13.png)

#### Bước 2: Đăng ký Email Subscription cho đội kỹ thuật

1. Trong trang chi tiết topic `exammaker-dev-alerts`, chọn **Create subscription**.
2. Chọn **Protocol:** `Email` và nhập địa chỉ email của các thành viên đội vận hành (**4 email subscribers**).
3. Xác nhận link **Confirm subscription** trong hộp thư đến để chuyển trạng thái sang `Confirmed`.

![Đăng ký Email Subscription cho SNS Topic](/images/5-Workshop/5.6-CloudWatch-And-SNS/13.2.png)
