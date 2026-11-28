---
title : "Thiết lập Hàng đợi Amazon SQS & DLQ"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

Trong phần này, chúng ta thiết lập kiến trúc xử lý bất đồng bộ bằng **Amazon SQS** cho các tác vụ sinh câu hỏi và thẩm định đáp án bằng AI (kéo dài 15–45 giây), bao gồm hàng đợi thư chết **Dead-Letter Queue** (`exammaker-dev-ai-jobs-dlq`) và hàng đợi chính (`exammaker-dev-ai-jobs`) với **Visibility timeout 300 giây**, **Long Polling 20 giây** và **Redrive Policy (`maxReceiveCount = 3`)**.

#### Nội dung thực hiện

1. [5.4.1. Khởi tạo Hàng đợi Thư chết — DLQ (Hình 8)](5.4.1-Create-DLQ/)
2. [5.4.2. Khởi tạo Hàng đợi Chính — Main Queue (Hình 9)](5.4.2-Create-Main-Queue/)
3. [5.4.3. Kiểm tra Kết quả 2 Hàng đợi SQS (Hình 10)](5.4.3-Verify-Queues/)
