---
title : "Configure & Verify 10 CloudWatch Alarms"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.6.3. </b> "
---

#### Bước 1: Kiểm tra Toàn bộ 10/10 CloudWatch Alarms ở Trạng thái OK (Hình 15)

Trong **CloudWatch → Alarms**, hệ thống thiết lập đúng **10 Standard Alarms** (chu kỳ đánh giá Period = 300s = 5 phút, gửi cảnh báo qua SNS Topic exammaker-dev-alerts), tận dụng tối đa **10/10 Alarms miễn phí của AWS Free Tier**:

1. **exammaker-dev-worker-heartbeat**: Giám sát nhịp đập của Background Worker (WorkerHeartbeat < 1 trong 5 phút).
2. **exammaker-dev-worker-errors**: Cảnh báo khi Worker gặp lỗi (WorkerErrorCount >= 3 trong 5 phút).
3. **exammaker-dev-api-5xx**: Cảnh báo khi API trả về lỗi HTTP 5xx (Api5xxCount >= 5 trong 5 phút).
4. **exammaker-dev-ebs-stalled-io**: Cảnh báo nghẽn I/O trên ổ EBS gốc của EC2 (VolumeStalledIOCheck > 0).
5. **exammaker-dev-worker-stuck-jobs**: Cảnh báo khi có job AI bị treo quá thời gian lease (StuckRunningJobs > 0).
6. **exammaker-dev-rds-connections-high**: Cảnh báo số kết nối vào RDS vượt ngưỡng (DatabaseConnections > 50).
7. **exammaker-dev-sqs-dlq-depth**: Cảnh báo ngay khi có message lỗi rơi vào DLQ (ApproximateNumberOfMessagesVisible > 0).
8. **exammaker-dev-sqs-oldest-msg**: Cảnh báo khi message chờ trong Main Queue quá 10 phút (ApproximateAgeOfOldestMessage > 600s).
9. **exammaker-dev-ec2-cpu-high**: Cảnh báo CPU của máy chủ EC2 vượt 80% trong 10 phút.
10. **exammaker-dev-rds-storage-low**: Cảnh báo dung lượng trống của RDS còn dưới 2 GB.

![Hình 15 — Bảng điều khiển CloudWatch Alarms (10) hiển thị toàn bộ 10 alarms ở trạng thái xanh OK và Actions enabled](/images/5-Workshop/5.6-CloudWatch-And-SNS/15.png)