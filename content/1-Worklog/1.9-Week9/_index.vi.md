---
title: "Tuần 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 9:

- Nghiên cứu và phân loại các chiến lược chuyển dịch đám mây theo phương pháp luận chuẩn của AWS: **7Rs Migration Strategies** (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate).
- Dành **2 ngày chuyên sâu (Thứ 2 & Thứ 3)** làm chủ toàn diện các giải pháp di trú máy chủ vật lý và máy chủ ảo: từ công cụ chuyển đổi ngoại tuyến **VM Import/Export** (Workshop 000027) đến giải pháp sao chép dữ liệu thời gian thực mức khối **AWS Application Migration Service (AWS MGN)**.
- Triển khai di trú cơ sở dữ liệu đồng nhất và dị thể (Heterogeneous Migration) với thời gian gián đoạn tối thiểu (Near-Zero Downtime) bằng **AWS Database Migration Service (DMS)** (Workshop 000031) kết hợp **AWS Schema Conversion Tool (SCT)**.
- Xây dựng mô hình mạng doanh nghiệp mở rộng kết nối đa VPC theo kiến trúc hình sao (Hub-and-Spoke Topology) với **AWS Transit Gateway (TGW)** thay thế mô hình VPC Peering phức tạp.
- Khám phá các giải pháp tích hợp lưu trữ đám mây lai (**Hybrid Cloud Storage**) và truyền tải dữ liệu khối lượng lớn với **AWS DataSync** và **AWS Storage Gateway**.
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và xây dựng kịch bản di trú dữ liệu mẫu cho đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Di trú máy chủ (Phần 1) - Phương pháp 7Rs & VM Import/Export:** <br>- Đánh giá hiện trạng hạ tầng và phân loại tải theo 7Rs Migration Framework. <br>- Xuất file đĩa ảo VMDK/OVA từ máy ảo VMware/Hyper-V On-Premises và tải lên S3. <br>- Sử dụng AWS CLI thực thi lệnh `aws ec2 import-image` chuyển đổi thành Custom AMI. <br>- Khởi chạy máy chủ EC2 từ AMI mới tạo và kiểm tra tính toàn vẹn ứng dụng. | 09/11/2026 | 09/11/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) |
| **Thứ 3** | **Di trú máy chủ (Phần 2) - Sao chép thời gian thực với AWS MGN:** <br>- Cài đặt AWS Replication Agent trên máy chủ nguồn Linux/Windows. <br>- Cấu hình Replication Settings (Subnet trung chuyển, EBS volume type, mã hóa KMS). <br>- Giám sát chu trình sao chép liên tục ở tầng khối (Block-level Replication). <br>- Thực hiện diễn tập chuyển đổi (Test Cutover) và chuyển đổi chính thức (Cutover). | 10/11/2026 | 10/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 4** | **Di trú cơ sở dữ liệu đồng bộ với AWS DMS & AWS SCT:** <br>- Chuyển đổi cấu trúc bảng, kiểu dữ liệu và ràng buộc bằng AWS Schema Conversion Tool. <br>- Khởi tạo DMS Replication Instance, cấu hình Source Endpoint và Target RDS MySQL Endpoint. <br>- Chạy tác vụ di trú Full Load kết hợp sao chép thay đổi thời gian thực (CDC - Change Data Capture). | 11/11/2026 | 11/11/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Thứ 5** | **Mạng doanh nghiệp tập trung với AWS Transit Gateway & AWS DataSync:** <br>- Khởi tạo AWS Transit Gateway làm đầu mối định tuyến tập trung đa VPC. <br>- Gắn kết các VPC chức năng (VPC Attachments: Dev, Prod, Shared Services). <br>- Thiết lập bảng định tuyến riêng biệt kiểm soát luồng giao tiếp chéo giữa các VPC. <br>- Đồng bộ hóa dữ liệu tệp tin dung lượng lớn từ On-Premises lên S3 với AWS DataSync. | 12/11/2026 | 12/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 6** | **Tổng kết Tuần 9, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ phương pháp luận 7Rs, công cụ di trú (MGN, DMS) và kiến trúc TGW. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 9 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Xây dựng kế hoạch di trú chi tiết từ hạ tầng Legacy sang kiến trúc AWS cho Đề xuất đồ án. | 13/11/2026 | 13/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (09/11/2026) - Di trú máy chủ (Phần 1): Phương pháp 7Rs & VM Import/Export

* **Ta học được những gì hôm nay?**
  * **Phương pháp luận di trú AWS 7Rs:** Phân tích bản chất từng chiến lược:
    * *Rehost (Lift-and-shift):* Chuyển nguyên trạng máy chủ lên EC2 mà không thay đổi kiến trúc mã nguồn.
    * *Replatform (Lift-tinker-and-shift):* Tối ưu nhẹ một số thành phần (ví dụ chuyển Database tự dựng sang Amazon RDS).
    * *Refactor / Re-architect:* Tái cấu trúc hoàn toàn ứng dụng sang mô hình Cloud-Native, Serverless hoặc Microservices.
    * *Repurchase:* Chuyển sang sử dụng giải pháp SaaS thương mại.
    * *Retain:* Giữ nguyên tại chỗ do ràng buộc pháp lý hoặc chi phí.
    * *Retire:* Loại bỏ các ứng dụng thừa thãi không còn giá trị kinh doanh.
    * *Relocate:* Chuyển đổi nhanh cụm máy ảo VMware sang VMware Cloud on AWS.
  * **Quy trình kỹ thuật của VM Import/Export:**
    1. Tạo một máy ảo Linux Ubuntu thử nghiệm trên môi trường VirtualBox/VMware cục bộ.
    2. Xuất đĩa cứng của máy ảo ra định dạng file `.vmdk`.
    3. Tạo S3 Bucket `fcaj-migration-staging-887086382708` và tải file `.vmdk` lên bucket.
    4. Cấu hình IAM Role `vmimport` đính kèm Trust Policy cho dịch vụ `vmie.amazonaws.com` và Role Policy cấp quyền đọc S3, ghi EC2.
    5. Thực thi câu lệnh chuyển đổi sang AMI:
       ```bash
       aws ec2 import-image \
         --description "Ubuntu Web Server Migration" \
         --disk-containers "Format=vmdk,UserBucket={S3Bucket=fcaj-migration-staging-887086382708,S3Key=ubuntu-server.vmdk}"
       aws ec2 describe-import-image-tasks --import-task-ids import-ami-0abc123def456
       ```
    6. Khởi chạy máy chủ EC2 từ Custom AMI vừa tạo, đăng nhập và xác minh toàn bộ dịch vụ web Apache, cơ sở dữ liệu và cấu hình hệ thống hoạt động chính xác nguyên trạng.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi thiếu driver mạng/đĩa ảo khi boot EC2:* Máy ảo khởi chạy từ AMI bị kẹt màn hình boot do thiếu driver ảo hóa ENA (Elastic Network Adapter) và NVMe. Cách xử lý: Đăng nhập vào máy ảo gốc trước khi xuất file `.vmdk`, cài đặt gói kernel cập nhật và kiểm tra driver ENA hỗ trợ kiến trúc AWS Nitro.

---

#### 📌 Thứ 3 (10/11/2026) - Di trú máy chủ (Phần 2): Sao chép liên tục với AWS MGN

* **Ta học được những gì hôm nay?**
  * **Cơ chế hoạt động của AWS Application Migration Service (MGN):** Hiểu rõ MGN là giải pháp Rehost chính thức của AWS, sử dụng agent gọn nhẹ cài trực tiếp lên hệ điều hành nguồn (Source Server) để sao chép dữ liệu ở tầng block (Block-level continuous data replication) mà không làm ảnh hưởng đến hiệu năng máy chủ đang chạy.
  * **Quy trình triển khai MGN từng bước:**
    1. Thiết lập Template cấu hình sao chép (Replication Settings Template): Chọn Subnet trung chuyển (Staging Area Subnet), loại đĩa EBS chi phí thấp (gp3/sc1) và khóa mã hóa KMS.
    2. Cài đặt AWS Replication Agent trên máy chủ nguồn:
       ```bash
       wget -O ./aws-replication-installer-init.py https://aws-application-migration-service-us-east-1.s3.amazonaws.com/latest/linux/aws-replication-installer-init.py
       python3 ./aws-replication-installer-init.py --region us-east-1 --aws-access-key-id <KEY> --aws-secret-access-key <SECRET>
       ```
    3. Giám sát quá trình đồng bộ dữ liệu ban đầu (Initial Sync) chuyển sang trạng thái liên tục `Continuous Data Replication`.
    4. Tiến hành kiểm thử chuyển đổi (Launch Test Instances) trong môi trường VPC thử nghiệm để rà soát chất lượng trước ngày chuyển giao chính thức.
    5. Thực hiện cắt chuyển chính thức (Cutover): Chuyển trạng thái sang `Ready for Cutover`, tắt máy chủ nguồn và kích hoạt máy chủ EC2 đích chạy môi trường Production với thời gian ngưng trệ hệ thống chỉ dưới 3 phút.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi chặn cổng kết nối replication (TCP 1500):* Agent trên máy chủ nguồn báo lỗi `Failed to connect to replication server`. Nguyên nhân: Tường lửa On-Premises chặn cổng TCP 1500 ra Internet. Cách xử lý: Cấu hình quy tắc tường lửa (Firewall Outbound Rule) cho phép traffic TCP Port 1500 đến dải IP của AWS MGN Endpoint hoặc cấu hình kết nối qua VPN nội bộ.

---

#### 📌 Thứ 4 (11/11/2026) - Di trú & Đồng bộ cơ sở dữ liệu với AWS DMS & SCT

* **Ta học được những gì hôm nay?**
  * **Chuyển đổi lược đồ với AWS Schema Conversion Tool (SCT):** Đánh giá mức độ tương thích giữa CSDL nguồn và CSDL đích, tự động dịch mã DDL của bảng, view, store procedures và các ràng buộc toàn vẹn khóa ngoại (Foreign Keys).
  * **Cấu hình thành phần trong AWS DMS:**
    * *DMS Replication Instance:* Máy chủ trung gian đảm nhiệm việc đọc transaction log từ CSDL nguồn, chuyển đổi và ghi vào CSDL đích. Lựa chọn instance `dms.t3.medium`.
    * *Source & Target Endpoints:* Cấu hình thông tin kết nối, port và kiểm tra kết nối (Test Connection) thành công.
    * *DMS Migration Task:* Lựa chọn kiểu tác vụ di trú `Migrate existing data and replicate ongoing changes` kết hợp CDC (Change Data Capture) dựa trên MySQL Binary Log (`binlog`).
  * **Quy trình chuyển đổi:** Chạy nạp dữ liệu toàn bộ (Full Load: 100% hoàn tất) và duy trì CDC liên tục. Khi ứng dụng sẵn sàng chuyển đổi, ngắt kết nối ghi ở CSDL nguồn, chờ DMS đồng bộ các transaction cuối cùng và trỏ ứng dụng sang endpoint của Amazon RDS.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi CDC không bắt được thay đổi mới:* DMS báo lỗi `Binary logging not enabled on source database`. Cách xử lý: Cấu hình tệp `my.cnf` trên máy chủ MySQL nguồn với các tham số bắt buộc: `log-bin=mysql-bin`, `binlog_format=ROW`, `binlog_row_image=FULL` và khởi động lại dịch vụ MySQL.

---

#### 📌 Thứ 5 (12/11/2026) - Mạng tập trung với AWS Transit Gateway & AWS DataSync

* **Ta học được những gì hôm nay?**
  * **Kiến trúc mạng hình sao (Hub-and-Spoke Architecture):** Khi số lượng VPC tăng lên từ 3 đến hàng chục VPC, mô hình VPC Peering trở thành một mạng lưới đan chéo rối rắm (Full-Mesh Topology với công thức $N(N-1)/2$ liên kết). AWS Transit Gateway đóng vai trò như một bộ định tuyến trung tâm đám mây (Cloud Router), mọi VPC chỉ cần tạo một liên kết duy nhất (Transit Gateway Attachment) vào TGW.
  * **Kiểm soát phân tầng giao tiếp bằng Route Tables:**
    * Tạo `Prod-Route-Table` trên TGW cho phép Prod VPC chỉ kết nối đến Shared Services VPC, chặn hoàn toàn kết nối từ Dev VPC.
    * Tạo `Dev-Route-Table` chỉ cho phép Dev VPC liên lạc nội bộ và kết nối tới dịch vụ chia sẻ.
  * **Truyền tải dữ liệu tệp khối lớn với AWS DataSync:** Triển khai DataSync Agent kết nối trực tiếp với hệ thống lưu trữ Network Attached Storage (NAS) cục bộ, tự động mã hóa và tăng tốc đồng bộ dữ liệu vào S3 với băng thông tối ưu, tự động kiểm tra tính toàn vẹn dữ liệu bằng mã băm MD5/SHA256.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi mất định tuyến hai chiều (Asymmetric Routing):* Gắn VPC vào TGW nhưng các máy ảo giữa 2 VPC vẫn không ping thấy nhau. Nguyên nhân: Quản trị viên mới chỉ thêm route trên Transit Gateway Route Table mà quên cập nhật Route Table cục bộ của Subnet bên trong VPC trỏ dải CIDR của VPC đối diện về `tgw-xxxx`. Cách xử lý: Thêm route tương ứng trên cả 2 Route Table cục bộ của 2 VPC.

---

#### 📌 Thứ 6 (13/11/2026) - Tổng kết Tuần 9, Viết Worklog & Hoàn thiện Kế hoạch Di trú Đồ án

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa toàn bộ bức tranh di trú:** Kết hợp nhuần nhuyễn chiến lược Rehost máy chủ bằng AWS MGN, di trú CSDL liên tục bằng AWS DMS, kết nối mạng mở rộng bằng Transit Gateway và sao chép dữ liệu khối lớn bằng DataSync.
  * **Thực hành quy trình dọn dẹp (Teardown):** Xóa DMS Replication Instance, tắt máy chủ thử nghiệm cutover, xóa Transit Gateway Attachments và hủy TGW để ngăn chặn phát sinh chi phí theo giờ.
  * **Hoàn thiện kế hoạch Cutover cho Capstone Project:** Xây dựng tài liệu hướng dẫn chuyển dịch chi tiết từng phút (Runbook) cho kịch bản di chuyển cơ sở dữ liệu và hệ thống web của đồ án thực tập lên hạ tầng Amazon RDS và EC2 Multi-AZ.

