---
title: "Tuần 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---


### Mục tiêu tuần 8:

- Tiếp cận tư duy quản trị **Hạ tầng dưới dạng mã (Infrastructure as Code - IaC)** để tự động hóa khởi tạo, kiểm soát phiên bản và tái sử dụng môi trường đám mây trên AWS.
- Làm chủ **AWS CloudFormation** (Workshop 000037): cấu trúc mẫu YAML, hàm nội tại, Nested Stacks, Change Sets, Drift Detection và Termination Protection.
- Lập trình hạ tầng hiện đại bằng **AWS Cloud Development Kit (AWS CDK)** với TypeScript qua 3 cấp độ Constructs (L1, L2, L3).
- Vận hành máy chủ từ xa an toàn không cần mở port SSH với **AWS Systems Manager (SSM)** (Workshop 000024) và thiết lập chiến lược sao lưu chống ransomware với **AWS Backup** (Workshop 000038).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và đóng gói hạ tầng đồ án (**Capstone Project**) dưới dạng mã IaC.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Hạ tầng dưới dạng mã với AWS CloudFormation:** <br>- Nắm vững cấu trúc YAML: Parameters, Mappings, Conditions, Resources, Outputs và hàm nội tại (`!Ref`, `!Sub`, `!GetAtt`). <br>- Xây dựng kiến trúc mô-đun hóa bằng Nested Stacks (Network, DB, App). <br>- Quản trị cập nhật an toàn với Change Sets, quét sai lệch Drift Detection và bật Termination Protection. | 02/11/2026 | 02/11/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Thứ 3** | **Lập trình hạ tầng đám mây hiện đại với AWS CDK:** <br>- Cài đặt CDK CLI, khởi tạo project (`cdk init app --language typescript`) và chạy `cdk bootstrap`. <br>- Phân biệt và vận dụng 3 cấp độ Construct: L1 (CfnResource), L2 (AWS best practices), L3 (Patterns). <br>- Thực thi chu trình `cdk synth`, `cdk diff`, `cdk deploy` và `cdk destroy`. | 03/11/2026 | 03/11/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Thứ 4** | **Vận hành tập trung không cổng SSH với AWS Systems Manager (SSM):** <br>- Kết nối máy chủ trong Private Subnet an toàn qua SSM Session Manager kèm Session Logging. <br>- Thực thi tác vụ bảo trì hàng loạt trên nhiều máy chủ bằng SSM Run Command. <br>- Quản trị cấu hình và bí mật mã hóa KMS với SSM Parameter Store (`SecureString`). | 04/11/2026 | 04/11/2026 | [AWS Systems Manager (000024)](https://000024.awsfcaj.com/) |
| **Thứ 5** | **Chiến lược sao lưu & Phục hồi thảm họa với AWS Backup:** <br>- Khởi tạo Backup Vault và kích hoạt khóa bảo vệ WORM (`Vault Lock`) chống xóa dữ liệu. <br>- Thiết lập Backup Plan tự động chụp snapshot hàng ngày cho Amazon EBS và Amazon RDS theo thẻ Tag. <br>- Diễn tập khôi phục dữ liệu (Restore Drill) và đánh giá chỉ số RTO/RPO. | 05/11/2026 | 05/11/2026 | [AWS Backup (000038)](https://000038.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 8, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ chu trình IaC (CloudFormation, CDK), SSM và AWS Backup. <br>- **Làm Worklog:** Chuẩn hóa báo cáo Worklog Tuần 8 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Đóng gói sơ đồ kiến trúc hạ tầng của Đề xuất đồ án thành template IaC tái sử dụng. | 06/11/2026 | 06/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (02/11/2026) - Hạ tầng dưới dạng mã toàn diện với AWS CloudFormation

* **Ta học được những gì hôm nay?**
  * **Cấu trúc template YAML & Hàm nội tại (Intrinsic Functions):** Thiết kế file `network-foundation.yaml` định nghĩa VPC (`10.0.0.0/16`), 2 Public Subnets, 2 Private Subnets, IGW và Route Tables; liên kết động các tài nguyên qua `!Ref`, `!Sub`, `!GetAtt` và `!Join`.
  * **Mô-đun hóa với Nested Stacks & Kiểm soát thay đổi:** Phân tách Root Stack tham chiếu đến các child stack (`network`, `database`, `compute`) lưu trên S3. Sử dụng **Change Sets** xem trước danh sách tài nguyên bị `Add / Modify / Replace`, chạy **Drift Detection** phát hiện chỉnh sửa thủ công ngoài template và bật **Termination Protection**.
  * **Thao tác dòng lệnh AWS CLI:**
    ```bash
    aws cloudformation create-stack \
      --stack-name fcaj-network-stack \
      --template-body file://network-foundation.yaml \
      --parameters ParameterKey=EnvironmentName,ParameterValue=Development
    aws cloudformation detect-stack-drift --stack-name fcaj-network-stack
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi phụ thuộc khi tạo Route trỏ tới IGW & lỗi `UPDATE_ROLLBACK_FAILED`:* Bổ sung `DependsOn: AttachGateway` cho tài nguyên `AWS::EC2::Route` để đảm bảo đúng thứ tự khởi tạo, và dùng `Continue Update Rollback` (Skip Resources) khi gỡ kẹt stack gặp sự cố Subnet Group.

---

#### 📌 Thứ 3 (03/11/2026) - Lập trình hạ tầng hiện đại với AWS CDK

* **Ta học được những gì hôm nay?**
  * **Tư duy Software-Defined Infrastructure:** Dùng TypeScript định nghĩa hạ tầng bằng vòng lặp, điều kiện và kiểm tra kiểu dữ liệu ngay lúc biên dịch (Compile-time Type Checking).
  * **Phân tầng Constructs:**
    * *L1 (`Cfn*`):* Ánh xạ 1-1 tài nguyên CloudFormation thuần.
    * *L2 (AWS Managed):* Đóng gói best practices bảo mật và mạng mặc định (ví dụ `new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 })`).
    * *L3 (Patterns):* Đóng gói kiến trúc đa dịch vụ hoàn chỉnh như `ApplicationLoadBalancedFargateService`.
  * **Chu trình triển khai CDK CLI:**
    ```bash
    cdk bootstrap aws://887086382708/us-east-1
    cdk synth && cdk diff && cdk deploy
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi thiếu Bootstrap Stack & xung đột gói CDK v1/v2:* Chạy `cdk bootstrap` khởi tạo stack `CDKToolkit` cho môi trường đích và chuẩn hóa toàn bộ dependency sang thư viện duy nhất `aws-cdk-lib` (CDK v2).

---

#### 📌 Thứ 4 (04/11/2026) - Vận hành tập trung không cổng SSH với AWS Systems Manager

* **Ta học được những gì hôm nay?**
  * **Zero-Trust Remote Access với SSM Session Manager:** Đóng hoàn toàn cổng 22 (SSH) trên Security Group và truy cập terminal của EC2 trong Private Subnet trực tiếp qua AWS Console/CLI, ghi toàn bộ lịch sử phiên (Session Logging) vào S3 & CloudWatch Logs.
  * **Tự động hóa cụm máy chủ với Run Command & Parameter Store:** Chạy kịch bản cập nhật hệ điều hành đồng loạt trên nhiều EC2 gắn thẻ mục tiêu qua Run Command; lưu trữ chuỗi kết nối và biến nhạy cảm dưới dạng `SecureString` mã hóa KMS trong Parameter Store thay vì hard-code.
* **Khó khăn gặp phải & Cách xử lý:**
  * *EC2 không hiện trong danh sách SSM Managed Nodes:* Gắn IAM Instance Profile chứa policy `AmazonSSMManagedInstanceCore` và cấu hình VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) cho Private Subnet không có NAT Gateway.

---

#### 📌 Thứ 5 (05/11/2026) - Chiến lược sao lưu & Phục hồi thảm họa với AWS Backup

* **Ta học được những gì hôm nay?**
  * **Quản trị sao lưu tập trung với AWS Backup:** Thiết lập Backup Plan tự động sao lưu EBS Volumes và Amazon RDS theo Tag (`Backup=Daily`) với chu kỳ lưu giữ 30 ngày và chính sách chuyển lạnh (Cold Storage).
  * **Phòng chống Ransomware với Vault Lock (WORM):** Áp dụng cơ chế *Write Once, Read Many* cho Backup Vault, đảm bảo bản sao lưu không thể bị xóa sớm ngay cả khi tài khoản quản trị bị xâm nhập.
  * **Diễn tập khôi phục (Restore Drill):** Khôi phục thành công một EBS Volume thử nghiệm từ Recovery Point để xác minh tính toàn vẹn dữ liệu và ước lượng thực tế thời gian phục hồi (RTO).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Backup Job không nhận diện được tài nguyên cần sao lưu:* Nguyên nhân do IAM Service Role cho AWS Backup thiếu quyền hoặc sai chữ hoa/thường trong điều kiện Tag Selection. Cách xử lý: Kiểm tra lại Tag chính xác (`Key`/`Value` case-sensitive) và gắn `AWSBackupServiceRolePolicyForBackup`.

---

#### 📌 Thứ 6 (06/11/2026) - Tổng kết Tuần 8, Hoàn thiện Worklog & Phát triển Capstone Project

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa chu trình IaC & Vận hành:** Kết nối trọn vẹn quy trình từ định nghĩa hạ tầng bằng mã (CloudFormation/CDK) ➔ quản trị vận hành không mở port (SSM) ➔ bảo vệ dữ liệu chuẩn doanh nghiệp (AWS Backup).
  * **Kiểm toán dọn dẹp tài nguyên:** Thực thi `cdk destroy` và `aws cloudformation delete-stack`, xác nhận trên AWS Billing/Cost Explorer không còn tài nguyên thử nghiệm chạy ngầm.
  * **Đóng gói hạ tầng Capstone Project:** Chuyển đổi khung hạ tầng mạng và máy chủ của đồ án sang mẫu template IaC mô-đun hóa.

---

### Mục tiêu cho tuần sau (Tuần 9):

* **Di trú hạ tầng & CSDL (Cloud Migration):** Áp dụng khung 7Rs, thực hành VM Import/Export (000027), AWS MGN, AWS DMS (000031) & SCT.
* **Mạng mở rộng lai & Lưu trữ khối lớn:** Triển khai AWS Transit Gateway (Hub-and-Spoke), AWS DataSync và AWS Storage Gateway.

