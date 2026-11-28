---
title : "Thiết lập Hàng đợi Amazon SQS & DLQ"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

Trong phần này, chúng ta thiết lập cặp hàng đợi **Amazon SQS** gồm **Dead-Letter Queue (exammaker-dev-ai-jobs-dlq)** và **Main Queue (exammaker-dev-ai-jobs)** với cơ chế Long Polling 20 giây, Visibility Timeout 300 giây và Redrive Policy tự động cách ly message lỗi sau 3 lần thử lại thất bại.

#### Nội dung thực hiện

1. [5.4.1. Khởi tạo Hàng đợi Thư chết Dead-Letter Queue (Hình 8)](5.4.1-Create-DLQ/)
2. [5.4.2. Khởi tạo Hàng đợi Chính Main Queue & Gắn Redrive Policy (Hình 9)](5.4.2-Create-Main-Queue/)
3. [5.4.3. Kiểm tra Kết quả 2 Hàng đợi SQS Đã Khởi tạo (Hình 10)](5.4.3-Verify-Queues/)