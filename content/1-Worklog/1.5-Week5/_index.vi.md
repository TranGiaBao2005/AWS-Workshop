---
title: "Worklog Tuần 5"
date: 2026-10-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 5:

- Xây dựng kiến trúc phân giải tên miền lai (**Hybrid DNS**) hai chiều giữa On-premises và AWS qua **Amazon Route 53 Resolver**.
- Làm chủ công cụ dòng lệnh **AWS Command Line Interface (AWS CLI v2)** và thiết lập cơ chế đa hồ sơ (**Multiple Named Profiles**) phục vụ tự động hóa hạ tầng (S3, SNS, VPC, EC2).
- Quản trị cơ sở dữ liệu phi quan hệ **Amazon DynamoDB**, tối ưu hóa truy vấn với **Global Secondary Index (GSI)** và lập trình tự động hóa với **Python SDK (Boto3)**.
- Triển khai cụm bộ nhớ đệm phân tán **Amazon ElastiCache - Redis** (Cluster Mode Disabled & Enabled), thiết lập bảo mật TLS/RBAC và lập trình tương tác.
- Tổng kết toàn bộ kiến thức tuần 5, hoàn thiện hệ thống Worklog và dành thời gian nghiên cứu triển khai đồ án thực tập (**Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ       | Công việc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                                                   |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------- | :-------------- | :--------------------------------------------------------------- |
| **Thứ 2** | **Thiết lập Hybrid DNS với Route 53 Resolver:** <br>- Tạo hạ tầng CloudFormation đa VPC & cấu hình Security Groups. <br>- Triển khai AWS Managed Microsoft AD đóng vai trò DNS On-premises. <br>- Khởi tạo Route 53 Outbound Endpoints & Forwarding Rules. <br>- Khởi tạo Inbound Endpoints & kiểm thử phân giải DNS hai chiều qua `nslookup`.                                                                                                                                                                                                                                                                                                            | 12/10/2026   | 12/10/2026      | [Hybrid DNS Workshop](https://000010.awsstudygroup.com/)         |
| **Thứ 3** | **Thao tác dòng lệnh với AWS CLI:** <br>- Thiết lập IAM Groups, Users & CLI Access Keys. <br>- Khởi tạo EC2 Management & kết nối MobaXterm. <br>- Cài đặt AWS CLI v2 & cấu hình đa hồ sơ (`default`, `devops`). <br>- Quản trị Amazon S3, Amazon SNS & IAM bằng CLI. <br>- Xây dựng mạng VPC & Tự động hóa máy chủ EC2.                                                                                                                                                                                                                                                                                                                                           | 13/10/2026   | 13/10/2026      | [AWS CLI Workshop](https://000011.awsstudygroup.com/)            |
| **Thứ 4** | **Làm việc với Amazon DynamoDB:** <br>- Quản trị cơ sở dữ liệu NoSQL qua AWS Management Console. <br>- Thao tác CRUD dòng lệnh và quản lý GSI bằng AWS CloudShell. <br>- Hiểu rõ cơ chế phân vùng (Partition Key) và Backfilling của GSI. <br>- Tự động hóa quy trình với Python SDK (Boto3). <br>- Nạp tập dữ liệu mẫu 4.609 phim (`moviedata.json`), Query & Scan.                                                                                                                                                                                                                                                                                              | 14/10/2026   | 14/10/2026      | [DynamoDB Workshop](https://000060.awsstudygroup.com/)           |
| **Thứ 5** | **Triển khai Amazon ElastiCache - Redis:** <br>- Quy hoạch VPC 3 AZs & tạo ElastiCache Subnet Group. <br>- Tạo cụm Cluster Mode Disabled & Enabled trên Web Console. <br>- Tự động hóa tạo cụm bằng Python Boto3 SDK. <br>- Thiết lập bảo mật mã hóa TLS & phân quyền RBAC Users/Groups. <br>- Lập trình Python tương tác Redis (Strings TTL, Hash, Pub/Sub).                                                                                                                                                                                                                                                                                                     | 15/10/2026   | 15/10/2026      | [ElastiCache Workshop](https://000061.awsstudygroup.com/)        |
| **Thứ 6** | **Tổng kết Tuần 5, Viết Worklog & Làm Project:** <br>- Tổng kết và hệ thống hóa kiến thức Route 53 Resolver, AWS CLI, DynamoDB, ElastiCache Redis. <br>- Hoàn thiện chi tiết nội dung và hình ảnh cho các trang Worklog từ 1.5.1 đến 1.5.4. <br>- Dành thời gian nghiên cứu kiến trúc AWS và tiếp tục phát triển Đồ án thực tập (Project Proposal).                                                                                                                                                                                                                                                                                                      | 16/10/2026   | 16/10/2026      | [Internal Review & Project Documentation](/vi/2-proposal/)       |

---

### Kết quả đạt được tuần 5:

#### 📌 Kết quả Thứ 2 (12/10/2026) - Thiết lập Hybrid DNS với Route 53 Resolver:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ 11 hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.5.1. Thiết lập Hybrid DNS với Route 53 Resolver](1.5.1-hybrid-dns/)**.
{{% /notice %}}

- **Mô hình kiến trúc mạng lai (Hybrid Cloud):** Hiểu rõ bài toán kết nối và định tuyến tên miền giữa trung tâm dữ liệu tại chỗ (On-premises) và môi trường đám mây AWS.
- **Phân giải tên miền hai chiều:** Nắm vững nguyên lý hoạt động của Inbound và Outbound Endpoints trong Route 53 Resolver để máy chủ hai bên nhận diện và phân giải DNS thông suốt.
- **Kiểm thử và xác thực thực tế:** Rèn luyện kỹ năng kiểm tra độ trễ và tính chính xác của các bản ghi DNS bằng `nslookup` trên môi trường đa VPC mô phỏng doanh nghiệp.

---

#### 📌 Kết quả Thứ 3 (13/10/2026) - Thao tác dòng lệnh với AWS CLI:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình kỹ thuật, quy trình thực hiện, 12 sự cố đã xử lý thành công và trọn bộ 38 hình ảnh minh chứng được trình bày chi tiết tại: **[1.5.2. Thao tác dòng lệnh với AWS CLI](1.5.2-aws-cli/)**.
{{% /notice %}}

- **Làm quen với giao diện dòng lệnh AWS CLI:** Hiểu rõ vai trò và sức mạnh của việc tự động hóa quản trị hạ tầng bằng dòng lệnh thay vì thao tác thủ công qua giao diện Web.
- **Quản trị người dùng & bảo mật định danh:** Nắm được cách phân quyền IAM, quản lý Access Key an toàn và thiết lập nhiều hồ sơ tài khoản (CLI Profiles) trên máy chủ quản trị.
- **Tự động hóa tài nguyên cơ bản:** Thực hành khởi tạo, cấu hình và dọn dẹp các dịch vụ cốt lõi (lưu trữ S3, kênh thông báo SNS, hệ thống mạng VPC và vòng đời máy chủ EC2) hoàn toàn bằng câu lệnh.
- **Kỹ năng xử lý sự cố thực tế:** Rèn luyện phản xạ phát hiện và khắc phục các vấn đề phổ biến về định tuyến mạng, khóa kết nối SSH, quyền truy cập và xung đột tài nguyên.

---

#### 📌 Kết quả Thứ 4 (14/10/2026) - Làm việc với Amazon DynamoDB:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình kỹ thuật, quy trình thực hiện, 10 sự cố đã xử lý thành công và trọn bộ 32 hình ảnh minh chứng được trình bày chi tiết tại: **[1.5.3. Làm việc với Amazon DynamoDB](1.5.3-amazon-dynamodb/)**.
{{% /notice %}}

- **Tư duy cơ sở dữ liệu NoSQL:** Hiểu sự khác biệt nền tảng giữa cơ sở dữ liệu phi quan hệ (NoSQL) và quan hệ truyền thống (SQL), đặc biệt là tính linh hoạt về cấu trúc dữ liệu theo từng bản ghi.
- **Thao tác dữ liệu đa nền tảng:** Nắm vững các thao tác thêm, đọc, cập nhật và xóa dữ liệu qua cả giao diện Console trực quan lẫn công cụ dòng lệnh CloudShell.
- **Tối ưu hóa tra cứu với Chỉ mục (Index):** Hiểu vai trò của khóa chính và cách áp dụng Global Secondary Index (GSI) để hỗ trợ tìm kiếm dữ liệu đa chiều hiệu quả.
- **Lập trình tự động hóa với Python SDK (Boto3):** Học cách viết mã nguồn Python để tự động tạo bảng, nạp tập dữ liệu lớn và thực thi các câu truy vấn, quét lọc dữ liệu theo nhu cầu thực tế.

---

#### 📌 Kết quả Thứ 5 (15/10/2026) - Triển khai Amazon ElastiCache - Redis:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình kỹ thuật, quy trình thực hiện, 12 sự cố đã xử lý thành công và trọn bộ 27 hình ảnh minh chứng được trình bày chi tiết tại: **[1.5.4. Triển khai Amazon ElastiCache - Redis](1.5.4-amazon-elasticache/)**.
{{% /notice %}}

- **Vai trò của bộ nhớ đệm (In-Memory Cache):** Hiểu cách ứng dụng bộ nhớ đệm tốc độ cao nhằm tăng tốc phản hồi cho ứng dụng và giảm tải cho hệ thống cơ sở dữ liệu chính.
- **Các mô hình cụm phân tán:** Phân biệt và trải nghiệm thực tế giữa cụm đảm bảo tính sẵn sàng cao (Cluster Mode Disabled) và cụm mở rộng phân mảnh dữ liệu (Cluster Mode Enabled).
- **Bảo mật và lập trình tích hợp:** Nắm được cách thiết lập mã hóa dữ liệu đường truyền (TLS), phân quyền người dùng (RBAC) và lập trình kết nối, lưu trữ dữ liệu có thời gian sống (TTL) cũng như truyền nhận thông điệp thời gian thực (Pub/Sub).
- **Tự động hóa và kinh nghiệm vận hành:** Rèn luyện việc triển khai cụm thông qua mã nguồn Python Boto3 và xử lý các ràng buộc phức tạp về mạng đa vùng sẵn sàng.

---

#### 📌 Kết quả Thứ 6 (16/10/2026) - Tổng kết Tuần 5, Viết Worklog & Làm Project:

{{% notice tip %}}
👉 **Kế hoạch định kỳ Thứ 6:** Dành trọn vẹn ngày Thứ 6 cho 3 trọng tâm chính: (1) Tổng kết kiến thức đã tích lũy trong tuần; (2) Hoàn thiện hệ thống Worklog và minh chứng thực hành; (3) Nghiên cứu và triển khai Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
{{% /notice %}}

* **1. Tổng kết kiến thức tuần 5:**
  * Hệ thống hóa các kiến thức mạng kết hợp (**Hybrid DNS**) với Route 53 Resolver giúp thông suốt tên miền đám mây và trung tâm dữ liệu.
  * Làm chủ kỹ năng quản trị dòng lệnh chuyên sâu với **AWS CLI v2** và các mô hình quản trị tài nguyên theo kịch bản.
  * Làm chủ nền tảng lưu trữ dữ liệu hiện đại: Cơ sở dữ liệu NoSQL **Amazon DynamoDB** và bộ nhớ đệm phân tán **Amazon ElastiCache Redis**.
* **2. Hoàn thiện hệ thống Worklog:**
  * Soát lỗi toàn bộ các bài thực hành trong tuần từ **1.5.1 đến 1.5.4**, bổ sung đầy đủ các bảng thông số kỹ thuật và hơn 100 hình ảnh minh chứng thực tế.
  * Đảm bảo tính nhất quán song ngữ (Tiếng Việt và Tiếng Anh), định dạng chuẩn Markdown và kiểm tra đường dẫn liên kết nội bộ.
* **3. Nghiên cứu & Triển khai Project (Proposal):**
  * Dành thời gian nghiên cứu áp dụng ElastiCache và DynamoDB vào kiến trúc hệ thống thương mại điện tử trong đề xuất đồ án.
  * Cập nhật và tinh chỉnh các phần kiến trúc đề xuất trong **[Project Proposal](/vi/2-proposal/)**.

---

### Mục tiêu cho tuần sau (Tuần 6):

* **Quản lý giới hạn tài nguyên với AWS Service Quotas (1.6.1):**
  * Hiểu rõ cơ chế hạn mức tài nguyên (Quotas) nhằm bảo vệ an toàn cho tài khoản AWS.
  * Thực hành gửi yêu cầu nâng hạn mức vCPU cho Spot Instances và làm việc với AWS Support Center.
  * Tự động hóa tra cứu hạn mức bằng AWS CLI và xây dựng cảnh báo qua CloudWatch.
* **Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (1.6.2):**
  * Xây dựng giải pháp tự động tắt/bật máy chủ phát triển ngoài giờ làm việc bằng serverless.
  * Lập trình Python Boto3 trên AWS Lambda, tích hợp ChatOps gửi thông báo về kênh Slack qua Incoming Webhooks.
  * Lên lịch kích hoạt định kỳ tự động bằng Amazon EventBridge Scheduler.
* **Giám sát với Grafana & CloudWatch (1.6.3):**
  * Triển khai giải pháp giám sát trực quan hóa với Grafana kết nối nguồn dữ liệu Amazon CloudWatch (Workshop 000029 - Getting started with Grafana basic).
  * Xây dựng Dashboard theo dõi các chỉ số hiệu năng và trạng thái hạ tầng hệ thống theo thời gian thực.
* **Tổng kết Tuần 6, Viết Worklog & Làm Project:** Hệ thống hóa kiến thức giám sát và tối ưu chi phí, hoàn thiện tài liệu và phát triển đồ án thực tập.
