---
title : "Kiểm tra Kết quả 2 Hàng đợi SQS"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

#### Xác nhận danh sách `Queues (2)` sẵn sàng tiếp nhận AI Jobs

Kiểm tra màn hình tổng quan **Amazon SQS → Queues** xác nhận đã có đủ **2 hàng đợi** (`exammaker-dev-ai-jobs` và `exammaker-dev-ai-jobs-dlq`) ở trạng thái sạch (`Messages available = 0`, `Messages in flight = 0`):

![Xác nhận danh sách 2 hàng đợi SQS sẵn sàng](/images/5-Workshop/5.4-SQS-And-DLQ/10.png)
