---
title: "Worklog Tuần 3"
date: 2026-09-28
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 3:

- Tiếp cận các mô hình Hiện đại hóa ứng dụng (**Application Modernization**) trên AWS theo phân hệ [Application Modernization & Containers](https://cloudjourney.awsfcaj.com/4-modernize/).
- Nắm vững kiến trúc không máy chủ (**Serverless Backend**) với AWS Lambda, Amazon DynamoDB, Amazon API Gateway và quản lý định danh người dùng tập trung với **Amazon Cognito**.
- Khám phá hệ sinh thái điều phối container doanh nghiệp với **Amazon ECS Fargate**, **Amazon EKS** và **Red Hat OpenShift on AWS (ROSA)**.
- Xây dựng nền tảng tư duy Hồ dữ liệu (**Data Lake**) trên Amazon S3, phân tích dữ liệu với **Amazon Athena** và trực quan hóa báo cáo với **Amazon QuickSight**.
- Dành trọng tâm ngày Thứ 5 triển khai bài thực hành chuyên sâu: **Thiết kế kiến trúc mạng 2 tầng (Two-Tier) và vận hành cơ sở dữ liệu quan hệ Amazon RDS Multi-AZ** (Workshop 000005).
- Dành ngày Thứ 6 tổng kết toàn bộ 3 tuần đầu, hoàn thiện hồ sơ Worklog và hoàn tất nộp Bản đề xuất dự án (**Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **App Modernization & Serverless Backend:** <br>- Xây dựng Serverless Backend với [Lambda, S3, DynamoDB (000078)](https://000078.awsfcaj.com). <br>- Quản lý xác thực người dùng an toàn với [Amazon Cognito (000081)](https://000081.awsfcaj.com). <br>- Tự động hóa đóng gói hạ tầng không máy chủ với [AWS SAM (000080)](https://000080.awsfcaj.com). | 28/09/2026 | 28/09/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 3** | **Dịch vụ Container & Kubernetes Doanh nghiệp:** <br>- Đóng gói microservices với [Amazon ECS Fargate (000067)](https://000067.awsfcaj.com). <br>- Khởi tạo cụm Kubernetes quản lý với [Amazon EKS (000126)](https://000126.awsfcaj.com). <br>- Khám phá nền tảng lai [Red Hat OpenShift on AWS - ROSA (000071)](https://000071.awsfcaj.com). | 29/09/2026 | 29/09/2026 | [Cloud Journey - Containers](https://cloudjourney.awsfcaj.com/5-container/) |
| **Thứ 4** | **Phân tích dữ liệu & Hồ dữ liệu đám mây:** <br>- Xây dựng kiến trúc hồ dữ liệu với [Data Lake Fundamentals (000035)](https://000035.awsfcaj.com). <br>- Truy vấn dữ liệu phân tán phi máy chủ với [Amazon Athena (000106)](https://000106.awsfcaj.com). <br>- Báo cáo trực quan hóa dữ liệu kinh doanh với [Amazon QuickSight (000073)](https://000073.awsfcaj.com). | 30/09/2026 | 30/09/2026 | [Cloud Journey - Data](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Thứ 5** | **Thực hành triển khai Amazon RDS (Trọng tâm thực chiến):** <br>- Thiết lập mạng VPC 2 AZs, phân tách Public Subnet và Private Subnet. <br>- Cấu hình Security Group chuỗi liên kết (Chaining) mở port MySQL 3306. <br>- Khởi tạo cụm Amazon RDS MySQL Multi-AZ và kết nối từ Web Server EC2. <br>- Thực hành tạo bản sao lưu thủ công (Manual Snapshot) và phục hồi CSDL. | 01/10/2026 | 01/10/2026 | [Amazon RDS Workshop (000005)](https://000005.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết tuần 3, Viết Worklog & Hoàn tất Project Proposal:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Serverless, Containers, Analytics và CSDL RDS. <br>- **Làm Worklog:** Hoàn thiện báo cáo chi tiết cho bài lab Amazon RDS (1.3.1) và tổng kết Worklog Tuần 3. <br>- **Làm Project:** Hoàn tất rà soát lần cuối và chính thức nộp Bản đề xuất dự án thực tập (Project Proposal). | 02/10/2026 | 02/10/2026 | [The First Cloud Journey](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (28/09/2026) - Hiện đại hóa ứng dụng không máy chủ (App Modernization)

* **Ta học được những gì hôm nay?**
  * **Mô hình kiến trúc không máy chủ (Serverless Architecture):** Nắm vững cách xây dựng ứng dụng Web ba tầng (Three-tier Web App) không máy chủ: Tầng giao diện lưu trữ trên Amazon S3 ➔ Tầng xử lý logic nghiệp vụ qua Amazon API Gateway và AWS Lambda ➔ Tầng dữ liệu bền bỉ trên Amazon DynamoDB.
  * **Quản trị định danh người dùng với Amazon Cognito:**
    * Khởi tạo **Cognito User Pool**: Cung cấp tính năng đăng ký tài khoản (Sign-up), đăng nhập (Sign-in), gửi email xác thực mã OTP, đặt lại mật khẩu và hỗ trợ xác thực đa yếu tố (MFA).
    * Khởi tạo **Cognito Identity Pool**: Cung cấp cơ chế phân quyền ủy thác (Federated Identities), cấp phát thông tin xác thực AWS tạm thời (Temporary AWS Credentials) cho người dùng cuối truy cập trực tiếp vào các tài nguyên AWS được phép (như tải ảnh lên thư mục riêng trên S3).
  * **Tự động hóa triển khai với AWS SAM (Serverless Application Model):** Khám phá công cụ CLI mã nguồn mở giúp định nghĩa hàm Lambda, bảng DynamoDB và API Gateway chỉ với một tệp `template.yaml` ngắn gọn, thực thi lệnh `sam build` và `sam deploy` tự động.

![Serverless Backend Architecture](/images/1-Worklog/1.3-Week3/serverless-lambda-automation.png)
*Hình 1.3.1: Kiến trúc luồng xử lý phi máy chủ tích hợp AWS Lambda điều phối tài nguyên theo sự kiện.*

![Cognito Authentication & IAM](/images/1-Worklog/1.3-Week3/cognito-iam-security.png)
*Hình 1.3.2: Cơ chế xác thực người dùng tập trung và phân quyền truy cập thông qua Amazon Cognito và IAM Roles.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi xác thực Token trên API Gateway:* Người dùng gửi JWT Token nhận từ Cognito User Pool vào API Gateway nhưng bị trả về lỗi `401 Unauthorized`. Nguyên nhân: Header `Authorization` thiếu từ khóa tiền tố `Bearer `. Cách xử lý: Cấu hình chuẩn hóa chuỗi header gửi từ phía client theo đúng định dạng `Bearer <id_token>`.

---

#### 📌 Thứ 3 (29/09/2026) - Dịch vụ đóng gói và điều phối Container doanh nghiệp

* **Ta học được những gì hôm nay?**
  * **Điều phối container doanh nghiệp với Amazon ECS Fargate:** Tìm hiểu cách phân tách ứng dụng nguyên khối (Monolith) thành các vi dịch vụ độc lập (Auth service, Product service, Order service), đóng gói từng service vào container và triển khai trên hạ tầng phi máy chủ AWS Fargate với khả năng co giãn độc lập.
  * **Hệ sinh thái Kubernetes quản lý (Amazon EKS):** Tiếp cận kiến trúc chuẩn công nghiệp của Kubernetes: Pods, Services, Deployments, ReplicaSets và Ingress. Khám phá cách EKS quản lý Control Plane có độ sẵn sàng cao, giúp doanh nghiệp vận hành các ứng dụng mã nguồn mở tiêu chuẩn mà không bị trói buộc vào một nhà cung cấp đám mây duy nhất (Multi-cloud portability).
  * **Nền tảng lai Red Hat OpenShift on AWS (ROSA):** Khám phá giải pháp tích hợp giữa Red Hat và AWS, mang lại môi trường vận hành Kubernetes đồng nhất giữa trung tâm dữ liệu tại chỗ (On-Premises) và đám mây công cộng AWS.

![ECS Fargate Microservices](/images/1-Worklog/1.3-Week3/ecs-microservices-fargate.png)
*Hình 1.3.3: Sơ đồ kiến trúc ứng dụng Microservices đa dịch vụ vận hành trên Amazon ECS và AWS Fargate.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Bài toán lựa chọn công nghệ:* Băn khoăn khi nào nên dùng ECS và khi nào nên dùng EKS. Bài học đúc kết: Chọn **ECS Fargate** khi đội ngũ muốn tập trung phát triển sản phẩm, cần sự đơn giản, tích hợp sâu vào AWS với chi phí vận hành thấp; Chọn **Amazon EKS** khi tổ chức đã có sẵn kinh nghiệm vận hành Kubernetes, có các hệ thống phức tạp hoặc yêu cầu chạy đồng nhất trên nhiều nền tảng đám mây khác nhau.

---

#### 📌 Thứ 4 (30/09/2026) - Hồ dữ liệu & Phân tích thông minh (Data Analytics)

* **Ta học được những gì hôm nay?**
  * **Kiến trúc Hồ dữ liệu hiện đại (Data Lake Fundamentals):** Hiểu rõ tư duy tập trung hóa toàn bộ dữ liệu có cấu trúc, bán cấu trúc và phi cấu trúc của doanh nghiệp về một "kho chứa" duy nhất trên Amazon S3, tách rời hoàn toàn giữa tầng lưu trữ (Storage) và tầng tính toán phân tích (Compute).
  * **Tự động hóa danh mục dữ liệu với AWS Glue:** Trải nghiệm khả năng của Glue Crawler tự động quét các tệp dữ liệu nhật ký trên S3, tự động suy diễn cấu trúc bảng và cập nhật vào AWS Glue Data Catalog.
  * **Truy vấn phân tán & Trực quan hóa dữ liệu:** Sử dụng Amazon Athena để truy vấn tức thì dữ liệu thô bằng các câu lệnh SQL ANSI quen thuộc mà không cần khởi chạy máy chủ CSDL, kết nối kết quả với Amazon QuickSight để vẽ các biểu đồ phân tích kinh doanh sinh động.

![Data Lake Analytics Pipeline](/images/1-Worklog/1.3-Week3/data-lake-pipeline.png)
*Hình 1.3.4: Kiến trúc luồng phân tích dữ liệu Data Lake từ Ingestion, lưu trữ S3, phân loại Glue đến trực quan hóa QuickSight.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Chi phí quét dữ liệu tăng cao khi truy vấn file CSV:* Khi dung lượng dữ liệu tăng lên hàng chục GB, mỗi câu lệnh `SELECT` trên file CSV thô quét toàn bộ tệp tin gây tốn kém chi phí. Cách xử lý: Ghi nhớ bài học bắt buộc phải chuyển đổi dữ liệu sang định dạng cột Parquet đi kèm nén Snappy và phân vùng ngày tháng (Partitioning) để giảm trên 90% lượng dữ liệu quét.

---

#### 📌 Thứ 5 (01/10/2026) - Thực hành triển khai cơ sở dữ liệu quan hệ Amazon RDS

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình mạng VPC, thiết lập Security Groups chuỗi liên kết, kết nối Web Server EC2, sao lưu Snapshot và trọn bộ 10 hình ảnh minh chứng được trình bày chi tiết tại bài viết riêng: **[1.3.1. Thực hành triển khai Amazon RDS](1.3.1-amazon-rds/)**.
{{% /notice %}}

* **Ta học được những gì hôm nay?**
  * **Kiến trúc mạng hai tầng an toàn (Two-Tier Architecture):**
    * Triển khai VPC `rds-vpc` (`10.0.0.0/16`) với 4 Subnets trên 2 AZs: 2 Public Subnets cho Web Server và 2 Private Subnets dành riêng cho cơ sở dữ liệu Amazon RDS.
    * Đảm bảo CSDL tuyệt đối không có Public IP và không có tuyến đường ra Internet, triệt tiêu 100% rủi ro bị tấn công trực tiếp từ bên ngoài.
  * **Bảo mật chuỗi liên kết (Chained Security Groups):**
    * Thay vì mở port MySQL 3306 cho một dải IP cụ thể, cấu hình Inbound Rule của `rds-sg` trỏ nguồn vào mã định danh của `ec2-sg` (`sg-0cec4d0fbfc6d4c41`). Chỉ có các máy ảo được gán đúng nhóm `ec2-sg` mới được phép bắt tay kết nối tới database.
  * **Tính sẵn sàng cao với Amazon RDS Multi-AZ:**
    * Khởi tạo DB Subnet Group `rds-subnet-group` bao gồm 2 Private Subnets trên `us-east-1a` và `us-east-1b`.
    * Triển khai CSDL MySQL Community (`db.m5.large`) với tùy chọn Multi-AZ Deployment. AWS tự động khởi tạo máy chủ Primary tại một AZ và tự động sao chép đồng bộ dữ liệu (Synchronous Replication) sang máy chủ Standby tại AZ thứ hai. Khi xảy ra sự cố phần cứng, AWS tự động chuyển đổi dự phòng (Failover) dưới 60 giây mà không cần can thiệp thủ công.
  * **Bảo vệ dữ liệu với Backup & Manual Snapshot:**
    * Nắm vững cơ chế sao lưu tự động hàng ngày (Automated Backups) với tính năng Point-in-Time Recovery (PITR) cho phép khôi phục dữ liệu về bất kỳ giây nào trong vòng 7 ngày qua.
    * Tự tay tạo một bản sao lưu thủ công (Manual Snapshot), lưu trữ độc lập trên S3 và kiểm thử quy trình khôi phục thành công một instance cơ sở dữ liệu mới từ snapshot này.

![Amazon RDS Two-Tier Architecture](/images/1-Worklog/1.3-Week3/arc.png)
*Hình 1.3.5: Sơ đồ kiến trúc hai tầng an toàn phân tách giữa máy chủ Web EC2 và cơ sở dữ liệu Amazon RDS.*

![Amazon RDS Instance Running](/images/1-Worklog/1.3-Week3/rds-endpoint-info.png)
*Hình 1.3.6: Cơ sở dữ liệu quan hệ Amazon RDS MySQL Multi-AZ trong trạng thái sẵn sàng (Available).*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Máy chủ Web EC2 không thể kết nối tới RDS Endpoint (Timeout):* Chạy lệnh `mysql -h <rds-endpoint> -u admin -p` bị treo và timeout. Nguyên nhân: Quên gắn máy chủ EC2 vào đúng `ec2-sg` hoặc DB Subnet Group bị cấu hình thiếu một Subnet trong dải định tuyến. Cách xử lý: Kiểm tra lại Security Group của cả EC2 và RDS, kiểm tra Routing Table của Private Subnet đảm bảo lưu lượng nội bộ VPC `10.0.0.0/16` được lưu thông.

---

#### 📌 Thứ 6 (02/10/2026) - Tổng kết tuần 3, Hoàn thiện Worklog & Nộp Project Proposal

* **Ta học được những gì hôm nay?**
  * **Tổng kết toàn diện 3 tuần thực tập đầu tiên:** Hệ thống hóa trọn vẹn lộ trình học tập nền tảng: từ dịch vụ cốt lõi (IAM, VPC, EC2, S3) ➔ Tối ưu hóa Well-Architected (Lambda, KMS, WAF, Fargate, Savings Plans) ➔ Hiện đại hóa ứng dụng và CSDL quan hệ Amazon RDS Multi-AZ.
  * **Đóng gói báo cáo bài thực hành 1.3.1:** Hoàn thiện bài viết chi tiết song ngữ [1.3.1. Thực hành triển khai Amazon RDS](1.3.1-amazon-rds/), đồng bộ 10 hình ảnh sơ đồ kiến trúc, bảng thông số và kiểm toán dọn dẹp môi trường.
  * **Chính thức hoàn thiện Bản đề xuất dự án (Project Proposal):** Hoàn thành tài liệu thiết kế kiến trúc kỹ thuật hệ thống, bảng phân bổ tài nguyên và dự toán chi phí chi tiết, chính thức nộp bản Đề xuất dự án thực tập lên hệ thống chương trình FCAJ để Mentor phê duyệt.
