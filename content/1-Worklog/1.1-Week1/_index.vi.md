---
title: "Tuần 1"
date: 2026-09-14
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---


### Mục tiêu tuần 1:

- Làm quen với hệ sinh thái điện toán đám mây và các dịch vụ cơ sở hạ tầng cốt lõi của AWS theo phân hệ **Explore AWS Services** trên lộ trình [The First Cloud Journey](https://cloudjourney.awsfcaj.com/).
- Nắm vững nguyên tắc quản trị ngân sách chi phí ban đầu (**AWS Budgets**) và thiết lập bảo mật định danh theo nguyên tắc đặc quyền tối thiểu (**AWS IAM**).
- Tự tay thiết kế và triển khai nền tảng mạng cô lập (**Amazon VPC**), vận hành máy chủ điện toán đám mây (**Amazon EC2**) và lưu trữ đối tượng kết hợp website tĩnh (**Amazon S3**).
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức tuần đầu, hoàn thiện hồ sơ Worklog và nghiên cứu ý tưởng Đề xuất dự án thực tập (**Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Quản trị chi phí & Bảo mật định danh:** <br>- Thiết lập tài khoản & cấu hình cảnh báo ngân sách với [AWS Budgets (000007)](https://000007.awsfcaj.com). <br>- Quản lý định danh và phân quyền truy cập với [AWS IAM (000002)](https://000002.awsfcaj.com). <br>- Kích hoạt xác thực đa yếu tố (MFA) bảo vệ tài khoản quản trị. | 14/09/2026 | 14/09/2026 | [000007](https://000007.awsfcaj.com) & [000002](https://000002.awsfcaj.com) |
| **Thứ 3** | **Hạ tầng mạng cốt lõi (Networking Essentials):** <br>- Khởi tạo mạng đám mây cô lập với [Amazon VPC (000003)](https://000003.awsfcaj.com) (Subnets, Route Tables, Internet Gateway). <br>- Phân tách rõ ràng giữa Public Subnet (Internet-facing) và Private Subnet (CSDL/Backend). | 15/09/2026 | 15/09/2026 | [Amazon VPC Workshop (000003)](https://000003.awsfcaj.com) |
| **Thứ 4** | **Điện toán đám mây (Compute Basics):** <br>- Khởi chạy và cấu hình máy chủ ảo với [Amazon EC2 (000004)](https://000004.awsfcaj.com). <br>- Cấu hình Security Groups, Key Pair, kết nối SSH từ máy cá nhân và cài đặt web server. | 16/09/2026 | 16/09/2026 | [Amazon EC2 Workshop (000004)](https://000004.awsfcaj.com) |
| **Thứ 5** | **Lưu trữ đối tượng & Web tĩnh (Object Storage):** <br>- Khởi tạo S3 Bucket, lưu trữ đối tượng và phân loại Storage Classes với [Amazon S3 (000057)](https://000057.awsfcaj.com). <br>- Cấu hình Static Website Hosting và thiết lập Bucket Policy cho phép người dùng đọc công khai. | 17/09/2026 | 17/09/2026 | [Amazon S3 Workshop (000057)](https://000057.awsfcaj.com) |
| **Thứ 6** | **Tổng kết tuần 1, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa lại toàn bộ dịch vụ cốt lõi đã học trong tuần (IAM, VPC, EC2, S3). <br>- **Làm Worklog:** Soạn thảo, chuẩn hóa bài báo cáo Worklog Tuần 1 và kiểm toán dọn dẹp tài nguyên. <br>- **Làm Project:** Nghiên cứu ý tưởng, phân tích yêu cầu kỹ thuật cho Bản đề xuất dự án (Project Proposal). | 18/09/2026 | 18/09/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (14/09/2026) - Quản trị chi phí ban đầu (AWS Budgets) & Bảo mật định danh (AWS IAM)

* **Ta học được những gì hôm nay?**
  * **Kiểm soát chi phí đám mây với AWS Budgets:**
    * Hiểu rõ rủi ro "bỏng túi" (Bill Shock) khi làm việc trên đám mây nếu để tài nguyên nhàn rỗi hoặc cấu hình sai.
    * Khởi tạo ngân sách chi tiêu hàng tháng (Monthly Cost Budget) với mức hạn ngạch tối đa $10.00.
    * Cấu hình 2 ngưỡng cảnh báo tự động: Ngưỡng thực tế 80% ($8.00) và Ngưỡng dự báo 100% ($10.00), tự động gửi email cảnh báo về hộp thư cá nhân khi chi phí chạm mốc.
  * **Bảo mật truy cập với AWS IAM:**
    * Tuân thủ nguyên tắc cốt lõi: Khóa tài khoản Root sau khi thiết lập ban đầu và tuyệt đối không dùng Root Account cho các tác vụ hàng ngày.
    * Khởi tạo IAM User riêng biệt `admin-dev` dành cho công việc thực hành kỹ thuật.
    * Phân quyền thông qua IAM User Groups thay vì gán quyền trực tiếp vào từng user, đính kèm AWS Managed Policy `AdministratorAccess` (hoặc các chính sách chuyên biệt theo nguyên tắc đặc quyền tối thiểu - Least Privilege).
    * Thiết lập chính sách mật khẩu mạnh (Password Policy: tối thiểu 12 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt).
    * Kích hoạt xác thực đa yếu tố (Virtual Multi-Factor Authentication - MFA) trên ứng dụng Google Authenticator cho cả Root Account và IAM User.

![IAM Access Architecture](/images/1-Worklog/1.1-Week1/iam-access-architecture.png)
*Hình 1.1.1: Mô hình quản trị định danh IAM phân quyền kiểm soát truy cập tài nguyên an toàn theo đặc quyền tối thiểu.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi không nhận được email kích hoạt cảnh báo ngân sách:* Nhập sai định dạng địa chỉ hộp thư trong phần SNS notification. Cách xử lý: Kiểm tra lại cấu hình thông báo trên giao diện AWS Budgets, nhập đúng địa chỉ email và xác nhận liên kết Subscription trong hộp thư Gmail.
  * *Rủi ro quên mã MFA khi thiết lập lại điện thoại:* Lưu ý bài học kinh nghiệm sao lưu chuỗi khóa khôi phục (Recovery Seed Key) của MFA tại nơi bảo mật an toàn để tránh nguy cơ mất quyền truy cập tài khoản.

---

#### 📌 Thứ 3 (15/09/2026) - Thiết lập hạ tầng mạng cô lập với Amazon VPC

* **Ta học được những gì hôm nay?**
  * **Kiến trúc mạng riêng ảo Amazon VPC:**
    * Hiểu rõ cách phân chia dải địa chỉ mạng CIDR (Classless Inter-Domain Routing). Khởi tạo VPC `fcaj-vpc` với dải mạng `10.0.0.0/16` (cung cấp 65.536 địa chỉ IP riêng).
    * Phân tách 2 vùng mạng độc lập trải rộng trên 2 Availability Zones (`us-east-1a` và `us-east-1b`):
      * *Public Subnets:* `10.0.1.0/24` (AZ-a) và `10.0.2.0/24` (AZ-b) dành cho các thành phần giao tiếp Internet (Load Balancer, Web Server). Bật tính năng `Enable auto-assign public IPv4 address`.
      * *Private Subnets:* `10.0.10.0/24` (AZ-a) và `10.0.20.0/24` (AZ-b) dành cho cơ sở dữ liệu và ứng dụng nội bộ, không có đường định tuyến trực tiếp ra Internet.
  * **Định tuyến lưu lượng mạng với Internet Gateway & Route Tables:**
    * Khởi tạo Internet Gateway `fcaj-igw` và gắn (Attach) vào VPC `fcaj-vpc`.
    * Tạo `Public-Route-Table`, thêm dòng route mặc định `0.0.0.0/0` trỏ tới `fcaj-igw` và liên kết với 2 Public Subnets.
    * Tạo `Private-Route-Table` chỉ chứa tuyến đường nội bộ `10.0.0.0/16 local`, đảm bảo tài nguyên trong Private Subnet hoàn toàn cô lập khỏi Internet.

![VPC Resource Map](/images/1-Worklog/1.1-Week1/vpc-resource-map.png)
*Hình 1.1.2: Bản đồ tài nguyên mạng Amazon VPC với hệ thống Subnets đa vùng sẵn sàng và Internet Gateway kết nối thành công.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Máy ảo trong Public Subnet không nhận được Public IP:* Khi bật máy ảo, chỉ thấy có Private IP mà không có Public IPv4. Nguyên nhân: Mặc định Subnet mới tạo chưa bật tính năng tự cấp IP công khai. Cách xử lý: Vào mục `Subnets` ➔ Chọn Public Subnet ➔ `Actions` ➔ `Edit subnet settings` ➔ Đánh dấu chọn `Enable auto-assign public IPv4 address`.

---

#### 📌 Thứ 4 (16/09/2026) - Vận hành máy chủ ảo điện toán đám mây Amazon EC2

* **Ta học được những gì hôm nay?**
  * **Vòng đời và cấu hình máy chủ ảo Amazon EC2:**
    * Lựa chọn hệ điều hành **Amazon Linux 2023 AMI** tối ưu hóa cho phần cứng AWS Nitro.
    * Chọn dòng máy ảo `t2.micro` (1 vCPU, 1GB RAM) thuộc diện miễn phí (Free Tier eligible).
    * Tạo cặp khóa xác thực RSA `fcaj-keypair.pem` và tải về máy tính cá nhân để thực hiện kết nối SSH an toàn.
  * **Thiết lập tường lửa ảo Security Group:**
    * Tạo `web-server-sg` gắn vào VPC `fcaj-vpc`.
    * Cấu hình Inbound Rules:
      * Port `22` (SSH): Giới hạn nghiêm ngặt từ `My IP` (địa chỉ IP mạng nhà), không mở `0.0.0.0/0` để ngăn chặn tấn công dò mật khẩu (Brute-Force).
      * Port `80` (HTTP): Mở công khai `0.0.0.0/0` để người dùng Internet có thể truy cập website.
  * **Kết nối SSH và cài đặt dịch vụ:**
    ```bash
    chmod 400 fcaj-keypair.pem
    ssh -i "fcaj-keypair.pem" ec2-user@<EC2-PUBLIC-IP>
    sudo dnf update -y
    sudo dnf install -y httpd
    sudo systemctl start httpd
    sudo systemctl enable httpd
    echo "<h1>Welcome to AWS First Cloud Journey - EC2 Running!</h1>" | sudo tee /var/www/html/index.html
    ```

![EC2 Launch Success](/images/1-Worklog/1.1-Week1/ec2-launch-success.png)
*Hình 1.1.3: Máy chủ ảo Amazon EC2 khởi chạy thành công ở trạng thái Running trên nền tảng AWS.*

* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi phân quyền file khóa SSH (`Permissions 0644 are too open`):* Lệnh SSH bị từ chối kết nối. Nguyên nhân: Trên Linux/macOS, tệp key `.pem` có quyền quá rộng khiến SSH coi là không an toàn. Cách xử lý: Chạy lệnh `chmod 400 fcaj-keypair.pem` (trên Windows PowerShell dùng công cụ chỉnh Permission loại bỏ quyền kế thừa).

---

#### 📌 Thứ 5 (17/09/2026) - Lưu trữ đối tượng & Hosting web tĩnh với Amazon S3

* **Ta học được những gì hôm nay?**
  * **Cơ chế lưu trữ đối tượng đám mây với Amazon S3:**
    * Hiểu nguyên lý không gian tên toàn cầu (**Global Namespace**): Tên bucket phải là duy nhất trên toàn thế giới và tuân thủ chuẩn ký danh DNS (chữ thường, không chứa ký tự đặc biệt). Tạo bucket `fcaj-static-web-887086382708`.
    * Tìm hiểu các lớp lưu trữ (Storage Classes) nhằm tối ưu chi phí: S3 Standard (truy cập thường xuyên), S3 Standard-IA (truy cập ít nhưng cần độ trễ thấp), S3 Glacier Flexible Retrieval (lưu trữ dài hạn chi phí cực thấp).
    * Bật tính năng **Bucket Versioning** giúp bảo vệ tệp tin trước nguy cơ bị ghi đè hoặc xóa nhầm.
  * **Triển khai Static Website Hosting:**
    * Kích hoạt tính năng `Static website hosting`, chỉ định Index document là `index.html` và Error document là `error.html`.
    * Tắt tính năng chặn truy cập công khai (**Block Public Access**) cho riêng bucket web tĩnh này.
    * Soạn thảo chính sách Bucket Policy cấp quyền đọc công khai cho mọi người dùng:
      ```json
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::fcaj-static-web-887086382708/*"
          }
        ]
      }
      ```
    * Truy cập đường dẫn endpoint website tĩnh `http://fcaj-static-web-887086382708.s3-website-us-east-1.amazonaws.com` thành công.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi `403 Forbidden` khi truy cập trang web S3:* Sau khi bật Static Website Hosting, mở link endpoint vẫn báo lỗi 403. Nguyên nhân: Quên cấu hình Bucket Policy cấp quyền `s3:GetObject` hoặc chưa tắt hoàn toàn 4 nút kiểm trong `Block Public Access`. Cách xử lý: Cập nhật Bucket Policy chuẩn JSON và xác nhận tắt BPA thành công.

---

#### 📌 Thứ 6 (18/09/2026) - Tổng kết tuần 1, Viết Worklog & Nghiên cứu Đề xuất Đồ án

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa 4 trụ cột cơ sở hạ tầng nền tảng:**
    * **Định danh (IAM):** Cổng bảo vệ vòng ngoài cùng, xác định *Ai* được làm *Cái gì*.
    * **Mạng (VPC):** Hạ tầng cách ly và định tuyến giao thông dữ liệu.
    * **Điện toán (EC2):** Khối xử lý tính toán máy chủ cho các ứng dụng.
    * **Lưu trữ (S3):** Khối lưu trữ đối tượng bền bỉ với độ sẵn sàng đạt 99.999999999% (11 số 9).
  * **Thực hành vệ sinh tài nguyên (Resource Teardown):** Dừng (Stop) máy chủ EC2 khi không sử dụng để tiết kiệm số giờ chạy Free Tier (750 giờ/tháng), xóa các Elastic IP chưa gán để tránh bị tính phí duy trì IP tĩnh.
  * **Nghiên cứu Đề xuất Đồ án (Project Proposal):** Bắt đầu định hình bài toán xây dựng hệ thống web hai tầng (Two-Tier Web Application) tích hợp khả năng tự động co giãn và cơ sở dữ liệu phân tán trên AWS.


