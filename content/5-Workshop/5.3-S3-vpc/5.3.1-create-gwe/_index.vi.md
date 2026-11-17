---
title : "Khởi tạo S3 Gateway Endpoint"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.3.1 </b> "
---

#### Các bước thực hiện:

1. Mở [Amazon VPC Console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#Home:) tại Region `us-east-1` (N. Virginia).
2. Tại thanh điều hướng bên trái, chọn **Endpoints** ➔ Nhấp chọn **Create endpoint**.

> [!NOTE]
> Danh sách hiện tại đã có sẵn 6 Interface Endpoints phục vụ kết nối cho AWS Systems Manager (SSM, `ssmmessages`, `ec2messages`). Các tài nguyên này được CloudFormation Stack khởi tạo sẵn để cho phép điều khiển máy ảo không cần SSH/Bastion Host.

![endpoint](/images/5-Workshop/5.3-S3-vpc/endpoints.png)

3. Cấu hình thông số Endpoint:
   - **Name tag:** Nhập `s3-gwe`
   - **Service category:** Chọn **AWS services**

![endpoint](/images/5-Workshop/5.3-S3-vpc/create-s3-gwe1.png)

4. Tại mục **Services**, nhập từ khóa `s3` vào ô tìm kiếm:
   - Chọn service: `com.amazonaws.us-east-1.s3`
   - Kiểm tra cột **Type:** Phải hiển thị loại **Gateway**

![endpoint](/images/5-Workshop/5.3-S3-vpc/services.png)

5. Cấu hình VPC & Bảng định tuyến:
   - **VPC:** Chọn **VPC Cloud** từ menu thả xuống.
   - **Route tables:** Tích chọn Route Table thứ 2 (bảng định tuyến liên kết với 2 private subnets do CloudFormation tạo, không phải Main Route Table).

![endpoint](/images/5-Workshop/5.3-S3-vpc/vpc.png)

6. Thiết lập Chính sách truy cập (Policy):
   - Chọn **Full access** (cho phép toàn quyền truy cập dịch vụ, chính sách giới hạn chi tiết sẽ được kiểm thử ở mục 5.5).

![endpoint](/images/5-Workshop/5.3-S3-vpc/policy.png)

7. Nhấp **Create endpoint**. Sau khi hệ thống thông báo trạng thái **Available**, chuyển sang bước kiểm thử.

![endpoint](/images/5-Workshop/5.3-S3-vpc/complete.png)
