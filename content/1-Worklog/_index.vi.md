---
title: "Nhật ký công việc"
date: 2026-09-14
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

Hệ thống nhật ký công việc (**Worklog**) ghi lại toàn bộ lộ trình học tập, nghiên cứu và thực hành chuyên sâu trong suốt **14 tuần thực tập** (từ ngày **14/09/2026** đến ngày **18/12/2026**) tại chương trình **First Cloud AI Journey (FCAJ)**. 

Lộ trình được thiết kế và sắp xếp theo chuẩn cấu trúc từ trên xuống dưới của tài liệu chính thức [The First Cloud Journey Roadmap](https://cloudjourney.awsfcaj.com/), kết hợp hài hòa giữa thực hành dịch vụ cốt lõi, tối ưu hóa kiến trúc Well-Architected, di trú hệ thống, hiện đại hóa ứng dụng không máy chủ, điều phối container, khai phá dữ liệu lớn và ứng dụng trí tuệ nhân tạo thế hệ mới (Generative AI) vào đồ án tốt nghiệp (**Capstone Project**).

---

### 🗺️ Bảng tổng hợp lộ trình 14 tuần thực tập (Curriculum Overview)

| Tuần | Thời gian | Chủ đề trọng tâm & Dịch vụ triển khai | Phân hệ Roadmap | Chi tiết |
| :---: | :---: | :--- | :--- | :---: |
| **Tuần 1** | 14/09 – 18/09/2026 | **Khám phá dịch vụ cốt lõi AWS:** Quản trị ngân sách AWS Budgets, phân quyền IAM, mạng cô lập Amazon VPC, máy chủ Amazon EC2, lưu trữ Amazon S3. | [Explore Services](https://cloudjourney.awsfcaj.com/) | [Xem Tuần 1](1.1-week1/) |
| **Tuần 2** | 21/09 – 25/09/2026 | **Tối ưu hóa hệ thống Well-Architected:** Vận hành tự động AWS Lambda, bảo mật khóa KMS, tường lửa WAF, container Fargate, chi phí Savings Plans & Glue/Athena. | [Optimize System](https://cloudjourney.awsfcaj.com/3-optimize/) | [Xem Tuần 2](1.2-week2/) |
| **Tuần 3** | 28/09 – 02/10/2026 | **Hiện đại hóa ứng dụng & CSDL quan hệ:** Serverless SAM & Cognito, Containers ECS/EKS/ROSA, QuickSight & Athena, thực hành CSDL Amazon RDS MySQL Multi-AZ. | [Modernize & DB](https://cloudjourney.awsfcaj.com/4-modernize/) | [Xem Tuần 3](1.3-week3/) |
| **Tuần 4** | 05/10 – 09/10/2026 | **Điện toán co giãn & Giám sát vận hành:** Amazon Lightsail, Lightsail Container, tự động co giãn EC2 Auto Scaling, giám sát tập trung Amazon CloudWatch. | [Compute & Monitor](https://cloudjourney.awsfcaj.com/) | [Xem Tuần 4](1.4-week4/) |
| **Tuần 5** | 12/10 – 16/10/2026 | **Mạng phân giải lai & CSDL chuyên dụng:** Route 53 Hybrid DNS, thao tác dòng lệnh AWS CLI, CSDL NoSQL Amazon DynamoDB, bộ nhớ đệm Amazon ElastiCache Redis. | [Hybrid & Databases](https://cloudjourney.awsfcaj.com/) | [Xem Tuần 5](1.5-week5/) |
| **Tuần 6** | 19/10 – 23/10/2026 | **Quản trị hạn ngạch & Giám sát trực quan:** AWS Service Quotas, tối ưu chi phí EC2 bằng Lambda & Slack, Tags & Resource Groups, Dashboard Grafana & CloudWatch. | [Cost & Observability](https://cloudjourney.awsfcaj.com/3-optimize/) | [Xem Tuần 6](1.6-week6/) |
| **Tuần 7** | 26/10 – 30/10/2026 | **Giám sát chuyên sâu & Bài viết kỹ thuật:** CloudWatch Advanced, Logs Insights, Metric Math & Dynamic Labels, cảnh báo SNS, sự kiện công nghệ & xuất bản Blog 1. | [Deep Observability](https://catalog.workshops.aws/observability/en-US/) | [Xem Tuần 7](1.7-week7/) |
| **Tuần 8** | 02/11 – 06/11/2026 | **Hạ tầng dưới dạng mã & Vận hành tập trung:** AWS CloudFormation (2 ngày chuyên sâu: Cấu trúc Template, Nested Stacks, Change Sets & Drift Detection), AWS CDK, AWS Systems Manager (SSM), AWS Backup. | [IaC & Operations](https://cloudjourney.awsfcaj.com/3-optimize/) | [Xem Tuần 8](1.8-week8/) |
| **Tuần 9** | 09/11 – 13/11/2026 | **Di trú hệ thống & Mạng mở rộng lai:** Di trú máy chủ (2 ngày chuyên sâu: Phương pháp luận 7Rs, VM Import/Export và AWS MGN sao chép mức khối), di trú CSDL AWS DMS & SCT, kết nối trung tâm AWS Transit Gateway, AWS DataSync. | [Cloud Migration](https://cloudjourney.awsfcaj.com/2-migration/) | [Xem Tuần 9](1.9-week9/) |
| **Tuần 10** | 16/11 – 20/11/2026 | **Kiến trúc phi máy chủ hướng sự kiện:** Quản trị bảo mật Amazon API Gateway, hàng đợi phân tách Amazon SQS (Standard, FIFO & DLQ), phát tin đa hướng Amazon SNS & EventBridge, điều phối luồng với AWS Step Functions. | [Serverless & Event](https://cloudjourney.awsfcaj.com/4-modernize/) | [Xem Tuần 10](1.10-week10/) |
| **Tuần 11** | 23/11 – 27/11/2026 | **Điều phối Container doanh nghiệp & Microservices:** Đóng gói Docker & Amazon ECR, vận hành Amazon ECS Fargate, quản trị cụm Kubernetes Amazon EKS (2 ngày chuyên sâu: Hạ tầng Node Groups, Ingress Controller & HPA Scaling). | [Containers & K8s](https://cloudjourney.awsfcaj.com/5-container/) | [Xem Tuần 11](1.11-week11/) |
| **Tuần 12** | 30/11 – 04/12/2026 | **Hồ dữ liệu lớn & Phân tích thông minh:** Hồ dữ liệu & ETL phi máy chủ (2 ngày chuyên sâu: AWS Lake Formation quản trị phân quyền dữ liệu & AWS Glue ETL chuyển đổi Parquet), truy vấn Amazon Athena, trực quan hóa Amazon QuickSight & Redshift. | [Data & Analytics](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) | [Xem Tuần 12](1.12-week12/) |
| **Tuần 13** | 07/12 – 11/12/2026 | **Trí tuệ nhân tạo thế hệ mới (GenAI) trên AWS:** Khám phá Foundation Models Amazon Bedrock & Kiến trúc RAG (2 ngày chuyên sâu: Bedrock Runtime API, Prompt Engineering & Knowledge Bases với OpenSearch Serverless), Bedrock Agents, Amazon SageMaker. | [Generative AI](https://cloudjourney.awsfcaj.com/) | [Xem Tuần 13](1.13-week13/) |
| **Tuần 14** | 14/12 – 18/12/2026 | **Bảo vệ Đồ án tốt nghiệp & Tổng kết thực tập:** Hoàn thiện tài liệu kiến trúc Capstone Project, Slide thuyết trình & Demo kịch bản, bảo vệ đồ án trước Hội đồng Mentor FCAJ, dọn dẹp tài nguyên Teardown an toàn ($0 phát sinh). | [Capstone & Completion](https://cloudjourney.awsfcaj.com/) | [Xem Tuần 14](1.14-week14/) |

---

### 🎯 Nguyên tắc triển khai và chuẩn mực thực hành

1. **Chuẩn lịch làm việc Thứ 2 – Thứ 6:**
   - **Thứ 2 đến Thứ 5:** Mỗi ngày tập trung nghiên cứu, thiết kế kiến trúc và thực hành trực tiếp một bài lab chuyên sâu trên AWS Management Console, CLI hoặc SDK, kèm ghi chép thông số cấu hình và thu thập hình ảnh kết quả thực tế.
   - **Thứ 6:** Dành riêng cho công tác tổng kết kiến thức đã tích lũy trong tuần, hoàn thiện hồ sơ Worklog song ngữ, thực hiện kiểm toán dọn dẹp tài nguyên và phát triển Đề xuất đồ án thực tập (**Project Proposal / Capstone Project**).
2. **Tuân thủ khung kiến trúc chuẩn mực:** Tất cả các giải pháp kỹ thuật đều được đối chiếu theo 6 trụ cột của **AWS Well-Architected Framework**: Vận hành xuất sắc (Operational Excellence), Bảo mật (Security), Độ tin cậy (Reliability), Hiệu quả hiệu năng (Performance Efficiency), Tối ưu hóa chi phí (Cost Optimization), và Tính bền vững (Sustainability).
3. **Nguồn tài liệu tham khảo chính thức:** Đồng bộ trực tiếp theo kho tài liệu hướng dẫn của chương trình tại **[https://cloudjourney.awsfcaj.com/](https://cloudjourney.awsfcaj.com/)** và hệ thống workshop chuyên đề `https://0000xx.awsfcaj.com/`.
