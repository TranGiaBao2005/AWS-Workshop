---
title: "Worklog Tuần 10"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 10:

- Làm chủ mô hình kiến trúc **Hướng sự kiện (Event-Driven Architecture - EDA)** và các mẫu thiết kế hệ thống phân tán bất đồng bộ trên nền tảng đám mây AWS.
- Xây dựng, quản lý và bảo vệ các điểm cuối API cấp doanh nghiệp với **Amazon API Gateway** (RESTful API, HTTP API, cơ chế ủy quyền Lambda Authorizers, kiểm soát lưu lượng với Throttling & Usage Plans).
- Triển khai giải pháp phân tách hệ thống (Decoupling) và hấp thụ tải đột biến với hàng đợi tin cậy **Amazon Simple Queue Service (Amazon SQS)** (Workshop 000078), so sánh chuyên sâu Standard Queue vs FIFO Queue và cô lập lỗi với Dead-Letter Queue (DLQ).
- Thiết lập mô hình phát hành và đăng ký nhận tin (Pub/Sub) cùng bus điều phối sự kiện đa nguồn với **Amazon SNS** và **Amazon EventBridge**.
- Xây dựng và tự động hóa quy trình nghiệp vụ phân tán, xử lý ngoại lệ và tự động thử lại (Retry/Catch) với **AWS Step Functions (State Machines)**.
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và tích hợp các thành phần hàng đợi xử lý bất đồng bộ vào đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Quản trị & Bảo mật API Gateway cấp doanh nghiệp:** <br>- So sánh chuyên sâu kiến trúc REST API vs HTTP API (tính năng, độ trễ, chi phí). <br>- Cấu hình tài nguyên, phương thức HTTP, CORS và tích hợp trực tiếp Lambda Backend. <br>- Xây dựng Lambda Custom Authorizer xác thực JSON Web Token (JWT). <br>- Thiết lập Usage Plans, API Keys và thuật toán Token Bucket Throttling. | 16/11/2026 | 16/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 3** | **Phân tách hệ thống & Xử lý bất đồng bộ với Amazon SQS:** <br>- Khởi tạo Standard Queue (thông lượng không giới hạn) vs FIFO Queue (bảo toàn thứ tự). <br>- Tối ưu chi phí và độ trễ nhận tin với cơ chế Long Polling (ReceiveMessageWaitTime = 20s). <br>- Cấu hình Visibility Timeout chống hiện tượng xử lý lặp lại bản tin giữa các worker. <br>- Thiết lập Dead-Letter Queue (DLQ) kèm chính sách Redrive Policy cô lập tin nhắn lỗi. | 17/11/2026 | 17/11/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Thứ 4** | **Phát tin & Điều phối sự kiện với Amazon SNS & EventBridge:** <br>- Xây dựng kiến trúc Fanout: Đăng ký nhiều hàng đợi SQS vào một SNS Topic duy nhất. <br>- Thiết lập Amazon EventBridge Default Event Bus và Custom Event Bus. <br>- Viết các bộ lọc mẫu sự kiện (Event Pattern Filtering) định tuyến tin nhắn thông minh theo nội dung. | 18/11/2026 | 18/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 5** | **Điều phối quy trình phân tán với AWS Step Functions:** <br>- Thiết kế trực quan quy trình nghiệp vụ bằng Workflow Studio qua Amazon States Language. <br>- Kết hợp các trạng thái: Task (gọi Lambda/SQS), Choice (rẽ nhánh điều kiện), Parallel, Wait. <br>- Cấu hình chiến lược phục hồi lỗi (Error Handling, Retry với Exponential Backoff). | 19/11/2026 | 19/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 6** | **Tổng kết Tuần 10, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức API Gateway, SQS, SNS, EventBridge và Step Functions. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 10 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp mô hình xử lý bất đồng bộ bằng SQS và Step Functions vào kiến trúc Đề xuất đồ án. | 20/11/2026 | 20/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (16/11/2026) - Quản trị & Bảo mật API Gateway cấp doanh nghiệp

* **Ta học được những gì hôm nay?**
  * **So sánh kiến trúc REST API vs HTTP API:**
    * *HTTP API:* Thế hệ mới tối ưu hóa cho độ trễ cực thấp (giảm tới 60% latency), cấu hình đơn giản hóa và tiết kiệm chi phí hơn 70% so với REST API, hỗ trợ OIDC/OAuth2 native authorizers.
    * *REST API:* Bộ tính năng đầy đủ cho bài toán doanh nghiệp phức tạp (Usage Plans, API Keys, Request/Response Data Mapping Templates, WAF integration, Private API Endpoints trong VPC).
  * **Bảo vệ cổng API với Lambda Custom Authorizer:** Viết một hàm Lambda Authorizer kiểm tra Bearer Token gửi trong Header `Authorization`. Chỉ khi token hợp lệ, Authorizer mới trả về tài liệu IAM Policy cho phép (`Effect: Allow`) tiếp cận endpoint tài nguyên.
  * **Chống quá tải hệ thống với Throttling & Usage Plans:** Áp dụng thuật toán Token Bucket kiểm soát lưu lượng truy cập: Rate Limit = 100 requests/giây và Burst Limit = 200 requests. Khi lưu lượng vượt ngưỡng, API Gateway tự động trả mã lỗi `429 Too Many Requests`, bảo vệ an toàn cho cơ sở dữ liệu backend.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi CORS trên trình duyệt (Cross-Origin Request Blocked):* Ứng dụng Frontend React/Vue gọi API bị chặn lỗi CORS. Nguyên nhân: Thiếu phương thức `OPTIONS` và các header phản hồi cho phép. Cách xử lý: Bật tính năng `Enable CORS` trên API Gateway Console, cấu hình các header phản hồi bắt buộc: `Access-Control-Allow-Origin: '*'`, `Access-Control-Allow-Methods: 'GET,POST,OPTIONS'`, `Access-Control-Allow-Headers: 'Content-Type,Authorization'`.

---

#### 📌 Thứ 3 (17/11/2026) - Phân tách hệ thống & Xử lý bất đồng bộ với Amazon SQS

* **Ta học được những gì hôm nay?**
  * **So sánh hai loại hàng đợi thông điệp:**
    * *Standard Queue:* Cung cấp thông lượng tin nhắn gần như không giới hạn, phân phối tin nhắn theo cơ chế "Ít nhất một lần" (At-least-once delivery), thứ tự thông điệp có thể bị đảo lộn đôi chút khi có tải lớn.
    * *FIFO Queue (First-In-First-Out):* Đảm bảo thứ tự thông điệp nghiêm ngặt chính xác 100%, phân phối chính xác một lần duy nhất (Exactly-once processing) thông qua cơ chế `MessageDeduplicationId` và nhóm xử lý tuần tự `MessageGroupId`.
  * **Tối ưu chi phí với Long Polling:** Thay vì cấu hình Short Polling liên tục gửi request hỏi hàng đợi gây phát sinh hàng triệu API calls vô ích, thiết lập `ReceiveMessageWaitTimeSeconds = 20`. Kết nối sẽ được giữ mở trong 20 giây cho đến khi có tin nhắn mới tới, giúp giảm hơn 80% chi phí gọi API SQS.
  * **Cơ chế Visibility Timeout:** Đặt thời gian ẩn tin nhắn `VisibilityTimeout = 30s`. Khi Worker A nhận tin nhắn để xử lý, tin nhắn này sẽ tạm thời ẩn đi đối với các Worker khác. Nếu Worker A xử lý thành công thì gọi lệnh `delete_message`. Nếu Worker A bị crash, sau 30 giây tin nhắn sẽ tự động hiển thị lại để Worker B nhận và xử lý, đảm bảo không bao giờ mất dữ liệu.
  * **Cô lập lỗi với Dead-Letter Queue (DLQ):** Tạo hàng đợi `orders-dlq`. Cấu hình Redrive Policy trên hàng đợi chính `orders-queue` với tham số `maxReceiveCount = 3`. Nếu một tin nhắn độc hại hoặc payload hỏng bị xử lý lỗi quá 3 lần, SQS tự động chuyển bản tin sang DLQ để các kỹ sư phân tích mà không làm nghẽn luồng xử lý của hệ thống.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi trùng lặp dữ liệu trên Worker:* Khi thời gian xử lý tác vụ của Worker kéo dài hơn Visibility Timeout (ví dụ xử lý mất 45s trong khi timeout là 30s), SQS tưởng Worker đã chết nên nhả tin nhắn cho Worker khác xử lý lại, dẫn đến tình trạng ghi đúp 2 lần vào CSDL. Cách xử lý: Viết mã Worker định kỳ gọi API `change_message_visibility` gia hạn thêm thời gian xử lý khi gặp tác vụ nặng.

---

#### 📌 Thứ 4 (18/11/2026) - Phát tin & Điều phối sự kiện với Amazon SNS & EventBridge

* **Ta học được những gì hôm nay?**
  * **Mô hình kiến trúc Fanout (One-to-Many):** Tạo một Amazon SNS Topic `order-created-topic`. Đăng ký (Subscribe) đồng thời 3 hàng đợi SQS độc lập vào Topic này: `billing-queue`, `inventory-queue` và `shipping-queue`. Khi có 1 đơn hàng mới, chỉ cần phát 1 thông điệp duy nhất tới SNS, cả 3 phân hệ dịch vụ đều nhận được bản sao tin nhắn và xử lý song song độc lập.
  * **Bus sự kiện doanh nghiệp với Amazon EventBridge:** Khám phá sự vượt trội của EventBridge so với SNS trong việc định tuyến sự kiện dựa trên cấu trúc dữ liệu JSON (Content-based filtering).
  * **Thiết lập Event Pattern Rules:** Viết quy tắc lọc JSON thông minh, chỉ định tuyến các sự kiện có giá trị đơn hàng trên 1.000 USD sang luồng xử lý đặc biệt của bộ phận chống gian lận:
    ```json
    {
      "source": ["ecommerce.orders"],
      "detail-type": ["OrderCreated"],
      "detail": {
        "amount": [{ "numeric": [">=", 1000] }]
      }
    }
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Hàng đợi SQS không nhận được tin nhắn từ SNS:* Đăng ký Subscription thành công nhưng kiểm tra hàng đợi SQS luôn trống rỗng. Nguyên nhân: Hàng đợi SQS thiếu chính sách tài nguyên (Access Policy) cho phép SNS Topic gọi hành động `sqs:SendMessage`. Cách xử lý: Cập nhật Access Policy của SQS cấp quyền cho ARN của SNS Topic tương ứng.

---

#### 📌 Thứ 5 (19/11/2026) - Điều phối quy trình phân tán với AWS Step Functions

* **Ta học được những gì hôm nay?**
  * **Thiết kế State Machine trực quan với Workflow Studio:** Tách rời logic điều phối (Orchestration) ra khỏi mã nguồn ứng dụng bằng cách mô hình hóa chu trình nghiệp vụ thành các trạng thái (States) rõ ràng thông qua ngôn ngữ Amazon States Language (ASL).
  * **Phối hợp các trạng thái chuyên dụng:**
    * *Task State:* Gọi thực thi một hàm Lambda hoặc gửi tin nhắn vào hàng đợi SQS.
    * *Choice State:* Rẽ nhánh điều kiện dựa trên dữ liệu đầu ra (ví dụ: Nếu số dư tài khoản đủ thì sang trạng thái Trừ tiền, nếu không đủ thì sang trạng thái Báo lỗi).
    * *Parallel State:* Thực thi đồng thời nhiều nhánh công việc độc lập (vừa gửi email vừa cập nhật phân tích).
  * **Chiến lược tự phục hồi lỗi (Error Handling):** Cấu hình khối `Retry` tự động thử lại tối đa 3 lần với thuật toán tăng độ trễ cấp số nhân (`BackoffRate = 2.0`), kết hợp khối `Catch` để chuyển hướng sang luồng bồi hoàn (Compensating Transaction) khi xảy ra lỗi nghiêm trọng không thể khắc phục.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi dữ liệu đầu ra không khớp đầu vào của State kế tiếp:* Quá trình thực thi văng lỗi do payload trả về từ hàm Lambda bọc trong object lớn khiến Choice State không đọc được trường điều kiện. Cách xử lý: Sử dụng các thuộc tính lọc đường dẫn JSONPath: `InputPath`, `ResultPath` và `OutputPath` để tinh gọn và chuẩn hóa cấu trúc dữ liệu truyền giữa các trạng thái.

---

#### 📌 Thứ 6 (20/11/2026) - Tổng kết Tuần 10, Viết Worklog & Tích hợp Kiến trúc Đồ án

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa toàn bộ kiến trúc phi máy chủ hiện đại:** Kết nối liền mạch chu trình từ tiếp nhận yêu cầu (API Gateway) ➔ đệm và phân tách thông điệp (SQS) ➔ phát tin đa hướng (SNS/EventBridge) ➔ điều phối nghiệp vụ kiên cường (Step Functions).
  * **Dọn dẹp tài nguyên thử nghiệm:** Hủy các Step Functions State Machines, xóa các hàng đợi SQS và API Gateway test để bảo toàn hạn mức tài khoản.
  * **Tích hợp vào Đồ án Capstone:** Thiết kế sơ đồ luồng dữ liệu bất đồng bộ cho tính năng đặt hàng và gửi thông báo của Capstone Project, giúp loại bỏ hoàn toàn các liên kết đồng bộ (Synchronous Coupling) dễ gây sập hệ thống dây chuyền.
