---
title: "Worklog Tuần 11"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 11:

- Nắm vững các kỹ thuật đóng gói ứng dụng bằng **Docker** theo chuẩn mực tối ưu hóa dung lượng (Multi-stage builds) và tăng cường bảo mật (Non-root user).
- Quản lý kho lưu trữ container doanh nghiệp an toàn với **Amazon Elastic Container Registry (ECR)** (Cấu hình chính sách dọn dẹp vòng đời Lifecycle Policy và quét lỗ hổng tự động Enhanced Scanning).
- Triển khai, vận hành và tự động co giãn kiến trúc Microservices phi máy chủ bằng **Amazon Elastic Container Service (Amazon ECS)** trên nền tảng **AWS Fargate** (Workshop 000067).
- Tiếp cận kiến trúc điều phối cụm Kubernetes cấp doanh nghiệp với **Amazon Elastic Kubernetes Service (Amazon EKS)** (Workshop 000126), quản trị tài nguyên qua `kubectl` và `eksctl`.
- Khám phá mô hình triển khai container siêu tốc với **AWS App Runner** và nền tảng đám mây mở **Red Hat OpenShift on AWS (ROSA)** (Workshop 000071).
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và đóng gói toàn bộ mã nguồn Backend của đồ án (**Capstone Project Proposal**) thành Docker image sẵn sàng triển khai trên ECS Fargate.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Đóng gói Docker chuẩn mực & Quản lý image với Amazon ECR:** <br>- Viết Dockerfile đa giai đoạn (Multi-stage build) giúp giảm 70% kích thước image. <br>- Khởi tạo Private Repository trên Amazon ECR và cấu hình phân quyền truy cập. <br>- Xác thực Docker CLI với ECR registry, gắn tag và đẩy (push) image lên kho lưu trữ. | 23/11/2026 | 23/11/2026 | [Cloud Journey - Containers](https://cloudjourney.awsfcaj.com/5-container/) |
| **Thứ 3** | **Điều phối Microservices không máy chủ với Amazon ECS Fargate:** <br>- Khởi tạo ECS Cluster chế độ Networking Only (AWS Fargate). <br>- Định nghĩa Task Definition (CPU/RAM, Port Mapping, IAM Task Execution Role, CloudWatch Logs). <br>- Khởi tạo ECS Service liên kết Application Load Balancer và cấu hình Service Auto Scaling. | 24/11/2026 | 24/11/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Thứ 4** | **Khởi tạo và Quản trị cụm Kubernetes với Amazon EKS:** <br>- Sử dụng công cụ dòng lệnh `eksctl` tạo cụm Amazon EKS và Managed Node Groups. <br>- Cấu hình ngữ cảnh `kubeconfig` và kiểm tra trạng thái nodes bằng `kubectl get nodes`. <br>- Triển khai các đối tượng Kubernetes chuẩn: Deployment, ClusterIP Service, Ingress và HPA. | 25/11/2026 | 25/11/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thứ 5** | **Triển khai ứng dụng nhanh với AWS App Runner & ROSA:** <br>- Triển khai ứng dụng web trực tiếp từ mã nguồn GitHub/ECR qua dịch vụ AWS App Runner. <br>- Tìm hiểu kiến trúc tích hợp sâu của Red Hat OpenShift on AWS (ROSA). <br>- Đánh giá so sánh chi phí, độ phức tạp quản trị giữa ECS, EKS, App Runner và ROSA. | 26/11/2026 | 26/11/2026 | [ROSA Workshop (000071)](https://000071.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 11, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức ECR, ECS Fargate, EKS, App Runner và ROSA. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 11 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Đóng gói và đẩy Docker image của Capstone Project lên Amazon ECR và cấu hình ECS Task. | 27/11/2026 | 27/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 11:

#### 📌 Kết quả Thứ 2 (23/11/2026) - Đóng gói Docker & Quản lý image với Amazon ECR:
* **Tối ưu hóa kích thước Image:** Áp dụng kỹ thuật Multi-stage build loại bỏ hoàn toàn các gói công cụ biên dịch (build tools) khỏi môi trường chạy thực tế (runtime), giúp giảm dung lượng image từ 850MB xuống còn 75MB.
* **Bảo mật chuỗi cung ứng phần mềm:** Kích hoạt tính năng quét lỗ hổng bảo mật tự động trên Amazon ECR khi có ảnh mới được đẩy lên (Scan on Push), phát hiện và ngăn chặn kịp thời các thư viện chứa mã độc theo cơ sở dữ liệu CVE.

#### 📌 Kết quả Thứ 3 (24/11/2026) - Vận hành Microservices trên ECS Fargate:
* **Vận hành không cần quản lý máy chủ:** Khởi chạy các container độc lập trên hạ tầng phi máy chủ AWS Fargate, loại bỏ hoàn toàn gánh nặng nâng cấp hệ điều hành máy chủ chủ (Host OS patching).
* **Cập nhật không gián đoạn dịch vụ (Zero-Downtime Deployment):** Cấu hình chiến lược triển khai Rolling Update với `Minimum healthy percent = 100` và `Maximum percent = 200`, đảm bảo hệ thống luôn sẵn sàng phục vụ người dùng trong suốt quá trình phát hành phiên bản mới.

#### 📌 Kết quả Thứ 4 (25/11/2026) - Quản trị cụm Kubernetes với Amazon EKS:
* **Chuẩn hóa hạ tầng điều phối:** Triển khai thành công cụm Kubernetes với phiên bản v1.29 trên Amazon EKS gồm 2 worker nodes thông qua cấu hình khai báo YAML với công cụ `eksctl`.
* **Tự động co giãn theo tải thực tế:** Thiết lập Horizontal Pod Autoscaler (HPA) theo dõi mức sử dụng CPU/Memory, tự động nhân bản số lượng pods từ 2 lên tối đa 10 pods khi tải hệ thống vượt ngưỡng 70%.

#### 📌 Kết quả Thứ 5 (26/11/2026) - Ứng dụng triển khai nhanh với AWS App Runner:
* **Rút ngắn thời gian phát hành:** Trải nghiệm tốc độ đóng gói và phát hành ứng dụng web ra Internet chỉ trong vòng 3 phút với AWS App Runner mà không cần phải viết cấu hình Kubernetes hay thiết lập Load Balancer thủ công.
* **Tự động cấp phát chứng chỉ SSL/TLS:** Dịch vụ tự động cấp phát domain HTTPS miễn phí kèm cơ chế Auto Scaling thông minh dựa trên số lượng kết nối đồng thời.
