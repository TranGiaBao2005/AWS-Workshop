---
title: "Tự đánh giá"
date: 2026-12-04
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Trong suốt 12 tuần thực tập tại **Công ty TNHH Amazon Web Services Việt Nam** (chương trình **Workforce Bootcamp - First Cloud AI Journey**) từ ngày **14/09/2026** đến ngày **04/12/2026**, em đã có cơ hội rèn luyện trực tiếp trên môi trường đám mây AWS và đối chiếu kiến thức học tại **Đại học FPT** với quy trình kỹ thuật thực tế.

Trong kỳ thực tập, em đã hoàn thành lộ trình **12 tuần thực hành chuyên sâu** (từ hạ tầng mạng VPC, máy chủ EC2 Auto Scaling, cơ sở dữ liệu RDS Multi-AZ, DynamoDB, ElastiCache Redis, Route 53 Hybrid DNS, quản trị hạn ngạch Service Quotas, tự động hóa tiết kiệm chi phí bằng AWS Lambda & Slack, giám sát Grafana & CloudWatch Advanced, cho tới IaC với CloudFormation/CDK, di trú hệ thống, container ECS/EKS, Data Lake và Amazon Bedrock), viết bài phân tích kỹ thuật về **AWS Continuum for Code Vulnerabilities** trên cộng đồng, tham gia 3 sự kiện chuyên môn tại văn phòng AWS Bitexco và triển khai bài thực hành **Kết nối Hybrid an toàn tới Amazon S3 qua VPC Endpoints**. Qua đó, em củng cố rõ rệt kỹ năng thiết kế kiến trúc mạng, tự động hóa bằng AWS CLI/Boto3, kiểm soát chi phí (FinOps), xử lý sự cố (troubleshooting) và trình bày tài liệu kỹ thuật song ngữ.

Dưới đây là bảng tự đánh giá khách quan của em dựa trên quá trình làm việc thực tế:

| STT | Tiêu chí | Mô tả | Tốt | Khá | Trung bình |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | **Kiến thức và kỹ năng chuyên môn** | Nắm vững dịch vụ cốt lõi AWS, tự triển khai được kiến trúc mạng nhiều tầng, CSDL, tự động hóa CLI/Boto3 và giám sát hệ thống | ✅ | ☐ | ☐ |
| 2 | **Khả năng học hỏi** | Chủ động tiếp thu dịch vụ mới (Hybrid DNS, CloudWatch Metric Math, AgentCore, AWS Continuum) qua tài liệu và thực hành lab | ✅ | ☐ | ☐ |
| 3 | **Chủ động** | Tự dựng môi trường thử nghiệm, tự đọc log tìm nguyên nhân lỗi trước khi hỏi Mentor và chủ động tham gia các buổi tọa đàm tại văn phòng AWS | ✅ | ☐ | ☐ |
| 4 | **Tinh thần trách nhiệm** | Hoàn thành đầy đủ báo cáo Worklog 12 tuần, ghi nhận minh chứng thực hành rõ ràng và rà soát chi phí tài khoản sau mỗi bài lab | ✅ | ☐ | ☐ |
| 5 | **Kỷ luật** | Tuân thủ lịch trình học tập Thứ 2 – Thứ 6, quy chuẩn đặt tên/gắn thẻ tài nguyên và quy trình dọn dẹp hạ tầng sau thực hành | ☐ | ✅ | ☐ |
| 6 | **Tính cầu tiến** | Tiếp thu góp ý từ Mentor và cộng đồng để chỉnh sửa lại cấu trúc báo cáo, tối ưu cách trình bày ngắn gọn, đúng trọng tâm kỹ thuật | ✅ | ☐ | ☐ |
| 7 | **Giao tiếp** | Trình bày báo cáo kỹ thuật song ngữ Việt – Anh mạch lạc, trao đổi rõ ràng với các thành viên và diễn giả trong các buổi Meetup | ☐ | ✅ | ☐ |
| 8 | **Hợp tác nhóm** | Phối hợp tốt với các bạn thực tập sinh trong chương trình khi thảo luận kiến trúc, chia sẻ kinh nghiệm xử lý lỗi và tham gia sự kiện | ✅ | ☐ | ☐ |
| 9 | **Ứng xử chuyên nghiệp** | Tôn trọng Mentor, ban tổ chức và các thành viên cộng đồng; tuân thủ quy định bảo mật tài khoản và quy tắc tại văn phòng AWS | ✅ | ☐ | ☐ |
| 10 | **Tư duy giải quyết vấn đề** | Biết khoanh vùng lỗi theo từng tầng (IAM Policy, Security Group, Route Table, DNS, CloudWatch Logs) và ghi chép lại cách khắc phục | ✅ | ☐ | ☐ |
| 11 | **Đóng góp vào dự án/tổ chức** | Đóng góp bài viết kỹ thuật trên nhóm Facebook AWS Study Group, hoàn thiện bộ tài liệu thực hành có hình ảnh và thông số đầy đủ | ✅ | ☐ | ☐ |
| 12 | **Tổng thể** | Đánh giá chung về mức độ hoàn thành mục tiêu và sự trưởng thành về tư duy kỹ sư đám mây sau 12 tuần thực tập | ✅ | ☐ | ☐ |

---

### Cần cải thiện

* **Siết chặt kỷ luật dọn dẹp tài nguyên (Resource Teardown):** Thời gian đầu thực hành, em từng để sót một địa chỉ Elastic IP chưa giải phóng ở Region Singapore (`ap-southeast-1`) và một AWS WAF Web ACL gắn với CloudFront đã tắt ở `us-east-1`, dẫn đến phát sinh phí nhỏ hằng ngày. Sau khi dùng AWS CLI và Cost Explorer quét toàn bộ 17 Regions để xử lý dứt điểm, em đã rút ra thói quen luôn kiểm tra lại mục Elastic IPs, WAF, Snapshots và Network Interfaces ngay sau khi kết thúc mỗi bài lab.
* **Quản lý thời gian khi xử lý các lỗi hạ tầng phức tạp:** Khi gặp các lỗi liên quan đến phân quyền chéo (IAM/KMS/Lake Formation) hoặc định tuyến mạng lai nhiều VPC, đôi lúc em còn mất nhiều thời gian thử-sai thủ công trên Console trước khi chuyển sang kiểm tra bằng AWS CLI và CloudWatch Logs.
* **Nâng cao khả năng thuyết trình và phản biện kiến trúc:** Cần luyện tập thêm kỹ năng giải thích ngắn gọn lý do chọn dịch vụ và phân tích đánh đổi chi phí – hiệu năng (trade-offs) bằng tiếng Anh trong các buổi bảo vệ kỹ thuật.
