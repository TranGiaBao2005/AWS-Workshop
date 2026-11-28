---
title : "Workshop"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

# Triển khai Hạ tầng AWS cho Hệ thống AI Exam Maker

#### Tổng quan

Trong bài thực hành (Workshop) này, chúng ta thiết lập toàn bộ các thành phần hạ tầng cốt lõi trên **AWS (`ap-southeast-1` — Singapore)** cho hệ thống **AI Exam Maker** theo đúng kiến trúc bảo mật quyền tối thiểu (Least Privilege) và tối ưu chi phí dưới trần ngân sách **$200.00/Quý**.

Toàn bộ quá trình triển khai được chia tách rõ ràng theo từng dịch vụ AWS và từng màn hình thao tác (`Hình 1` đến `Hình 19.2`), kèm quy trình dọn dẹp tài nguyên sau demo ở mục cuối.

#### Nội dung Workshop

1. [5.1. Tổng quan về Workshop](5.1-Workshop-overview/)
2. [5.2. Thiết lập Amazon Cognito User Pool, App Client & Groups](5.2-Cognito/)
3. [5.3. Thiết lập Cơ sở dữ liệu Amazon RDS PostgreSQL 16](5.3-RDS-PostgreSQL/)
4. [5.4. Thiết lập Hàng đợi Amazon SQS & Dead-Letter Queue](5.4-SQS-And-DLQ/)
5. [5.5. Quản trị Cấu hình Tập trung với SSM Parameter Store](5.5-SSM-Parameter-Store/)
6. [5.6. Thiết lập Cảnh báo Amazon SNS & Giám sát CloudWatch](5.6-CloudWatch-And-SNS/)
7. [5.7. Kiểm soát Chi phí với AWS Budgets ($200/Quý)](5.7-AWS-Budgets/)
8. [5.8. Thiết lập Phân quyền IAM Roles & S3 Artifact Bucket cho CI/CD](5.8-IAM-And-S3-CD/)
9. [5.9. Dọn dẹp tài nguyên (Clean up)](5.9-Cleanup/)
