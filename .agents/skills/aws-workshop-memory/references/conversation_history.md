# Conversation History & Decision Log - AWS Workshop Session

**Thời gian tạo:** 01/10/2026  
**Dự án:** AWS Workshop - Get Started with Amazon RDS (`d:\AWS\template_AWS\fcj-workshop-template-main`)

---

## 📜 1. Lịch sử Thảo luận & Yêu cầu từ Người dùng

### 🔹 Giai đoạn 1: Đọc & Phân tích tài liệu Amazon RDS Introduce

- **Yêu cầu:** Đọc và phân tích toàn bộ nội dung từ URL `https://000005.awsstudygroup.com/1-introduce/` và hình ảnh sơ đồ kiến trúc `arc.png`.
- **Kết quả:**
  - **Lý thuyết RDS:** Managed Relational Database Service cho OLTP. Hỗ trợ Aurora, MySQL, PostgreSQL, Oracle, SQL Server, MariaDB. Các tính năng cốt lõi: Multi-AZ (HA/Failover), Read Replicas (Read Scaling), Auto Backup, Maintenance Window.
  - **Hình ảnh sơ đồ kiến trúc (`assets/arc.png`):**
    - AWS Region ➔ VPC ➔ 1 Availability Zone.
    - **Public Subnet:** Chứa Amazon EC2 Instance (Security Group: `ec2-rds-n`), kết nối 2 chiều với Internet Gateway.
    - **Private Subnet:** Chứa MySQL DB Instance (Security Group: `rds-ec2-n`), chỉ cho phép kết nối từ EC2 Instance.

---

### 🔹 Giai đoạn 2: Thống nhất Quy trình Làm việc & Định dạng Worklog Tuần 3

- **Quy trình:**
  - AI làm vai trò Trợ lý (Co-pilot), tạo/chỉnh sửa code/markdown.
  - Người dùng xem xét, kiểm tra và phê duyệt.
  - Chỉ tập trung làm **Week 3 Worklog (`content/1-Worklog/1.3-Week3/`)**, không đụng vào các tuần khác.
- **Quy tắc ngôn ngữ:**
  - Tiêu đề chính giữ tiếng Anh (`title: "Week 3 Worklog"`, `### Week 3 Objectives:`, `### Tasks to be carried out this week:`, `### Week 3 Achievements:`).
  - Nội dung mô tả bằng Tiếng Việt.
- **Cấu hình Thứ & Ngày:**
  - Mốc thời gian làm việc hiện tại: **Thứ 3, ngày 01/10/2026**.
  - **Quy tắc đặc biệt:** Chỉ điền nội dung & kết quả cho ngày hôm nay (**Thứ 3 ngày 01/10/2026**). Tất cả các ngày khác (Thứ 2, Thứ 4, Thứ 5, Thứ 6) để trống hoàn toàn để tránh lẫn lộn.

---

### 🔹 Giai đoạn 3: Khắc phục Lỗi Hệ thống & Sắp xếp Sidebar Hugo

- **Lỗi Live Reload không cập nhật:** Do tiến trình Hugo cũ bị treo chiếm cổng 1313. Đã kill tiến trình cũ và khởi động lại `hugo server -D --port 1313`.
- **Lỗi thứ tự Sidebar (1.3 xuất hiện trước 1.1, 1.2):** Do thuộc tính `weight: 1` bị trùng lặp ở tất cả các folder tuần. Đã cập nhật `weight` chuẩn từ `1` đến `12` cho toàn bộ 12 tuần (`1.1-Week1` weight: 1 ➔ `1.12-Week12` weight: 12).

---

## 🛠️ 2. Danh sách File đã Chỉnh sửa & Khởi tạo

1. `content/1-Worklog/1.3-Week3/_index.vi.md` - Đã cập nhật xong Thứ 3 (Module 1 RDS Introduce) và Thứ 4 (Module 2 Prerequisites với 5 hình ảnh + Module 3 Create RDS DB Instance với 3 hình ảnh & logs/events).
2. `content/1-Worklog/1.3-Week3/_index.md` - Bản tiếng Anh (chờ dịch sau khi hoàn tất toàn bộ tiếng Việt).
3. `content/1-Worklog/1.1-Week1/` đến `1.12-Week12/` - Đã cập nhật thuộc tính `weight` chuẩn (1 đến 12) cho cả 2 bản VI và EN.
4. `.agents/skills/aws-workshop-memory/SKILL.md` - File Skill bộ nhớ chính.
5. `.agents/skills/aws-workshop-memory/references/memory.md` - File bộ nhớ chi tiết tiến trình & thông số AWS.
6. `.agents/skills/aws-workshop-memory/references/conversation_history.md` - Nhật ký trò chuyện & quyết định.

---

### 🔹 Giai đoạn 4: Hoàn thành Module 2 & Module 3 (Thứ 4 - 02/10/2026)

- **Module 2 (Prerequisites):** Đã ghi thông số cấu hình VPC `rds-vpc`, Security Groups (`ec2-sg`, `rds-sg`), DB Subnet Group (`rds-subnet-group`) kèm 5 hình minh chứng & phần giải thích Ý nghĩa.
- **Module 3 (Create RDS Database Instance):** Đã ghi đầy đủ thông số DB MySQL (`db-instance`, `db.m5.large`, Multi-AZ, `gp3 20GiB`, DB `fcaj`) kèm 3 hình minh chứng (`rds-endpoint-info.png`, `rds-log-and-events.png`, `rds-maintenance-backups.png`) & phần giải thích Ý nghĩa.
- **Lưu trữ trạng thái:** Đã ghi lại toàn bộ tiến trình vào bộ nhớ Skill `aws-workshop-memory` để ngày mai mở lại AI có thể tiếp tục công việc ngay lập tức mà không bị quên.

---

### 🔹 Giai đoạn 5: Tái cấu trúc lộ trình bằng tài liệu Cloud Journey (04/10/2026)

- **Yêu cầu:**
  - Lấy tài liệu từ `cloudjourney.awsstudygroup.com` phân bổ đều vào 3 tuần (từ 14/09/2026 đến 02/10/2026).
  - Sửa lại ngày Thứ 6 hàng tuần thành thời gian tập trung ôn tập và viết/chỉnh sửa Worklog.
  - Thêm mục "Kế hoạch tuần sau" ở cuối nội dung từng Worklog.
- **Kết quả:**
  - Hoàn tất thay đổi toàn bộ nội dung của `1.1-Week1/_index.vi.md`, `1.2-Week2/_index.vi.md` và `1.3-Week3/_index.vi.md`.
  - Tuần 1: Explore AWS Services & Migrate.
  - Tuần 2: Optimizing the system & Application Modernization.
  - Tuần 3: App Modernization, Container, Data Analytics & AI/ML. Ngày Thứ 5 (01/10) vẫn là nội dung thực hành **Get Started with Amazon RDS** đã làm trước đó.
  - Cập nhật lại bộ nhớ `memory.md`, `SKILL.md` và `conversation_history.md`.

---

### 🔹 Giai đoạn 6: Triển khai Database trên Lightsail & Worklog Tuần 4 (05/10/2026)

- **Yêu cầu:** Lấy nội dung thực hành "Deploy a Database on Lightsail" từ URL `https://000045.awsstudygroup.com/1-database/` và điền vào ngày Thứ 2 (05/10) của Worklog Tuần 4.
- **Kết quả:**
  - Viết lại toàn bộ nội dung của `content/1-Worklog/1.4-Week4/_index.vi.md`.
  - Cập nhật mục tiêu Tuần 4 tập trung vào Lightsail.
  - Điền công việc Thứ 2 (05/10/2026) với thông tin cấu hình MySQL Database (plan STANDARD $15, master DB: `WordPress` -> `dbWordPress`, tài khoản: `LightsailAdmin`, tag: `dbname=dbWordPress`).
  - Ghi nhận trạng thái cấu hình vào bộ nhớ `memory.md` và `conversation_history.md`.

---

### 🔹 Giai đoạn 7: Di chuyển hình ảnh và hoàn thiện Module 2 (05/10/2026)

- **Yêu cầu:** Chèn các hình ảnh thực hành từ Module 1 đến Module 2.3 (Deploy Database, Deploy WP, Ubuntu Config, Networking Config) vào Worklog.
- **Kết quả:**
  - Di chuyển các file ảnh (`1.png`, `2.1.png`, `2.2.png`, `2.3.png`) từ thư mục `content/1-Worklog/1.4-Week4/picture/` sang đúng chuẩn Hugo tại `static/images/1-Worklog/1.4-Week4/`.
  - Gom toàn bộ nội dung từ Module 1 đến 2.3 vào duy nhất **ngày Thứ 2 (05/10/2026)** trong `1.4-Week4/_index.vi.md` theo đúng yêu cầu của người dùng.
  - Các ngày Thứ 3, Thứ 4, Thứ 5 được để trống ("Sẽ cập nhật nội dung sau").
  - Chèn hình ảnh minh họa tương ứng vào các bước kết quả của ngày Thứ 2.

---

### 🔹 Giai đoạn 8: Cập nhật Modules 2.4, 3, 6, 7 vào Worklog (05/10/2026)

- **Yêu cầu:** Bổ sung các hình ảnh mới của các module 2.4 (WP Config), 3.2-3.3 (Prestashop), 6 (Snapshots) và 7 (Migrate) vào Worklog.
- **Kết quả:**
  - Đổi tên ảnh `6.1 create snapshot.png` thành `6.1.png` để tránh lỗi khoảng trắng của Hugo.
  - Phân bổ Module 2.4 và Module 3 vào ngày **Thứ 3 (06/10/2026)**.
  - Phân bổ Module 6 và Module 7 vào ngày **Thứ 4 (07/10/2026)**.
  - Cập nhật lịch trình bảng và chèn toàn bộ ảnh tương ứng vào `content/1-Worklog/1.4-Week4/_index.vi.md`.

---

### 🔹 Giai đoạn 9: Hoàn thiện Worklog Tuần 4 & Định chuẩn Ngôn ngữ (05/10/2026)

- **Yêu cầu:** Ghi chép 2 bài Workshop thực hiện trong cùng một ngày (Amazon Lightsail và Hybrid DNS & Active Directory) vào ngày Thứ 2, xử lý lỗi quyền IAM, chuẩn hóa hình ảnh và đồng bộ đa ngôn ngữ.
- **Kết quả:**
  - Hướng dẫn cấu hình cấp quyền `AmazonLightsailFullAccess` cho IAM user `Bao` để xử lý lỗi AccessDenied khi chạy `aws lightsail push-container-image`.
  - Thiết kế lại Worklog Tuần 4 (ngày Thứ 2) bằng cách chia thành 2 phần: `Phần 1: Thực hành Amazon Lightsail` và `Phần 2: Hybrid DNS & Active Directory`.
  - Đổi tên và sắp xếp toàn bộ ảnh minh họa theo chuẩn `lab-step-X-Y.png` (tránh khoảng trắng).
  - Bổ sung chuyên mục **💡 Khó khăn gặp phải** (Difficulties Encountered) dưới mỗi bước thực hành để phản ánh thực tế khó khăn khi cấu hình (SSH, RDP, CloudFormation, Security Group).
  - Tách bạch 2 phiên bản ngôn ngữ: `_index.md` (chuẩn 100% Tiếng Anh) hiển thị ở `http://localhost:1313/` và `_index.vi.md` (chuẩn 100% Tiếng Việt) hiển thị ở `http://localhost:1313/vi/`.

---

### 🔹 Giai đoạn 10: Khởi tạo Trang Chuyên biệt cho Thứ 2 (13/10/2026)

- Khởi tạo trang chuyên biệt cho bài thực hành Thứ 2 Lightsail nhằm giảm tải cho trang tổng quan Worklog.

---

### 🔹 Giai đoạn 11: Chuẩn hóa Tên Chuyên nghiệp & Áp dụng cho Thứ 3, Thứ 4 (13/10/2026)

- **Yêu cầu:** Đổi tên bài 1.4.1 từ tên marketing "Simplified Computing" thành tên chuẩn kỹ thuật chuyên nghiệp, đồng thời tạo luôn các file chuyên biệt cho Thứ 3 và Thứ 4 để chứa toàn bộ hình ảnh thực hành trong code thư mục một cách ngăn nắp.
- **Kết quả:**
  - Chuẩn hóa tên file và tiêu đề song ngữ (VI & EN):
    1. **Thứ 2 (1.4.1):**
       - [1.4.1-amazon-lightsail.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.1-amazon-lightsail.vi.md) — _Triển khai Amazon Lightsail_ (13 ảnh minh chứng)
       - [1.4.1-amazon-lightsail.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.1-amazon-lightsail.md) — _Amazon Lightsail Deployment_
    2. **Thứ 3 (1.4.2):**
       - [1.4.2-hybrid-dns.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.2-hybrid-dns.vi.md) — _Triển khai Hybrid DNS & Active Directory_ (11 ảnh minh chứng)
       - [1.4.2-hybrid-dns.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.2-hybrid-dns.md) — _Hybrid DNS & Active Directory Infrastructure_
    3. **Thứ 4 (1.4.3):**
       - [1.4.3-ec2-auto-scaling.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.3-ec2-auto-scaling.vi.md) — _Tự động co giãn với EC2 Auto Scaling_ (44 ảnh minh chứng)
       - [1.4.3-ec2-auto-scaling.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.3-ec2-auto-scaling.md) — _Scaling Applications with EC2 Auto Scaling_
  - Tái cấu trúc trang chính Worklog Tuần 4 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/_index.md)): Tóm tắt súc tích và đính kèm link điều hướng trực quan tới từng bài lab.
  - Xóa bỏ các file cũ có tên dài/khoảng trắng. Tổng cộng gom 68 hình ảnh thực hành vào đúng module một cách chuẩn mực.
    - `1.4.1-amazon-lightsail/` (13 ảnh Lightsail)
    - `1.4.2-lightsail-container/` (11 ảnh Lightsail Container)
    - `1.4.3-ec2-auto-scaling/` (44 ảnh EC2 Auto Scaling, đổi tên từ folder cũ có khoảng trắng)
  - Đồng bộ và kiểm tra 100% đường dẫn ảnh trong tất cả các bài viết.

---

### 🔹 Giai đoạn 12: Đính chính & Đồng bộ chính xác bài lab Thứ 3 (13/10/2026)

- **Kiểm tra & Xác minh:** Đã phân tích trực quan toàn bộ 11 hình ảnh (`lab-step-1-1` đến `lab-step-4-6`) và xác nhận chính xác bài thực hành là **Amazon Lightsail Container - Run Apps on Lightsail Container** từ nguồn:
  `https://000046.awsstudygroup.com/`
- **Kết quả điều chỉnh:**
  - Đổi tên thư mục ảnh thành `1.4.2-lightsail-container/`.
  - Thay thế file bài viết thành:
    - [1.4.2-lightsail-container.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.2-lightsail-container.vi.md) — _Triển khai Amazon Lightsail Container_
    - [1.4.2-lightsail-container.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.4-Week4/1.4.2-lightsail-container.md) — _Run Applications on Amazon Lightsail Container_
  - Cập nhật nguồn tài liệu Thứ 3 trong bảng và phần Notice thành: `https://000046.awsstudygroup.com/`.
  - Xác nhận bộ ảnh Hybrid DNS thực tế nằm ở folder `1.4.4-Hybrid DNS Management with Amazon Route 53/` sẵn sàng cho bài sau.

---

### 🔹 Giai đoạn 13: Hoàn thiện Worklog Thứ 2 Tuần 5 - Thao tác dòng lệnh với AWS CLI (14/10/2026)

- **Yêu cầu:** Triển khai bài thực hành Thứ 2 Tuần 5 (12/10/2026) dựa trên Workshop **Getting Started with the AWS CLI** (`https://000011.awsstudygroup.com/`), kết nối trọn bộ 38 hình ảnh thực hành và đúc kết chi tiết 12 sự cố kỹ thuật đã giải quyết.
- **Tiến độ & Kết quả:**
  - Chuẩn hóa tên thư mục ảnh từ `Command Line Operations with AWS CLI` sang `1.5.1-aws-cli/` (loại bỏ khoảng trắng để chuẩn hóa URL trong Hugo).
  - Tái cấu trúc và viết lại toàn bộ bài viết chi tiết song ngữ theo **phong cách Step-by-step thực chiến (Walkthrough)** theo đúng yêu cầu người dùng:
    - Loại bỏ hoàn toàn kiểu viết "nguyên tài liệu lý thuyết ụp vào mặt".
    - Chia thành 38 bước hành động rõ ràng tương ứng từng ảnh: Thao tác click chuột ở đâu, ô nào điền thông số gì (Name, Policy, AMI, Instance type, CIDR, Key pair...), lệnh CLI gõ cụ thể ra sao và kết quả trả về.
    - [1.5.1-aws-cli.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.1-aws-cli.vi.md) — _Thao tác dòng lệnh với AWS CLI_ (100% Tiếng Việt).
    - [1.5.1-aws-cli.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.1-aws-cli.md) — _Command Line Operations with AWS CLI_ (100% Tiếng Anh).
  - Tái cấu trúc và đồng bộ trang tổng quan Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Đúc kết chi tiết 12 khó khăn kỹ thuật thực tế:
    1. Missing Default Subnet khi tạo EC2 ➔ Tạo `subnet-01` thủ công (`172.31.100.0/24`) và bật Auto-assign Public IP.
    2. Lỗi MobaXterm SSH Connection Timed Out ➔ Tạo Internet Gateway, Attach vào VPC và tạo route `0.0.0.0/0 ➔ igw`.
    3. Lệnh CLI kiểm tra EC2 không ra dữ liệu ➔ Thêm cờ `--region us-east-1` và `--output table`.
    4. Lỗi S3 `BucketAlreadyExists` ➔ Đổi tên bucket duy nhất toàn cầu: `aws-cli-trangiabao-2026`.
    5. Lỗi placeholder `bucket-name` ➔ Thay đúng tên bucket thật.
    6. Lỗi xóa S3 bucket không rỗng `BucketNotEmpty` ➔ Dùng cờ `--force`.
    7. Lỗi cú pháp SNS `Unknown options: Topic**` ➔ Thay bằng ARN thật.
    8. Không nhận email xác nhận SNS ➔ Sửa typo email thiếu chữ "o" và kiểm tra hòm thư Spam.
    9. Internet Gateway tạo bằng CLI không thấy trên Web ➔ Chuyển Region trên web sang Singapore (`ap-southeast-1`).
    10. Lỗi `Resource.AlreadyAssociated` khi attach IGW ➔ Nhận diện trạng thái đã gắn thành công trước đó.
    11. Máy chủ EC2 tạo bằng CLI bị thiếu Public IP (`Address: null`) và treo SSH ➔ Cấp Elastic IP và chạy `associate-address` gán vào máy.
    12. Lỗi `NoCredentials` khi chạy `terminate-instances` ➔ Gõ `exit` thoát khỏi máy khách mới quay về máy quản trị ban đầu.

---

### 🔹 Giai đoạn 14: Đồng bộ Toàn bộ Tuần 4 sang phong cách Step-by-Step Thực tế (14/10/2026)

- **Yêu cầu:** Áp dụng đồng bộ cách trình bày Step-by-Step (từng bước làm cụ thể, hướng dẫn nhấp menu nào, điền ô nào giá trị gì, lệnh CLI, ảnh minh chứng và khó khăn xử lý thực tế) đã áp dụng thành công ở Tuần 5 cho toàn bộ 5 bài lab Tuần 4.
- **Tiến độ & Kết quả:**
  - Tái cấu trúc toàn bộ 5 bài lab (song ngữ 10 bài viết cả `.vi.md` và `.md`):
    1. **1.4.1 (Amazon Lightsail):** 13 bước chi tiết (Tạo DB `Workshop-DB-Instance`, User `LightsailAdmin`, Static IP, WP install wizard, Prestashop wizard, Snapshot ~20GB, Migration sang máy chủ lớn hơn).
    2. **1.4.2 (Lightsail Container):** 11 bước chi tiết (Cài AWS CLI v2 PowerShell, cấp quyền `AmazonLightsailFullAccess`, tạo Container Service Nano, build instance Ubuntu, plugin `lightsailctl`, push Docker image, kiểm tra HTTPS domain).
    3. **1.4.3 (EC2 Auto Scaling):** 44 bước chi tiết tương ứng trọn bộ 44 ảnh (Tạo Custom AMI `fcaj-app-ami`, Target Group `fcaj-tg`, ALB `fcaj-alb`, Launch Template `fcaj-launch-template`, ASG Multi-AZ Min=1/Desired=1/Max=3, Dynamic Scaling Target Tracking 50% CPU, Stress test 600s, teardown 4 bước).
    4. **1.4.4 (Amazon CloudWatch):** 33 bước chi tiết tương ứng trọn bộ 33 ảnh (Cài CloudWatch Agent, All Metrics, Search expressions, Math expressions, Dynamic labels, Logs Insights query/filter/parse/stats, Metric filter HTTP 404, Alarm SNS).
    5. **1.4.5 (Hybrid DNS):** 11 bước chi tiết tương ứng 11 ảnh (Key pair, CloudFormation đa VPC, mở Port 53 UDP & TCP, Active Directory `corp.example.com`, Outbound/Inbound Resolver Endpoints, Forwarding Rules, `nslookup` 2 chiều).
  - Tích hợp các hộp ghi chú thực chiến trực tiếp dưới từng bước tương ứng (**💡 Khó khăn gặp phải & Cách xử lý tại Bước X**).
  - Giữ vững cấu trúc chuẩn đầu trang: **🎯 Mục tiêu bài thực hành (Lab Objectives)** và **📊 Bảng tổng hợp thông số tài nguyên đã triển khai (Provisioned Resource Specifications)**.
  - Kiểm thử `hugo -D`: 88 trang EN, 87 trang VI, 337 static files, 0 errors.

---

### 🔹 Giai đoạn 15: Hoàn thiện Worklog Thứ 3 Tuần 5 - Amazon DynamoDB (15/10/2026)

- **Yêu cầu:** Triển khai bài thực hành Thứ 3 Tuần 5 (13/10/2026) dựa trên Workshop **000060 - Work with Amazon DynamoDB** (`https://000060.awsstudygroup.com/`), kết nối trọn bộ 32 hình ảnh thực hành và đúc kết chi tiết 10 sự cố kỹ thuật đã giải quyết.
- **Tiến độ & Kết quả:**
  - Chuẩn hóa tên thư mục ảnh từ `1.5.2-Amazon DynamoDB` sang `1.5.2-amazon-dynamodb/` (loại bỏ khoảng trắng, chuẩn hóa tên file `2.1.png` đến `3.2.9.png`).
  - Tải và giải nén bộ dữ liệu phim mẫu `moviedata.json` (4.609 bản ghi, kích thước 3.7MB) vào thư mục gốc dự án.
  - Khởi tạo đầy đủ các script Python phục vụ tương tác SDK Boto3 với DynamoDB: `MoviesCreateTable.py`, `MoviesItemOps01.py`, `MoviesItemOps02.py`, `MoviesItemOps03.py`, `MoviesItemOps04.py`, `MoviesLoadData.py`, `MoviesQuery01.py`, `MoviesScan.py`, `MoviesDeleteTable.py`.
  - Tái cấu trúc và biên soạn hoàn thiện 2 bài lab song ngữ theo đúng chuẩn thực chiến:
    - [1.5.2-amazon-dynamodb.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb.vi.md) — _Làm việc với Amazon DynamoDB_ (100% Tiếng Việt, 32 bước hành động, 10 sự cố kỹ thuật).
    - [1.5.2-amazon-dynamodb.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb.md) — _Work with Amazon DynamoDB_ (100% Tiếng Anh).
  - Cập nhật trang tổng quan lộ trình Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Đúc kết chi tiết 10 khó khăn kỹ thuật thực tế:
    1. **Lỗi chính tả tham số trong tài liệu gốc:** Tài liệu viết nhầm `--provided-throughput` thay vì `--provisioned-throughput`.
    2. **Lỗi phân quyền IAM (`AccessDeniedException`):** IAM user `AWS-FCAJ-DynamDB` thiếu quyền thao tác DynamoDB ➔ Gán policy `AmazonDynamoDBFullAccess`.
    3. **Xung đột bảng đã tồn tại (`ResourceInUseException`):** Bảng `Music` đã được tạo từ bước Web Console ➔ Dùng lệnh `describe-table` để kiểm tra và tái sử dụng.
    4. **Ký tự tàng hình Zero-Width Unicode (`\u200b`):** Copy lệnh từ trang HTML bị dính 2 ký tự khoảng trắng vô hình sau `--expression-attribute-values`, gây lỗi parser `Expected: '=', received: ''` ➔ Loại bỏ ký tự ẩn bằng text editor.
    5. **AWS CLI Pager tự động thoát lệnh:** CLI v2 mặc định mở trình xem trang `less` khi JSON dài; nhấn `q` hoặc đọc hết trang thoát ra `~ $` ➔ Tắt pager bằng `export AWS_PAGER=""`.
    6. **Khóa truy vấn khi GSI đang Backfilling:** Truy vấn ngay khi vừa tạo GSI gặp lỗi `ValidationException: Cannot read from backfilling global secondary index` ➔ Đợi ~1 phút cho `IndexStatus` chuyển sang `ACTIVE`.
    7. **Dán nhầm code Python vào CMD:** Dán trực tiếp code Python vào Command Prompt gây lỗi cú pháp hàng loạt ➔ Lưu vào file `.py` và thực thi bằng `python <file>.py`.
    8. **Thư mục làm việc CMD bị đặt ở `System32`:** CMD mặc định mở tại `C:\Windows\System32` ➔ Di chuyển đúng vào thư mục dự án `cd /d D:\AWS\template_AWS\fcj-workshop-template-main`.
    9. **Nghẽn throughput khi nạp dữ liệu lớn:** Nạp 4.609 phim trong `moviedata.json` vào bảng 10 WCU bị throttle ➔ Nạp đủ số lượng mẫu phục vụ lab hoặc nâng WCU tạm thời.
    10. **Lỗi lệch Region khi xóa bảng (`ResourceNotFoundException`):** Bảng `Music` tạo ở `us-east-1` nhưng AWS CloudShell mặc định ở `ap-southeast-1` ➔ Bổ sung cờ `--region us-east-1` khi thực thi lệnh.
  - Đồng bộ và cập nhật bộ nhớ dài hạn trong Skill `aws-workshop-memory` (`references/memory.md` và `SKILL.md`).
  - Kiểm thử `hugo -D`: 89 trang EN, 88 trang VI, 369 static files, 0 errors.

---

### 🔹 Giai đoạn 16: Thực hành Amazon ElastiCache - Redis (19/10/2026)

- **Yêu cầu:** Triển khai bài thực hành Thứ 4 Tuần 5 (14/10/2026) dựa trên Workshop **000061 - Amazon ElastiCache - Redis** (`https://000061.awsstudygroup.com/`).
- **Phạm vi & Tiến độ đã thực hiện:**
  1. **Khởi tạo hạ tầng mạng & bảo mật VPC (Region `us-east-1`):**
     - Tạo VPC `vpc-0fc9d5490a843944e` và 3 subnets trải rộng trên 3 AZs khác biệt (`us-east-1a`, `us-east-1b`, `us-east-1c`) để đáp ứng điều kiện Multi-AZ và Sharding.
     - Tạo Subnet Group `subnet-group` bao gồm cả 3 subnets.
     - Tạo Security Group `sg-06c03603fe1cca808` mở port 22 (SSH) và 6379 (Redis).
     - Khắc phục sự cố bảng định tuyến dính route `Blackhole` bằng cách gắn `my-igw` và trỏ route `0.0.0.0/0 -> my-igw`.
  2. **Thiết lập máy ảo EC2 Client (`redis-client`):**
     - Tạo instance Amazon Linux 2023 tại `subnet-01` (`us-east-1a`).
     - Kết nối thông qua EC2 Instance Connect.
     - Khắc phục lỗi thiếu pip và thư viện redis bằng cách chạy `sudo dnf install -y python3-pip` và `pip3 install redis`.
  3. **Khởi tạo 5 Cụm ElastiCache Redis:**
     - **Console:** Tạo cụm `my-cluster-disable` (Mode Disabled) và `my-cluster-enable` (Mode Enabled, 2 Shards).
     - **Boto3 SDK:** Tạo và chạy thành công các script `CreateClusterModeDisabledCluster.py`, `ClusterModeEnabled.py`, `ClusterModeDisabledWithRBAC.py`, `ClusterModeEnabledWithRBAC.py`.
     - **Cụm RBAC + TLS:** Tạo thành công cụm `redis-rbac-sdk` với mã hóa Transit Encryption (TLS) và gán User Group `mygroup`.
  4. **Quản trị quyền truy cập Redis RBAC:**
     - Tạo và chạy thành công script `UserAndUserGroups.py` để tạo User Group `mygroup`, `mygroup2` và các user `myuser`, `default`.
  5. **Tương tác dữ liệu với Redis:**
     - `ConnectClusterModeDisabled.py`: Kết nối và ping kiểm tra Mode Disabled.
     - `ConnectClusterModeEnabled.py`: Sử dụng cú pháp mới `from redis.cluster import RedisCluster` kết nối thành công cụm Cluster Mode Enabled.
     - `SetAndGetStrings.py`: Thiết lập chuỗi String và kiểm tra cơ chế TTL (Time to Live) tự xóa sau 60 giây.
     - `SetAndGetHash.py`: Thao tác cấu trúc Hash đa trường (`datetime`, `epochtime`), xử lý xóa key cũ để chống lỗi `WRONGTYPE`.
     - `PubAndSub.py`: Triển khai mô hình Publisher / Subscriber bất đồng bộ đa luồng (`run_in_thread`) kèm cơ chế dừng an toàn với `Ctrl + C`.
  6. **Đúc kết 12 sự cố kỹ thuật thực tế:**
     - Không thấy IGW và Route Table bị dính Blackhole làm mất mạng, EC2 không kết nối được.
     - Lệnh `pip3` không tìm thấy (`-bash: pip3: command not found`) trên Amazon Linux 2023.
     - EC2 thiếu thư viện `redis` (`ModuleNotFoundError: No module named 'redis'`).
     - Thư viện `redis-py-cluster` (`from rediscluster import RedisCluster`) bị khai tử, thay bằng `redis.cluster`.
     - Tài liệu workshop để endpoint mẫu dạng placeholder `xxx.yyy...` khiến code không chạy nếu không lấy đúng Configuration Endpoint thật.
     - Code mẫu tài liệu Workshop ở bài 4.3 và 4.4 bị cắt cụt, thiếu phần khởi tạo biến `redis`.
     - Xung đột kiểu dữ liệu `WRONGTYPE` giữa String và Hash trên cùng tên key `mykey`.
     - Code mẫu Pub/Sub (bài 4.5) thiếu lệnh import `from redis import Redis`.
     - Cụm ElastiCache nằm trong Private VPC, máy local bị Connection Timed Out, phải dựng EC2 client cùng VPC.
     - Subnet Group thiếu AZ gây lỗi `Each Node Group needs to have at least two distinct Availability Zones`.
     - Code mẫu Python SDK `ClusterModeDisabledWithRBAC.py` bị lỗi cú pháp `non-default argument follows default argument`.
     - Độ trễ truyền tải quyền IAM (IAM propagation delay) gây `AccessDeniedException` tạm thời.

---

### 🔹 Giai đoạn 17: Hoàn thiện Toàn diện Worklog Thứ 4 Tuần 5 - Amazon ElastiCache Redis (20/10/2026)

- **Yêu cầu của người dùng:**
  - Khởi tạo tài liệu Worklog Thứ 4 Tuần 5 (1.5.3) kết nối trọn bộ 27 hình ảnh thực hành từ thư mục 1.5.3-Amazon ElastiCache.
  - **Trọng tâm đặc biệt:** Thêm nội dung phân tích chi tiết lỗi phát sinh khi chưa tạo User Group ( estusergroup / mygroup), giải pháp khắc phục bằng script tạo User Group và ảnh minh chứng thành công sau khi đã có User Group.
- **Tiến độ & Kết quả thực hiện:**
  - Chuẩn hóa và đồng bộ 27 hình ảnh vào thư mục static/images/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache/ (đồng thời giữ folder gốc để tránh gãy link).
  - Soạn thảo 2 bài viết song ngữ chuẩn mực Step-by-Step thực chiến:
    - [1.5.3-amazon-elasticache.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache.vi.md) (100% Tiếng Việt, 26 bước chi tiết, 12 khó khăn thực tế).
    - [1.5.3-amazon-elasticache.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache.md) (100% Tiếng Anh chuẩn kỹ thuật).
  - Trình bày chi tiết chuỗi sự kiện RBAC theo yêu cầu:
    1. **Bước 14 (Lỗi):** Chạy ClusterModeDisabledWithRBAC.py văng lỗi UserGroupNotFoundFault: User group mygroup not found vì chưa tạo mygroup (hoặc estusergroup) trên ElastiCache (ảnh 4.1.1.1.png và 4.1.2.1.png).
    2. **Bước 17 (Giải pháp):** Chạy UserAndUserGroups.py tạo myuser, user bắt buộc default và gán vào mygroup (ảnh 4.1.3.png).
    3. **Bước 18 & 19 (Thành công):** Chạy lại script tạo cụm RBAC thành công với HTTP 200 (ảnh 4.1.3.1.png và 4.1.3.2.png).
  - Cập nhật trang tổng quan lộ trình Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Kiểm thử hugo -D: 90 trang EN, 89 trang VI, 423 static files, 0 errors.

---

### 🔹 Giai đoạn 18: Chuẩn hóa và Ghi nhớ Toàn diện Cẩm nang Trình bày Worklog Áp dụng cho các Tuần sau (20/10/2026)

- **Yêu cầu của người dùng:**
  - Thiết lập cơ chế mục tiêu tuần sau nối tiếp: ở cuối dòng mỗi tuần hiện thêm mục tiêu cho tuần sau theo kiểu "tuần 2 xong đã làm gì thì ghi mục tiêu tuần 2 ở tuần 1, các tuần sau cứ thế làm".
  - Lưu vào memory và skill cách trình bày này để áp dụng cho các tuần sau.
- **Tiến độ & Kết quả thực hiện:**
  1. **Đồng bộ mục tiêu tuần sau nối tiếp xuyên suốt từ Tuần 1 đến Tuần 5:**
     - Tuần 1: Thêm mục `Mục tiêu cho tuần sau (Tuần 2)` (VI) & `Next Week's Objectives (Week 2)` (EN) phản ánh toàn diện nội dung Tuần 2 (Tối ưu hóa Operations, Security, Reliability, Cost & Serverless).
     - Tuần 2: Thêm mục `Mục tiêu cho tuần sau (Tuần 3)` phản ánh trọn vẹn nội dung Tuần 3 (App Modernization, Containers, Data Analytics, Lab Amazon RDS).
     - Tuần 3: Thêm mục `Mục tiêu cho tuần sau (Tuần 4)` phản ánh trọn vẹn 5 bài lab Tuần 4 (1.4.1 Lightsail, 1.4.2 Lightsail Container, 1.4.3 EC2 Auto Scaling, 1.4.4 CloudWatch, 1.4.5 Hybrid DNS).
     - Tuần 4: Thêm mục `Mục tiêu cho tuần sau (Tuần 5)` phản ánh trọn vẹn 3 bài lab Tuần 5 (1.5.1 AWS CLI v2, 1.5.2 DynamoDB, 1.5.3 ElastiCache Redis).
     - Tuần 5: Thêm mục `Mục tiêu cho tuần sau (Tuần 6)` phản ánh định hướng Tuần 6 (IaC CloudFormation/CDK/Terraform, KMS, Secrets Manager, CI/CD Pipeline).
  2. **Ghi nhớ và cập nhật vào Skill & Memory:**
     - Cập nhật mục 4 trong [SKILL.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/SKILL.md) thành bộ cẩm nang chi tiết gồm 5 trụ cột: Quy tắc nối tiếp cuốn chiếu, cấu trúc trang Index tuần, cấu trúc bài lab Step-by-Step, quản trị hình ảnh và nguyên tắc song ngữ độc lập.
     - Cập nhật nhật ký [memory.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/references/memory.md) ghi nhận đầy đủ 5 trụ cột để áp dụng tự động cho Tuần 6 trở đi.
  3. **Kiểm thử hệ thống:**
     - Chạy `hugo -D` xác nhận biên dịch thành công: 90 pages EN, 89 pages VI, 423 static files, 0 errors.

---

### 🔹 Giai đoạn 19: Hoàn thiện Toàn diện Event 3 - Meetup "First Cloud AI Journey" (27/10/2026)

- **Yêu cầu của người dùng:**
  - Khởi tạo Event 3 từ dữ liệu recap Facebook, xử lý file ảnh chụp cá nhân (`person`), ảnh ban tổ chức (`to chuc`) và ảnh minh chứng tham dự (`minh chung`).
- **Tiến độ & Kết quả thực hiện:**
  - Đồng bộ và chuẩn hóa toàn bộ 17 hình ảnh thực tế sang `static/images/4-EventParticipated/4.3-Event3/`:
    - `event3-minh-chung.jpg`: Ảnh selfie check-in thẻ đeo sự kiện tại Bitexco lầu 26.
    - `event3-to-chuc-2.jpg` & `event3-to-chuc-7.jpg`: Ảnh lưu niệm tập thể toàn thể cộng đồng và vẫy tay chào.
    - Trọn bộ ảnh các phiên diễn giả và slides kỹ thuật từ Session 1 đến Session 5.
  - Biên soạn hoàn chỉnh tài liệu song ngữ theo phong cách chuẩn kỹ thuật:
    - [4.3-Event3/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/4-EventParticipated/4.3-Event3/_index.vi.md) (100% Tiếng Việt, 5 sessions chi tiết + 14 ảnh minh chứng có chú thích sâu).
    - [4.3-Event3/\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/4-EventParticipated/4.3-Event3/_index.md) (100% Tiếng Anh học thuật/AWS Technical Writing).
  - Tối ưu mỹ thuật giao diện & Bố cục Session: Đưa toàn bộ ảnh chất lượng cao của ban tổ chức lên đặt ngay dưới tiêu đề của từng Session (Session 1 đến 5), đồng thời đồng bộ tiêu đề hiển thị trên menu sidebar thành `Event 3: First Cloud AI Journey Meetup (Cloud & AI Agent)` giống với phong cách của Event 2.
  - Cập nhật bộ nhớ `memory.md` và `SKILL.md`.
  - Kiểm thử `hugo -D`: 94 trang EN, 93 trang VI, 465 static files, 0 errors.

---

### 🔹 Giai đoạn 20: Tra cứu Chủ đề Blog Mới & Định dạng Bài đăng Facebook (28/10/2026)

- **Yêu cầu của người dùng:**
  - Tra cứu các bài viết mới và thú vị trên AWS News Blog.
  - Tìm hiểu về group Facebook cộng đồng [AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj) và ý nghĩa của các hashtag (`#`).
  - Yêu cầu tạm dừng/không sửa vào code báo cáo Blog 1 khi người dùng chưa thực sự đăng blog lên web AWS.
- **Tiến độ & Kết quả thực hiện:**
  - **Khôi phục nguyên trạng:** Đã khôi phục toàn vẹn 100% nội dung ban đầu của **Blog 1: Amazon ECS Gateway** ([3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) và `_index.md`), cũng như trang mục lục [3-BlogsPosted/](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/).
  - **Tư vấn & Thảo luận:** Giải thích rõ ý nghĩa các hashtag cộng đồng FCJ (`#FirstCloudJourney`, `#AWSStudyGroup`...) và phân tích các bài blog mới trên web AWS để người dùng lựa chọn khi sẵn sàng.
  - Kiểm thử `hugo -D`: 94 trang EN, 93 trang VI, 465 static files, 0 errors.

---

### 🔹 Giai đoạn 21: Hoàn thiện Blog 1: Enterprise Agentic Retrieval với Amazon Bedrock & AWS CDK (28/10/2026)

- **Yêu cầu của người dùng:**
  - Lựa chọn đề tài chuẩn bài và phù hợp làm đồ án cấp sinh viên (Đề xuất 1: Chatbot RAG với Amazon Bedrock & AWS CDK).
  - Yêu cầu chính thức cập nhật đề tài này vào mục **Blog 1 (3.1-Blog1)** của Workshop.
- **Tiến độ & Kết quả thực hiện:**
  - Đã tải và tích hợp 3 ảnh minh họa kỹ thuật chính thức từ bài viết AWS Blog vào `static/images/3-BlogsPosted/3.1-Blog1/`:
    - `bedrock-agentic-rag-hero.png`: Sơ đồ luồng xử lý câu hỏi tổng quan.
    - `bedrock-agentic-flow.png`: Sơ đồ kết nối AgentCore Gateway và MCP tools.
    - `bedrock-cloudwatch-dashboard.jpg`: Bảng điều khiển quan sát viễn thám CloudWatch.
  - Soạn thảo và hoàn thiện tài liệu song ngữ chuyên sâu cho Blog 1:
    - [3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) (100% Tiếng Việt, 7 phần phân tích chuyên sâu + code CDK Python + sơ đồ Mermaid).
    - [3.1-Blog1/\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.md) (100% Tiếng Anh học thuật/AWS Technical Writing).
  - Cập nhật trang mục lục [3-BlogsPosted/](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/) đồng bộ tóm tắt Blog 1.
  - Thiết kế sẵn khung chờ đường link bài viết và ảnh chụp màn hình sau khi người dùng đăng lên nhóm Facebook AWS Study Group.
  - Cập nhật bộ nhớ `memory.md` và `SKILL.md`.
  - Kiểm thử biên dịch Hugo thành công: 94 trang EN, 93 trang VI, 469 static files, 0 errors.---

### 🔹 Giai đoạn 22: Chuyển đổi & Hoàn thiện Blog 1 với AWS Continuum for Code Vulnerabilities (22/10/2026 GA) & Thẩm định Sơ đồ Draw.io

- **Yêu cầu & Quyết định từ Người dùng:**
  - Người dùng yêu cầu đề tài phải mang tính đột phá, hoàn toàn mới mẻ trên đám mây AWS, không chỉ là nâng cấp nhỏ và không đóng khung bài viết là "đồ án sinh viên" vì bài viết nhằm chia sẻ cho toàn bộ cộng đồng cloud chuyên nghiệp.
  - Thống nhất chuyển sang bài viết GA mới nhất: **AWS Continuum for code vulnerabilities is now generally available** (Phát hành ngày 22/10/2026 bởi Esra Kayabali - Principal Solutions Architect AWS).
  - Người dùng hỏi về việc vẽ mô hình Draw.io: _"cái này có cần vẽ mô hình draw.io ko ?"_, _"hướng dẫn vẽ trên draw.io, có khung ko ? Cần icon gì, tên gì"_.
  - Người dùng thắc mắc về phân nhóm hạ tầng (AWS/group), cách tìm các icon người dùng/developer (`Dev / Security Reviewer`) và hướng mũi tên của Bước 2 (`2. Read Cloud Context` từ AWS Config sang Continuum).
  - Người dùng chụp và tải lên sơ đồ Draw.io nhiều lần để AI thẩm định, căn chỉnh và hoàn thiện.
- **Tiến độ & Kết quả Thực hiện:**
  - **Tải và tích hợp 4 hình ảnh Console chính thức:**
    - `continuum-overview.png`, `continuum-issues.png`, `continuum-risk-assessment.png`, `continuum-pr-github.png`.
  - **Thẩm định & Chuẩn hóa Sơ đồ Draw.io:**
    - Hướng dẫn thiết kế 2 nhóm `AWS/group`: `AWS Cloud / Security Context` và `Developer Environment (GitHub / GitLab)`.
    - Hướng dẫn định vị `Dev / Security Reviewer` và `PR: Continuum fix` nằm trong nhóm Developer Environment.
    - Làm rõ bản chất Bước 2: AWS Continuum đọc dữ liệu từ AWS Config/VPC để xây dựng đồ thị ngữ cảnh (Context Graph), do đó mũi tên xuất phát từ AWS Config trỏ sang AWS Continuum.
    - Người dùng gửi sơ đồ hoàn chỉnh, AI thẩm định đạt điểm tuyệt đối **10/10** (đầy đủ 6 bước luồng dữ liệu, icon AWS chuẩn, màu sắc chuyên nghiệp, bố cục rõ ràng).
    - File ảnh từ Draw.io sẽ được lưu tại: `static/images/3-BlogsPosted/3.1-Blog1/continuum-architecture.png`.
  - **Soạn thảo và Hoàn thiện Bài viết Song ngữ:**
    - [3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) (100% Tiếng Việt).
    - [3.1-Blog1/\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.md) (100% Tiếng Anh học thuật).
    - Cập nhật trang mục lục `content/3-BlogsPosted/`.
  - **Chuẩn bị Bài đăng Facebook & Báo cáo Minh chứng:**
    - Soạn sẵn toàn văn bài post Facebook kỹ thuật hấp dẫn, chuẩn phong cách DevSecOps, sẵn sàng đăng lên [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj).
    - Bộ hashtag chuẩn: `#FirstCloudJourney #FCJ #AWSStudyGroup #AWSUserGroupVietnam #AWS #AWSContinuum #DevSecOps #CloudSecurity #GenerativeAI`.
    - Thiết lập khung chờ link và hình ảnh bằng chứng `facebook-post-proof.png`.
  - **Xác nhận từ Người dùng:** Người dùng hài lòng và chốt: _"ok vậy xog lưu rùi mai tui up facbook"_.
  - **Kiểm thử Hugo Build:** `hugo -D` biên dịch thành công 94 trang EN, 93 trang VI, 473 static files, **0 lỗi**.

---

### 🔹 Giai đoạn 23: Tinh chỉnh Nhãn Sơ đồ Draw.io & Đăng bài Blog 1 lên Nhóm Facebook AWS (29/10/2026)

- **Yêu cầu & Thảo luận từ Người dùng:**
  - Người dùng hỏi về nguyên lý **Tỉ lệ vàng (Golden Ratio $\varphi \approx 1.618$)** trong thiết kế khung bao kiến trúc Draw.io (tham khảo video hướng dẫn: chiều cao 500px nhân 1.618 ra chiều rộng ~809px).
  - Đánh giá kích thước sơ đồ Blog 1 hiện tại (`1024 x 530 px` tỉ lệ ~1.932 Widescreen), xác nhận đạt chuẩn hiển thị tối ưu trên slide thuyết trình 16:9 và trang web Hugo mà không cần vẽ lại toàn bộ.
  - Người dùng yêu cầu hướng dẫn căn chỉnh các khối chữ bị co cụm: `AWS Config & VPC Topology` và `PR:Continuum fix` để dàn thẳng hàng ngay ngắn.
  - Hướng dẫn 2 cách: Tắt tự động ngắt dòng (Word Wrap) và tách riêng Text box khỏi icon để tránh bị khoá kích thước bởi shape icon.
  - Người dùng gửi lại ảnh sơ đồ đã căn chỉnh hoàn hảo. AI thẩm định đạt chuẩn 10/10.
  - Người dùng yêu cầu soạn bài đăng Facebook: loại bỏ lời chào xã giao, loại bỏ từ xưng hô thân mật ("ae", "chúng ta"), bỏ mốc ngày tháng GA, diễn đạt bình dân, trực diện và dễ hiểu theo đúng bản chất: Quét code trên Git ➔ Đối chiếu dịch vụ AWS xem lỗi có khai thác thực tế được không ➔ Tự viết code sửa và mở sẵn PR trên Git cho Dev bấm Merge.
  - Bổ sung đường link bài viết gốc từ AWS News Blog.
  - Người dùng hỏi về các thuật ngữ chuyên ngành thay thế cho "mạng VPC, quyền truy cập IAM, cổng nào đang mở ra Internet" ➔ Đã cung cấp các cụm từ chuẩn DevSecOps: _cấu hình mạng VPC, chính sách phân quyền IAM, và bề mặt phơi nhiễm Internet (Internet Exposure / Security Groups)_.
  - Giải đáp thắc mắc về dấu gạch đỏ lượn sóng (tính năng spell check của trình duyệt, không hiển thị trên bài đăng thật) và dấu `#` màu xanh (Facebook nhận diện hashtag thành công).
- **Trạng thái & Tiến độ:**
  - Người dùng đã hoàn tất việc nộp bài đăng lên cộng đồng [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj).
  - ⏳ **Trạng thái:** Đang chờ đội ngũ Admin nhóm Facebook duyệt bài viết.
  - **Kế hoạch tiếp theo:**
    1. Khi bài viết được phê duyệt: Lấy link bài viết dán vào [3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) và `_index.md`.
    2. Chụp màn hình bài viết lưu vào `static/images/3-BlogsPosted/3.1-Blog1/facebook-post-proof.png`.
    3. Triển khai tiếp nội dung Worklog Tuần 6 / Tuần 7.

### Giai đoạn 24: Bổ sung Hình ảnh & Đồng bộ Link từ Cloud Journey Mới (`cloudjourney.awsfcaj.com`) cho Worklog Tuần 1, 2, 3

- **Bối cảnh & Yêu cầu:**
  - Người dùng yêu cầu lấy ảnh từ cổng tài liệu mới `https://cloudjourney.awsfcaj.com/` để thế vào Worklog tuần 1, 2, 3.
  - Hướng dẫn bổ sung: Với các bài chưa có ảnh thì bổ sung cho đầy đủ từ Thứ 2 đến Thứ 6, chọn lọc vài ảnh kết quả thực tế, không lấy tràn lan.
  - Đồng bộ toàn bộ các đường link tài liệu tham khảo trong bảng 5 cột từ domain cũ `awsstudygroup.com` sang domain mới `awsfcaj.com`.
- **Hành động & Giải pháp:**
  - **Banner & Lộ trình chung:** Tải banner chính thức `Cloud-Journey-1.png` từ `cloudjourney.awsfcaj.com` và chèn vào đầu trang của cả 3 tuần.
  - **Phân bổ hình ảnh kết quả theo tuần:**
    - **Tuần 1 (Core Services & Networking):** Bổ sung 10 ảnh kết quả thực tế cho Thứ 2 (VPC Resource Map, IAM Access), Thứ 3 (EC2 Running, CloudWatch Alarm OK), Thứ 4 (Lightsail WordPress Active, DynamoDB Query Result), Thứ 5 (AWS Managed Microsoft AD Active, Route 53 Hybrid DNS Resolution), Thứ 6 (AWS Backup Disaster Recovery Arch).
    - **Tuần 2 (Automation & Security & Data):** Bổ sung 7 ảnh kết quả thực tế cho Thứ 2 (Lambda Execution Automation, KMS Customer Managed Key Arch), Thứ 3 (AWS WAF Web ACL Protection, ECS Fargate Microservices), Thứ 4 (CodePipeline / CodeBuild Succeeded), Thứ 5 (AWS Glue Crawler & Athena Query), Thứ 6 (S3 Data Lake Analytics Pipeline).
    - **Tuần 3 (Multi-tier RDS, Decoupling & Serverless):** Bổ sung 6 ảnh kết quả tiêu biểu cho Thứ 2 (Sơ đồ Multi-AZ RDS & VPC Subnet), Thứ 3 (RDS Endpoint, IAM Role & SQS/SNS Decoupling), Thứ 4 (API Gateway & Lambda Serverless Result), Thứ 5 (Cognito User Pool Auth & CloudWatch Logs), Thứ 6 (Kinesis & Glue Streaming Data Lake). Kèm link điều hướng sang bài thực hành chi tiết [1.3.1-Multi-tier-Architecture-with-AWS-RDS](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.3-Week3/1.3.1-Multi-tier-Architecture-with-AWS-RDS/_index.vi.md).
  - **Cập nhật link tài liệu tham khảo:** Toàn bộ link trong bảng công việc 5 cột của Tuần 1, 2, 3 đã được cập nhật sang `000002.awsfcaj.com`, `000003.awsfcaj.com`, `000004.awsfcaj.com`, `000008.awsfcaj.com`, `000013.awsfcaj.com`, `000016.awsfcaj.com`, `000017.awsfcaj.com`, `000022.awsfcaj.com`, `000026.awsfcaj.com`, `000033.awsfcaj.com`, `000035.awsfcaj.com`, `000040.awsfcaj.com`...
  - **Tuân thủ chuẩn đa ngôn ngữ độc lập:** File `.vi.md` 100% Tiếng Việt chuẩn mực kỹ thuật, File `.md` 100% Tiếng Anh chuyên nghiệp.
  - **Kiểm thử Hugo:** Biên dịch thành công `hugo -D`, 94 trang EN, 93 trang VI, 462 static files, **0 errors, 0 warnings**.

### Giai đoạn 25: Đồng bộ Trạng thái Thực tế: Tuần 5 Thứ 6 Chưa có gì & Tuần 6 Không có gì
- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Người dùng khẳng định: "là tuần 5 thứ 6 chưa có gì và tuần 6 ko có gì".
- **Hành động & Kết quả:**
  - **1. Tuần 5:** Bảng công việc dòng Thứ 6 ghi `*(Chưa thực hiện)*`, phần kết quả xóa bỏ hoàn toàn mục Thứ 6, thư mục bài viết con 1.5.5 và ảnh tạm đã được xóa sạch.
  - **2. Tuần 6:** Đã đưa `_index.vi.md` và `_index.md` về lại template nguyên bản (như các tuần chưa làm), không ghi bất kỳ công việc hay kết quả thực hành nào.
  - **3. Kiểm thử Hugo:** `hugo -D` biên dịch chuẩn xác: **94 trang EN, 93 trang VI, 509 static files, 0 errors, 0 warnings**.

---

### Giai đoạn 26: Hoàn thành Bài bù Thứ 6 Tuần 5 - Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (31/10/2026)

- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Người dùng quyết định thực hành bù cho Thứ 6 Tuần 5 bằng bài lab: **Optimizing the system on AWS** (Workshop 000022 - `https://000022.awsfcaj.com/`).
  - Người dùng trực tiếp thực hành trên AWS Console, gặp các lỗi thực tế (chọn nhầm Default VPC khi tạo EC2 dẫn đến không thấy Security Group; lỗi `IncorrectInstanceState` khi gọi Lambda Start/Stop do máy cũ `i-099b2108fbf1a9175` bị Terminated nhưng còn dính Tag `environment_auto=true`).
  - AI đã đồng hành hướng dẫn xử lý: Tạo máy mới `i-003cb6dbd0f4e5b31`, tối ưu mã nguồn Python Boto3 với bộ lọc trạng thái máy `running`/`stopped`.
  - Người dùng chạy test thành công mỹ mãn: Cả 2 hàm Lambda đều trả về `Executing function: succeeded` (StatusCode 200) và nhận trọn vẹn thông báo từ Slack `#notification`.
  - Người dùng nạp trọn bộ 18 ảnh thực hành thật vào thư mục: `static/images/1-Worklog/1.5-Week5/1.5.6-AWS Lambda/`.
- **Hành động & Kết quả:**
  - **1. Chuẩn hóa hình ảnh:** Sao chép và chuẩn hóa toàn bộ 18 ảnh sang `static/images/1-Worklog/1.5-Week5/1.5.5-aws-lambda/` (`2.1.png` đến `6.3.png`).
  - **2. Soạn thảo bài viết song ngữ chi tiết:**
    - `content/1-Worklog/1.5-Week5/1.5.5-aws-lambda/1.5.5-aws-lambda.vi.md` (100% Tiếng Việt, 9 bước thực hành, bảng tài nguyên thật, mã Python Boto3 tối ưu, 10 sự cố thực tế & dọn dẹp tài nguyên).
    - `content/1-Worklog/1.5-Week5/1.5.5-aws-lambda/1.5.5-aws-lambda.md` (100% Tiếng Anh chuẩn mực).
  - **3. Cập nhật trang tổng quan Tuần 5:**
    - Cập nhật dòng Thứ 6 trong bảng công việc và thêm mục kết quả Thứ 6 kèm link điều hướng tại `_index.vi.md` và `_index.md`.
  - **4. Bảo toàn trạng thái Tuần 6:** Giữ nguyên template tuần 6 trống đúng yêu cầu.
  - **5. Kiểm thử biên dịch Hugo:** `hugo -D` biên dịch thành công: **95 trang EN, 94 trang VI, 545 static files, 0 errors, 0 warnings**.

---

### Giai đoạn 27: Rà soát Toàn diện & Khắc phục Các Lỗi Kỹ thuật của Báo cáo Workshop (01/11/2026)

- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Sau khi nghe báo cáo đánh giá hiện trạng toàn bộ dự án, người dùng chỉ đạo: "ảnh đại diện thì bỏ qua, còn lại sửa".
  - Giữ nguyên ảnh avatar hiện tại theo ý người dùng, tập trung sửa triệt để tất cả lỗi kỹ thuật, lỗi đường dẫn, thông tin sinh viên và cấu hình.
- **Hành động & Kết quả:**
  1. **Sửa lỗi tên thư mục 1.5.1:** Đổi `static/images/1-Worklog/1.5-Week5/1.5.1-AWS CLI` ➔ `1.5.1-aws-cli`, phục hồi trọn vẹn 38 ảnh minh chứng hiển thị thành công.
  2. **Dọn dẹp thư mục ảnh thừa:** Xóa `1.5.5-static-website-hosting-s3` và `1.5.6-AWS Lambda`, giảm file tĩnh từ 545 xuống 480 files sạch sẽ.
  3. **Đồng bộ trang chủ tiếng Việt (`_index.vi.md`):** Đưa thông tin thật của Trần Gia Bảo (FPT University, thời gian 14/09/2026 - 14/12/2026) vào trang chủ; gỡ bỏ hộp cảnh báo Warning mẫu trên cả 2 trang chủ.
  4. **Sửa link 404:** Cập nhật đường dẫn mục lục trong `5.3-S3-vpc/_index.vi.md` & `.md` thành `5.3.1-create-gwe/` và `5.3.2-test-gwe/`; thêm menu điều hướng 4 bài con cho `5.4-S3-onprem`; loại bỏ link PDF hỏng trong `2-Proposal`.
  5. **Cập nhật tác giả Hugo:** Đổi `author = "trangiabao4461@gmail.com"` trong `config.toml`.
  6. **Kiểm thử tự động:**
     - Missing images: 0
     - Broken links: 0
     - `hugo -D`: **95 trang EN, 94 trang VI, 480 static files, 0 errors, 0 warnings**.

---

### Giai đoạn 28: Chuẩn hóa Quy tắc Lịch học 1 bài/ngày & Thứ 6 Review/Project (Bắt đầu từ Tuần 1)

- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Người dùng yêu cầu chuẩn hóa lại cơ chế phân bổ lịch học của toàn bộ dự án:
    - **Thứ 2 đến Thứ 5:** Mỗi ngày tập trung thực hành 1 nội dung / bài lab kỹ thuật rõ ràng.
    - **Thứ 6:** Cố định làm ngày **Tổng kết, ôn tập review kiến thức tuần & Dành thời gian làm Đề xuất dự án (Project Proposal)**.
    - Các bài học vốn ở Thứ 6 theo syllabus cũ sẽ được dời cuốn chiếu sang Thứ 2 của tuần tiếp theo.
  - Người dùng chỉ đạo: "giờ hãy chỉnh lên tuần 1 ta học từ bấy giờ đi" ➔ Tiến hành áp dụng ngay từ Tuần 1.
- **Hành động & Kết quả:**
  1. Cập nhật trang tổng quan Tuần 1 ([`1.1-Week1/_index.vi.md`](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.1-Week1/_index.vi.md) và [`_index.md`](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.1-Week1/_index.md)):
     - **Thứ 2 (14/09):** AWS Budgets (000007) & AWS IAM (000002).
     - **Thứ 3 (15/09):** Amazon VPC (000003).
     - **Thứ 4 (16/09):** Amazon EC2 (000004).
     - **Thứ 5 (17/09):** Amazon S3 (000057).
     - **Thứ 6 (18/09):** Tổng kết, ôn tập review Tuần 1 & Dành thời gian nghiên cứu ý tưởng Đề xuất dự án (Project Proposal).
  2. Bổ sung mô tả kết quả đạt được chi tiết cho từng ngày Thứ 2, Thứ 3, Thứ 4, Thứ 5, Thứ 6; liên kết chính xác 3 hình ảnh minh chứng (`iam-access-architecture.png`, `vpc-resource-map.png`, `ec2-launch-success.png`).
  3. Kiểm thử biên dịch Hugo build thành công 100%: **95 trang EN, 94 trang VI, 0 errors, 0 warnings**.
  4. Cập nhật trang tổng quan Tuần 2 ([`1.2-Week2/_index.vi.md`](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.2-Week2/_index.vi.md) và [`_index.md`](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.2-Week2/_index.md)):
     - **Thứ 2 (21/09):** Tối ưu hóa vận hành & Tự động hóa không máy chủ: AWS Lambda (000022), CloudWatch/Grafana (000029), CloudFormation (000037).
     - **Thứ 3 (22/09):** Tối ưu hóa bảo mật & Mã hóa dữ liệu: AWS KMS (000033), AWS WAF (000026), Amazon GuardDuty (000098).
     - **Thứ 4 (23/09):** Độ tin cậy & Đóng gói container CI/CD: Docker & Amazon ECS Fargate (000016), AWS CodePipeline & CodeBuild (000017).
     - **Thứ 5 (24/09):** Tối ưu chi phí & Phân tích dữ liệu: Savings Plans & Reserved Instances (000042), AWS Glue & Athena (000040).
     - **Thứ 6 (25/09):** Tổng kết tuần 2 & Hoàn thiện Đề xuất dự án (Project Proposal): Hệ thống hóa 4 trụ cột Well-Architected, kiểm toán tài nguyên và dành thời gian hoàn thiện khung kiến trúc Proposal.
     - Đồng bộ song ngữ và kiểm thử Hugo build thành công 100% (**0 errors, 0 warnings**).

---

### Giai đoạn 29: Hoàn thiện Lịch trình Cuốn chiếu Tuần 3, 4, 5 và Chuẩn bị Tuần 6

- **Bối cảnh & Chỉ đạo từ Người dùng:** Tiếp tục triển khai quy tắc "Thứ 2 đến Thứ 5 mỗi ngày 1 bài lab, Thứ 6 là tổng kết tuần học được những gì, làm worklog, làm project" xuyên suốt toàn bộ các tuần còn lại.
- **Hành động & Kết quả:**
  1. **Tuần 3 (`content/1-Worklog/1.3-Week3/`):**
     - Thứ 2 đến Thứ 4: App Modernization Serverless, Containers, Data Analytics.
     - Thứ 5: Thực hành chuyên sâu Amazon RDS (1.3.1).
     - Thứ 6: Tổng kết Tuần 3, Hoàn thiện Worklog 1.3.1 & Triển khai Đề xuất dự án (Project Proposal).
     - Đồng bộ song ngữ `_index.vi.md` và `_index.md`.
  2. **Tuần 4 (`content/1-Worklog/1.4-Week4/`):**
     - Thứ 2: 1.4.1 Triển khai Amazon Lightsail (13 ảnh).
     - Thứ 3: 1.4.2 Triển khai Amazon Lightsail Container (11 ảnh).
     - Thứ 4: 1.4.3 Tự động co giãn với EC2 Auto Scaling (44 ảnh).
     - Thứ 5: 1.4.4 Giám sát với Amazon CloudWatch (33 ảnh).
     - Thứ 6: Tổng kết Tuần 4, Viết Worklog (1.4.1 - 1.4.4) & Làm Project (Proposal).
     - Bài Hybrid DNS (1.4.5 cũ) chuyển cuốn chiếu sang Thứ 2 Tuần 5 thành **1.5.1**.
  3. **Tuần 5 (`content/1-Worklog/1.5-Week5/`):**
     - Thứ 2: 1.5.1 Thiết lập Hybrid DNS với Route 53 Resolver (11 ảnh, di chuyển từ 1.4.5).
     - Thứ 3: 1.5.2 Thao tác dòng lệnh với AWS CLI (38 ảnh, đổi số từ 1.5.1).
     - Thứ 4: 1.5.3 Làm việc với Amazon DynamoDB (32 ảnh, đổi số từ 1.5.2).
     - Thứ 5: 1.5.4 Triển khai Amazon ElastiCache - Redis (27 ảnh, đổi số từ 1.5.3).
     - Thứ 6: Tổng kết Tuần 5, Viết Worklog (1.5.1 - 1.5.4) & Làm Project (Proposal).
     - Đồng bộ toàn bộ thư mục hình ảnh tương ứng (`static/images/1-Worklog/1.5-Week5/1.5.1-hybrid-dns/`, `1.5.2-aws-cli/`, `1.5.3-amazon-dynamodb/`, `1.5.4-amazon-elasticache/`).
  4. **Tuần 6 (`content/1-Worklog/1.6-Week6/`):**
     - Thứ 2: 1.6.1 Quản lý và Nâng hạn mức tài nguyên với AWS Service Quotas (chuyển từ 1.5.4 cũ).
     - Thứ 3: 1.6.2 Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (18 ảnh, chuyển từ 1.5.5 cũ).
     - Thứ 4: 1.6.3 Giám sát với Grafana & CloudWatch (Workshop 000029 - Getting started with Grafana basic).
     - Thứ 5: Mở rộng Giám sát & Quản trị Vận hành Đám mây (CloudWatch Advanced).
     - Thứ 6: Tổng kết Tuần 6, Viết Worklog & Làm Project (Proposal).
     - Đồng bộ hình ảnh 1.6.1 và 1.6.2 sang `static/images/1-Worklog/1.6-Week6/`.
     - Cập nhật trang tổng quan song ngữ `1.6-Week6/_index.vi.md` và `_index.md`.
  5. **Kiểm thử tự động hóa toàn diện:**
     - `scratch/verify_links.ps1`: **0 missing images** (Tất cả 100% hình ảnh trong mọi bài viết đều tồn tại chính xác trên disk).
     - `scratch/verify_internal_links.ps1`: **0 broken internal links** (Tất cả liên kết nội bộ đều hợp lệ).
     - `hugo -D`: **95 trang EN, 94 trang VI, 541 static files, 0 errors, 0 warnings**.





