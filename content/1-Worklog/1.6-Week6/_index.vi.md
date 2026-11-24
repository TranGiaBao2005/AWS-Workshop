---
title: "Tuần 6"
date: 2026-10-19
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 6:

* Quản trị trần giới hạn tài nguyên và hạn mức vCPU của hệ thống máy chủ với **AWS Service Quotas** và làm việc với **AWS Support Center**.
* Xây dựng giải pháp tự động hóa tối ưu chi phí hạ tầng máy chủ EC2 với kiến trúc không máy chủ **AWS Lambda**, **Amazon EventBridge Scheduler** và tích hợp ChatOps qua **Slack Incoming Webhooks**.
* Chuẩn hóa chiến lược phân loại và gom nhóm quản trị tài nguyên thông qua **AWS Tags** (gắn thẻ thủ công và tự động hóa với AWS CLI) cùng **AWS Resource Groups**.
* Triển khai hệ thống giám sát và trực quan hóa hiệu năng nâng cao bằng bảng điều khiển **Grafana** tích hợp nguồn dữ liệu **Amazon CloudWatch** (Workshop 000029 - Getting started with Grafana basic).
* Tổng kết toàn bộ kiến thức tuần 6, hoàn thiện hệ thống Worklog và dành thời gian nghiên cứu triển khai đồ án thực tập (**Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :--- | :--- | :--- |
| **Thứ 2** | **Quản trị giới hạn tài nguyên với AWS Service Quotas:** <br>- Khám phá hệ thống Service Quotas & tra cứu hạn mức EC2 Spot vCPU. <br>- Kiểm thử cơ chế xác thực dữ liệu đầu vào (Input Validation). <br>- Gửi yêu cầu nâng hạn mức vCPU từ 32 lên 64 cho Spot Instances (`L-34B43A08`). <br>- Theo dõi và nhận phê duyệt từ AWS Support Center (Case ID: `179257232100832`). <br>- Tự động hóa tra cứu bằng AWS CLI & thiết lập giám sát CloudWatch. | 19/10/2026 | 19/10/2026 | [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/) |
| **Thứ 3** | **Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack:** <br>- Gắn nhãn tự động hóa `environment_auto: true` cho máy chủ EC2 cần tối ưu chi phí. <br>- Thiết lập kênh ChatOps gửi thông báo trạng thái qua Slack Incoming Webhooks. <br>- Cấu hình IAM Execution Role cấp quyền kiểm soát vòng đời máy chủ EC2. <br>- Lập trình và triển khai hàm Lambda tự động dừng/bật máy chủ (`dc-common-lambda-auto-stop`, `dc-common-lambda-auto-start`). <br>- Thiết lập lịch kích hoạt tự động theo khung giờ làm việc với Amazon EventBridge Scheduler. <br>- Kiểm thử thực tế bật/tắt máy ảo tự động và nhận thông báo Slack tức thời. | 20/10/2026 | 20/10/2026 | [Optimize EC2 Cost with Lambda](https://000022.awsfcaj.com/) |
| **Thứ 4** | **Quản trị Thẻ định danh và Nhóm tài nguyên AWS (Tags & Resource Groups):** <br>- Khởi chạy máy chủ EC2 và thực hành quản trị thẻ thủ công trên AWS Console. <br>- Tạo IAM Access Key và cấu hình AWS CLI để tự động hóa gán thẻ (`create-tags`). <br>- Truy vấn và lọc danh sách tài nguyên máy chủ theo điều kiện thẻ phức tạp (`describe-instances --filters`). <br>- Khởi tạo nhóm tài nguyên AWS Resource Groups (`EnvTest`) tự động gom nhóm máy ảo theo thẻ môi trường. <br>- Đúc kết kinh nghiệm xử lý giới hạn thẻ, phân biệt hoa thường và phạm vi vùng của Resource Groups. | 21/10/2026 | 21/10/2026 | [AWS Tagging & Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html) |
| **Thứ 5** | **Giám sát với Grafana & CloudWatch (Workshop 000029):** <br>- Cấu hình VPC, Public Subnet tự động cấp Public IP và Security Group mở cổng 3000 & 22. <br>- Khởi chạy máy chủ EC2 chạy Amazon Linux 2023 và thiết lập IAM Role cấp quyền CloudWatch an toàn. <br>- Cài đặt và kích hoạt dịch vụ nền `grafana-server` qua YUM repository và systemd. <br>- Kết nối nguồn dữ liệu CloudWatch Data Source và xác thực thành công các API đo lường. <br>- Xây dựng bảng điều khiển Time Series và trực quan hóa chuyên sâu chỉ số CPUUtilization với Explore (Bars). | 22/10/2026 | 22/10/2026 | [Getting started with Grafana basic](https://000029.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 6, Viết Worklog & Làm Project:** <br>- Tổng kết và hệ thống hóa kiến thức Service Quotas, Lambda FinOps, Tagging & Grafana CloudWatch. <br>- Hoàn thiện chi tiết nội dung và hình ảnh cho các trang Worklog từ 1.6.1 đến 1.6.4. <br>- Dành thời gian nghiên cứu tài liệu kiến trúc và xây dựng báo cáo Đồ án thực tập (Project Proposal). | 23/10/2026 | 23/10/2026 | [Internal Review & Project Documentation](/vi/2-proposal/) |

---

### Kết quả đạt được tuần 6:

#### 📌 Kết quả Thứ 2 (19/10/2026) - Quản lý giới hạn tài nguyên với AWS Service Quotas:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình kỹ thuật, quy trình thực hiện, bài toán kinh tế đám mây (nâng Quota hoàn toàn miễn phí), các bài học thực tế và trọn bộ hình ảnh minh chứng được trình bày chi tiết tại: **[1.6.1. Quản lý và Nâng hạn mức tài nguyên với AWS Service Quotas](1.6.1-service-quotas/)**.
{{% /notice %}}

- **Vai trò quản trị trần tài nguyên (Service Quotas):** Hiểu rõ cơ chế hạn mức của AWS nhằm bảo vệ an toàn cho tài khoản, ngăn chặn các sự cố chi phí bất thường do cấu hình nhầm hoặc rò rỉ mã bảo mật.
- **Quy trình gửi yêu cầu nâng hạn mức thực chiến:** Trải nghiệm thực tế quá trình gửi yêu cầu tăng gấp đôi trần vCPU cho cụm máy chủ Spot Instances (từ 32 lên 64 vCPUs) trên AWS Management Console và vượt qua các ràng buộc xác thực dữ liệu đầu vào.
- **Làm việc với hệ thống hỗ trợ kỹ thuật (AWS Support Center):** Nắm bắt quy trình phối hợp và nhận thông báo phê duyệt hồ sơ hỗ trợ (Support Case) qua thư điện tử chính thức từ Amazon Web Services ngay trên gói dịch vụ cơ bản (Basic Support).
- **Tự động hóa và giám sát chủ động:** Thực hành sử dụng câu lệnh AWS CLI để tra cứu mã hạn mức, lịch sử thay đổi và lên phương án thiết lập cảnh báo CloudWatch trước khi tài nguyên chạm ngưỡng tới hạn.

---

#### 📌 Kết quả Thứ 3 (20/10/2026) - Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình kỹ thuật, mã nguồn Python Boto3 tối ưu, 10 sự cố thực tế đã xử lý thành công và trọn bộ 18 hình ảnh minh chứng thực tế được trình bày tại: **[1.6.2. Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack](1.6.2-aws-lambda/)**.
{{% /notice %}}

- **Tự động hóa quản trị vòng đời máy chủ EC2:** Xây dựng quy trình tự động dừng các máy chủ môi trường phát triển/thử nghiệm ngoài giờ hành chính và tự động bật lại vào đầu giờ làm việc, giúp tiết kiệm tới 65% - 70% chi phí chạy máy ảo.
- **Lập trình Serverless với AWS Lambda & Boto3:** Viết hàm Lambda xử lý linh hoạt dựa trên tài nguyên gán nhãn (`tag:environment_auto = true`), đồng thời tối ưu hóa logic lọc theo trạng thái máy (`instance-state-name`) để loại trừ các máy đã hủy (`terminated`).
- **Tích hợp ChatOps với Slack Incoming Webhooks:** Kết nối thông báo thời gian thực về kênh chat của đội ngũ vận hành (`#notification`), hiển thị trực quan danh sách Instance ID và trạng thái thao tác.
- **Điều phối tác vụ định kỳ với Amazon EventBridge Scheduler:** Cấu hình lịch kích hoạt định kỳ (Cron / Rate expression) hoàn toàn không máy chủ, độc lập và độ tin cậy cao.

---

#### 📌 Kết quả Thứ 4 (21/10/2026) - Quản trị Thẻ định danh và Nhóm tài nguyên AWS (Tags & Resource Groups):

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, câu lệnh AWS CLI thực chiến, phân tích kiến trúc ABAC, bảng tổng hợp tài nguyên và trọn bộ 14 hình ảnh minh chứng được trình bày tại: **[1.6.3. Quản trị Thẻ định danh và Nhóm tài nguyên AWS (Tags & Resource Groups)](1.6.3-tags-and-resource-groups/)**.
{{% /notice %}}

- **Chuẩn hóa chiến lược gắn thẻ (AWS Tagging Strategy):** Hiểu rõ tầm quan trọng của thẻ định danh trong quản trị môi trường đa tài khoản, phân bổ chi phí (Cost Allocation Tags) và kiểm soát truy cập dựa trên thuộc tính (ABAC).
- **Thực hành quản trị thẻ đa nền tảng:** Kết hợp nhuần nhuyễn giữa thao tác trực quan trên AWS Management Console và tự động hóa hàng loạt với các câu lệnh `aws ec2 create-tags` và `aws ec2 describe-instances --filters`.
- **Tổ chức quản trị tập trung với AWS Resource Groups:** Thiết lập nhóm tài nguyên `EnvTest` theo truy vấn thẻ giúp quản trị viên gom nhóm, theo dõi và thao tác đồng thời trên toàn bộ các tài nguyên cùng thuộc một môi trường thử nghiệm.
- **Kinh nghiệm xử lý sự cố thực tế:** Nắm vững quy tắc phân biệt chữ hoa/chữ thường (Case-sensitive) của Tag Key/Value, giới hạn 50 thẻ trên mỗi tài nguyên và cơ chế phạm vi theo vùng (Region-scoped) của Resource Groups.

---

#### 📌 Kết quả Thứ 5 (22/10/2026) - Giám sát hệ thống với Grafana & Amazon CloudWatch:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số hạ tầng mạng, chính sách IAM Policy/Role bảo mật, lệnh cài đặt YUM trên Amazon Linux 2023, cấu hình CloudWatch Data Source và trọn bộ 18 hình ảnh minh chứng được trình bày tại: **[1.6.4. Giám sát hệ thống với Grafana & Amazon CloudWatch](1.6.4-grafana-basic/)**.
{{% /notice %}}

- **Triển khai máy chủ giám sát Grafana trên AL2023:** Khởi tạo môi trường hiển thị trực quan dữ liệu mã nguồn mở Grafana v13.3.0, cấu hình kho lưu trữ YUM chính thức và quản lý tiến trình nền bằng systemd.
- **Tích hợp nguồn dữ liệu CloudWatch không cần Access Key:** Thiết lập phân quyền IAM Role (`GrafanaAccessRole`) gắn trực tiếp vào EC2 Instance Profile, giúp Grafana tự động xác thực an toàn theo nguyên tắc Zero-Trust.
- **Xây dựng Dashboard & Khám phá dữ liệu đa chiều:** Thiết kế các bảng đồ thị chuỗi thời gian (Time Series) theo dõi chỉ số `CPUUtilization` theo thời gian thực và sử dụng công cụ Explore trực quan hóa dạng cột (Bars).
- **Ngân hàng xử lý sự cố giám sát:** Đúc kết giải pháp mở cổng 3000 trên Security Group, xử lý lỗi phân quyền CloudWatch 403 Access Denied và quy trình dọn dẹp tài nguyên tránh phát sinh chi phí.

---

#### 📌 Kết quả Thứ 6 (23/10/2026) - Tổng kết Tuần 6, Viết Worklog & Làm Project:

{{% notice tip %}}
👉 **Kế hoạch định kỳ Thứ 6:** Dành trọn vẹn ngày Thứ 6 cho 3 trọng tâm chính: (1) Tổng kết kiến thức đã tích lũy trong tuần; (2) Hoàn thiện hệ thống Worklog và minh chứng thực hành; (3) Nghiên cứu và triển khai Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
{{% /notice %}}

* **1. Tổng kết kiến thức tuần 6:**
  * Hệ thống hóa toàn diện các kiến thức về quản trị hạn mức tài nguyên **AWS Service Quotas** và quy trình làm việc với AWS Support.
  * Làm chủ kiến trúc FinOps tự động hóa kiểm soát chi phí điện toán bằng **AWS Lambda**, **EventBridge Scheduler** và **Slack ChatOps**.
  * Chuẩn hóa quy trình gắn nhãn và quản trị tài nguyên tập trung với **AWS Tags** và **AWS Resource Groups**.
  * Nắm vững kỹ thuật xây dựng hệ thống giám sát tập trung hiện đại kết hợp sức mạnh đo lường của **CloudWatch** và tính trực quan đa dạng của **Grafana**.
* **2. Hoàn thiện hệ thống Worklog:**
  * Soát lỗi toàn bộ các bài thực hành trong tuần từ **1.6.1 đến 1.6.4**, bổ sung đầy đủ các bảng thông số kỹ thuật và hình ảnh thực tế.
  * Đảm bảo tính nhất quán song ngữ (Tiếng Việt và Tiếng Anh), định dạng chuẩn Markdown và kiểm tra đường dẫn liên kết nội bộ.
* **3. Nghiên cứu & Triển khai Project (Proposal):**
  * Tích hợp các giải pháp giám sát Grafana/CloudWatch, phân loại nhãn Tags và tối ưu chi phí tự động vào kiến trúc của Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
  * Chuẩn bị các sơ đồ kiến trúc và phân tích chi phí chi tiết cho báo cáo đề xuất dự án.

---

### Mục tiêu cho tuần sau (Tuần 7):

* **Giám sát chuyên sâu với CloudWatch Advanced Workshop:**
  * Thực hành các kỹ thuật giám sát nâng cao, cấu hình Metric Math, Search Expressions và thuộc tính động (PROP DimName).
  * Xây dựng hệ thống cảnh báo đa kênh và phân tích tải hệ thống phức tạp.
* **Tham gia Sự kiện Công nghệ & Đóng góp Bài viết Chuyên môn:**
  * Tham gia sự kiện cộng đồng **First Cloud AI Journey Meetup** (24/10/2026) tại Văn phòng AWS Việt Nam (Bitexco Lầu 26).
  * Nghiên cứu và xuất bản bài viết chuyên sâu **Blog 1** về **AWS Continuum for Code Vulnerabilities** trên nhóm Facebook AWS Study Group - First Cloud Journey.
* **Tổng kết Tuần 7, Viết Worklog & Làm Project:** Hệ thống hóa toàn bộ kiến thức, hoàn thiện bài viết và tiếp tục đẩy mạnh đề xuất đồ án.

