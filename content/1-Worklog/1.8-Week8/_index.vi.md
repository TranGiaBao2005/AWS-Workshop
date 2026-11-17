---
title: "Tuần 8"
date: 2026-11-02
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 8:

- Tiếp cận tư duy quản trị **Hạ tầng dưới dạng mã (Infrastructure as Code - IaC)** để tự động hóa việc khởi tạo, kiểm soát phiên bản và tái sử dụng môi trường đám mây trên AWS.
- Dành trọn vẹn **2 ngày chuyên sâu (Thứ 2 & Thứ 3)** để làm chủ toàn diện **AWS CloudFormation** (Workshop 000037): từ cấu trúc mẫu khai báo YAML, hàm nội tại, khởi tạo ngăn xếp đến các kỹ thuật nâng cao như Nested Stacks, Change Sets và Drift Detection.
- Làm quen với khung phát triển hạ tầng hiện đại **AWS Cloud Development Kit (AWS CDK)**, mô hình hóa kiến trúc bằng ngôn ngữ lập trình TypeScript/Python thông qua các tầng cấu trúc trừu tượng (L1, L2, L3 Constructs).
- Quản trị vận hành máy chủ từ xa an toàn không cần mở port SSH/RDP với **AWS Systems Manager (SSM)** (Workshop 000024) và quản lý bí mật cấu hình với Parameter Store.
- Thiết lập chiến lược sao lưu dữ liệu tập trung, chống mã độc tống tiền (Ransomware) với **AWS Backup** (Workshop 000038).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và chuyển đổi toàn bộ hạ tầng của đồ án (**Capstone Project Proposal**) sang dạng template IaC.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **AWS CloudFormation (Phần 1) - Cấu trúc Template & Khởi tạo Ngăn xếp:** <br>- Nắm vững cấu trúc template mẫu chuẩn: AWSTemplateFormatVersion, Parameters, Resources, Outputs. <br>- Sử dụng các hàm nội tại: `!Ref`, `!Sub`, `!GetAtt`, `!Join` để liên kết động tài nguyên. <br>- Khởi tạo ngăn xếp hạ tầng mạng VPC 2 AZs, 4 Subnets và Route Tables hoàn toàn tự động. | 02/11/2026 | 02/11/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Thứ 3** | **AWS CloudFormation (Phần 2) - Nested Stacks, Change Sets & Drift Detection:** <br>- Thiết kế kiến trúc mô-đun hóa với ngăn xếp lồng nhau (Nested Stacks: Network, DB, App). <br>- Quản lý rủi ro khi cập nhật hạ tầng production thông qua tính năng Change Sets. <br>- Quét và phát hiện sai lệch cấu hình thực tế so với mẫu thiết kế với Drift Detection. <br>- Cấu hình bảo vệ chống xóa ngăn xếp nhầm (Termination Protection). | 03/11/2026 | 03/11/2026 | [AWS CloudFormation (000037)](https://000037.awsfcaj.com/) |
| **Thứ 4** | **Lập trình hạ tầng đám mây hiện đại với AWS CDK:** <br>- Thiết lập môi trường AWS CDK CLI, khởi tạo project (`cdk init app --language typescript`). <br>- Phân biệt 3 cấp độ Construct: L1 (CfnResource), L2 (AWS-managed best practices), L3 (Architectural Patterns). <br>- Thực thi quy trình phát triển: Biên dịch template (`cdk synth`), so sánh sai biệt (`cdk diff`) và triển khai (`cdk deploy`). | 04/11/2026 | 04/11/2026 | [Cloud Journey - Operations](https://cloudjourney.awsfcaj.com/3-optimize/) |
| **Thứ 5** | **Vận hành tập trung với AWS Systems Manager & Sao lưu AWS Backup:** <br>- Kết nối máy chủ EC2 an toàn không cần mở port SSH (22) qua SSM Session Manager. <br>- Thực thi script hàng loạt trên quy mô lớn không cần truy cập máy ảo bằng Run Command. <br>- Lưu trữ biến môi trường và chuỗi kết nối an toàn với SSM Parameter Store (`SecureString`). <br>- Thiết lập kế hoạch sao lưu tự động với AWS Backup Vaults (WORM lock) cho EBS và RDS. | 05/11/2026 | 05/11/2026 | [SSM (000024)](https://000024.awsfcaj.com/) & [Backup (000038)](https://000038.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 8, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức IaC (CloudFormation, CDK), SSM và AWS Backup. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 8 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Đóng gói toàn bộ kiến trúc hạ tầng của Đề xuất đồ án (Proposal) thành mã CloudFormation template. | 06/11/2026 | 06/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (02/11/2026) - AWS CloudFormation (Phần 1): Cấu trúc Template & Khởi tạo Ngăn xếp

* **Ta học được những gì hôm nay?**
  * **Cấu trúc khung mẫu YAML của CloudFormation:** Hiểu rõ giải phẫu của một template chuẩn gồm: `AWSTemplateFormatVersion: '2010-09-09'`, `Description`, `Parameters` (nhận tham số linh hoạt như CIDR, Environment, InstanceType), `Mappings` (tra cứu AMI ID theo từng Region), `Conditions` (điều kiện bật/tắt tài nguyên theo môi trường Dev/Prod), `Resources` (khai báo tài nguyên bắt buộc) và `Outputs` (xuất thông số tài nguyên như VPC ID, Subnet IDs để các stack khác kế thừa).
  * **Sử dụng linh hoạt các hàm nội tại (Intrinsic Functions):**
    * `!Ref`: Tham chiếu đến tham số người dùng nhập hoặc mã định danh vật lý (Physical ID) của tài nguyên vừa tạo.
    * `!Sub`: Thay thế chuỗi động (ví dụ: `${AWS::StackName}-public-subnet-1`).
    * `!GetAtt`: Trích xuất thuộc tính chuyên sâu của tài nguyên (ví dụ: `!GetAtt MyVPC.Arn` hoặc `!GetAtt MyEC2.PrivateIp`).
    * `!Join`: Nối chuỗi với ký tự phân tách xác định.
  * **Thực hành triển khai hạ tầng mạng:** Viết một file template hoàn chỉnh `network-foundation.yaml` dài 180 dòng khai báo VPC (`10.0.0.0/16`), Internet Gateway, 2 Public Subnets (`10.0.1.0/24`, `10.0.2.0/24`), 2 Private Subnets (`10.0.10.0/24`, `10.0.20.0/24`), Route Tables và Subnet Route Table Associations.
  * **Thao tác dòng lệnh AWS CLI:**
    ```bash
    aws cloudformation create-stack \
      --stack-name fcaj-network-stack \
      --template-body file://network-foundation.yaml \
      --parameters ParameterKey=EnvironmentName,ParameterValue=Development
    aws cloudformation describe-stacks --stack-name fcaj-network-stack --query "Stacks[0].StackStatus"
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi cú pháp định dạng YAML:* Quá trình khởi tạo báo lỗi `Template format error: YAML not well-formed`. Nguyên nhân do thụt dòng khoảng trắng (indentation) không đồng đều giữa các block `Properties`. Cách xử lý: Sử dụng công cụ kiểm tra cú pháp `cfn-lint` và extension CloudFormation trên VS Code để bắt lỗi trước khi deploy.
  * *Lỗi phụ thuộc vòng (Circular Dependency):* Khi gắn Internet Gateway vào VPC bằng tài nguyên `AWS::EC2::VPCGatewayAttachment`, route `0.0.0.0/0` trỏ tới IGW bị lỗi vì IGW chưa gắn xong vào VPC. Cách xử lý: Bổ sung chỉ thị phụ thuộc tường minh `DependsOn: AttachGateway` vào tài nguyên `AWS::EC2::Route`.

---

#### 📌 Thứ 3 (03/11/2026) - AWS CloudFormation (Phần 2): Nested Stacks, Change Sets & Drift Detection

* **Ta học được những gì hôm nay?**
  * **Kiến trúc ngăn xếp lồng nhau (Nested Stacks):** Giải quyết giới hạn số lượng tài nguyên trong 1 template đơn lẻ và tách biệt trách nhiệm (Separation of Concerns). Xây dựng Root Stack (`master.yaml`) tham chiếu đến 3 child stacks được lưu trữ trên S3 Bucket: `network-stack.yaml`, `database-stack.yaml` (RDS) và `compute-stack.yaml` (EC2 & ALB) thông qua tài nguyên `AWS::CloudFormation::Stack`.
  * **Quản trị thay đổi an toàn với Change Sets:** Thay vì cập nhật trực tiếp (Direct Update) có nguy cơ làm gián đoạn hệ thống đang chạy, Change Sets cho phép xem trước danh sách tài nguyên sẽ được thêm mới (`Add`), chỉnh sửa (`Modify`), hoặc xóa bỏ (`Remove`), đặc biệt là đánh giá xem tài nguyên có bị tái tạo lại hay không (`Replacement: True/False`).
  * **Kiểm toán sai lệch cấu hình với Drift Detection:** Hiểu cơ chế quét Drift Detection giúp so sánh cấu hình thực tế hiện tại của tài nguyên trên AWS với cấu hình được định nghĩa ban đầu trong template. Nhận diện các thay đổi "chui" do quản trị viên chỉnh sửa thủ công trên giao diện web (như mở thêm port trên Security Group).
  * **Bảo vệ an toàn tài nguyên:** Kích hoạt tính năng `Termination Protection` trên Stack để ngăn chặn tuyệt đối nguy cơ nhân sự bấm nhầm nút Delete Stack làm mất sạch hạ tầng Production.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi kẹt trạng thái `UPDATE_ROLLBACK_FAILED`:* Khi cập nhật thay đổi thông số RDS Subnet Group không tương thích, stack rollback thất bại và rơi vào trạng thái khóa cứng `UPDATE_ROLLBACK_FAILED`. Cách xử lý: Phân tích sự kiện lỗi (Stack Events), sử dụng tùy chọn `Continue Update Rollback` và bỏ qua tài nguyên gặp sự cố (Skip Resources) để đưa stack về trạng thái ổn định `UPDATE_ROLLBACK_COMPLETE`.

---

#### 📌 Thứ 4 (04/11/2026) - Lập trình hạ tầng hiện đại với AWS Cloud Development Kit (CDK)

* **Ta học được những gì hôm nay?**
  * **Tư duy Software-Defined Infrastructure:** Tạm biệt các file JSON/YAML dài dòng, chuyển sang sử dụng TypeScript để định nghĩa hạ tầng bằng lập trình hướng đối tượng (OOP), tận dụng sức mạnh của vòng lặp, câu lệnh điều kiện, biến môi trường và kiểm tra lỗi kiểu dữ liệu tại thời điểm biên dịch (Compile-time Type Checking).
  * **Hệ thống cấp bậc Constructs:**
    * *Level 1 (L1 - Cfn Resources):* Ánh xạ trực tiếp 1-1 với tài nguyên CloudFormation thuần (ví dụ: `CfnVPC`).
    * *Level 2 (L2 - AWS Managed):* Đóng gói sẵn các thiết lập mặc định chuẩn bảo mật của AWS, tự động tính toán CIDR, cấu hình Route Tables và Security Groups chỉ với vài dòng mã (ví dụ: `new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 })`).
    * *Level 3 (L3 - Architectural Patterns):* Đóng gói giải pháp kiến trúc hoàn chỉnh đa dịch vụ (ví dụ: `ApplicationLoadBalancedFargateService`).
  * **Quy trình làm việc với CDK CLI:**
    ```bash
    cdk bootstrap aws://887086382708/us-east-1  # Khởi tạo S3 bucket & IAM Roles cho CDK
    cdk synth                                    # Biên dịch code TypeScript sang CloudFormation template
    cdk diff                                     # So sánh thay đổi giữa code local và stack trên AWS
    cdk deploy                                   # Tự động đóng gói và triển khai hạ tầng
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi thiếu môi trường Bootstrap:* Chạy lệnh `cdk deploy` báo lỗi `This stack uses assets, so the toolkit stack must be deployed to the environment`. Cách xử lý: Chạy lệnh `cdk bootstrap` một lần duy nhất cho tài khoản và Region để khởi tạo stack `CDKToolkit` lưu trữ assets.
  * *Xung đột phiên bản thư viện:* Lỗi xung đột version giữa `aws-cdk-lib` và `@aws-cdk` legacy. Cách xử lý: Chuẩn hóa toàn bộ project sang AWS CDK v2 với thư viện duy nhất `aws-cdk-lib`.

---

#### 📌 Thứ 5 (05/11/2026) - Vận hành tập trung với AWS Systems Manager & Sao lưu với AWS Backup

* **Ta học được những gì hôm nay?**
  * **Quản trị an toàn tuyệt đối với SSM Session Manager:** Loại bỏ hoàn toàn cổng 22 (SSH) trên Security Group và không cần cấp phát Public IP cho máy chủ. Kết nối trực tiếp vào terminal của máy ảo trong Private Subnet qua giao diện trình duyệt hoặc AWS CLI, mọi thao tác gõ lệnh đều được ghi lại (Session Logging) vào S3 và CloudWatch Logs phục vụ kiểm toán bảo mật.
  * **Thực thi lệnh quy mô lớn với SSM Run Command:** Chạy các lệnh bảo trì, cập nhật phần mềm hoặc thu thập thông tin đồng loạt trên 50 máy chủ cùng lúc chỉ với 1 thao tác mà không cần đăng nhập từng máy.
  * **Bảo mật bí mật với SSM Parameter Store:** Lưu trữ chuỗi kết nối CSDL, API Key với kiểu dữ liệu `SecureString` được mã hóa bởi khóa AWS KMS. Ứng dụng đọc cấu hình qua IAM Role mà không cần lưu cứng (hard-code) mật khẩu trong file cấu hình.
  * **Bảo vệ dữ liệu tập trung với AWS Backup:** Khởi tạo Backup Vault được khóa bằng chính sách `Vault Lock` theo chuẩn WORM (Write Once, Read Many) ngăn chặn việc xóa bản sao lưu ngay cả bởi tài khoản Root. Thiết lập Backup Plan tự động chụp snapshot hàng ngày cho EBS và RDS với chu kỳ lưu trữ 30 ngày.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Máy ảo EC2 không hiển thị trong danh sách SSM Managed Nodes:* Sau khi bật máy ảo, Session Manager báo `Target Not Connected`. Nguyên nhân: Máy ảo chưa được gán IAM Instance Profile chứa quyền `AmazonSSMManagedInstanceCore` và máy chủ nằm trong Private Subnet chưa có route ra Internet hoặc chưa có VPC Endpoints cho SSM (`ssm`, `ssmmessages`, `ec2messages`). Cách xử lý: Gán IAM Role phù hợp và tạo VPC Endpoints để máy chủ liên lạc nội bộ với SSM Agent.

---

#### 📌 Thứ 6 (06/11/2026) - Tổng kết Tuần 8, Hoàn thiện Worklog & Phát triển Capstone Project

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa toàn bộ chu trình IaC:** Liên kết chặt chẽ quy trình từ thiết kế kiến trúc hạ tầng bằng mã (CloudFormation/CDK) ➔ Quản trị vận hành máy chủ không cổng mở (SSM) ➔ Bảo vệ dữ liệu và phòng ngừa thảm họa (AWS Backup).
  * **Kỹ năng kiểm toán chi phí:** Thực thi lệnh `cdk destroy` và `aws cloudformation delete-stack` để dọn dẹp sạch sẽ toàn bộ tài nguyên thử nghiệm phát sinh trong tuần, xác nhận trên Cost Explorer không còn tài nguyên nhàn rỗi.
  * **Phát triển Đề xuất Đồ án (Capstone Project Proposal):** Chuyển đổi toàn bộ sơ đồ kiến trúc thủ công của đồ án tốt nghiệp sang dạng mẫu template AWS CloudFormation mô-đun hóa, sẵn sàng cho việc triển khai tự động trong môi trường thực tế.

