---
title: "Tuần 14"
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

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (14/12/2026) - Đóng gói hồ sơ & Xuất bản mã nguồn

* **Ta học được những gì hôm nay?**
  * **Kỹ năng đóng gói hồ sơ kỹ thuật chuyên nghiệp:** Hệ thống hóa toàn bộ các bài viết từ Tuần 1 đến Tuần 13, rà soát tính nhất quán của các tham số kỹ thuật, đường dẫn hình ảnh và bảng thông số tài nguyên. Đảm bảo toàn bộ 14 tuần đều đạt chuẩn song ngữ 100% Tiếng Việt và 100% Tiếng Anh.
  * **Xuất bản mã nguồn mở trên GitHub:** Đóng gói toàn bộ các file mẫu CloudFormation YAML, mã nguồn AWS CDK TypeScript, script Python Boto3 và Dockerfiles vào kho lưu trữ GitHub chính thức. Viết file `README.md` hướng dẫn triển khai từ đầu (Quick Start Guide) kèm sơ đồ kiến trúc hệ thống trực quan.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi liên kết tệp tin Markdown bị gãy:* Khi rà soát lại các bài viết cũ phát hiện một vài đường dẫn nội bộ bị sai tiền tố URL. Cách xử lý: Sử dụng công cụ `markdown-link-check` quét tự động toàn bộ thư mục `content/` và sửa lại đường dẫn tương đối chuẩn xác.

---

#### 📌 Thứ 3 (15/12/2026) - Thiết kế Slide thuyết trình & Kịch bản Demo thực chiến

* **Ta học được những gì hôm nay?**
  * **Nghệ thuật truyền tải giải pháp kiến trúc đám mây:** Thiết kế bộ 25 slide thuyết trình tập trung vào việc giải quyết bài toán nghiệp vụ, cấu trúc theo phương pháp luận STAR (Situation, Task, Action, Result). Nhấn mạnh các chỉ số định lượng: Khả năng chịu lỗi 99.99%, thời gian phục hồi RTO < 1 phút, và tiết kiệm 42% chi phí hạ tầng.
  * **Xây dựng kịch bản Demo mô phỏng sự cố thực tế:**
    1. Kịch bản 1: Bơm tải CPU giả lập lên 85%, quan sát CloudWatch Alarms kích hoạt và EC2 Auto Scaling tự động khởi chạy thêm 2 máy chủ mới trong 3 phút.
    2. Kịch bản 2: Ép khởi động lại máy chủ cơ sở dữ liệu chính (Reboot with Failover), kiểm chứng Amazon RDS Multi-AZ tự động chuyển hướng kết nối sang máy chủ dự phòng trong vòng 45 giây mà ứng dụng web không bị sập.
    3. Kịch bản 3: Tương tác trực tiếp với Trợ lý AI Amazon Bedrock hỏi đáp dữ liệu thời gian thực.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Thời lượng Demo bị vượt quá giới hạn cho phép:* Bài thuyết trình thử nghiệm kéo dài 28 phút (vượt khung 20 phút của ban giám khảo). Cách xử lý: Cắt bỏ các bước cấu hình chi tiết trên console, tập trung vào sơ đồ kiến trúc tổng quan và kết quả kiểm thử trực tiếp trên dashboard giám sát.

---

#### 📌 Thứ 4 (16/12/2026) - Bảo vệ Đồ án tốt nghiệp trước Hội đồng đánh giá FCAJ

* **Ta học được những gì hôm nay?**
  * **Bản lĩnh thuyết trình và phản biện kỹ thuật:** Trình bày giải pháp mạch lạc, tự tin trước các chuyên gia giải pháp đám mây (AWS Solutions Architects) và Mentor của chương trình.
  * **Bài học kinh nghiệm từ câu hỏi phản biện:**
    * *Câu hỏi về bảo mật:* Làm thế nào để đảm bảo không bị rò rỉ dữ liệu khi giao tiếp giữa EC2 và S3? ➔ Phản biện thuyết phục nhờ giải pháp VPC Gateway Endpoints kèm VPC Endpoint Policy nghiêm ngặt đã thực hành ở Tuần 7.
    * *Câu hỏi về chi phí:* Tại sao lựa chọn kiến trúc kết hợp EC2 Auto Scaling và RDS Multi-AZ thay vì thuần túy Serverless? ➔ Phân tích rõ bài toán chi phí dự đoán được (Predictable Baseline Traffic) kết hợp Savings Plans giúp tiết kiệm hơn Serverless khi lưu lượng truy cập duy trì ổn định 24/7.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Hồi hộp khi Demo trực tiếp:* Kết nối mạng lúc bắt đầu demo hơi chập chờn. Nhờ chuẩn bị sẵn video quay lại kịch bản dự phòng (Backup Recording) và giải thích nguyên lý rõ ràng, hội đồng đánh giá cao sự chuẩn bị chu đáo và tính chuyên nghiệp.

---

#### 📌 Thứ 5 (17/12/2026) - Dọn dẹp tài nguyên đám mây an toàn (Cloud Teardown)

* **Ta học được những gì hôm nay?**
  * **Quy trình hủy tài nguyên theo đúng chiều phụ thuộc (Dependency Hierarchy):** Tránh lỗi kẹt `DependencyViolation` bằng cách giải phóng tài nguyên tuần tự từ tầng ứng dụng ngược về tầng mạng cốt lõi:
    1. Hủy Auto Scaling Groups và xóa Launch Templates.
    2. Xóa Application Load Balancers, Target Groups và giải phóng Elastic IPs.
    3. Chụp bản Snapshot cuối cùng (Final DB Snapshot) và xóa cụm cơ sở dữ liệu Amazon RDS Multi-AZ.
    4. Xóa các cụm ElastiCache Redis và các bộ sưu tập OpenSearch Serverless.
    5. Xóa các VPC Endpoints, Internet Gateways, NAT Gateways và bảng định tuyến.
    6. Cuối cùng mới xóa mạng Amazon VPC.
  * **Kiểm toán chi phí FinOps:** Đăng nhập AWS Billing Console và Cost Explorer, kiểm tra từng Region (`us-east-1`, `ap-southeast-1`), xác nhận mọi tài nguyên tính phí theo giờ đã biến mất hoàn toàn, đưa dự toán chi phí sau thực tập về $0.
* **Khó khăn gặp phải & Cách xử lý:**
  * *VPC không thể xóa do dính lỗi `DependencyViolation`:* Console báo VPC vẫn đang có Network Interface hoạt động. Nguyên nhân: Một số Elastic Network Interfaces (ENIs) của Lambda gắn vào VPC hoặc VPC Endpoints chưa kịp giải phóng. Cách xử lý: Kiểm tra danh sách Network Interfaces trong bảng điều khiển EC2, ngắt kết nối thủ công các ENI còn sót lại và xóa VPC thành công.

---

#### 📌 Thứ 6 (18/12/2026) - Tổng kết kỳ thực tập & Tiếp thu phản hồi Mentor

* **Ta học được những gì hôm nay?**
  * **Tự đánh giá và hoàn thiện bản thân:** Hoàn tất bản tự đánh giá kết quả thực tập ([Báo cáo Tự đánh giá](/vi/6-self-evaluation/)), nhìn lại sự tiến bộ vượt bậc sau 14 tuần: từ một người mới bắt đầu làm quen với Console đến một kỹ sư có khả năng thiết kế, triển khai và tự động hóa hệ thống đám mây chuẩn AWS Well-Architected.
  * **Tiếp thu phản hồi chuyên môn từ Mentor:** Ghi nhận những lời nhận xét quý báu về tư duy tối ưu hóa chi phí (FinOps), kỹ năng viết tài liệu kỹ thuật chuẩn xác và tinh thần chủ động giải quyết sự cố thực tế.
  * **Định hướng sự nghiệp:** Xác định các mục tiêu tiếp theo: chinh phục chứng chỉ AWS Certified Solutions Architect - Associate (SAA-C03) và theo đuổi con đường kỹ sư Cloud & DevOps chuyên nghiệp.

