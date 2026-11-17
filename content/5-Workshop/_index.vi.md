---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Thiết lập Kết nối Hybrid An toàn tới Amazon S3 qua VPC Endpoints

#### Mục tiêu Kiến trúc
Trong môi trường doanh nghiệp kết hợp (Hybrid Cloud), việc kết nối trực tiếp các ứng dụng nội bộ tới dịch vụ lưu trữ đám mây như **Amazon S3** thường gặp rủi ro rò rỉ dữ liệu nếu lưu lượng phải định tuyến qua Internet công cộng. Bài thực hành chuyên sâu (Workshop) này triển khai giải pháp cô lập lưu lượng hoàn toàn trong mạng nội bộ AWS thông qua hai cơ chế **VPC Endpoints**:

1. **Gateway VPC Endpoint (Truy cập nội bộ AWS VPC):** Định tuyến trực tiếp các gói tin từ máy chủ EC2 tới Amazon S3 thông qua bảng định tuyến nội bộ của VPC (Route Table), không cần gắn Internet Gateway (IGW) hay NAT Gateway.
2. **Interface VPC Endpoint / AWS PrivateLink (Truy cập từ On-Premises):** Cung cấp các địa chỉ IP private (ENI) trong dải mạng VPC, cho phép các máy chủ từ trung tâm dữ liệu On-Premises truy cập S3 qua đường truyền riêng (Site-to-Site VPN hoặc AWS Direct Connect).

```
[On-Premises Data Center] 
       │ (IPsec VPN / Direct Connect)
       ▼
[AWS Transit Gateway] 
       ▼
[Interface Endpoint (ENI Private IP)] ────(AWS PrivateLink)────► [Amazon S3]
                                                                      ▲
[Cloud VPC EC2] ─────(Route Table: Gateway Endpoint)─────────────────┘
```

#### Cấu trúc Bài thực hành

1. [5.1 Tổng quan kiến trúc Workshop](5.1-Workshop-overview/) — Sơ đồ kết nối giữa VPC Cloud và VPC On-Premises.
2. [5.2 Khởi tạo môi trường & Phân quyền IAM](5.2-Prerequiste/) — Triển khai hạ tầng mẫu bằng AWS CloudFormation và cấu hình chính sách IAM.
3. [5.3 Truy cập Amazon S3 nội bộ từ VPC (Gateway Endpoint)](5.3-S3-vpc/) — Cấu hình bảng định tuyến và kiểm thử tải tệp 1GB qua AWS Systems Manager.
4. [5.4 Truy cập Amazon S3 từ On-Premises (Interface Endpoint & PrivateLink)](5.4-S3-onprem/) — Thiết lập định tuyến VPN StrongSwan, Interface Endpoint và Route 53 Resolver DNS forwarding.
5. [5.5 Kiểm soát truy cập với VPC Endpoint Policy](5.5-Policy/) — Giới hạn quyền truy cập chỉ cho phép thao tác trên Bucket được chỉ định.
6. [5.6 Dọn dẹp tài nguyên & Đánh giá chi phí](5.6-Cleanup/) — Xóa Hosted Zone, Resolver Rule, Endpoint và hủy CloudFormation Stacks để tối ưu chi phí.
