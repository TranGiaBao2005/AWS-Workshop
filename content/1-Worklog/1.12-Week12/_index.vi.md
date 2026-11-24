---
title: "Tuần 12"
date: 2026-11-30
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 12:

- Tổng kết toàn diện hành trình **12 tuần thực tập** tại chương trình **First Cloud AI Journey (FCAJ)** (từ 14/09/2026 đến 04/12/2026).
- Hoàn thiện và xuất bản Báo cáo Đồ án thực tập chính thức (**Final Capstone Project Report**) cùng toàn bộ tài liệu kỹ thuật song ngữ và mã nguồn trên GitHub.
- Thiết kế bộ Slide thuyết trình chuyên nghiệp, diễn tập kịch bản Demo trực tiếp và bảo vệ đồ án trước Hội đồng Mentor FCAJ.
- Thực hiện quy trình dọn dẹp tài nguyên đám mây (**Cloud Resource Teardown**) theo đúng thứ tự phụ thuộc, kiểm toán Billing về $0.
- Hoàn tất báo cáo Tự đánh giá (**Self-Evaluation**), tiếp thu phản hồi từ Mentor và định hướng lộ trình chứng chỉ AWS tiếp theo.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Tổng kết 11 tuần & Đóng gói hồ sơ, mã nguồn:** <br>- Rà soát toàn diện các bài viết từ Tuần 1 đến Tuần 11, đảm bảo đồng bộ song ngữ EN/VI và không gãy liên kết. <br>- Đóng gói các file mẫu IaC (CloudFormation/CDK), script Python Boto3 và Dockerfile kèm `README.md` lên GitHub. <br>- Kiểm tra bản dựng tĩnh Hugo (`hugo --minify`) và giao diện hiển thị trên website báo cáo. | 30/11/2026 | 30/11/2026 | [Final Report Review](/vi/2-proposal/) |
| **Thứ 3** | **Chuẩn bị Slide thuyết trình & Diễn tập Kịch bản Demo:** <br>- Thiết kế Slide báo cáo đồ án theo cấu trúc STAR (Vấn đề, Kiến trúc AWS, Kết quả kiểm thử, FinOps). <br>- Xây dựng kịch bản Demo trực tiếp và chuẩn bị video dự phòng (Backup Recording). <br>- Diễn tập thuyết trình căn chỉnh chuẩn khung thời lượng báo cáo. | 01/12/2026 | 01/12/2026 | [Presentation Deck](/vi/2-proposal/) |
| **Thứ 4** | **Bảo vệ Đồ án thực tập trước Hội đồng Mentor FCAJ:** <br>- Thuyết trình giải pháp kiến trúc và kết quả triển khai trên nền tảng AWS. <br>- Trình diễn Demo trực tiếp hệ thống hoạt động và dashboard giám sát. <br>- Trả lời các câu hỏi phản biện chuyên sâu về bảo mật, độ sẵn sàng cao và tối ưu chi phí. | 02/12/2026 | 02/12/2026 | [Capstone Defense](https://cloudjourney.awsfcaj.com/) |
| **Thứ 5** | **Dọn dẹp tài nguyên đám mây an toàn (Cloud Teardown):** <br>- Hủy tài nguyên theo đúng chiều phụ thuộc (Compute/ALB ➔ DB/Cache ➔ NAT/EIP/Endpoints ➔ VPC) tránh lỗi `DependencyViolation`. <br>- Quét kiểm tra toàn bộ các Region (`us-east-1`, `ap-southeast-1`) qua AWS CLI và Billing/Cost Explorer. <br>- Xác nhận tài khoản ở trạng thái sạch 100%, không còn chi phí chạy ngầm. | 03/12/2026 | 03/12/2026 | [AWS Resource Cleanup](https://cloudjourney.awsfcaj.com/) |
| **Thứ 6** | **Hoàn tất Tự đánh giá & Tổng kết kỳ thực tập:** <br>- Hoàn thiện trang Tự đánh giá (`6-Self-evaluation`) và Đóng góp ý kiến (`7-Feedback`). <br>- Tiếp thu phản hồi chuyên môn từ Mentor phụ trách để hoàn thiện kỹ năng kỹ sư đám mây. <br>- Lập kế hoạch chinh phục chứng chỉ AWS Certified Solutions Architect - Associate (SAA-C03). | 04/12/2026 | 04/12/2026 | [Tự đánh giá](/vi/6-self-evaluation/) |

---

### Chi tiết nội dung và đầu ra dự kiến mỗi ngày:

#### 📌 Thứ 2 (30/11/2026) - Đóng gói hồ sơ kỹ thuật & Xuất bản mã nguồn

* **Trọng tâm công việc:**
  * **Kiểm toán chất lượng toàn bộ báo cáo:** Rà soát chéo tất cả 12 tuần Worklog, Proposal, Blogs, Events và Workshop, xác nhận 100% ảnh minh chứng hiển thị chính xác và đường dẫn nội bộ hoạt động ổn định.
  * **Chuẩn hóa kho mã nguồn GitHub:** Đóng gói các file mẫu CloudFormation/CDK, mã nguồn Boto3, cấu hình Docker kèm tài liệu `README.md` rõ ràng về kiến trúc và hướng dẫn triển khai.
* **Lưu ý kỹ thuật cần kiểm soát:**
  * Kiểm tra tuyệt đối không để lộ AWS Access Key, Secret Key hoặc mật khẩu trong lịch sử Git (`.gitignore`, kiểm tra bằng `git diff` trước khi push).

---

#### 📌 Thứ 3 (01/12/2026) - Thiết kế Slide thuyết trình & Diễn tập Demo

* **Trọng tâm công việc:**
  * **Cấu trúc Slide súc tích (chuẩn STAR):** Trình bày rõ bài toán thực tế, lý do lựa chọn dịch vụ AWS theo 6 trụ cột Well-Architected, sơ đồ kiến trúc, kết quả đo đạc hiệu năng và bảng ước tính chi phí từ AWS Pricing Calculator.
  * **Diễn tập kịch bản Demo & Dự phòng rủi ro:** Chạy thử toàn bộ luồng demo thực tế, đo thời lượng vừa vặn khung quy định và quay sẵn video dự phòng phòng trường hợp sự cố đường truyền mạng tại hội trường.

---

#### 📌 Thứ 4 (02/12/2026) - Bảo vệ Đồ án tốt nghiệp trước Hội đồng FCAJ

* **Trọng tâm công việc:**
  * **Trình bày & Demo thực chiến:** Thuyết trình tự tin về kiến trúc giải pháp, minh chứng bằng hệ thống vận hành thực tế trên AWS Management Console và dashboard giám sát.
  * **Phản biện kỹ thuật:** Làm rõ các quyết định đánh đổi kiến trúc (Trade-offs) về bảo mật (Least Privilege, Private Subnets, VPC Endpoints), khả năng chịu lỗi (Multi-AZ, Auto Scaling) và bài toán FinOps (tối ưu chi phí định kỳ).

---

#### 📌 Thứ 5 (03/12/2026) - Dọn dẹp tài nguyên đám mây an toàn (Cloud Teardown)

* **Trọng tâm công việc:**
  * **Quy trình hủy tài nguyên chuẩn thứ tự phụ thuộc:**
    1. Hủy Auto Scaling Groups, ECS/EKS Clusters và Launch Templates.
    2. Xóa Application Load Balancers, Target Groups và giải phóng toàn bộ Elastic IPs.
    3. Xóa Amazon RDS, ElastiCache, OpenSearch/SageMaker Endpoints và các CloudFront/WAF Web ACL không còn sử dụng.
    4. Xóa VPC Endpoints, NAT Gateways, Internet Gateways và cuối cùng là VPC.
  * **Kiểm toán chi phí FinOps:** Dùng AWS CLI quét toàn bộ 17 Regions và đối chiếu AWS Cost Explorer/Budgets để đảm bảo chi phí chạy ngầm bằng $0.
* **Lưu ý xử lý sự cố:**
  * Nếu xóa VPC bị kẹt lỗi `DependencyViolation`, kiểm tra mục **Network Interfaces (ENIs)** trong EC2 Console để gỡ các ENI còn sót lại từ Lambda hoặc VPC Endpoints trước khi xóa lại VPC.

---

#### 📌 Thứ 6 (04/12/2026) - Tự đánh giá & Tổng kết hành trình 12 tuần thực tập

* **Trọng tâm công việc:**
  * **Tự đánh giá khách quan ([Báo cáo Tự đánh giá](/vi/6-self-evaluation/)):** Nhìn lại toàn bộ chặng đường 12 tuần từ những bước làm quen IAM/VPC/EC2 đầu tiên cho đến khả năng thiết kế, tự động hóa IaC, giám sát Observability và tích hợp Generative AI trên AWS.
  * **Tiếp thu phản hồi Mentor & Lộ trình tiếp theo:** Ghi nhận nhận xét chuyên môn từ Mentor FCAJ, hoàn tất thủ tục kết thúc thực tập và bắt tay vào lộ trình ôn luyện chứng chỉ **AWS Certified Solutions Architect - Associate (SAA-C03)**.
