---
title: "Tuần 10"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 10:

- Làm chủ kiến trúc **Hướng sự kiện phi máy chủ (Serverless & Event-Driven Architecture)** với **Amazon API Gateway**, **Amazon SQS** (Workshop 000078), **Amazon SNS**, **Amazon EventBridge** và **AWS Step Functions**.
- Chuẩn hóa đóng gói container tối ưu với **Docker Multi-Stage Builds**, quản trị kho ảnh bảo mật **Amazon ECR** và vận hành microservices phi máy chủ trên **Amazon ECS Fargate** (Workshop 000067).
- Triển khai và tự động co giãn ứng dụng trên cụm Kubernetes quản lý **Amazon EKS** (Workshop 000126) với `eksctl`, IRSA, AWS Load Balancer Controller và Horizontal Pod Autoscaler (HPA).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và tích hợp kiến trúc bất đồng bộ + container hóa vào đồ án (**Capstone Project**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Amazon API Gateway & Phân tách tải với Amazon SQS:** <br>- So sánh REST API vs HTTP API; cấu hình CORS, Lambda Custom Authorizer (JWT) và Token Bucket Throttling. <br>- Triển khai SQS Standard Queue vs FIFO Queue, tối ưu chi phí với Long Polling (`20s`). <br>- Thiết lập Visibility Timeout và Dead-Letter Queue (DLQ) kèm Redrive Policy cô lập bản tin lỗi. | 16/11/2026 | 16/11/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Thứ 3** | **Phát tin đa hướng (SNS/EventBridge) & Điều phối AWS Step Functions:** <br>- Xây dựng mô hình Fanout (1 SNS Topic đẩy song song tới nhiều SQS Queues). <br>- Thiết lập Amazon EventBridge Event Bus và quy tắc lọc JSON (Event Pattern Filtering). <br>- Thiết kế State Machine trên Workflow Studio kết hợp Task, Choice, Parallel và chiến lược Retry/Catch. | 17/11/2026 | 17/11/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thứ 4** | **Docker Multi-Stage, Amazon ECR & Amazon ECS Fargate:** <br>- Tối ưu Dockerfile bằng Multi-Stage Build và chạy tiến trình với Non-root user. <br>- Đẩy image lên Private ECR, cấu hình Lifecycle Policy và quét lỗ hổng CVE (Scan on Push). <br>- Triển khai ECS Service trên AWS Fargate sau ALB và kiểm thử Zero-Downtime Rolling Update. | 18/11/2026 | 18/11/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Thứ 5** | **Điều phối Kubernetes doanh nghiệp với Amazon EKS:** <br>- Khởi tạo cụm Amazon EKS và Managed Node Groups bằng `eksctl`, cấu hình `kubeconfig`. <br>- Thiết lập IAM OIDC Provider và phân quyền chi tiết ở mức Pod với IRSA. <br>- Cài đặt AWS Load Balancer Controller (Ingress ALB), Metrics Server và cấu hình HPA co giãn Pods tự động. | 19/11/2026 | 19/11/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 10, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến trúc Serverless EDA và Container Orchestration (ECS/EKS). <br>- **Làm Worklog:** Chuẩn hóa báo cáo Worklog Tuần 10 song ngữ và hủy cụm EKS/ECS thử nghiệm. <br>- **Làm Project:** Tích hợp hàng đợi bất đồng bộ SQS và đóng gói Docker/ECR cho Capstone Project. | 20/11/2026 | 20/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (16/11/2026) - Quản trị Amazon API Gateway & Phân tách tải với Amazon SQS

* **Ta học được những gì hôm nay?**
  * **Amazon API Gateway (REST API vs HTTP API):** HTTP API giảm độ trễ và tiết kiệm hơn 70% chi phí cho microservice nhẹ; REST API cung cấp đầy đủ Usage Plans, API Keys, WAF và Private Endpoints. Triển khai Lambda Authorizer xác thực Bearer JWT và cấu hình Rate/Burst Throttling chống quá tải backend.
  * **Phân tách hệ thống với Amazon SQS:** Phân biệt Standard Queue (thông lượng cao, *At-least-once*) và FIFO Queue (*Exactly-once*, đảm bảo thứ tự qua `MessageGroupId`). Cấu hình `ReceiveMessageWaitTimeSeconds = 20` (Long Polling), `VisibilityTimeout = 30s` và `RedrivePolicy` (`maxReceiveCount = 3`) chuyển tin nhắn hỏng sang Dead-Letter Queue (DLQ).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi CORS trên trình duyệt & Worker xử lý trùng tin nhắn:* Bật đầy đủ phương thức `OPTIONS` cùng header `Access-Control-Allow-*` trên API Gateway; dùng API `change_message_visibility` gia hạn timeout cho các tác vụ Worker kéo dài vượt 30 giây.

---

#### 📌 Thứ 3 (17/11/2026) - Phát tin Amazon SNS, EventBridge & Điều phối AWS Step Functions

* **Ta học được những gì hôm nay?**
  * **Kiến trúc Fanout với SNS & Lọc nội dung với EventBridge:** Gắn nhiều hàng đợi SQS đăng ký cùng một SNS Topic để xử lý song song các nghiệp vụ độc lập. Thiết lập quy tắc lọc JSON trên EventBridge để định tuyến sự kiện theo ngưỡng dữ liệu:
    ```json
    {
      "source": ["app.events"],
      "detail-type": ["JobSubmitted"],
      "detail": { "priority": ["HIGH"] }
    }
    ```
  * **Điều phối luồng với AWS Step Functions:** Xây dựng State Machine bằng Amazon States Language (ASL) phối hợp `Task`, `Choice`, `Parallel`, kèm khối `Retry` (`BackoffRate = 2.0`) và `Catch` để tự động phục hồi lỗi mà không nhồi logic điều phối vào mã ứng dụng.
* **Khó khăn gặp phải & Cách xử lý:**
  * *SQS không nhận được tin nhắn từ SNS & sai cấu trúc JSON giữa các State:* Bổ sung `sqs:SendMessage` cho ARN của SNS Topic trong SQS Access Policy; sử dụng `InputPath`, `ResultPath`, `OutputPath` trong Step Functions để chuẩn hóa payload truyền tiếp.

---

#### 📌 Thứ 4 (18/11/2026) - Docker Multi-Stage, Amazon ECR & Amazon ECS Fargate

* **Ta học được những gì hôm nay?**
  * **Tối ưu Docker Image & Quản trị Amazon ECR:** Áp dụng Multi-Stage Build tách biệt tầng biên dịch (`builder`) và tầng chạy tối giản (`alpine`/`distroless`) kèm `USER appuser` (non-root), giúp giảm kích thước image mạnh và hạn chế bề mặt tấn công. Cấu hình ECR Lifecycle Policy và `Scan on Push`.
    ```bash
    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 887086382708.dkr.ecr.us-east-1.amazonaws.com
    docker build -t fcaj/backend-api:v1.0 .
    docker tag fcaj/backend-api:v1.0 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
    docker push 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
    ```
  * **Vận hành Serverless Container trên Amazon ECS Fargate:** Tách bạch `Task Execution Role` (kéo ảnh ECR, đẩy log CloudWatch) và `Task Role` (quyền nghiệp vụ của ứng dụng). Cấu hình `Minimum healthy percent = 100%`, `Maximum percent = 200%` gắn sau ALB để cập nhật không gián đoạn (Zero-Downtime Rolling Update).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi `CannotPullContainerError` khi chạy Task trong Private Subnet:* Bổ sung NAT Gateway hoặc thiết lập đầy đủ VPC Endpoints (`ecr.api`, `ecr.dkr`, `s3`) để ECS Agent kéo được image nội bộ.

---

#### 📌 Thứ 5 (19/11/2026) - Điều phối Kubernetes doanh nghiệp với Amazon EKS

* **Ta học được những gì hôm nay?**
  * **Khởi tạo cụm EKS & Bảo mật IRSA:** Dùng `eksctl` tạo cụm EKS Managed Node Groups trong Private Subnets và bật IAM OIDC Provider để gán IAM Role riêng cho từng Kubernetes `ServiceAccount` (IRSA) thay vì cấp quyền rộng ở mức Node.
    ```bash
    eksctl create cluster --name fcaj-eks-cluster --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2
    kubectl autoscale deployment web-backend --cpu-percent=70 --min=2 --max=10
    ```
  * **Ingress ALB & Horizontal Pod Autoscaler (HPA):** Cài đặt **AWS Load Balancer Controller** qua Helm Chart để tự động cấp phát ALB từ Kubernetes Ingress; cài Metrics Server và kiểm thử HPA tự động tăng/giảm số lượng Pods theo mức CPU thực tế.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Ingress không sinh ra địa chỉ ALB (`ADDRESS` trống):* Gắn thẻ Subnet Tag bắt buộc `kubernetes.io/role/elb = 1` cho Public Subnets và `kubernetes.io/role/internal-elb = 1` cho Private Subnets.

---

#### 📌 Thứ 6 (20/11/2026) - Tổng kết Tuần 10, Viết Worklog & Đóng gói Đồ án

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa kiến trúc phân tán hiện đại:** Kết nối liền mạch giữa mô hình giao tiếp bất đồng bộ (API Gateway, SQS, SNS, EventBridge, Step Functions) và mô hình chạy container linh hoạt (ECR, ECS Fargate, EKS).
  * **Dọn dẹp tài nguyên có chi phí cao:** Thực thi `eksctl delete cluster` xóa cụm EKS (tránh phí Control Plane $0.10/giờ) và hủy ECS Services/ALB thử nghiệm ngay sau khi hoàn thành bài lab.
  * **Phát triển Capstone Project:** Thiết kế luồng xử lý bất đồng bộ và đóng gói mã nguồn Backend thành Docker image đẩy lên Amazon ECR.

---

### Mục tiêu cho tuần sau (Tuần 11):

* **Hồ dữ liệu & Phân tích dữ liệu lớn:** AWS Lake Formation (000035), AWS Glue ETL (Parquet), Amazon Athena (000106), Kinesis, QuickSight (000073) & Redshift.
* **Trí tuệ nhân tạo tạo sinh (Generative AI) & MLOps:** Amazon Bedrock Foundation Models, RAG Knowledge Bases, Bedrock Agents & Amazon SageMaker.
