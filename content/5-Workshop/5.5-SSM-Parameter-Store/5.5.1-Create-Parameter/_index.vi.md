---
title : "Khởi tạo Tham số Cấu hình Chuẩn"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.5.1. </b> "
---

#### Bước 1: Tạo tham số theo cấu trúc đường dẫn `/exammaker/dev/*`

1. Mở **AWS Systems Manager → Parameter Store → Create parameter**.
2. Cấu hình tham số mẫu `/exammaker/dev/Bedrock/ModelId` (cho phép ứng dụng .NET 10 nạp tự động vào `IConfiguration` lúc khởi động):
  * *Name:* `/exammaker/dev/Bedrock/ModelId`
  * *Description:* `Active Bedrock inference profile ID (Claude Haiku 4.5 for dev, Claude Sonnet 4.6 for demo)`
  * *Tier:* `Standard` (tối đa 10.000 parameters, kích thước ≤ 4 KB, chi phí **$0**)

![Tạo tham số /exammaker/dev/Bedrock/ModelId ở Tier Standard](/images/5-Workshop/5.5-SSM-Parameter-Store/11.png)

#### Bước 2: Chọn Type (`String` / `SecureString`) & Giá trị

* *Type:* `String` (đối với các biến nhạy cảm như mật khẩu DB, chọn `SecureString` kèm KMS key mặc định `alias/aws/ssm` — chi phí $0).
* *Data type:* `text`
* *Value:* `global.anthropic.claude-haiku-4-5-20251001-v1:0` (chuyển sang `global.anthropic.claude-sonnet-4-6` khi demo mà không cần sửa mã nguồn).
- Bấm **Create parameter**.

![Cấu hình Type String và giá trị Bedrock ModelId](/images/5-Workshop/5.5-SSM-Parameter-Store/11.2.png)
