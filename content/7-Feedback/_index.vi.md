---
title: "Chia sẻ, đóng góp ý kiến"
date: 2026-12-04
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Sau 12 tuần tham gia chương trình **Workforce Bootcamp - First Cloud AI Journey (FCAJ)**, em xin gửi lại những chia sẻ thực tế và một số góp ý cá nhân với mong muốn đóng góp cho chương trình ngày càng hoàn thiện hơn ở các khóa tiếp theo.

---

### Đánh giá chung

**1. Môi trường học tập và làm việc**  
Môi trường sinh hoạt tại cộng đồng FCAJ và các buổi hội thảo trực tiếp tại Văn phòng AWS Việt Nam (Tầng 26, tòa nhà Bitexco) rất cởi mở và giàu năng lượng kỹ thuật. Việc được ngồi nghe trực tiếp các chuyên gia AWS, Tech Lead từ doanh nghiệp và thảo luận cùng các bạn thực tập sinh đến từ nhiều trường đại học khác nhau tạo động lực học tập rõ rệt hơn nhiều so với chỉ tự học qua video.

**2. Sự hỗ trợ của Mentor và đội ngũ Admin**  
Các anh chị Mentor và đội ngũ Admin hỗ trợ rất sát sao từ khâu định hướng lộ trình `cloudjourney.awsfcaj.com`, nhắc nhở quy tắc bảo mật tài khoản, kiểm soát chi phí cho tới cách trình bày báo cáo kỹ thuật. Điểm em trân trọng nhất là Mentor luôn định hướng để thực tập sinh tự đọc tài liệu, tự tra cứu log và tự làm chủ kiến trúc thay vì làm thay.

**3. Sự phù hợp giữa nội dung thực tập và chuyên ngành CNTT**  
Lộ trình 12 tuần kết nối rất tốt với các môn học nền tảng ở trường (Mạng máy tính, Hệ điều hành, Cơ sở dữ liệu, Kiến trúc phần mềm) nhưng đưa thẳng vào bối cảnh vận hành thực tế trên AWS: quy hoạch CIDR/Subnet đa vùng, nối chuỗi Security Group cho RDS Multi-AZ, tự động hóa bằng AWS CLI/Boto3, giám sát bằng CloudWatch/Grafana và bảo mật AI Agent với Bedrock AgentCore.

**4. Cơ hội học hỏi và phát triển kỹ năng thực chiến**  
Ngoài kỹ năng cấu hình dịch vụ AWS, em học được ba thói quen quan trọng của một kỹ sư đám mây:
- Tư duy kiểm soát chi phí (**FinOps**) ngay từ khi thiết lập AWS Budgets, Lambda tắt/bật EC2 tự động và dọn dẹp tài nguyên sau lab.
- Kỹ năng viết tài liệu kỹ thuật song ngữ rõ ràng, có sơ đồ kiến trúc, bảng tham số và ghi chép nguyên nhân – cách xử lý lỗi.
- Cơ hội tiếp cận rất sớm với các xu hướng mới qua bài viết **AWS Continuum** và các buổi tọa đàm về **Enterprise AI Agent**.

**5. Văn hóa cộng đồng & Tinh thần chia sẻ**  
Tinh thần *"Learn and Be Curious"* và chia sẻ kiến thức trong cộng đồng AWS Study Group Vietnam rất rõ nét. Từ buổi Fireside Chat cùng Dr. Werner Vogels (CTO Amazon) cho tới các buổi Meetup cuối tuần, các anh chị đi trước đều chia sẻ thẳng thắn cả những bài học thất bại và chi phí thực tế khi vận hành hệ thống lớn.

**6. Học liệu và sự kiện chuyên môn**  
Hệ thống bài lab trên `cloudjourney.awsfcaj.com` được biên soạn có trình tự rõ ràng từ cơ bản đến nâng cao. Bên cạnh đó, việc được tạo điều kiện tham dự các sự kiện kỹ thuật trực tiếp tại văn phòng AWS Việt Nam là một quyền lợi rất giá trị đối với sinh viên thực tập.

---

### Một số câu hỏi khác

- **Điều bạn hài lòng nhất trong thời gian thực tập?**  
  Em hài lòng nhất ở hai điểm: thứ nhất là được tự tay triển khai và gỡ lỗi hàng chục bài lab thực tế trên tài khoản AWS thật (từ Auto Scaling, Hybrid DNS, DynamoDB, ElastiCache đến CloudWatch Advanced và VPC Endpoints); thứ hai là được tham dự trực tiếp buổi đối thoại cùng **Dr. Werner Vogels** và các buổi workshop chuyên sâu về **AI Agent Architecture & Security** tại Bitexco Lầu 26.

- **Điều bạn nghĩ chương trình cần cải thiện cho các thực tập sinh khóa sau?**  
  Một số bài lab trên hệ thống hướng dẫn sử dụng giao diện AWS Management Console hoặc thư viện Python từ phiên bản cũ (ví dụ `redis-py-cluster` trên Python 3.12 hay một vài thay đổi nhỏ trên giao diện VPC/CloudWatch mới). Dù việc tự tìm cách xử lý sự khác biệt này giúp rèn kỹ năng troubleshooting rất tốt, nhưng nếu có thêm ghi chú cập nhật phiên bản ngắn ở đầu bài lab thì các bạn mới bắt đầu sẽ đỡ bỡ ngỡ hơn.

- **Nếu giới thiệu cho bạn bè, bạn có khuyên họ thực tập ở đây không? Vì sao?**  
  Chắc chắn **Có**. Vì chương trình không dạy lý thuyết suông mà rèn kỷ luật tự học, tự triển khai hạ tầng thật, tự quản lý ngân sách AWS và viết tài liệu kỹ thuật chuẩn chỉnh — những kỹ năng rất sát với yêu cầu tuyển dụng vị trí Cloud / DevOps / Backend Engineer hiện nay.

---

### Đề xuất & mong muốn

- **Bạn có đề xuất gì để cải thiện trải nghiệm trong kỳ thực tập?**  
  1. Bổ sung một checklist **"FinOps & Teardown 5 phút cuối ngày"** ngay trong tuần đầu tiên (liệt kê các tài nguyên dễ bị bỏ quên gây trừ tiền ngầm như Idle Elastic IP, NAT Gateway, WAF Web ACL gắn với CloudFront đã disable, EBS Volumes chưa xóa hoặc OpenSearch Serverless) để sinh viên kiểm tra nhanh sau mỗi buổi lab.
  2. Tổ chức thêm các phiên **Architecture Clinic / Code & Worklog Review ngắn (30–45 phút)** theo cụm 3–4 tuần để các nhóm giao lưu và học hỏi cách thiết kế kiến trúc của nhau.

- **Bạn có muốn tiếp tục đồng hành cùng cộng đồng trong tương lai?**  
  Em rất mong muốn tiếp tục sinh hoạt trong cộng đồng **AWS Study Group - First Cloud Journey**, đóng góp thêm các bài viết kỹ thuật và hỗ trợ lại các bạn sinh viên khóa sau khi có điều kiện.

- **Lời cảm ơn:**  
  Em xin gửi lời cảm ơn chân thành đến đội ngũ Mentor, Admin chương trình **First Cloud AI Journey** và các anh chị diễn giả AWS Community Builders đã tận tâm hướng dẫn, tạo điều kiện và truyền cảm hứng cho em trong suốt 12 tuần thực tập vừa qua.
