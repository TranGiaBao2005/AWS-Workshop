---
title: "Tuần 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---


### Mục tiêu tuần 9:

- Nắm vững khung chiến lược chuyển dịch đám mây **AWS 7Rs Migration Strategies** và quy trình di trú máy chủ bằng **VM Import/Export** (Workshop 000027) kết hợp **AWS Application Migration Service (AWS MGN)**.
- Triển khai di trú cơ sở dữ liệu với thời gian gián đoạn tối thiểu (Near-Zero Downtime) bằng **AWS Database Migration Service (DMS)** (Workshop 000031) và **AWS Schema Conversion Tool (SCT)**.
- Thiết kế mô hình mạng doanh nghiệp hình sao (**Hub-and-Spoke Topology**) kết nối đa VPC bằng **AWS Transit Gateway (TGW)**.
- Khám phá các giải pháp lưu trữ đám mây lai và truyền tải dữ liệu dung lượng lớn với **AWS DataSync** và **AWS Storage Gateway**.
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện Worklog và xây dựng tài liệu hướng dẫn chuyển dịch (Migration Runbook) cho đồ án.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Chiến lược 7Rs, VM Import/Export & Sao chép liên tục AWS MGN:** <br>- Phân loại tải ứng dụng theo khung 7Rs (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate). <br>- Chuyển đổi đĩa ảo VMDK/OVA thành Custom AMI qua `aws ec2 import-image`. <br>- Tìm hiểu cơ chế cài đặt Replication Agent, sao chép mức khối liên tục (Block-level) và Test Cutover / Cutover trên AWS MGN. | 09/11/2026 | 09/11/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) & [Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 3** | **Di trú cơ sở dữ liệu đồng bộ với AWS DMS & AWS SCT:** <br>- Chuyển đổi lược đồ bảng, view và kiểu dữ liệu dị thể bằng AWS Schema Conversion Tool (SCT). <br>- Khởi tạo DMS Replication Instance, cấu hình Source & Target Endpoints (Amazon RDS MySQL). <br>- Chạy tác vụ Full Load kết hợp sao chép thay đổi thời gian thực (CDC - Change Data Capture). | 10/11/2026 | 10/11/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Thứ 4** | **Kiến trúc mạng đa VPC tập trung với AWS Transit Gateway:** <br>- So sánh bài toán mở rộng giữa VPC Peering (Full-Mesh) và Transit Gateway (Hub-and-Spoke). <br>- Khởi tạo Transit Gateway, gắn kết các VPC Attachments (Dev, Prod, Shared Services). <br>- Cấu hình Route Tables phân tách luồng giao tiếp an toàn giữa các môi trường. | 11/11/2026 | 11/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 5** | **Lưu trữ lai & Truyền tải khối lượng lớn với AWS DataSync & Storage Gateway:** <br>- Triển khai luồng đồng bộ tệp dung lượng lớn từ NAS cục bộ lên S3 qua AWS DataSync kèm kiểm tra toàn vẹn dữ liệu. <br>- Phân biệt 3 chế độ AWS Storage Gateway: S3 File Gateway, Volume Gateway và Tape Gateway. <br>- Đánh giá bảo mật đường truyền mã hóa TLS và quản trị băng thông truyền tải. | 12/11/2026 | 12/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 6** | **Tổng kết Tuần 9, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa khung 7Rs, MGN, DMS/SCT, Transit Gateway và DataSync. <br>- **Làm Worklog:** Chuẩn hóa báo cáo Worklog Tuần 9 song ngữ và dọn dẹp DMS/TGW thử nghiệm. <br>- **Làm Project:** Hoàn thiện tài liệu kế hoạch di trú và kịch bản chuyển đổi dữ liệu cho Capstone Project. | 13/11/2026 | 13/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (09/11/2026) - Chiến lược 7Rs, VM Import/Export & AWS MGN

* **Ta học được những gì hôm nay?**
  * **Khung quyết định di trú AWS 7Rs:** Phân biệt rõ 7 hướng đi: *Rehost* (Lift-and-shift lên EC2), *Replatform* (tối ưu sang Managed Service như RDS), *Refactor* (tái kiến trúc sang Serverless/Microservices), *Repurchase* (chuyển sang SaaS), *Retain*, *Retire* và *Relocate* (VMware Cloud on AWS).
  * **Chuyển đổi máy ảo ngoại tuyến với VM Import/Export:** Tạo IAM Role `vmimport` cho `vmie.amazonaws.com`, đẩy tệp `.vmdk` lên S3 và khởi tạo AMI bằng CLI:
    ```bash
    aws ec2 import-image \
      --description "Ubuntu Server Migration Lab" \
      --disk-containers "Format=vmdk,UserBucket={S3Bucket=fcaj-migration-staging,S3Key=ubuntu-server.vmdk}"
    ```
  * **Sao chép liên tục với AWS Application Migration Service (AWS MGN):** Cài Replication Agent lên máy chủ nguồn, đồng bộ dữ liệu ở mức khối (Block-level) vào Staging Area Subnet, diễn tập kiểm thử (**Test Cutover**) trước khi thực hiện **Cutover** chính thức giúp giảm downtime xuống chỉ vài phút.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi thiếu driver ENA/NVMe khi khởi chạy AMI & chặn cổng TCP 1500:* Kiểm tra và cập nhật kernel hỗ trợ ENA trước khi xuất `.vmdk`; mở tường lửa Outbound TCP Port 1500 cho MGN Replication Agent.

---

#### 📌 Thứ 3 (10/11/2026) - Di trú & Đồng bộ cơ sở dữ liệu với AWS DMS & SCT

* **Ta học được những gì hôm nay?**
  * **Chuyển đổi lược đồ với AWS SCT:** Đánh giá độ tương thích giữa CSDL nguồn và đích, tự động dịch mã DDL bảng, view và ràng buộc khi chuyển đổi dị thể (Heterogeneous Migration).
  * **Di trú Near-Zero Downtime với AWS DMS:** Khởi tạo DMS Replication Instance (`dms.t3.medium`), kiểm tra kết nối Source/Target Endpoints và chạy tác vụ `Migrate existing data and replicate ongoing changes` (Full Load + CDC theo MySQL `binlog`) để giữ CSDL đích luôn đồng bộ tới sát giây chuyển đổi.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi CDC báo `Binary logging not enabled on source database`:* Cấu hình tệp `my.cnf` trên MySQL nguồn bổ sung `log-bin=mysql-bin`, `binlog_format=ROW`, `binlog_row_image=FULL` và khởi động lại dịch vụ.

---

#### 📌 Thứ 4 (11/11/2026) - Mạng doanh nghiệp hình sao với AWS Transit Gateway

* **Ta học được những gì hôm nay?**
  * **Giải quyết bài toán Full-Mesh của VPC Peering:** Khi có $N$ VPC cần kết nối chéo, VPC Peering cần tới $N(N-1)/2$ liên kết và không hỗ trợ định tuyến bắc cầu (Transitive Routing). AWS Transit Gateway đóng vai trò bộ định tuyến đám mây trung tâm (Hub-and-Spoke), mỗi VPC chỉ cần đúng 1 Attachment.
  * **Phân vùng bảo mật bằng TGW Route Tables:** Tách biệt `Prod-Route-Table` và `Dev-Route-Table` sao cho cả hai đều truy cập được Shared Services VPC nhưng bị cô lập hoàn toàn với nhau.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Các máy ảo giữa 2 VPC không ping được nhau (Asymmetric Routing):* Bổ sung đầy đủ tuyến đường trỏ CIDR của VPC đích về `tgw-xxxx` trong cả TGW Route Table lẫn Subnet Route Table nội bộ của hai đầu VPC.

---

#### 📌 Thứ 5 (12/11/2026) - Lưu trữ lai với AWS DataSync & AWS Storage Gateway

* **Ta học được những gì hôm nay?**
  * **Truyền tải dữ liệu khối lượng lớn với AWS DataSync:** Kết nối DataSync Agent với hệ thống NFS/SMB tại chỗ để đẩy dữ liệu lên Amazon S3/EFS với giao thức truyền tải tăng tốc, mã hóa TLS trên đường truyền và tự động đối soát mã băm (checksum) đảm bảo toàn vẹn.
  * **Tích hợp lưu trữ lai với AWS Storage Gateway:**
    * *S3 File Gateway:* Truy cập đối tượng S3 thông qua giao thức NFS/SMB kèm bộ nhớ đệm cục bộ độ trễ thấp.
    * *Volume Gateway:* Cung cấp ổ đĩa khối iSCSI (Cached/Stored Volumes) sao lưu tự động thành EBS Snapshots.
    * *Tape Gateway:* Thay thế băng từ vật lý bằng thư viện băng từ ảo (VTL) lưu trữ chi phí thấp trên S3 Glacier.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Nghẽn băng thông đường truyền mạng văn phòng khi đồng bộ tệp lớn:* Thiết lập tham số `BytesPerSecond` (Bandwidth Throttling) trên DataSync Task để giới hạn băng thông sử dụng trong giờ làm việc hành chính.

---

#### 📌 Thứ 6 (13/11/2026) - Tổng kết Tuần 9, Viết Worklog & Runbook Di trú Đồ án

* **Ta học được những gì hôm nay?**
  * **Bức tranh tổng thể về Cloud Migration & Hybrid Networking:** Kết nối trọn vẹn bộ công cụ di trú máy chủ (MGN/VM Import), di trú CSDL (DMS/SCT), kết nối mạng doanh nghiệp (TGW) và đồng bộ tệp khối lượng lớn (DataSync).
  * **Dọn dẹp tài nguyên tính phí theo giờ:** Xóa DMS Replication Instance, gỡ Transit Gateway Attachments và hủy TGW ngay sau khi hoàn tất thực hành để đảm bảo không phát sinh phí nhàn rỗi.
  * **Hoàn thiện Migration Runbook cho Capstone Project:** Lập quy trình từng bước cho kịch bản đưa dữ liệu và ứng dụng lên môi trường AWS Multi-AZ.

---

### Mục tiêu cho tuần sau (Tuần 10):

* **Kiến trúc phi máy chủ hướng sự kiện (Serverless EDA):** Amazon API Gateway, Amazon SQS (000078), Amazon SNS, EventBridge và AWS Step Functions.
* **Điều phối Container doanh nghiệp:** Docker Multi-Stage, Amazon ECR, Amazon ECS Fargate (000067) và Kubernetes Amazon EKS (000126).

