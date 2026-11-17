---
title: "Worklog Tuần 14"
date: 2026-12-14
weight: 14
chapter: false
pre: " <b> 1.14. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 14:

- Tổng kết toàn diện hành trình **14 tuần thực tập** tại chương trình **First Cloud AI Journey (FCAJ)** (từ 14/09/2026 đến 18/12/2026).
- Hoàn thiện và xuất bản Báo cáo Đồ án thực tập chính thức (**Final Capstone Project Report**) cùng toàn bộ tài liệu kiến trúc kỹ thuật song ngữ trên AWS.
- Thiết kế bộ Slide thuyết trình chuyên nghiệp, xây dựng kịch bản Demo trực tiếp và tham gia buổi bảo vệ đồ án tốt nghiệp trước Hội đồng Mentor & Ban giám khảo FCAJ.
- Thực hiện quy trình dọn dẹp và hủy tài nguyên đám mây (**Cloud Resource Teardown**) an toàn theo đúng chiều phụ thuộc, đảm bảo tài khoản không phát sinh chi phí dư thừa.
- Hoàn tất các thủ tục tự đánh giá, tiếp thu phản hồi chuyên môn từ Mentor phụ trách và định hình lộ trình phát triển nghề nghiệp Cloud & DevOps Engineer.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Tổng kết hành trình thực tập & Đóng gói báo cáo:** <br>- Hệ thống hóa toàn bộ các bài thực hành từ Tuần 1 đến Tuần 13. <br>- Rà soát tính nhất quán và hoàn thiện hồ sơ báo cáo thực tập song ngữ. <br>- Xuất bản tài liệu kiến trúc kỹ thuật và mã nguồn đồ án lên kho lưu trữ GitHub. | 14/12/2026 | 14/12/2026 | [Final Report Review](/vi/2-proposal/) |
| **Thứ 3** | **Chuẩn bị Slide thuyết trình & Kịch bản Demo:** <br>- Thiết kế bộ Slide báo cáo đồ án (Vấn đề, Giải pháp kiến trúc AWS, Kết quả kiểm thử, Bài toán chi phí FinOps). <br>- Xây dựng kịch bản Demo trực tiếp các tính năng: Auto Scaling, RDS Multi-AZ Failover và Giám sát CloudWatch. <br>- Chạy thử nghiệm diễn tập thuyết trình và căn chỉnh thời lượng báo cáo. | 15/12/2026 | 15/12/2026 | [Presentation Deck](/vi/2-proposal/) |
| **Thứ 4** | **Bảo vệ Đồ án thực tập trước Hội đồng đánh giá:** <br>- Thuyết trình báo cáo Đồ án thực tập tốt nghiệp trước Mentor và Ban giám khảo FCAJ. <br>- Thực hiện Demo trực tiếp giải pháp kiến trúc vận hành trên nền tảng AWS. <br>- Trả lời các câu hỏi phản biện chuyên sâu về bảo mật, tính sẵn sàng cao và tối ưu hóa chi phí. | 16/12/2026 | 16/12/2026 | [Capstone Defense Session](https://cloudjourney.awsfcaj.com/) |
| **Thứ 5** | **Dọn dẹp tài nguyên đám mây an toàn (Cloud Teardown):** <br>- Thực hiện quy trình hủy tài nguyên theo đúng chiều phụ thuộc (tránh lỗi `DependencyViolation`). <br>- Xóa các máy chủ EC2, cơ sở dữ liệu RDS, ElastiCache clusters, Load Balancers và VPC Endpoints. <br>- Sao lưu mã nguồn, snapshot và tài liệu lên kho lưu trữ dài hạn an toàn. | 17/12/2026 | 17/12/2026 | [AWS Resource Cleanup Guide](https://cloudjourney.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết kỳ thực tập & Tiếp thu phản hồi:** <br>- Hoàn tất các biểu mẫu tự đánh giá và tiếp nhận đánh giá chính thức từ Mentor phụ trách. <br>- Lắng nghe phản hồi kỹ thuật, đúc kết các bài học kinh nghiệm quý báu cho sự nghiệp. <br>- Hoàn tất thủ tục kết thúc kỳ thực tập thành công tốt đẹp tại First Cloud AI Journey! | 18/12/2026 | 18/12/2026 | [Self-Evaluation & Feedback](/vi/6-self-evaluation/) |

---

### Kết quả đạt được tuần 14:

#### 📌 Kết quả Thứ 2 (14/12/2026) - Đóng gói hồ sơ & Xuất bản mã nguồn:
* **Hồ sơ năng lực hoàn chỉnh:** Đóng gói toàn bộ tài liệu 14 tuần thực tập với hơn 20 bài workshop chuyên sâu, hệ thống bài viết song ngữ chuẩn mực (100% Tiếng Việt và 100% Tiếng Anh) và báo cáo kỹ thuật chi tiết.
* **Mã nguồn chuẩn hóa:** Toàn bộ mẫu hạ tầng CloudFormation, CDK scripts và mã kiểm thử được lưu trữ trên kho GitHub công khai, đính kèm tài liệu README hướng dẫn triển khai tự động.

#### 📌 Kết quả Thứ 3 (15/12/2026) - Chuẩn bị Slide & Kịch bản Demo:
* **Tài liệu thuyết trình chất lượng:** Hoàn thành bộ 25 slide trình chiếu súc tích, trực quan, tập trung vào bài toán thực tế, mô hình kiến trúc High Availability, chiến lược bảo mật nhiều lớp và phân tích chi phí FinOps.
* **Kịch bản diễn tập thông suốt:** Diễn tập thành công kịch bản Demo mô phỏng sự cố: tắt máy chủ Database chính để kiểm tra tính năng RDS Multi-AZ tự động chuyển đổi dự phòng (Failover) dưới 60 giây và kích hoạt máy chủ EC2 tự động co giãn khi CPU vượt 70%.

#### 📌 Kết quả Thứ 4 (16/12/2026) - Bảo vệ Đồ án tốt nghiệp xuất sắc:
* **Bảo vệ đồ án thành công:** Thuyết trình tự tin giải pháp trước hội đồng Mentor và chuyên gia công nghệ, minh chứng rõ nét tính khả thi và độ tin cậy của kiến trúc đã xây dựng trên AWS.
* **Phản biện chuyên môn vững vàng:** Trả lời thuyết phục các câu hỏi kỹ thuật về cơ chế mã hóa dữ liệu KMS, tối ưu hóa độ trễ qua ElastiCache Redis và chiến lược phân quyền đặc quyền tối thiểu qua IAM Roles.

#### 📌 Kết quả Thứ 5 (17/12/2026) - Dọn dẹp tài nguyên đám mây an toàn:
* **Quy trình Teardown chuẩn mực:** Thực hiện giải phóng tài nguyên tuần tự từ tầng ứng dụng xuống tầng hạ tầng mạng (Auto Scaling Groups -> EC2 Instances -> Load Balancers -> RDS Multi-AZ -> ElastiCache Clusters -> NAT Gateways & Elastic IPs -> VPC Endpoints -> VPC), không để xảy ra bất kỳ lỗi phụ thuộc `DependencyViolation`.
* **Kiểm toán chi phí 0 đồng phát sinh:** Kiểm tra bảng điều khiển AWS Billing và Cost Explorer, đảm bảo mọi tài nguyên trả phí theo giờ đã được dọn sạch hoàn toàn, đưa chi phí phát sinh sau thực tập về $0.

#### 📌 Kết quả Thứ 6 (18/12/2026) - Hoàn tất kỳ thực tập thành công:
* **Đánh giá xuất sắc:** Hoàn tất bản tự đánh giá kết quả thực tập ([Báo cáo Tự đánh giá](/vi/6-self-evaluation/)) và nhận được đánh giá chính thức tích cực từ Mentor phụ trách chương trình FCAJ.
* **Trưởng thành nghề nghiệp:** Đúc kết hành trang vững chắc về tư duy thiết kế kiến trúc đám mây chuẩn Well-Architected, kỹ năng giải quyết sự cố thực tế và tác phong làm việc chuyên nghiệp, sẵn sàng đón nhận các cơ hội nghề nghiệp Cloud/DevOps Engineer trong tương lai.
