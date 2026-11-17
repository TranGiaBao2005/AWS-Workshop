---
title: "Worklog Tuần 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 8:

- Tiếp cận tư duy quản trị **Hạ tầng dưới dạng mã (Infrastructure as Code - IaC)** để tự động hóa việc khởi tạo, kiểm soát phiên bản và tái sử dụng môi trường đám mây.
- Thực hành triển khai ngăn xếp tài nguyên với **AWS CloudFormation** (Workshop 000037) thông qua các mẫu khai báo YAML/JSON chuẩn hóa.
- Làm quen với khung phát triển hạ tầng hiện đại **AWS Cloud Development Kit (AWS CDK)**, mô hình hóa kiến trúc bằng ngôn ngữ lập trình quen thuộc (TypeScript/Python).
- Quản trị vận hành máy chủ từ xa an toàn và tự động hóa cập nhật bản vá với **AWS Systems Manager (SSM)** (Workshop 000024).
- Thiết lập chiến lược sao lưu dữ liệu tập trung, chống mã độc tống tiền (Ransomware) với **AWS Backup** (Workshop 000038).
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và chuyển đổi các tài nguyên thủ công của đồ án (**Capstone Project Proposal**) sang dạng template IaC.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Quản trị hạ tầng tự động hóa với AWS CloudFormation:** <br>- Cấu trúc mẫu khai báo (Template Sections: AWSTemplateFormatVersion, Parameters, Resources, Outputs). <br>- Khởi tạo và cập nhật ngăn xếp tài nguyên (Stack & Nested Stacks). <br>- Kiểm tra thay đổi trước khi triển khai với Change Sets và phát hiện sai lệch cấu hình (Drift Detection). | 02/11/2026 | 02/11/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Thứ 3** | **Lập trình hạ tầng đám mây hiện đại với AWS CDK:** <br>- Thiết lập môi trường AWS CDK CLI và cấu trúc project (`cdk init app`). <br>- Xây dựng tài nguyên VPC, Subnet, Security Groups bằng Construct bậc cao (L2/L3 Constructs). <br>- Biên dịch (`cdk synth`), so sánh sai biệt (`cdk diff`) và tự động triển khai (`cdk deploy`). | 03/11/2026 | 03/11/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Thứ 4** | **Vận hành & Quản trị máy chủ tập trung với AWS Systems Manager (SSM):** <br>- Kết nối máy chủ bảo mật không cần mở port SSH/RDP qua SSM Session Manager. <br>- Thực thi lệnh hàng loạt trên quy mô lớn không cần đăng nhập trực tiếp bằng Run Command. <br>- Quản lý cấu hình nhạy cảm và chuỗi kết nối an toàn với SSM Parameter Store (SecureString). | 04/11/2026 | 04/11/2026 | [AWS Systems Manager (000024)](https://000024.awsfcaj.com/) |
| **Thứ 5** | **Bảo vệ dữ liệu tập trung & Phòng ngừa thảm họa với AWS Backup:** <br>- Khởi tạo Backup Vault và cấu hình khóa bảo vệ WORM (Write Once, Read Many). <br>- Lập kế hoạch sao lưu định kỳ tự động (Backup Plans) cho Amazon EBS, RDS và EFS. <br>- Kiểm thử quy trình phục hồi dữ liệu từ bản sao lưu và nhân bản liên vùng (Cross-Region Backup). | 05/11/2026 | 05/11/2026 | [AWS Backup Workshop (000038)](https://000038.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 8, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức IaC (CloudFormation, CDK), SSM và AWS Backup. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 8 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Đóng gói toàn bộ kiến trúc hạ tầng của Đề xuất đồ án (Proposal) thành mã CloudFormation template. | 06/11/2026 | 06/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 8:

#### 📌 Kết quả Thứ 2 (02/11/2026) - Quản trị hạ tầng tự động hóa với AWS CloudFormation:
* **Tự động hóa vòng đời hạ tầng:** Định nghĩa toàn bộ hạ tầng mạng (VPC 2 AZs, 4 Subnets, Route Tables) bằng mẫu tệp YAML duy nhất. Quá trình khởi tạo và hủy tài nguyên diễn ra hoàn toàn tự động, loại bỏ 100% lỗi sai sót thủ công khi thao tác trên Console.
* **Kiểm soát thay đổi an toàn:** Làm chủ cơ chế **Change Sets** để xem trước tác động hạ tầng trước khi phê duyệt cập nhật; sử dụng tính năng **Drift Detection** để phát hiện kịp thời các chỉnh sửa ngoài luồng (out-of-band changes) tác động vào hạ tầng production.

#### 📌 Kết quả Thứ 3 (03/11/2026) - Lập trình hạ tầng đám mây hiện đại với AWS CDK:
* **Nâng tầm trải nghiệm IaC:** Khai thác sức mạnh của ngôn ngữ lập trình bậc cao với hệ thống kiểu tĩnh (Type Safety), tự động hoàn thiện mã (IntelliSense) và kiểm thử đơn vị (Unit Testing) cho hạ tầng đám mây.
* **Tối ưu hóa số dòng mã:** Nhờ các thư viện L2 Constructs định sẵn best practices của AWS, cấu hình cụm máy chủ tự động co giãn và cân bằng tải chỉ cần ít hơn 50 dòng code TypeScript so với hơn 400 dòng JSON/YAML thuần túy.

#### 📌 Kết quả Thứ 4 (04/11/2026) - Vận hành tập trung với AWS Systems Manager:
* **Bảo mật tuyệt đối kênh truy cập:** Triệt tiêu hoàn toàn nhu cầu mở cổng 22 (SSH) hay 3389 (RDP) trên Security Group. Mọi thao tác kết nối được mã hóa đầu cuối thông qua AWS KMS và ghi vết đầy đủ trên AWS CloudTrail.
* **Quản trị cấu hình tập trung:** Tách rời cấu hình bí mật khỏi mã nguồn ứng dụng bằng cách lưu trữ các chuỗi kết nối cơ sở dữ liệu và API keys vào **SSM Parameter Store** với chế độ mã hóa `SecureString`.

#### 📌 Kết quả Thứ 5 (05/11/2026) - Bảo vệ dữ liệu tập trung với AWS Backup:
* **Tập trung hóa chính sách bảo vệ dữ liệu:** Thiết lập chính sách sao lưu tự động cho toàn bộ cụm cơ sở dữ liệu Amazon RDS và máy ảo EC2 theo lịch trình hàng ngày, thời gian lưu trữ 30 ngày và tự động chuyển về bộ lưu trữ lạnh (Cold Storage) sau 7 ngày.
* **Sẵn sàng ứng phó thảm họa:** Kiểm thử thành công quy trình khôi phục bản sao lưu dữ liệu sang vùng thứ hai (`ap-southeast-1` sang `ap-southeast-2`), đảm bảo đáp ứng các chỉ số RPO (Recovery Point Objective) dưới 15 phút và RTO (Recovery Time Objective) dưới 30 phút.
