---
title: "Session Policies trong Amazon EKS Pod Identity"
date: 2026-10-25
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

{{% notice info %}}
**Thông tin bài viết chuyên môn:**
* **Chủ đề:** Giới hạn đặc quyền tối thiểu (Least Privilege) với Session Policies trong Amazon EKS Pod Identity.
* **Dịch vụ trọng tâm:** Amazon EKS, AWS IAM, EKS Pod Identity Agent.
* **Người tổng hợp:** Kỹ sư thực tập Điện toán đám mây (Cloud Intern Builder).
{{% /notice %}}

Amazon EKS Pod Identity bổ sung tính năng **Session Policies**, cho phép thu hẹp quyền IAM linh hoạt và chính xác cho từng pod mà không cần tạo thêm nhiều IAM roles riêng biệt. Đây là bước tiến quan trọng giúp áp dụng nguyên tắc đặc quyền tối thiểu (Least Privilege) hiệu quả trong môi trường Kubernetes quy mô doanh nghiệp.

---

### 📌 1. Các Điểm Kỹ Thuật Trọng Tâm

* **Bản chất của Session Policy:** Là một IAM policy inline được chỉ định khi tạo hoặc cập nhật liên kết Pod Identity (Pod Identity association).
* **Cơ chế tính quyền hiệu quả:**
  $$\text{Effective Permissions} = \text{IAM Role Permissions} \cap \text{Session Policy}$$
  Session policy chỉ có khả năng **thu hẹp (narrow down)** quyền, không bao giờ có thể mở rộng quyền vượt quá quyền hạn của Role gốc.
* **Loại bỏ rủi ro cấp thừa quyền (Over-permissioning):** Khi nhiều workload dùng chung một IAM Role (ví dụ Data Processing Role), từng pod cụ thể có thể được siết chặt chỉ truy cập bucket S3 hoặc bảng DynamoDB riêng của nó.
* **Hỗ trợ đa tài khoản:** Hoạt động ổn định trên cùng tài khoản AWS và xuyên tài khoản (Cross-account qua IAM Role Chaining).
* **Tránh chạm ngưỡng IAM Quota:** Giảm thiểu đáng kể số lượng IAM Role cần khởi tạo, ngăn ngừa tình trạng chạm giới hạn quota IAM trong các cụm EKS hàng nghìn pods.

---

### 🛠️ 2. Ví Dụ Cấu Hình Session Policy Thực Tế

Giả sử IAM Role `AppSharedRole` có quyền truy cập toàn bộ tài nguyên S3 trong tài khoản. Ta muốn pod xử lý hóa đơn (`billing-service`) chỉ được phép đọc/ghi duy nhất bucket `my-company-billing-records`:

#### Cấu hình Policy JSON:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-company-billing-records/*"
    }
  ]
}
```

#### Thiết lập Pod Identity Association qua AWS CLI:
```bash
aws eks create-pod-identity-association \
  --cluster-name production-eks-cluster \
  --namespace billing-app \
  --service-account billing-sa \
  --role-arn arn:aws:iam::123456789012:role/AppSharedRole \
  --policy-statement '{"Effect":"Allow","Action":["s3:GetObject","s3:PutObject"],"Resource":"arn:aws:s3:::my-company-billing-records/*"}'
```

---

### 🚀 3. Giá Trị Thực Tiễn Cho Vận Hành Hạ Tầng

1. **Đơn giản hóa quản trị IAM:** Không còn tình trạng bùng nổ số lượng IAM Role (Role Sprawl) khi mở rộng cụm microservices.
2. **Tuân thủ chuẩn bảo mật khắt khe:** Dễ dàng đáp ứng các tiêu chuẩn PCI-DSS, ISO/IEC 27001 bằng cách cô lập truy cập theo từng Namespace và ServiceAccount.
3. **Hiệu năng cao hơn IRSA truyền thống:** EKS Pod Identity sử dụng DaemonSet agent cục bộ trên Node, loại bỏ phụ thuộc vào OIDC discovery endpoint và cải thiện tốc độ cấp phát STS temporary credentials.
