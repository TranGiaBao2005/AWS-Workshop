---
title : "Tạo Log Group 7 Ngày & Metric Filters"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.6.2. </b> "
---

#### Bước 1: Khởi tạo CloudWatch Log Group /exammaker/dev/app Lưu trữ 7 Ngày (Hình 14)

1. Mở **Amazon CloudWatch Console** (p-southeast-1) → menu trái chọn **Logs** → **Log Management** → bấm **Create log group**.
2. Tại mục **Log group details**:
   - **Log group name:** Điền **/exammaker/dev/app**.
   - **Retention setting:** Chọn **1 week (7 days)** (xoay vòng log tự động sau 7 ngày để không vượt 5 GB Free Tier).
   - **Log class:** Chọn **Standard**.
3. Bấm **Create**.

![Hình 14 — Tạo CloudWatch Log Group /exammaker/dev/app với Retention 1 week (7 days) và Log class Standard](/images/5-Workshop/5.6-CloudWatch-And-SNS/14.png)

---

#### Bước 2: Khởi tạo Metric Filter Đẩy Chỉ số vào Namespace ExamMaker/Dev (Hình 14.2)

1. Bấm vào log group **/exammaker/dev/app** → chọn tab **Metric filters** → bấm **Create metric filter**.
2. Sau khi nhập Filter pattern ở Bước 1, tại **Step 2 (Assign metric)** điền thông số tại khung **Metric details**:
   - **Metric namespace:** Điền **ExamMaker/Dev**.
   - **Metric name:** Điền **Api5xxCount** *(tương tự cho 3 bộ lọc còn lại: WorkerHeartbeat, StuckRunningJobs, WorkerErrorCount)*.
   - **Metric value:** Điền **1**.
   - **Unit - optional:** Chọn **Count**.
3. Bấm **Next** → **Create metric filter**.

![Hình 14.2 — Cấu hình Metric details đẩy chỉ số Api5xxCount (Value = 1, Unit = Count) vào namespace ExamMaker/Dev](/images/5-Workshop/5.6-CloudWatch-And-SNS/14.2.png)