---
title: "Worklog Tuần 9"
date: 2026-11-09
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 9:

- Nghiên cứu và phân loại các chiến lược di trú hạ tầng lên nền tảng đám mây theo phương pháp luận **AWS 7Rs Migration Strategies** (Rehost, Replatform, Refactor, Repurchase, Retain, Retire, Relocate).
- Thực hành đóng gói và chuyển dịch máy chủ ảo từ môi trường On-Premises (VMware, VirtualBox, Hyper-V) lên AWS bằng công cụ **VM Import/Export** (Workshop 000027) và **AWS Application Migration Service (AWS MGN)**.
- Triển khai di trú cơ sở dữ liệu đồng nhất và dị thể (Heterogeneous Migration) với thời gian gián đoạn gần như bằng 0 (Near-Zero Downtime) bằng **AWS Database Migration Service (DMS)** (Workshop 000031) và **AWS Schema Conversion Tool (SCT)**.
- Xây dựng mô hình mạng doanh nghiệp tập trung đa kết nối hình sao (Hub-and-Spoke Topology) với **AWS Transit Gateway (TGW)** thay thế cấu hình VPC Peering phức tạp.
- Khám phá các giải pháp tích hợp lưu trữ đám mây lai (**Hybrid Cloud Storage**) và truyền tải dữ liệu khối lượng lớn với **AWS DataSync** và **AWS Storage Gateway**.
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và xây dựng kịch bản di trú dữ liệu mẫu cho đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Di trú máy chủ ảo lên đám mây với VM Import/Export & AWS MGN:** <br>- Đóng gói đĩa ảo định dạng OVA/VMDK từ môi trường On-Premises và tải lên S3. <br>- Sử dụng AWS CLI thực thi lệnh `aws ec2 import-image` chuyển đổi thành AMI. <br>- Khám phá cơ chế sao chép khối liên tục ở tầng block-level của AWS MGN. | 09/11/2026 | 09/11/2026 | [VM Import/Export (000027)](https://000027.awsfcaj.com/) |
| **Thứ 3** | **Di trú & Đồng bộ cơ sở dữ liệu với AWS DMS & AWS SCT:** <br>- Chuyển đổi lược đồ cơ sở dữ liệu (Schema Conversion) giữa các engine CSDL khác nhau. <br>- Cấu hình DMS Replication Instance, Source Endpoint và Target RDS MySQL Endpoint. <br>- Khởi chạy tác vụ di trú Full Load kết hợp nhân bản dữ liệu thời gian thực (CDC - Change Data Capture). | 10/11/2026 | 10/11/2026 | [AWS DMS Workshop (000031)](https://000031.awsfcaj.com/) |
| **Thứ 4** | **Kết nối mạng doanh nghiệp quy mô lớn với AWS Transit Gateway (TGW):** <br>- Khởi tạo Transit Gateway làm đầu mối định tuyến tập trung kết nối đa VPC. <br>- Gắn kết (Attachments) các VPC chức năng (Shared Services VPC, Web VPC, DB VPC). <br>- Thiết lập bảng định tuyến Transit Gateway Route Tables và kiểm tra kết nối chéo VPC. | 11/11/2026 | 11/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 5** | **Truyền tải dữ liệu & Lưu trữ lai với AWS DataSync & Storage Gateway:** <br>- Triển khai DataSync Agent kết nối và đồng bộ tự động dữ liệu tệp lớn lên Amazon S3. <br>- Khám phá kiến trúc AWS Storage Gateway: File Gateway (NFS/SMB), Volume Gateway và Tape Gateway. <br>- Tối ưu hóa băng thông truyền tải và quản trị chi phí lưu trữ lai. | 12/11/2026 | 12/11/2026 | [Cloud Journey - Migration](https://cloudjourney.awsfcaj.com/2-migration/) |
| **Thứ 6** | **Tổng kết Tuần 9, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ phương pháp luận 7Rs, công cụ di trú (MGN, DMS) và kiến trúc TGW. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 9 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Xây dựng kế hoạch di trú chi tiết từ hạ tầng Legacy sang kiến trúc AWS cho Đề xuất đồ án. | 13/11/2026 | 13/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 9:

#### 📌 Kết quả Thứ 2 (09/11/2026) - Di trú máy chủ với VM Import/Export:
* **Chuyển đổi máy chủ ảo an toàn:** Thực hiện quy trình xuất máy ảo Linux từ định dạng VMDK cục bộ, tải lên S3 và kích hoạt tác vụ chuyển đổi dòng lệnh `import-image` để tạo Custom AMI trên AWS. Khởi chạy máy chủ EC2 từ AMI mới tạo và xác nhận tính toàn vẹn của hệ điều hành, cấu hình mạng và dữ liệu ứng dụng.
* **Tối ưu thời gian chuyển dịch (Lift-and-Shift):** Hiểu rõ cách thức AWS MGN sử dụng AWS Replication Agent để sao chép liên tục dữ liệu mức block-level qua kênh TLS, cho phép cắt chuyển hệ thống (Cutover) chỉ trong vòng vài phút mà không làm gián đoạn người dùng.

#### 📌 Kết quả Thứ 3 (10/11/2026) - Di trú cơ sở dữ liệu với AWS DMS & SCT:
* **Di trú dữ liệu dị thể không gián đoạn:** Ứng dụng AWS Schema Conversion Tool (SCT) để tự động phân tích và chuyển đổi cấu trúc bảng, kiểu dữ liệu và chỉ mục từ cơ sở dữ liệu nguồn sang Amazon RDS MySQL mục tiêu.
* **Đồng bộ hóa dữ liệu thời gian thực (CDC):** Cấu hình tác vụ DMS với tùy chọn Change Data Capture (CDC), đảm bảo mọi thao tác ghi mới (INSERT/UPDATE/DELETE) trên cơ sở dữ liệu gốc trong quá trình di trú đều được tái hiện chính xác sang RDS mục tiêu trước khi chuyển đổi chính thức.

#### 📌 Kết quả Thứ 4 (11/11/2026) - Mạng doanh nghiệp tập trung với AWS Transit Gateway:
* **Đơn giản hóa cấu trúc mạng:** Loại bỏ mô hình kết nối lưới đa điểm (Full-Mesh VPC Peering) phức tạp dễ gây nghẽn và khó quản lý khi số lượng VPC tăng lên.
* **Kiểm soát định tuyến phân tầng:** Thiết lập các bảng định tuyến riêng biệt trên Transit Gateway, cho phép phân tách lưu lượng giữa môi trường Phát triển (Dev VPC) và Môi trường Sản xuất (Prod VPC), đồng thời chia sẻ an toàn các dịch vụ dùng chung (Shared Services VPC như DNS, Active Directory, Logging).

#### 📌 Kết quả Thứ 5 (12/11/2026) - Lưu trữ lai với AWS DataSync & Storage Gateway:
* **Tăng tốc truyền tải dữ liệu:** Trải nghiệm tốc độ truyền tải tệp tin dung lượng lớn nhanh gấp 10 lần so với các công cụ truyền thống (rsync, scp) nhờ giao thức tối ưu hóa độc quyền của AWS DataSync.
* **Tích hợp lưu trữ đám mây liền mạch:** Khám phá giải pháp File Gateway cho phép các máy chủ trong doanh nghiệp đọc/ghi dữ liệu lên Amazon S3 dưới dạng các thư mục chia sẻ chuẩn NFS/SMB thông thường.
