---
title: "Tuần 7"
date: 2026-10-26
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 7:

* Làm chủ các kỹ thuật giám sát hạ tầng nâng cao với **Amazon CloudWatch Advanced Workshop**: tính toán chỉ số với **Metric Math**, truy vấn động với **Search Expressions**, chuẩn hóa hiển thị bằng **Dynamic Labels**.
* Ứng dụng **AWS Systems Manager Session Manager** kết nối máy chủ an toàn không cần SSH, phát sinh nhật ký giả lập và phân tích chuyên sâu với **CloudWatch Logs Insights**.
* Xây dựng cơ chế trích xuất chỉ số định lượng từ nhật ký dạng text bằng **Metric Filter**, kích hoạt cảnh báo tức thời với **CloudWatch Alarm** qua **Amazon SNS** và tích hợp vào **Custom Dashboard**.
* Tổng hợp báo cáo thu hoạch sự kiện **First Cloud AI Journey Meetup (24/10/2026)** và hoàn thiện bài viết kỹ thuật **Blog 1: Giới thiệu AWS Continuum for Code Vulnerabilities**.
* Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và đẩy mạnh nghiên cứu đề xuất đồ án thực tập (**Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Giám sát chuyên sâu với Amazon CloudWatch (CloudWatch Advanced Workshop):** <br>- Dựng cụm máy chủ lab tự động bằng AWS CloudFormation (`AwsWorkshopStack`). <br>- Thiết lập biểu thức tính toán Metric Math và hàm tìm kiếm động `SEARCH()`. <br>- Chuẩn hóa nhãn đồ thị với Dynamic Labels `${PROP('Dim.DimName')}`. <br>- Kết nối SSM Session Manager, chạy script phát sinh log mô phỏng (`logger.py`). <br>- Truy vấn phân tích log với CloudWatch Logs Insights và lưu Saved Query. <br>- Tạo Metric Filter `PythonAppErrors`, cảnh báo Alarm và tích hợp vào `ssmDashboard`. | 26/10/2026 | 26/10/2026 | [Amazon CloudWatch Observability Workshop](https://catalog.workshops.aws/observability/en-US/) |
| **Thứ 3** | **Giám sát tải & Tự động phản ứng sự cố với CloudWatch & SNS:** <br>- Xây dựng kịch bản kiểm thử tải máy chủ (Stress Testing) giả lập sự cố nghẽn tài nguyên. <br>- Cấu hình chính sách cảnh báo đa ngưỡng (Composite Alarms) kết hợp CPU và Memory. <br>- Tích hợp cảnh báo thời gian thực về hộp thư kỹ sư và hệ thống ChatOps qua Amazon SNS. <br>- Đánh giá độ trễ phát hiện sự cố (MTTD) và tối ưu hóa chu kỳ quét chỉ số đo lường. | 27/10/2026 | 27/10/2026 | [AWS Observability Best Practices](https://aws.amazon.com/cloudwatch/) |
| **Thứ 4** | **Tổng hợp bài thu hoạch Sự kiện First Cloud AI Journey Meetup (24/10/2026):** <br>- Hệ thống hóa 5 phiên chia sẻ chuyên sâu: Voice AI Tiếng Việt, AWS RAM, AI Pentest, Bedrock AgentCore & Kiro Crew. <br>- Rút ra các bài học về Latency Budget, Shift-Left Security và quản trị Context Window. <br>- Hoàn thiện báo cáo sự kiện kèm hình ảnh minh chứng trên website thực tập. | 28/10/2026 | 28/10/2026 | [Sự kiện đã tham gia](/vi/4-eventparticipated/) |
| **Thứ 5** | **Hoàn thiện & xuất bản Blog 1: AWS Continuum for Code Vulnerabilities:** <br>- Nghiên cứu thông báo GA ngày 22/10/2026 trên AWS News Blog về AWS Continuum. <br>- Phân tích kiến trúc Context Graph, thẩm định bằng chứng Sandbox và quy trình mở Pull Request vá lỗi tự động. <br>- Xuất bản bài viết lên nhóm Facebook AWS Study Group - First Cloud Journey và đồng bộ song ngữ vào báo cáo. | 29/10/2026 | 29/10/2026 | [Blog 1 - AWS Continuum](/vi/3-blogsposted/3.1-blog1/) |
| **Thứ 6** | **Tổng kết Tuần 7, Viết Worklog & Làm Project:** <br>- Tổng kết toàn bộ kiến thức CloudWatch Advanced, Logs Insights, Metric Math & SNS Alarms. <br>- Rà soát và hoàn thiện chi tiết nội dung, bảng thông số kỹ thuật và hình ảnh bài viết 1.7.1. <br>- Dành thời gian nghiên cứu tài liệu kiến trúc và xây dựng báo cáo Đồ án thực tập (Project Proposal). | 30/10/2026 | 30/10/2026 | [Internal Review & Project Documentation](/vi/2-proposal/) |

---

### Kết quả đạt được tuần 7:

#### 📌 Kết quả Thứ 2 (26/10/2026) - Giám sát chuyên sâu với Amazon CloudWatch:

{{% notice tip %}}
👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình hạ tầng CloudFormation, công thức Metric Math, các câu lệnh Logs Insights, bộ lọc Metric Filter và trọn bộ 20 hình ảnh minh chứng được trình bày tại: **[1.7.1. Giám sát chuyên sâu với Amazon CloudWatch (CloudWatch Advanced Workshop)](1.7.1-cloudwatch-advanced/)**.
{{% /notice %}}

- **Tự động hóa triển khai hạ tầng với CloudFormation:** Khởi tạo thành công cụm máy chủ kiểm thử độc lập (Instance-A đến Instance-E) với trạng thái `CREATE_COMPLETE` thông qua mẫu template `AwsWorkshopStack`.
- **Làm chủ tính toán chỉ số với Metric Math & Search Expressions:** Xây dựng các đồ thị giám sát thông minh tự động co giãn và cập nhật máy chủ mới qua hàm `SEARCH('used', 'Average', 300)` và `SEARCH('disk_used_percent', 'Average')`.
- **Chuẩn hóa giao diện trực quan với Dynamic Labels:** Sử dụng thuộc tính `${PROP('Dim.DimName')}` để hiển thị tên máy chủ ngắn gọn, trực quan thay cho mã định danh ID phức tạp.
- **Phân tích nhật ký chuyên sâu với CloudWatch Logs Insights:** Viết các truy vấn lọc Regex bóc tách lỗi `/ERROR/`, cảnh báo `/WARN/`, thống kê phân bố lỗi theo luồng log (`@logStream`) và vẽ đồ thị chuỗi thời gian phân nhóm `bin(5m)`.
- **Cảnh báo tự động và bảng điều khiển vận hành:** Trích xuất chỉ số lỗi từ log qua Metric Filter `PythonAppErrors`, kích hoạt cảnh báo qua Amazon SNS Topic và thiết kế Dashboard điều hành tập trung `ssmDashboard`.

---

#### 📌 Kết quả Thứ 3 (27/10/2026) - Giám sát tải & Tự động phản ứng sự cố với CloudWatch & SNS:

- **Mô phỏng sự cố tải hệ thống:** Triển khai các kịch bản kiểm thử tải giả lập tình huống CPU tăng đột biến trên máy chủ EC2.
- **Hệ thống cảnh báo đa tầng:** Thiết lập cơ chế gửi thông báo qua Amazon Simple Notification Service (SNS) giúp đội ngũ vận hành phản ứng nhanh chóng với sự cố.
- **Tối ưu hóa thời gian phát hiện lỗi (MTTD):** Giảm thiểu thời gian phát hiện và khoanh vùng sự cố hạ tầng nhờ cơ chế quét và báo động chủ động.

---

#### 📌 Kết quả Thứ 4 & Thứ 5 (28/10 – 29/10/2026) - Tổng kết FCAJ Meetup & Xuất bản Blog 1:

- **Hoàn thiện báo cáo First Cloud AI Journey Meetup:** Tổng hợp đầy đủ kiến thức thực chiến từ 5 phiên chia sẻ về Voice AI, AWS RAM, Frontier Security Agent, Bedrock AgentCore và Kiro Crew cùng trọn bộ hình ảnh tại Bitexco Lầu 26.
- **Xuất bản Blog 1 (AWS Continuum for Code Vulnerabilities):** Phân tích chi tiết kiến trúc bảo mật tự chủ (Autonomous DevSecOps), đồ thị ngữ cảnh 2 chiều, kiểm chứng lỗ hổng trong Sandbox cô lập và cơ chế tạo Pull Request vá lỗi theo nguyên tắc Human-in-the-Loop.

---

#### 📌 Kết quả Thứ 6 (30/10/2026) - Tổng kết Tuần 7, Viết Worklog & Làm Project:

{{% notice tip %}}
👉 **Kế hoạch định kỳ Thứ 6:** Dành trọn vẹn ngày Thứ 6 cho 3 trọng tâm chính: (1) Tổng kết kiến thức đã tích lũy trong tuần; (2) Hoàn thiện hệ thống Worklog và minh chứng thực hành; (3) Nghiên cứu và triển khai Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
{{% /notice %}}

* **1. Tổng kết kiến thức tuần 7:**
  * Hệ thống hóa toàn bộ các kỹ thuật giám sát hiện đại: **Metric Math**, **Search Expressions**, **Dynamic Labels**, **Logs Insights** và **Metric Filters**.
  * Nắm vững quy trình vận hành và ứng cứu sự cố không cần mở cổng SSH truyền thống nhờ **AWS Systems Manager Session Manager**.
  * Củng cố kiến trúc cảnh báo tự động thông qua **CloudWatch Alarms** và **Amazon SNS**.
* **2. Hoàn thiện hệ thống Worklog:**
  * Rà soát toàn diện nội dung bài viết **1.7.1**, bảo đảm trọn bộ 20 hình ảnh minh chứng hiển thị sắc nét, chính xác.
  * Đảm bảo tính chuẩn hóa song ngữ (Tiếng Việt và Tiếng Anh) và tính toàn vẹn của các liên kết nội bộ.
* **3. Nghiên cứu & Triển khai Project (Proposal):**
  * Tích hợp kiến trúc giám sát CloudWatch Advanced, Logs Insights và Metric Filters vào thiết kế giải pháp của Đồ án thực tập (**[Project Proposal](/vi/2-proposal/)**).
  * Chuẩn bị các phương án tối ưu độ trễ phát hiện sự cố cho hệ thống production trong đề xuất dự án.

---

### Mục tiêu cho tuần sau (Tuần 8):

* **Hạ tầng dưới dạng mã (IaC) với AWS CloudFormation (000037) & AWS CDK:**
  * Làm chủ cấu trúc template YAML, hàm nội tại, Nested Stacks, Change Sets, Drift Detection và lập trình hạ tầng với AWS CDK (TypeScript, L1/L2/L3 Constructs).
* **Vận hành tập trung với AWS Systems Manager (000024) & Bảo vệ dữ liệu với AWS Backup (000038):**
  * Kết nối máy chủ không cổng SSH qua Session Manager, chạy lệnh hàng loạt bằng Run Command, mã hóa bí mật với Parameter Store và khóa sao lưu chống ransomware với Backup Vault Lock (WORM).
* **Tổng kết Tuần 8, Viết Worklog & Làm Project:** Hệ thống hóa kiến thức IaC và đóng gói hạ tầng Capstone Project bằng mẫu template tự động.
