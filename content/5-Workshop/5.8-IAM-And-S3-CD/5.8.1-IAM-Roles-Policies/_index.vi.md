---
title : "Thiết lập 3 IAM Roles & Permissions Policies"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.8.1. </b> "
---

#### Bước 1: Kiểm tra 3 IAM Roles Cốt lõi (em-*) & Chi tiết Permissions Policies (Hình 18)

Mở **AWS IAM Console** → menu trái chọn **Roles** → nhập từ khóa **em-** vào ô tìm kiếm để kiểm tra 3 IAM Roles của dự án:

![Hình 18 — Danh sách 3 IAM Roles cốt lõi của dự án: aem-exammaker-ec2-role, aem-github-backend-deploy-role và aem-github-frontend-deploy-role](/images/5-Workshop/5.8-IAM-And-S3-CD/18.png)

---

#### Chi tiết cấu hình và các Permissions Policies bên trong từng IAM Role:

1. **em-exammaker-ec2-role (Trusted entity: AWS Service: ec2 — Gắn làm Instance Profile cho máy chủ EC2 em-exammaker-ec2):**
   - **AmazonSSMManagedInstanceCore** (*AWS managed policy*): Cho phép quản trị máy chủ qua **SSM Session Manager** và nhận lệnh triển khai từ **SSM Run Command** mà không cần mở cổng SSH 22.
   - **em-ec2-runtime-policy** (*Customer inline policy*):
     - Quyền gửi/nhận/xóa message trên hàng đợi chính exammaker-dev-ai-jobs.
     - Quyền gọi edrock:InvokeModel khóa chặt vào 2 inference profiles đã duyệt (global.anthropic.claude-haiku-4-5-20251001-v1:0 và global.anthropic.claude-sonnet-4-6).
     - Quyền quản trị tài khoản và nhóm người dùng trên Cognito User Pool exammaker-dev-users.
     - Quyền đọc tham số dưới /exammaker/dev/* và giải mã SecureString bằng KMS key lias/aws/ssm.
     - Quyền ghi log vào /exammaker/dev/app và đẩy metric vào namespace ExamMaker/Dev.
   - **em-ec2-read-backend-artifacts** (*Customer inline policy*): Cho phép s3:GetObject trên nhánh ackend/releases/* của bucket em-dev-backend-artifacts-9d07a0f131.
   - **ReadFrontendReleaseArtifacts & ReadFrontendStagingArtifact** (*Customer inline policies*): Cho phép EC2 tải gói build static frontend từ S3 về thư mục phục vụ của Nginx.

2. **em-github-backend-deploy-role (Trusted entity: Identity Provider: token.actions.githubusercontent.com — OIDC cho CI/CD Backend):**
   - **Trust policy:** Xác thực OIDC với Audience sts.amazonaws.com, khóa chặt vào repository lwndyy/new-ai-exam-maker, nhánh main và workflow .github/workflows/deploy-backend.yml.
   - **Inline policy em-github-backend-deploy-policy:**
     - UploadBackendReleaseArtifact: Đẩy gói build .tar.gz và .sha256 lên s3://aem-dev-backend-artifacts-9d07a0f131/backend/releases/*.
     - CreatePreMigrationRdsSnapshot: Chụp manual snapshot trên exammaker-dev-pg trước các đợt migration lớn.
     - TriggerSsmDeployOnTaggedEc2 & PollSsmCommandStatus: Gửi lệnh ssm:SendCommand (AWS-RunShellScript) tới máy chủ EC2 có tag Name = aem-exammaker-ec2 để chạy efbundle migration và cập nhật symlink /opt/exammaker/current.

3. **em-github-frontend-deploy-role (Trusted entity: Identity Provider: token.actions.githubusercontent.com — OIDC cho CI/CD Frontend):**
   - **Trust policy:** Khóa chặt vào repository lwndyy/new-ai-exam-maker, nhánh main.
   - **2 Inline policies (FrontendS3DeployAccess & FrontendO7SsmDeployAccess):** Cho phép đẩy bản build Next.js static export lên S3 và kích hoạt SSM đồng bộ xuống máy chủ EC2.