---
title: "Worklog Tuần 13"
date: 2024-01-01
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 13:

* Thực hiện kiểm thử chịu tải (**Load Testing / Stress Testing**) cho toàn bộ hệ sinh thái đồ án thực tập bằng kịch bản mô phỏng người dùng thực tế.
* Đánh giá bảo mật chuyên sâu (**Security Assessment**), rà soát cấu hình IAM, Security Groups và các chính sách mã hóa dữ liệu.
* Tối ưu hóa chi phí vận hành (**FinOps & Cost Optimization**) bằng cách tinh chỉnh kích thước tài nguyên (Right-sizing) và áp dụng các khuyến nghị từ AWS Compute Optimizer.
* Kiểm toán toàn diện kiến trúc đồ án theo 6 trụ cột của **AWS Well-Architected Framework**.
* Tổng kết tuần 13, hoàn thiện Worklog và chuẩn bị hồ sơ nghiệm thu đồ án.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :--- | :--- | :--- |
| **Thứ 2** | **Kiểm thử chịu tải hệ thống đồ án (Load & Stress Testing):** <br>- Xây dựng kịch bản kiểm thử tải với Locust / Apache Benchmark. <br>- Giám sát hành vi co giãn tự động của Auto Scaling Group và ALB khi tải tăng vọt. <br>- Đo lường độ trễ phản hồi (Response Latency) và tỷ lệ lỗi HTTP 5xx. | 07/12/2026 | 07/12/2026 | [AWS Well-Architected Reliability](https://aws.amazon.com/architecture/well-architected/) |
| **Thứ 3** | **Đánh giá bảo mật & Kiểm toán tuân thủ (Security Assessment):** <br>- Rà soát toàn bộ IAM Roles, Policies và áp dụng nguyên tắc đặc quyền tối thiểu (Least Privilege). <br>- Quét cấu hình mạng, cổng truy cập Inbound/Outbound và kích hoạt mã hóa dữ liệu (At-Rest & In-Transit). <br>- Đánh giá bảo mật hạ tầng với AWS Security Hub & Amazon GuardDuty. | 08/12/2026 | 08/12/2026 | [AWS Security Pillar](https://aws.amazon.com/architecture/well-architected/) |
| **Thứ 4** | **Tối ưu hóa Chi phí & Tinh chỉnh Tài nguyên (FinOps Tuning):** <br>- Phân tích báo cáo chi phí từ AWS Cost Explorer và AWS Budgets. <br>- Áp dụng khuyến nghị từ AWS Compute Optimizer để điều chỉnh đúng cỡ máy ảo EC2 và cơ sở dữ liệu RDS. <br>- Đánh giá phương án sử dụng Spot Instances và Savings Plans để tiết kiệm ngân sách. | 09/12/2026 | 09/12/2026 | [AWS Cost Optimization Pillar](https://aws.amazon.com/architecture/well-architected/) |
| **Thứ 5** | **Diễn tập khôi phục sau thảm họa (Disaster Recovery Simulation):** <br>- Kiểm thử quy trình sao lưu tự động (Automated Backups & Snapshots) cho RDS và S3. <br>- Mô phỏng sự cố mất vùng sẵn sàng (AZ Outage) và đánh giá cơ chế tự động chuyển vùng dự phòng (Multi-AZ Failover). <br>- Đo lường thời gian phục hồi (RTO) và mức tổn thất dữ liệu chấp nhận được (RPO). | 10/12/2026 | 10/12/2026 | [AWS Disaster Recovery](https://aws.amazon.com/disaster-recovery/) |
| **Thứ 6** | **Tổng kết Tuần 13, Viết Worklog & Hoàn thiện Đồ án:** <br>- Tổng kết kết quả kiểm thử chịu tải, tối ưu chi phí và đánh giá bảo mật đồ án. <br>- Hoàn thiện chi tiết nội dung tài liệu Worklog tuần 13. <br>- Khóa phiên bản kiến trúc đồ án (Architecture Freeze) chuẩn bị cho buổi báo cáo tuần 14. | 11/12/2026 | 11/12/2026 | [Project Documentation](/vi/2-proposal/) |

---

### Kết quả đạt được tuần 13:

* Hệ sinh thái đồ án vượt qua bài kiểm thử chịu tải thực tế với tải mô phỏng hàng ngàn người dùng đồng thời, hệ thống tự động scale out/in mượt mà.
* Tối ưu hóa thành công chi phí vận hành hạ tầng đám mây dự kiến giảm 35% so với phương án thiết kế ban đầu.
* Hoàn thiện ma trận đánh giá 6 trụ cột AWS Well-Architected Framework cho đề tài thực tập.

---

### Mục tiêu cho tuần sau (Tuần 14):

* **Tổng kết toàn diện kỳ thực tập & Đóng gói hồ sơ:** Hoàn thiện báo cáo thực tập chính thức, xuất bản tài liệu kiến trúc.
* **Chuẩn bị Slide thuyết trình & Kịch bản Demo:** Rèn luyện thuyết trình bảo vệ đồ án trước hội đồng đánh giá.
* **Bàn giao & Dọn dẹp tài nguyên:** Hủy hạ tầng thử nghiệm an toàn, bàn giao sản phẩm và kết thúc kỳ thực tập.
