---
title: "Tuần 11"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 11:

- Nắm vững các kỹ thuật đóng gói ứng dụng bằng **Docker** theo chuẩn mực tối ưu hóa dung lượng (Multi-stage builds) và tăng cường bảo mật chuỗi cung ứng phần mềm.
- Quản lý kho lưu trữ container doanh nghiệp an toàn với **Amazon Elastic Container Registry (ECR)** (Chính sách vòng đời Lifecycle Policies và quét lỗ hổng tự động Enhanced Scanning theo chuẩn CVE).
- Triển khai, vận hành và tự động co giãn kiến trúc Microservices phi máy chủ bằng **Amazon Elastic Container Service (Amazon ECS)** trên nền tảng **AWS Fargate** (Workshop 000067).
- Dành **2 ngày chuyên sâu (Thứ 4 & Thứ 5)** làm chủ toàn diện hệ sinh thái điều phối container tiêu chuẩn doanh nghiệp **Amazon Elastic Kubernetes Service (Amazon EKS)** (Workshop 000126): từ khởi tạo cụm với `eksctl`, phân quyền IAM Roles for Service Accounts (IRSA) đến triển khai Ingress Controller và tự động co giãn với Horizontal Pod Autoscaler (HPA).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và đóng gói toàn bộ mã nguồn Backend của đồ án (**Capstone Project Proposal**) thành Docker image sẵn sàng triển khai trên ECS Fargate / EKS.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Đóng gói Docker chuẩn mực & Quản lý image với Amazon ECR:** <br>- Viết Dockerfile đa giai đoạn (Multi-stage build) giúp giảm 70% kích thước image. <br>- Áp dụng các nguyên tắc bảo mật: Non-root user, Alpine/Distroless base images. <br>- Khởi tạo Private ECR Repository, xác thực Docker CLI và đẩy (push) image. <br>- Cấu hình Lifecycle Policy dọn dẹp image cũ và kích hoạt Scan on Push. | 23/11/2026 | 23/11/2026 | [Cloud Journey - Containers](https://cloudjourney.awsfcaj.com/5-container/) |
| **Thứ 3** | **Điều phối Microservices không máy chủ với Amazon ECS Fargate:** <br>- Khởi tạo ECS Cluster chế độ Networking Only (AWS Fargate). <br>- Định nghĩa Task Definition (CPU/RAM, Port Mapping, IAM Task Execution Role, CloudWatch Logs). <br>- Khởi tạo ECS Service liên kết Application Load Balancer và cấu hình Service Auto Scaling. <br>- Kiểm thử chiến lược triển khai cập nhật phiên bản không gián đoạn (Rolling Update). | 24/11/2026 | 24/11/2026 | [ECS Workshop (000067)](https://000067.awsfcaj.com/) |
| **Thứ 4** | **Amazon EKS (Phần 1) - Khởi tạo cụm Kubernetes & Quản trị hạ tầng:** <br>- Sử dụng công cụ dòng lệnh `eksctl` tạo cụm Amazon EKS v1.29 và Managed Node Groups. <br>- Cấu hình ngữ cảnh `kubeconfig` và kiểm tra trạng thái nodes bằng `kubectl get nodes`. <br>- Thiết lập IAM OIDC Provider và cơ chế phân quyền IAM Roles for Service Accounts (IRSA). <br>- Triển khai các đối tượng K8s cơ bản: Namespaces, ConfigMaps, Secrets và Pods. | 25/11/2026 | 25/11/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thứ 5** | **Amazon EKS (Phần 2) - Triển khai sản xuất: Ingress Controller & HPA Scaling:** <br>- Triển khai Kubernetes Deployment và ClusterIP Service cho ứng dụng web. <br>- Cài đặt AWS Load Balancer Controller thông qua Helm Chart để tự động cấp phát ALB qua Ingress. <br>- Cài đặt Kubernetes Metrics Server thu thập chỉ số CPU/Memory của từng Pod. <br>- Thiết lập Horizontal Pod Autoscaler (HPA) tự động co giãn pods từ 2 lên 10 khi CPU vượt 70%. | 26/11/2026 | 26/11/2026 | [Amazon EKS Workshop (000126)](https://000126.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 11, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Docker, ECR, ECS Fargate và Kubernetes EKS. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 11 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Đóng gói và đẩy Docker image của Capstone Project lên Amazon ECR và cấu hình ECS/EKS Task. | 27/11/2026 | 27/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (23/11/2026) - Đóng gói Docker chuẩn mực & Quản trị kho ảnh Amazon ECR

* **Ta học được những gì hôm nay?**
  * **Kỹ thuật đóng gói tối ưu với Multi-Stage Builds:** Chia quy trình Dockerfile thành 2 giai đoạn: `builder stage` (chứa toàn bộ công cụ Node.js/Go/Maven để biên dịch mã nguồn) và `runner stage` (chỉ sao chép artifact nhị phân hoặc thư mục build vào image gốc tối giản `alpine:3.19` hoặc `distroless`). Kết quả: Giảm dung lượng image từ 850MB xuống còn 75MB, giúp thời gian tải và khởi chạy container nhanh gấp 5 lần.
  * **Tăng cường bảo mật Container:** Khai báo chỉ thị `USER appuser` trong Dockerfile để chặn ứng dụng chạy với quyền `root`, ngăn chặn kẻ tấn công leo thang đặc quyền ra máy chủ host khi container bị khai thác lỗ hổng.
  * **Quản trị kho ảnh bảo mật với Amazon ECR:**
    * Tạo Private Repository `fcaj/backend-api`.
    * Đăng nhập xác thực Docker CLI với ECR Registry token:
      ```bash
      aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 887086382708.dkr.ecr.us-east-1.amazonaws.com
      docker build -t fcaj/backend-api:v1.0 .
      docker tag fcaj/backend-api:v1.0 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
      docker push 887086382708.dkr.ecr.us-east-1.amazonaws.com/fcaj/backend-api:v1.0
      ```
    * Cấu hình ECR Lifecycle Policy tự động xóa các image không gắn tag (`untagged`) sau 14 ngày và chỉ giữ lại 10 phiên bản mới nhất.
    * Kích hoạt tính năng `Scan on Push` phát hiện ngay lập tức 0 lỗ hổng nghiêm trọng (CRITICAL) và 1 cảnh báo mức trung bình (MEDIUM) trên image vừa đẩy lên.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi xác thực Docker Login bị từ chối:* Lệnh `docker login` trả về lỗi `denied: Your authorization token has expired`. Nguyên nhân: Token xác thực ECR chỉ có hiệu lực tối đa trong 12 giờ. Cách xử lý: Tái tạo token mới và truyền pipe trực tiếp vào lệnh login như cú pháp ở trên.

---

#### 📌 Thứ 3 (24/11/2026) - Điều phối Microservices không máy chủ với Amazon ECS Fargate

* **Ta học được những gì hôm nay?**
  * **Vận hành Container không máy chủ (Serverless Containers):** Hiểu rõ sự khác biệt giữa ECS EC2 Launch Type (phải tự quản lý cụm máy ảo EC2) và AWS Fargate (AWS quản lý hoàn toàn hạ tầng, chỉ định nghĩa CPU và Memory cho container, tính phí chính xác theo tài nguyên sử dụng thực tế).
  * **Cấu trúc Task Definition chuẩn sản xuất:**
    * Phân bổ tài nguyên: `0.5 vCPU` và `1GB RAM`.
    * Cổng dịch vụ (Port Mapping): Container port `8080`.
    * Phân tách IAM Roles rõ ràng: `Task Execution Role` cấp quyền cho ECS Agent kéo image từ ECR và ghi log vào CloudWatch Logs (`/ecs/backend-api`), trong khi `Task Role` cấp quyền cho chính ứng dụng bên trong container truy cập DynamoDB/S3.
  * **Vận hành ECS Service & Cân bằng tải:** Tạo ECS Service gắn đằng sau Application Load Balancer (ALB), cấu hình Health Check đường dẫn `/healthz`.
  * **Cập nhật không gián đoạn dịch vụ (Zero-Downtime Rolling Update):** Cấu hình `Minimum healthy percent = 100%` và `Maximum percent = 200%`. Khi đẩy bản cập nhật v1.1, ECS tự động khởi chạy các Task mới, chờ ALB kiểm tra sức khỏe thành công (Healthy) rồi mới nhẹ nhàng dừng các Task cũ.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Container liên tục khởi động lại (CrashLoop / CannotPullContainerError):* Task chuyển sang trạng thái `STOPPED` ngay sau khi bật. Nguyên nhân: ECS Task nằm trong Private Subnet không có route ra Internet để kéo image từ ECR Public/Private và thiếu VPC Endpoints cho ECR (`ecr.api`, `ecr.dkr`, `s3`). Cách xử lý: Bổ sung NAT Gateway hoặc cấu hình VPC Endpoints cho ECR và S3.

---

#### 📌 Thứ 4 (25/11/2026) - Amazon EKS (Phần 1): Khởi tạo cụm Kubernetes & Quản trị hạ tầng

* **Ta học được những gì hôm nay?**
  * **Kiến trúc cụm Kubernetes cấp doanh nghiệp:** Tìm hiểu cách Amazon EKS quản lý Control Plane tự động co giãn trải rộng trên 3 Availability Zones, đảm bảo tính sẵn sàng đạt chuẩn SLA 99.95%.
  * **Khởi tạo cụm với công cụ chuẩn mực `eksctl`:** Viết file khai báo cấu hình cụm `cluster-config.yaml` và thực thi:
    ```yaml
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    metadata:
      name: fcaj-eks-cluster
      region: us-east-1
      version: "1.29"
    managedNodeGroups:
      - name: standard-workers
        instanceType: t3.medium
        desiredCapacity: 2
        minSize: 1
        maxSize: 4
        privateNetworking: true
    ```
    ```bash
    eksctl create cluster -f cluster-config.yaml
    kubectl get nodes -o wide
    ```
  * **Cơ chế bảo mật IAM Roles for Service Accounts (IRSA):** Loại bỏ việc gán quyền thô cấp Node Group (Node IAM Role) khiến mọi pod đều có quyền quá lớn. Thiết lập IAM OIDC Provider cho EKS, cho phép gắn trực tiếp IAM Role vào từng Kubernetes ServiceAccount chuyên biệt theo nguyên tắc đặc quyền tối thiểu.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi phân quyền kubectl (Unauthorized / Access Denied):* Sau khi đồng nghiệp tạo cụm, máy khác chạy `kubectl` bị báo `error: You must be logged in to the server (Unauthorized)`. Nguyên nhân: Mặc định chỉ có IAM Identity tạo cụm mới có quyền quản trị trong Kubernetes RBAC. Cách xử lý: Cập nhật EKS Access Entries (tính năng mới của EKS) hoặc chỉnh sửa `aws-auth` ConfigMap trong namespace `kube-system` để bổ sung IAM Role của người dùng.

---

#### 📌 Thứ 5 (26/11/2026) - Amazon EKS (Phần 2): Triển khai sản xuất, Ingress & HPA Scaling

* **Ta học được những gì hôm nay?**
  * **Triển khai ứng dụng sản xuất (Production Deployment):** Viết manifest `deployment.yaml` định nghĩa 2 bản sao (replicas), cấu hình Liveness Probe và Readiness Probe kiểm tra cổng `8080/healthz`, cùng cấu hình giới hạn tài nguyên `resources: requests/limits`.
  * **Cài đặt AWS Load Balancer Controller với Helm:** Thay vì dùng Service kiểu `LoadBalancer` truyền thống (cấp phát Classic Load Balancer lỗi thời cho mỗi service), cài đặt **AWS Load Balancer Controller** qua Helm Chart. Controller tự động giám sát các đối tượng Ingress trong Kubernetes và tự động cấu hình Application Load Balancer (ALB) cấp doanh nghiệp, định tuyến lưu lượng theo đường dẫn (Path-based Routing).
  * **Tự động co giãn theo tải thực tế với Horizontal Pod Autoscaler (HPA):**
    * Cài đặt Kubernetes Metrics Server thu thập dữ liệu tài nguyên thời gian thực.
    * Thiết lập chính sách HPA co giãn số lượng Pods:
      ```bash
      kubectl autoscale deployment web-backend --cpu-percent=70 --min=2 --max=10
      kubectl get hpa
      ```
    * Chạy kịch bản kiểm thử tải liên tục bằng công cụ `hey`, quan sát số lượng Pods tự động nhân bản từ 2 pods lên 6 pods khi CPU chạm ngưỡng 85% và tự động co lại sau 5 phút tải lắng xuống.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Ingress không cấp phát được ALB (Address bị trống):* Lệnh `kubectl get ingress` hiển thị cột `ADDRESS` trống rỗng. Phân tích log controller `kubectl logs -n kube-system deployment.apps/aws-load-balancer-controller` phát hiện lỗi: Các Subnets trong VPC thiếu thẻ Tag bắt buộc. Cách xử lý: Gắn Tag `kubernetes.io/role/elb = 1` cho Public Subnets và `kubernetes.io/role/internal-elb = 1` cho Private Subnets.

---

#### 📌 Thứ 6 (27/11/2026) - Tổng kết Tuần 11, Viết Worklog & Đóng gói Container Đồ án

* **Ta học được những gì hôm nay?**
  * **So sánh và lựa chọn nền tảng Container:** Đúc kết bảng ma trận so sánh giữa ECS Fargate (đơn giản, dễ vận hành, phù hợp Microservices vừa và nhỏ) và Amazon EKS (hệ sinh thái phong phú, linh hoạt, chuẩn mở đa đám mây nhưng chi phí quản trị cao hơn).
  * **Quy trình dọn dẹp cụm EKS hoàn chỉnh:** Xóa sạch các Ingress để ALB được giải phóng trước, sau đó thực thi lệnh `eksctl delete cluster -f cluster-config.yaml` để xóa toàn bộ Node Groups và CloudFormation stacks liên quan, tránh phát sinh chi phí vận hành $0.10/giờ cho EKS Control Plane.
  * **Đóng gói Capstone Project thành Container chuẩn mực:** Hoàn thiện Dockerfile đa giai đoạn cho toàn bộ backend dự án tốt nghiệp, đẩy lên ECR và viết mẫu Task Definition sẵn sàng cho ngày bảo vệ đồ án.

