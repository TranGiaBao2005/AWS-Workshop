---
title: "Worklog Tuần 10"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 10:

- Làm chủ mô hình kiến trúc **Hướng sự kiện (Event-Driven Architecture - EDA)** và các mẫu thiết kế hệ thống phân tán phi tập trung trên nền tảng AWS.
- Xây dựng, quản lý và bảo vệ các điểm cuối API cấp doanh nghiệp với **Amazon API Gateway** (REST API, HTTP API, cơ chế ủy quyền Lambda Authorizers, giới hạn tần suất truy cập Throttling).
- Triển khai giải pháp phân tách hệ thống (Decoupling) và chống quá tải dịch vụ với hàng đợi tin cậy **Amazon Simple Queue Service (Amazon SQS)** (Standard, FIFO, Dead-Letter Queue - DLQ).
- Thiết lập mô hình phát hành và đăng ký nhận tin (Pub/Sub) cùng bus điều phối sự kiện đa nguồn với **Amazon SNS** và **Amazon EventBridge**.
- Xây dựng và tự động hóa quy trình nghiệp vụ phân tán, xử lý ngoại lệ và tự động thử lại (Retry/Catch) với **AWS Step Functions (State Machines)**.
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và tích hợp các thành phần hàng đợi xử lý bất đồng bộ vào đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Quản trị và Bảo vệ API Gateway cấp doanh nghiệp:** <br>- So sánh và khởi tạo REST API vs HTTP API với Amazon API Gateway. <br>- Cấu hình tài nguyên, phương thức HTTP, CORS và tích hợp trực tiếp Lambda Backend. <br>- Thiết lập Usage Plans, API Keys và Rate Limiting để bảo vệ backend trước tấn công DDoS. | 16/11/2026 | 16/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 3** | **Phân tách hệ thống & Xử lý bất đồng bộ với Amazon SQS:** <br>- Khởi tạo Standard Queue (thông lượng cao) vs FIFO Queue (bảo toàn thứ tự nghiêm ngặt). <br>- Cấu hình Visibility Timeout, Message Retention và cơ chế Long Polling để tiết kiệm chi phí. <br>- Thiết lập Dead-Letter Queue (DLQ) và Redrive Policy để cô lập và xử lý các thông điệp lỗi. | 17/11/2026 | 17/11/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Thứ 4** | **Phát tin & Điều phối sự kiện với Amazon SNS & EventBridge:** <br>- Xây dựng mô hình Fanout: Đăng ký nhiều hàng đợi SQS vào một SNS Topic duy nhất. <br>- Thiết lập Amazon EventBridge Default Event Bus và Custom Event Bus. <br>- Viết các quy tắc lọc sự kiện (Event Pattern Filtering) định tuyến tin nhắn thông minh. | 18/11/2026 | 18/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 5** | **Điều phối luồng công việc phức tạp với AWS Step Functions:** <br>- Thiết kế State Machine trực quan bằng công cụ Workflow Studio qua ngôn ngữ Amazon States Language (ASL). <br>- Kết hợp các trạng thái: Task, Choice (rẽ nhánh điều kiện), Parallel (chạy song song) và Wait. <br>- Cấu hình xử lý lỗi (Error Handling), khối Retry tự động với Exponential Backoff. | 19/11/2026 | 19/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 6** | **Tổng kết Tuần 10, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức API Gateway, SQS, SNS, EventBridge và Step Functions. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 10 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp mô hình xử lý bất đồng bộ bằng SQS và Step Functions vào kiến trúc Đề xuất đồ án. | 20/11/2026 | 20/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 10:

#### 📌 Kết quả Thứ 2 (16/11/2026) - Bảo vệ API với Amazon API Gateway:
* **Quản trị API an toàn:** Triển khai thành công HTTP API kết nối trực tiếp với backend không máy chủ. Thiết lập chính sách bảo mật CORS, bảo vệ tài nguyên bằng AWS Lambda Custom Authorizers xác thực JWT Tokens.
* **Chống nghẽn tài nguyên:** Cấu hình Usage Plan với giới hạn Rate Limit (100 requests/giây) và Burst Limit (200 requests), đảm bảo hạ tầng backend được bảo vệ tuyệt đối trước các đợt lưu lượng tăng đột biến ngoài dự kiến.

#### 📌 Kết quả Thứ 3 (17/11/2026) - Phân tách hệ thống với Amazon SQS:
* **Hấp thụ tải đột biến:** Xây dựng hàng đợi tin cậy đóng vai trò bộ đệm (Buffer) giữa tầng tiếp nhận người dùng và tầng xử lý nghiệp vụ nặng, giúp loại bỏ hoàn toàn hiện tượng nghẽn cổ chai (Bottleneck) khi lưu lượng gửi đến tăng đột biến.
* **Xử lý thông điệp lỗi tự động:** Cấu hình Dead-Letter Queue (DLQ) tự động chuyển tiếp các tin nhắn bị lỗi sau 3 lần thử lại không thành công, cho phép các kỹ sư dễ dàng kiểm tra, phân tích nguyên nhân và thực hiện redrive mà không làm gián đoạn luồng vận hành chính.

#### 📌 Kết quả Thứ 4 (18/11/2026) - Điều phối sự kiện với SNS & EventBridge:
* **Mô hình kiến trúc Fanout:** Phát một thông điệp đơn lẻ từ Amazon SNS đồng thời tới nhiều subscriber độc lập (SQS tính cước, SQS phân tích và SQS thông báo), giúp các dịch vụ hoạt động hoàn toàn độc lập mà không cần biết đến sự tồn tại của nhau.
* **Lọc sự kiện chính xác:** Khai thác Amazon EventBridge Event Bus để định tuyến các sự kiện hệ thống dựa trên nội dung payload JSON, giảm thiểu 80% lưu lượng không cần thiết đến các consumer không liên quan.

#### 📌 Kết quả Thứ 5 (19/11/2026) - Điều phối quy trình với AWS Step Functions:
* **Tự động hóa chu trình phức tạp:** Xây dựng thành công chu trình xử lý đơn hàng gồm 5 bước (Kiểm tra kho -> Trừ tiền -> Cập nhật trạng thái -> Gửi thông báo -> Ghi nhật ký) bằng giao diện trực quan trực tiếp trên AWS Console.
* **Xử lý sự cố linh hoạt:** Cấu hình chiến lược phục hồi thông minh với khối Retry có độ trễ cấp số nhân (Exponential Backoff), đảm bảo tính kiên cường (Resiliency) trước các sự cố mạng tạm thời (Transient Errors).
