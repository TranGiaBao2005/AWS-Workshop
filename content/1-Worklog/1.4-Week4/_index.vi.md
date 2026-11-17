---
title: "Worklog Tuần 4"
date: 2026-10-05
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 4:

- Làm quen và thực hành trên **Amazon Lightsail** (Triển khai Managed Database, WordPress, Prestashop, Snapshot và Migration).
- Thực hành chạy ứng dụng container hóa đơn giản và nhanh chóng với **Amazon Lightsail Container**.
- Thiết lập kiến trúc ứng dụng co giãn linh hoạt và cân bằng tải với **Amazon EC2 Auto Scaling** và **Application Load Balancer**.
- Thiết lập giải pháp giám sát tập trung, phân tích log chuyên sâu và cấu hình cảnh báo tự động với **Amazon CloudWatch**.
- Tổng kết toàn bộ kiến thức tuần 4, hoàn thiện hệ thống Worklog và dành thời gian nghiên cứu triển khai đồ án thực tập (**Project Proposal**).

### Các công việc cần triển khai trong tuần này:

| Thứ       | Công việc                                                                                                                                                                                                                                                                                                                                     | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                                             |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------- | :-------------- | :--------------------------------------------------------- |
| **Thứ 2** | **Triển khai Amazon Lightsail:** <br>- Managed MySQL Database & WordPress Instance. <br>- Cấu hình Ubuntu, Static IP & Networking. <br>- Nền tảng Prestashop E-Commerce. <br>- Bản sao lưu Snapshots & Nâng cấp Migration.                                                                                                                    | 05/10/2026   | 05/10/2026      | [Lightsail Workshop](https://000045.awsfcaj.com/)    |
| **Thứ 3** | **Triển khai Amazon Lightsail Container:** <br>- Chuẩn bị AWS CLI & Khắc phục phân quyền IAM. <br>- Khởi tạo Container Service trên Lightsail. <br>- Triển khai Public Container Image (Nginx). <br>- Đóng gói & Đẩy Custom Image lên Lightsail qua Build-Instance.                                                                           | 06/10/2026   | 06/10/2026      | [Lightsail Container](https://000046.awsfcaj.com/)   |
| **Thứ 4** | **Tự động co giãn với EC2 Auto Scaling:** <br>- Đóng gói Custom AMI & Tạo Launch Template. <br>- Thiết lập Target Group & Application Load Balancer. <br>- Khởi tạo Auto Scaling Group & Scaling Policies. <br>- Kiểm thử chịu tải Stress Test & Scale Out/In.                                                                                | 07/10/2026   | 07/10/2026      | [Auto Scaling Workshop](https://000006.awsfcaj.com/) |
| **Thứ 5** | **Giám sát với Amazon CloudWatch:** <br>- Cài đặt CloudWatch Agent và thu thập Metrics/Logs từ EC2. <br>- Đồ thị hóa chỉ số với Search Expressions & Math Expressions. <br>- Khai thác và phân tích log với CloudWatch Logs Insights. <br>- Thiết lập Metric Filters và chuông báo động CloudWatch Alarms.                                    | 08/10/2026   | 08/10/2026      | [CloudWatch Workshop](https://000008.awsfcaj.com/)   |
| **Thứ 6** | **Tổng kết Tuần 4, Viết Worklog & Làm Project:** <br>- Tổng kết và hệ thống hóa kiến thức các dịch vụ Lightsail, Auto Scaling, CloudWatch. <br>- Hoàn thiện chi tiết nội dung và hình ảnh cho các trang Worklog từ 1.4.1 đến 1.4.4. <br>- Dành thời gian nghiên cứu tài liệu kiến trúc và xây dựng báo cáo Đồ án thực tập (Project Proposal). | 09/10/2026   | 09/10/2026      | [Internal Review & Project Documentation](/vi/2-proposal/) |

---

### Kết quả đạt được tuần 4:

#### 📌 Kết quả Thứ 2 (05/10/2026) - Triển khai Amazon Lightsail:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ 13 hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.4.1. Triển khai Amazon Lightsail](1.4.1-amazon-lightsail/)**.
{{% /notice %}}

- **Làm quen với Amazon Lightsail:** Hiểu được mô hình dịch vụ đám mây tinh giản của AWS, phù hợp cho việc khởi tạo nhanh các ứng dụng vừa và nhỏ với chi phí dự đoán được.
- **Triển khai ứng dụng Web & Cơ sở dữ liệu:** Nắm vững quy trình dựng website (WordPress và nền tảng thương mại điện tử Prestashop) kết nối với cơ sở dữ liệu quản lý độc lập (Managed Database).
- **Quản trị mạng và bảo vệ dữ liệu:** Nắm được cách cấp phát IP tĩnh, cấu hình tường lửa cơ bản, tạo bản sao lưu (Snapshot) và nâng cấp cấu hình máy chủ linh hoạt khi nhu cầu tài nguyên tăng.

---

#### 📌 Kết quả Thứ 3 (06/10/2026) - Triển khai Amazon Lightsail Container:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ 11 hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.4.2. Triển khai Amazon Lightsail Container](1.4.2-lightsail-container/)**.
{{% /notice %}}

- **Khái niệm Container Service trên Lightsail:** Hiểu cách vận hành ứng dụng đóng gói dưới dạng container trên đám mây mà không cần trực tiếp quản trị cụm máy chủ phức tạp.
- **Triển khai ứng dụng Container:** Làm quen với việc chạy các image có sẵn từ Docker Hub cũng như cách đóng gói và đẩy container image tùy chỉnh lên kho lưu trữ đám mây.
- **Truy cập ứng dụng an toàn:** Nắm được quy trình kích hoạt và kiểm tra ứng dụng chạy thực tế với chứng chỉ bảo mật SSL/HTTPS tự động được tích hợp sẵn.

---

#### 📌 Kết quả Thứ 4 (07/10/2026) - Tự động co giãn với EC2 Auto Scaling:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ 44 hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.4.3. Tự động co giãn với EC2 Auto Scaling](1.4.3-ec2-auto-scaling/)**.
{{% /notice %}}

- **Chuẩn hóa khuôn mẫu máy chủ:** Hiểu cách tạo bản sao ảnh (AMI) và mẫu khởi chạy (Launch Template) để tự động hóa việc sinh ra các máy chủ đồng nhất.
- **Phân phối tải với Application Load Balancer:** Nắm nguyên lý điều phối lưu lượng truy cập của người dùng đến nhiều máy chủ phân bổ trên các vùng sẵn sàng khác nhau nhằm tăng tính sẵn sàng.
- **Cơ chế tự động co giãn (Auto Scaling):** Trải nghiệm cách hệ thống tự động bổ sung máy chủ khi tải tăng cao và tự động thu gọn lại khi tải giảm để tối ưu hóa chi phí vận hành.

---

#### 📌 Kết quả Thứ 5 (08/10/2026) - Giám sát với Amazon CloudWatch:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ 33 hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.4.4. Giám sát với Amazon CloudWatch](1.4.4-amazon-cloudwatch/)**.
{{% /notice %}}

- **Thu thập dữ liệu giám sát hệ thống:** Hiểu cách cài đặt tác tử (Agent) để theo dõi các chỉ số hiệu năng (CPU, RAM, ổ đĩa) và tập trung nhật ký (Logs) của máy chủ.
- **Trực quan hóa và truy vấn nhật ký:** Học cách xây dựng biểu đồ giám sát trực quan và sử dụng công cụ truy vấn nâng cao (Logs Insights) để nhanh chóng phát hiện các bất thường của hệ thống.
- **Thiết lập cảnh báo tự động:** Nắm cách định nghĩa ngưỡng kích hoạt cảnh báo (Alarms) và kết hợp với dịch vụ thông báo (SNS) để gửi tin tức thời cho quản trị viên khi có sự cố.

---

#### 📌 Kết quả Thứ 6 (09/10/2026) - Tổng kết Tuần 4, Viết Worklog & Làm Project:

{{% notice tip %}}
👉 **Kế hoạch định kỳ Thứ 6:** Dành trọn vẹn ngày Thứ 6 cho 3 trọng tâm chính: (1) Tổng kết kiến thức đã tích lũy trong tuần; (2) Hoàn thiện hệ thống Worklog và minh chứng thực hành; (3) Nghiên cứu và triển khai Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
{{% /notice %}}

- **1. Tổng kết kiến thức tuần 4:**
  - Hệ thống hóa toàn diện kiến thức về giải pháp triển khai ứng dụng đơn giản với **Amazon Lightsail** và **Lightsail Container Service**.
  - Nắm vững nguyên lý xây dựng hạ tầng co giãn tự động linh hoạt với **EC2 Auto Scaling** kết hợp cân bằng tải **Application Load Balancer**.
  - Làm chủ công cụ giám sát, thu thập chỉ số hiệu năng và phân tích log chuyên sâu với **Amazon CloudWatch** (CloudWatch Agent, Alarms, Logs Insights).
- **2. Hoàn thiện hệ thống Worklog:**
  - Soát lỗi toàn bộ các bài thực hành trong tuần từ **1.4.1 đến 1.4.4**, bổ sung đầy đủ các bảng thông số kỹ thuật và hình ảnh thực tế.
  - Đảm bảo tính nhất quán song ngữ (Tiếng Việt và Tiếng Anh), định dạng chuẩn Markdown và kiểm tra đường dẫn liên kết nội bộ.
- **3. Nghiên cứu & Triển khai Project (Proposal):**
  - Dành thời gian nghiên cứu tài liệu kỹ thuật của AWS Well-Architected Framework phục vụ cho đồ án thực tập.
  - Cập nhật và tinh chỉnh các phần kiến trúc đề xuất trong **[Project Proposal](/vi/2-proposal/)**, chuẩn bị các kịch bản triển khai thực tế.

---

### Mục tiêu cho tuần sau (Tuần 5):

- **Thiết lập Hybrid DNS với Route 53 Resolver (1.5.1):**
  - Tạo hạ tầng CloudFormation đa VPC mô phỏng môi trường On-premises và AWS Cloud.
  - Triển khai AWS Directory Service (AWS Managed Microsoft AD) đóng vai trò máy chủ phân giải tên miền On-premises.
  - Cấu hình Route 53 Outbound Endpoints & Forwarding Rules và Inbound Endpoints để thực hiện phân giải tên miền hai chiều thông suốt qua `nslookup`.
- **Thao tác dòng lệnh với AWS CLI (1.5.2):**
  - Quản trị tập trung IAM User Groups, Users và cấp phát Access Keys an toàn.
  - Thiết lập máy trạm quản trị EC2 Linux và kết nối từ xa qua SSH (MobaXterm).
  - Cài đặt AWS CLI v2 trên Linux, cấu hình đa hồ sơ định danh (`default`, `devops`).
  - Quản trị lưu trữ hướng đối tượng trên Amazon S3 và kênh phân phối thông điệp Amazon SNS bằng lệnh CLI.
  - Tự động hóa toàn diện quy trình xây dựng hệ thống mạng Amazon VPC độc lập và điều khiển vòng đời máy chủ EC2.
- **Làm việc với Amazon DynamoDB (1.5.3):**
  - Quản trị cơ sở dữ liệu NoSQL, tạo bảng `Music` và thao tác dữ liệu linh hoạt trên AWS Management Console.
  - Thao tác dòng lệnh toàn diện qua AWS CloudShell (CRUD, quản trị và truy vấn qua Global Secondary Index - GSI).
  - Lập trình tự động hóa với Python 3 & Boto3 SDK: khởi tạo bảng `Movies`, nạp tập dữ liệu lớn 4.609 bộ phim (`moviedata.json`), thực thi truy vấn Primary Key và quét bảng (Scan) có điều kiện lọc nâng cao.
- **Triển khai Amazon ElastiCache - Redis (1.5.4):**
  - Quy hoạch VPC 3 Subnets trải đều 3 Availability Zones (`us-east-1a`, `1b`, `1c`) và tạo ElastiCache Subnet Group.
  - Triển khai cụm Redis cả hai chế độ: Cluster Mode Disabled và Cluster Mode Enabled trên Web Console và Python Boto3 SDK.
  - Thiết lập bảo mật doanh nghiệp với Mã hóa đường truyền (TLS Transit Encryption) kết hợp phân quyền RBAC Users & User Groups.
  - Viết mã nguồn Python trên EC2 Client tương tác với Redis: kiểm tra TLS RBAC, Strings kèm TTL 60s, Hash kèm xử lý ngoại lệ WRONGTYPE, và Pub/Sub thời gian thực.
- **Tổng kết Tuần 5, Viết Worklog & Làm Project:** Hệ thống hóa toàn bộ kiến thức, hoàn thiện bài viết và tiếp tục hoàn thiện đề xuất đồ án.
