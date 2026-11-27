---
title : "Dọn dẹp tài nguyên"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

Tài liệu hướng dẫn quy trình giải phóng toàn bộ tài nguyên hạ tầng của dự án **AI Exam Maker** tại region **`ap-southeast-1` (Singapore)** sau khi kết thúc báo cáo và chấm điểm, đảm bảo không phát sinh chi phí ngầm ngoài ý muốn.

{{% notice info %}}
**Lưu ý về mặt vận hành (nếu chỉ tạm dừng qua đêm trước ngày demo):**
Khi chỉ dừng tạm thời (`Stop temporarily`) đối với **Amazon RDS (`exammaker-dev-pg`)**, AWS chỉ giữ trạng thái dừng tối đa **7 ngày** và sẽ **tự động khởi động lại sau 7 ngày** làm phát sinh chi phí theo giờ trở lại. Do đó, sau khi hoàn tất môn học, bắt buộc thực hiện quy trình **xóa triệt để (Cleanup)** theo đúng thứ tự phụ thuộc dưới đây.
{{% /notice %}}

---

#### Bước 1: Làm rỗng và xóa các S3 Buckets lưu trữ

S3 không cho phép xóa trực tiếp bucket còn chứa dữ liệu bên trong, vì vậy cần làm rỗng (`Empty`) trước khi xóa (`Delete`):

1. Mở **Amazon S3** → menu trái chọn **General purpose buckets** `(1)`.
2. Lần lượt chọn 2 bucket của dự án tại region `ap-southeast-1` `(2)` (gồm bucket chứa static frontend và bucket chứa backend release artifacts).
3. Bấm nút **Empty** `(3)` → nhập cụm từ xác nhận `permanently delete` để xóa toàn bộ object và version bên trong.
4. Quay lại danh sách, chọn lại bucket và bấm **Delete** `(4)` để xóa hoàn toàn bucket.

![Làm rỗng và xóa các S3 Buckets](/images/5-Workshop/5.6-Cleanup/4.png)

---

#### Bước 2: Xóa cơ sở dữ liệu Amazon RDS PostgreSQL & Kiểm tra Snapshot

1. Mở **Aurora and RDS** → menu trái chọn **Databases** `(1)`.
2. Chọn instance **`exammaker-dev-pg`** `(2)` *(Lưu ý: nếu trước buổi demo đã bật `Deletion protection`, bấm **Modify** → bỏ chọn *Enable deletion protection* → chọn *Apply immediately* trước khi xóa)*.
3. Bấm **Actions** `(3)` → chọn **Delete** `(4)`.

![Chọn xóa cơ sở dữ liệu Amazon RDS PostgreSQL](/images/5-Workshop/5.6-Cleanup/5a.png)

4. Tại hộp thoại xác nhận **Delete exammaker-dev-pg instance**:
   - **Bỏ chọn (uncheck)** ô `Create final snapshot` (tránh phát sinh phí lưu trữ snapshot $0.095/GB-tháng).
   - **Bỏ chọn (uncheck)** ô `Retain automated backups` (không giữ lại bản sao lưu tự động có tính phí sau khi xóa).
   - Gõ cụm từ xác nhận `delete me` vào ô trống và bấm nút **Delete**.

![Xác nhận xóa RDS exammaker-dev-pg không giữ snapshot và backup](/images/5-Workshop/5.6-Cleanup/5a1.png)

{{% notice warning %}}
**Lưu ý kiểm tra bổ sung (Manual Snapshots):** Các bản sao lưu thủ công (*Manual Snapshots* tạo trước khi chạy migration lớn hoặc khi diễn tập khôi phục) **không tự động mất đi** khi xóa DB instance. Sau bước trên, vào menu trái **Snapshots → tab Manual**, kiểm tra nếu còn tồn đọng bản snapshot cũ nào của dự án thì chọn **Actions → Delete snapshot** để xóa sạch.
{{% /notice %}}

---

#### Bước 3: Hủy máy chủ EC2 (Terminate Instance) & Kiểm tra ổ cứng EBS rời

1. Mở **EC2** → menu trái chọn **Instances** `(1)`.
2. Tick chọn máy chủ **`aem-exammaker-ec2`** (`t4g.small`) `(2)`.
3. Bấm **Actions** (hoặc **Instance state**) `(3)` → chọn **Terminate (delete) instance** `(4)`.

![Chọn Terminate máy chủ EC2 aem-exammaker-ec2](/images/5-Workshop/5.6-Cleanup/6a.png)

4. Tại hộp thoại xác nhận **Terminate (delete) instance**, kiểm tra thông báo mặc định ổ đĩa gốc EBS (`30 GiB gp3`) sẽ tự động xóa kèm theo máy chủ, sau đó bấm **Terminate (delete)**.

![Xác nhận Terminate máy chủ EC2 kèm ổ đĩa gốc EBS](/images/5-Workshop/5.6-Cleanup/6a1.png)

{{% notice warning %}}
**Lưu ý kiểm tra bổ sung (Ổ cứng EBS rời — Unattached Volumes):** Sau khi máy chủ EC2 đã chuyển hẳn sang trạng thái `Terminated`, vào menu trái **Elastic Block Store → Volumes**, lọc trạng thái `Volume state = Available` (các ổ đĩa nằm rời không gắn vào máy nào). Nếu còn sót ổ đĩa `Available` nào, chọn **Actions → Delete volume** để tránh bị tính phí lưu trữ $0.096/GB-tháng.
{{% /notice %}}

---

#### Bước 4: Giải phóng địa chỉ IP tĩnh (Release Elastic IP) — *Quan trọng nhất*

AWS thu phí **$0.005/giờ (~$3.65/tháng)** đối với mọi địa chỉ Public IPv4 / Elastic IP giữ trong tài khoản, kể cả khi máy chủ EC2 đã bị xóa.

1. Trong giao diện **EC2**, kéo menu trái xuống mục **Network & Security → Elastic IPs** `(1)`.
2. Tick chọn địa chỉ **`aem-exammaker-eip`** của dự án `(2)` (đảm bảo thực hiện sau khi đã Terminate hoặc Disassociate khỏi EC2).
3. Bấm **Actions** `(3)` → chọn **Release Elastic IP addresses** `(4)` → bấm **Release** để trả lại địa chỉ IP cho AWS.

![Giải phóng địa chỉ tĩnh Elastic IP aem-exammaker-eip](/images/5-Workshop/5.6-Cleanup/7.png)

---

#### Bước 5: Rà soát các tài nguyên mạng đắt đỏ & Dọn dịch vụ phụ trợ

1. **Xác nhận không tồn tại Load Balancer & NAT Gateway:**
   - Kiểm tra mục **EC2 → Load Balancing → Load Balancers** đảm bảo danh sách trống (`0 load balancers`).
   - Kiểm tra mục **VPC → NAT gateways** đảm bảo danh sách trống (`0 NAT gateways` — tuân thủ kiến trúc tiết kiệm ngân sách $200).

![Xác nhận danh sách Load Balancers trống](/images/5-Workshop/5.6-Cleanup/8b.png)

2. **Dọn dẹp các dịch vụ cấu hình & giám sát còn lại (làm sạch tài khoản):**
   - **Amazon Route 53 (nếu dùng Hosted Zone trên AWS):** vào **Hosted zones**, xóa các bản ghi `A`/`CNAME` của tên miền dự án rồi xóa Hosted Zone (tránh phí duy trì cố định **$0.50/tháng/zone**).
   - **Amazon CloudWatch & SNS:** xóa Log Group `/exammaker/dev/app`, xóa 10 Alarms `exammaker-dev-*` và xóa SNS Topic `exammaker-dev-alerts`.
   - **Amazon SQS:** xóa 2 hàng đợi `exammaker-dev-ai-jobs` và `exammaker-dev-ai-jobs-dlq`.
   - **Amazon Cognito:** xóa User Pool `exammaker-dev-users`.
   - **AWS Systems Manager Parameter Store:** xóa các tham số cấu hình dưới `/exammaker/dev/*` và `/exammaker-ops/dev/*`.
   - **IAM & VPC:** xóa các role của dự án (`aem-exammaker-ec2-role`, `aem-github-*-deploy-role`) và xóa VPC `aem-demo-vpc` (các Subnet, Route Table, Internet Gateway, Security Group miễn phí đi kèm sẽ được gỡ cùng VPC).
   - **Kiểm tra cuối cùng:** sau 24 giờ, mở **AWS Billing and Cost Management → Bills** để xác nhận không còn dịch vụ nào tiếp tục nhảy phí theo giờ.
