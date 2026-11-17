# Detailed Memory Ledger - AWS Workshop

File này đóng vai trò là nhật ký ghi nhớ chi tiết (Persistent Memory Ledger) cho dự án AWS Workshop.

---

## 🕒 Lịch sử cập nhật bộ nhớ (Memory Update Logs)

### [2026-11-17] Di trú toàn bộ tài liệu tham khảo sang tên miền chính thức https://cloudjourney.awsfcaj.com/

- **Bối cảnh:** Hệ thống tên miền cũ `awsstudygroup.com` (và các subdomains `0000xx.awsstudygroup.com`, `cloudjourney.awsstudygroup.com`) có nguy cơ bị hủy hoặc không truy cập được do chương trình First Cloud Journey (FCJ) đã chuyển đổi hoàn toàn sang nền tảng tên miền mới `awsfcaj.com`.
- **Phạm vi cập nhật (33 files):**
  - `config.toml`: Cập nhật menu shortcut sang `https://cloudjourney.awsfcaj.com`.
  - Cập nhật toàn bộ link lộ trình `https://cloudjourney.awsstudygroup.com/` ➔ `https://cloudjourney.awsfcaj.com/` (từ Tuần 8 đến Tuần 14).
  - Cập nhật toàn bộ link bài lab con:
    - 1.3.1 (Amazon RDS): `000005.awsstudygroup.com` ➔ `https://000005.awsfcaj.com/`.
    - 1.4.1 (Amazon Lightsail): `000045.awsstudygroup.com` ➔ `https://000045.awsfcaj.com/`.
    - 1.4.2 (Lightsail Container): `000046.awsstudygroup.com` ➔ `https://000046.awsfcaj.com/`.
    - 1.4.3 (EC2 Auto Scaling): `000006.awsstudygroup.com` ➔ `https://000006.awsfcaj.com/`.
    - 1.4.4 (Amazon CloudWatch): `000008.awsstudygroup.com` ➔ `https://000008.awsfcaj.com/`.
    - 1.5.1 (Hybrid DNS): `000010.awsstudygroup.com` ➔ `https://000010.awsfcaj.com/`.
    - 1.5.2 (AWS CLI): `000011.awsstudygroup.com` ➔ `https://000011.awsfcaj.com/`.
    - 1.5.3 (Amazon DynamoDB): `000060.awsstudygroup.com` ➔ `https://000060.awsfcaj.com/`.
    - 1.5.4 (Amazon ElastiCache): `000061.awsstudygroup.com` ➔ `https://000061.awsfcaj.com/`.
  - Giữ nguyên nhóm Facebook: `https://www.facebook.com/groups/awsstudygroupfcj`.

### [2026-11-17] Khắc phục toàn diện lỗi mất hình ảnh trên GitHub Pages & Hướng dẫn minh chứng Blog Facebook

- **Nguyên nhân mất hình ảnh (Lỗi 404 hình ảnh trên GitHub Pages):**
  - Website được deploy tại subpath `https://trangiabao2005.github.io/AWS-Workshop/`.
  - Trong Markdown, các thẻ ảnh ghi đường dẫn gốc tuyệt đối: `![alt](/images/...)`.
  - Trình duyệt hiểu dấu `/` đầu tiên là root domain, dẫn đến gửi request tới `https://trangiabao2005.github.io/images/...` (thiếu tiền tố repo `/AWS-Workshop/`), gây lỗi 404 cho toàn bộ hình ảnh.
- **Giải pháp xử lý triệt để:**
  - Tạo render hook Markdown chính thức tại `layouts/_default/_markup/render-image.html`: Tự động loại bỏ dấu `/` đầu và chạy qua pipe `| relURL` của Hugo.
  - Kết quả: Mọi ảnh trên toàn website tự động được gán tiền tố `/AWS-Workshop/images/...` khi deploy lên GitHub Pages và tích hợp popup zoom ảnh `data-featherlight="image"` mượt mà.
- **Hỗ trợ minh chứng bài đăng Facebook Blog 1 (`3.1-Blog1`):**
  - Vị trí dán link: `content/3-BlogsPosted/3.1-Blog1/_index.vi.md` và `_index.md`.
  - Thư mục lưu ảnh chụp màn hình minh chứng: `static/images/3-BlogsPosted/3.1-Blog1/facebook-post-proof.png`.

### [2026-11-17] Tích hợp Skill Avoid-AI-Writing & Chuẩn hóa toàn bộ Mục 5 (Workshop S3 Hybrid Access)

- **Tích hợp Skill `avoid-ai-writing`:**
  - Khởi tạo thành công tại `.agents/skills/avoid-ai-writing/` và đồng bộ vào thư mục skill toàn cục `C:\Users\se193234_TranGiaBao\.gemini\config\skills\avoid-ai-writing\SKILL.md`.
  - Bao gồm `SKILL.md`, `references/patterns.md`, và `references/voice-profiles.md`.
  - Định hình hồ sơ giọng văn `Technical Profile` cho Cloud Engineer, bộ quy tắc bảo tồn 100% mã nguồn/CLI/CIDR, và từ điển loại bỏ văn phong máy móc song ngữ Việt - Anh.

- **Chuẩn hóa toàn diện 24 files trong mục 5 (Workshop - S3 Hybrid Access via VPC Endpoints):**
  - **Xóa bỏ triệt để cảnh báo template:** Xóa hộp thoại *"⚠️ Lưu ý: Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng không sao chép nguyên văn..."* ở cả `_index.vi.md` và `_index.md`.
  - **Khắc phục lỗi dịch máy thô thiển:**
    - Thay thế *"môi trường truyền thống"* ➔ **"Môi trường On-Premises (Doanh nghiệp)"**.
    - Thay thế *"bộ chứa S3"* ➔ **"S3 Bucket"**.
    - Thay thế *"bản ghi Bí danh"* ➔ **"Alias Record"**.
    - Thay thế *"điểm cuối cổng"* ➔ **"Gateway Endpoint"**.
    - Loại bỏ các câu kết thúc sáo rỗng (*"Xin chúc mừng bạn đã hoàn thành..."*).
  - **Nâng cấp nội dung chuyên nghiệp:**
    - Bổ sung bảng so sánh Gateway Endpoint vs Interface Endpoint (AWS PrivateLink).
    - Làm rõ nguyên lý Conditional DNS Forwarding qua Route 53 Resolver (Inbound/Outbound Endpoints & Private Hosted Zone).
    - Chuẩn hóa các bước kiểm thử thực tế với Session Manager, `fallocate` 1GB, và kiểm soát rò rỉ dữ liệu qua VPC Endpoint Policy.
    - 100% build sạch trên Hugo (102 trang EN, 101 trang VI, 536 static files).

### [2026-11-17] Khắc phục GitHub Pages 404 & Tối ưu tự động bung menu Worklog Tuần 1-14

- **Vấn đề 1 (Lỗi GitHub Pages 404 - Page Not Found):**
  - **Nguyên nhân:** Cài đặt Settings ➔ Pages chọn nhánh `main` (chỉ chứa mã nguồn thô, không có `index.html` của Hugo). File `.gitmodules` gây xung đột khi GitHub Actions checkout theme.
  - **Khắc phục:** 
    - Xóa file `.gitmodules` (do thư mục theme `themes/hugo-theme-learn` đã được commit trực tiếp vào git tree).
    - Cập nhật `.github/workflows/hugo.yml` tích hợp chuẩn GitHub Pages Deployment chính thức (`actions/upload-pages-artifact@v3` và `actions/deploy-pages@v4`).
    - Hướng dẫn chuyển cài đặt GitHub Pages sang **Source: GitHub Actions**.

- **Vấn đề 2 (Tự động mở danh mục con khi bấm vào Tuần 1 tới Tuần 14):**
  - **Yêu cầu:** Khi bấm vào bất kỳ tuần nào (Week 1 đến Week 14) trên menu sidebar, tự động hiển thị ngay danh mục bài lab/ngày con bên dưới, không bắt người dùng phải bấm vào mũi tên nhỏ bên phải.
  - **Khắc phục:**
    - `layouts/partials/menu.html`: Cập nhật logic `{{ $isActive := or (eq .RelPermalink $currentNode.RelPermalink) (and $currentFileUniqueID .File (eq .File.UniqueID $currentFileUniqueID)) }}` và cấp class `parent` cho `li` khi active (`{{if or $isAncestor $isActive }}parent{{end}}`).
    - `static/css/theme-workshop.css`: Bổ sung selector `#sidebar ul.topics > li > ul > li.active > ul` hiển thị `display: block !important` và tự động xoay icon mũi tên 90 độ khi tuần đang được chọn.
    - `layouts/partials/custom-footer.html`: Cập nhật script JavaScript hỗ trợ toggle đóng/mở ngay cả khi `li` có class `active`.

### [2026-10-04] Tái cấu trúc & Phân bổ nội dung Cloud Journey

- **Dự án & Phạm vi:** AWS Workshop (`d:\AWS\template_AWS\fcj-workshop-template-main`). Hoàn thiện phân bổ lộ trình học từ **Cloud Journey** cho Tuần 1, Tuần 2 và Tuần 3.
- **Tiến độ đã hoàn thành:**
  - **Week 1 (14/09 - 18/09):** Đã điền các chủ đề _Explore AWS Services_ (IAM, VPC, EC2, S3, CLI...) và _Migrate to AWS_.
  - **Week 2 (21/09 - 25/09):** Đã điền các chủ đề _Optimizing the system on AWS_ (Security, Operations, Reliability, Cost) và một phần _Application Modernization (Serverless)_.
  - **Week 3 (28/09 - 02/10):** Tiếp tục _Application Modernization_, _Container Services_, _Data Analytics_, và _AI/ML_.
  - Riêng **Thứ 5 (01/10/2026)** ở Week 3 vẫn giữ nguyên bài thực hành trọng tâm: **Get Started with Amazon RDS** (Gồm: VPC, EC2 Web, RDS DB, Backup & Restore).
  - Tạm thời chưa có hình ảnh minh họa cho các phần bổ sung từ Cloud Journey, sẽ update ảnh thực hành sau. Lộ trình học trải đều liên tục từ 14/09/2026.

- **Lộ trình công việc buổi tiếp theo:**
  - Sẵn sàng chuyển sang các bài thực hành/Worklog của tuần tiếp theo (Ví dụ: Week 4 hoặc Week 5).

### [2026-10-13] Chuẩn hóa toàn bộ cấu trúc bài thực hành Tuần 4 (Trọn bộ Thứ 2 đến Thứ 6)

- **Dự án & Phạm vi:** Cập nhật và hoàn thiện hệ thống tài liệu Worklog Tuần 4 (`content/1-Worklog/1.4-Week4/`).
- **Tiến độ đã hoàn thành:**
  - Chuẩn hóa tên bài thực hành chuyên nghiệp, tổ chức thư mục hình ảnh riêng biệt và liên kết nguồn workshop:
    - **1.4.1 (Thứ 2):** `1.4.1-amazon-lightsail.vi.md` & `.md` — **Triển khai Amazon Lightsail** (13 ảnh, nguồn: `https://000045.awsstudygroup.com/`).
    - **1.4.2 (Thứ 3):** `1.4.2-lightsail-container.vi.md` & `.md` — **Triển khai Amazon Lightsail Container** (11 ảnh, nguồn: `https://000046.awsstudygroup.com/`).
    - **1.4.3 (Thứ 4):** `1.4.3-ec2-auto-scaling.vi.md` & `.md` — **Tự động co giãn với EC2 Auto Scaling** (44 ảnh, nguồn: `https://000006.awsstudygroup.com/`).
    - **1.4.4 (Thứ 5):** `1.4.4-amazon-cloudwatch.vi.md` & `.md` — **Giám sát với Amazon CloudWatch** (33 ảnh, nguồn: `https://000008.awsstudygroup.com/`).
    - **1.4.5 (Thứ 6):** `1.4.5-hybrid-dns.vi.md` & `.md` — **Thiết lập Hybrid DNS với Route 53 Resolver** (11 ảnh, nguồn: `https://000010.awsstudygroup.com/`).
  - Tái cấu trúc trang tổng quan `_index.vi.md` và `_index.md` đầy đủ 5 ngày (Thứ 2 đến Thứ 6) với bảng kế hoạch, mục tiêu, thành tựu từng ngày và link báo cáo thực hành chi tiết.
  - Phân loại toàn bộ hình ảnh trong `static/images/1-Worklog/1.4-Week4/` thành 5 thư mục con chuẩn hóa:
    - `1.4.1-amazon-lightsail/` (13 ảnh)
    - `1.4.2-lightsail-container/` (11 ảnh)
    - `1.4.3-ec2-auto-scaling/` (44 ảnh)
    - `1.4.4-amazon-cloudwatch/` (33 ảnh)
    - `1.4.5-hybrid-dns/` (11 ảnh)
  - Đồng bộ đường dẫn hình ảnh tuyệt đối cho Hugo (`/images/1-Worklog/1.4-Week4/...`), không chứa khoảng trắng.
  - Tuân thủ nghiêm ngặt quy tắc song ngữ: 100% Tiếng Việt cho `.vi.md` và 100% Tiếng Anh cho `.md`.

### [2026-10-14] Hoàn thiện Worklog Thứ 2 Tuần 5 (Thao tác dòng lệnh với AWS CLI)

- **Dự án & Phạm vi:** Cập nhật tài liệu Tuần 5 (`content/1-Worklog/1.5-Week5/`).
- **Nguồn tài liệu:** [Getting Started with the AWS CLI](https://000011.awsstudygroup.com/)
- **Tiến độ đã hoàn thành:**
  - Chuẩn hóa tên thư mục ảnh từ `Command Line Operations with AWS CLI` sang `1.5.1-aws-cli/` (chứa trọn vẹn 38 ảnh minh chứng từ Module 2 đến Module 9).
  - Khởi tạo trang bài viết chi tiết song ngữ theo **phong cách Step-by-step thực tế (từng bước làm, từng thông số điền cụ thể, câu lệnh và ảnh minh chứng)**:
    - [1.5.1-aws-cli.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.1-aws-cli.vi.md) (100% Tiếng Việt, chia 38 bước tương ứng 38 ảnh, không viết văn suông lý thuyết).
    - [1.5.1-aws-cli.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.1-aws-cli.md) (100% Tiếng Anh chuẩn mực).
  - Cập nhật trang tổng quan Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Đúc kết chi tiết 12 khó khăn kỹ thuật thực tế (Default Subnet missing, Connection timed out, S3 Global Namespace, SNS syntax & email spam, VPC CLI vs Web Region mismatch, Elastic IP association, NoCredentials when inside guest instance).

### [2026-10-14] Đồng bộ toàn diện phong cách Step-by-Step (thực hành từng bước) cho toàn bộ Tuần 4

- **Dự án & Phạm vi:** Tái cấu trúc và chuẩn hóa toàn bộ 5 bài lab Tuần 4 (`content/1-Worklog/1.4-Week4/`) theo phong cách thực hành thực chiến:
  - Loại bỏ hoàn toàn lối viết lý thuyết chung chung ("không ụp nguyên tài liệu lý thuyết").
  - Chia nhỏ thành từng bước cụ thể (`#### Bước X / Step X`), chỉ rõ thao tác nhấp chuột trên console, thông số nhập liệu chính xác, câu lệnh CLI và ảnh minh chứng tương ứng:
    - **1.4.1 (Amazon Lightsail):** 13 bước thực hành chi tiết (MySQL 8.0, gói $15, Static IP, WordPress wizard, Prestashop setup, Snapshot ~20GB, Migration gói lớn hơn).
    - **1.4.2 (Lightsail Container):** 11 bước thực hành chi tiết (Cài đặt AWS CLI, phân quyền `AmazonLightsailFullAccess`, khởi tạo Container Service Nano, build instance Ubuntu, plugin `lightsailctl`, push image, truy cập HTTPS).
    - **1.4.3 (EC2 Auto Scaling):** 44 bước thực hành chi tiết (Tạo Custom AMI, Target Group `fcaj-tg`, ALB `fcaj-alb`, Launch Template `fcaj-launch-template`, ASG Min=1/Desired=1/Max=3, Target Tracking CPU 50%, Stress test 600s, teardown an toàn 4 bước).
    - **1.4.4 (Amazon CloudWatch):** 33 bước thực hành chi tiết (Cài agent, Search expressions, Math expressions, Dynamic labels, Logs Insights query/filter/parse/stats, Metric filter HTTP 404, Alarm SNS).
    - **1.4.5 (Hybrid DNS):** 11 bước thực hành chi tiết (Key pair, CloudFormation 2 VPC, mở Port 53 TCP & UDP, AWS Managed Microsoft AD `corp.example.com`, Outbound/Inbound Resolver Endpoints, Resolver Rules, kiểm tra `nslookup` hai chiều).
  - Đặt các hộp ghi chú sự cố thực tế trực tiếp dưới từng bước tương ứng (**💡 Khó khăn gặp phải & Cách xử lý**).
  - Giữ nguyên các phần đầu trang chuẩn mực: **🎯 Lab Objectives** và **📊 Provisioned Resource Specifications**.
  - Kiểm thử Hugo build: 88 trang EN, 87 trang VI, 337 static files, 0 errors.

### [2026-10-15] Hoàn thiện Worklog Thứ 3 Tuần 5 (Làm việc với Amazon DynamoDB)

- **Dự án & Phạm vi:** Hoàn thiện toàn bộ tài liệu Worklog Thứ 3 Tuần 5 (`content/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb.vi.md` và `.md`).
- **Nguồn tài liệu:** [Work with Amazon DynamoDB](https://000060.awsstudygroup.com/)
- **Tiến độ đã hoàn thành:**
  - Chuẩn hóa tên thư mục ảnh từ `1.5.2-Amazon DynamoDB` sang `1.5.2-amazon-dynamodb/` (trọn bộ 32 hình ảnh minh chứng thực tế từ Module 2.1 đến 3.2).
  - Tải và giải nén thành công tệp dữ liệu mẫu `moviedata.json` (3.7MB, 4.609 bộ phim) phục vụ lập trình SDK.
  - Soạn thảo song ngữ Step-by-Step thực chiến:
    - [1.5.2-amazon-dynamodb.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb.vi.md) (100% Tiếng Việt, 32 bước thực hành, 10 khó khăn kỹ thuật chuyên sâu).
    - [1.5.2-amazon-dynamodb.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb.md) (100% Tiếng Anh chuẩn kỹ thuật).
  - Khởi tạo bộ 8 script Python tự động hóa: `MoviesCreateTable.py`, `MoviesItemOps01.py` -> `04.py`, `MoviesLoadData.py`, `MoviesQuery01.py`, `MoviesScan.py`, `MoviesDeleteTable.py`.
  - Cập nhật trang tổng quan Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Đúc kết chi tiết 10 khó khăn kỹ thuật thực tế: Lỗi cú pháp workshop gốc (`--provided-throughput`), phân quyền IAM User `AccessDeniedException`, lỗi trùng tên bảng `ResourceInUseException`, ký tự ẩn Unicode `\u200b`, cơ chế terminal Pager tự out, lỗi Backfilling index khi query, nhầm lẫn môi trường Windows CMD/Python, lỗi đường dẫn `System32`, và lỗi lệch Region khi xóa bảng (`ResourceNotFoundException`).
  - Kiểm thử Hugo build: 89 trang EN, 88 trang VI, 369 static files, 0 errors.

### [2026-10-20] Hoàn thiện Worklog Thứ 4 Tuần 5 (Triển khai Amazon ElastiCache - Redis)

- **Dự án & Phạm vi:** Hoàn thiện toàn bộ tài liệu Worklog Thứ 4 Tuần 5 (`content/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache.vi.md` và `.md`).
- **Nguồn tài liệu:** [Amazon ElastiCache - Redis](https://000061.awsstudygroup.com/) (Workshop 000061).
- **Khu vực AWS (Region):** `us-east-1` (N. Virginia).
- **Tiến độ đã hoàn thành:**
  - Chuẩn hóa và đồng bộ trọn bộ 27 hình ảnh thực hành tại `static/images/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache/` (từ `2.1.png` đến `4.6.png`).
  - Soạn thảo tài liệu song ngữ theo phong cách **Step-by-Step thực chiến**:
    - [1.5.3-amazon-elasticache.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache.vi.md) (100% Tiếng Việt, 26 bước chi tiết, 12 khó khăn kỹ thuật).
    - [1.5.3-amazon-elasticache.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache.md) (100% Tiếng Anh chuẩn kỹ thuật).
  - Tích hợp chuyên sâu tình huống người dùng yêu cầu:
    - **Lỗi khi chưa tạo User Group (`testusergroup` / `mygroup`):** `botocore.errorfactory.UserGroupNotFoundFault` khi chạy `ClusterModeDisabledWithRBAC.py` (minh chứng ảnh `4.1.1.1.png` và `4.1.2.1.png`).
    - **Khởi tạo User Group qua `UserAndUserGroups.py`:** Tạo `myuser`, `default` user bắt buộc và gán vào `mygroup` (minh chứng ảnh `4.1.3.png`).
    - **Kết quả thành công:** Chạy lại kịch bản tạo cụm RBAC thành công với HTTP 200 (minh chứng ảnh `4.1.3.1.png` và `4.1.3.2.png`).
  - Triển khai đầy đủ các script tương tác: kiểm tra kết nối mã hóa TLS RBAC (`4.2.1.2.png`), kết nối cụm phân mảnh (`4.2.2.1.png`), thao tác Strings TTL 60s (`4.3.png`), thao tác Hash kèm xóa key cũ chống xung đột WRONGTYPE (`4.4.png`), và phát/nhận luồng tin Pub/Sub (`4.5.png`, `4.6.png`).
  - Cập nhật trang tổng quan Tuần 5 ([\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).

### [2026-10-21] Hoàn thiện Worklog Thứ 5 Tuần 5 (Quản lý và Nâng hạn mức với AWS Service Quotas)

- **Dự án & Phạm vi:** Hoàn thiện toàn bộ tài liệu Worklog Thứ 5 Tuần 5 (`content/1-Worklog/1.5-Week5/1.5.4-service-quotas.vi.md` và `.md`).
- **Nguồn tài liệu:** [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/) & AWS Support Center.
- **Khu vực AWS (Region):** `us-east-1` (US East - N. Virginia).
- **Tiến độ đã hoàn thành:**
  - Đồng bộ và chuẩn hóa bộ 4 hình ảnh thực hành tại `static/images/1-Worklog/1.5-Week5/1.5.4-service-quotas/`:
    - `1-request-quota-modal.png`: Giao diện modal yêu cầu tăng hạn mức, bắt lỗi validation khi nhập 32.
    - `2-service-quotas-dashboard.png`: Dashboard Service Quotas ghi nhận yêu cầu tăng trần vCPU lên 64, trạng thái `Case Closed`.
    - `3-email-approval.png`: Thư điện tử phê duyệt chính thức từ Amazon Web Services gửi về Gmail.
    - `4-support-case-details.png`: Chi tiết hồ sơ hỗ trợ Case ID `179257232100832` trên AWS Support Center (Basic Support Plan).
  - Soạn thảo song ngữ Step-by-Step chuẩn mực:
    - [1.5.4-service-quotas.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.4-service-quotas.vi.md) (100% Tiếng Việt, 5 mục, 13 bước chi tiết, 8 bài học kinh nghiệm).
    - [1.5.4-service-quotas.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.4-service-quotas.md) (100% Tiếng Anh kỹ thuật FinOps & Cloud Architecture).
  - Phân tích và làm sáng tỏ câu hỏi kinh tế đám mây cốt lõi: _Việc nâng hạn mức Quota từ 32 lên 64 vCPU có bị trừ tiền không?_ (Hoàn toàn MIỄN PHÍ; AWS chỉ tính phí khi người dùng thực sự khởi chạy máy ảo).
  - Bổ sung kịch bản tự động hóa dòng lệnh AWS CLI (`aws service-quotas`) và phương án giám sát chủ động với CloudWatch Alarms ở ngưỡng 80% và 95%.

### [2026-10-21] Chuẩn hóa toàn diện Tuần 1, Tuần 2 và Tuần 3

- **Dự án & Phạm vi:** Tái cấu trúc và tinh gọn toàn bộ trang tổng quan Tuần 1, 2, 3; tách riêng bài thực hành CSDL Amazon RDS ở Tuần 3 thành trang con `1.3.1-amazon-rds.vi.md` và `.md`.
- **Tiến độ đã hoàn thành:**
  - **Khởi tạo bài thực hành con 1.3.1 (Amazon RDS):**
    - [1.3.1-amazon-rds.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.3-Week3/1.3.1-amazon-rds.vi.md) & [1.3.1-amazon-rds.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.3-Week3/1.3.1-amazon-rds.md).
    - Đồng bộ bộ 10 hình ảnh kiến trúc và cấu hình vào `static/images/1-Worklog/1.3-Week3/1.3.1-amazon-rds/`.
    - Trình bày đầy đủ: Sơ đồ kiến trúc 2 tầng (Two-Tier), bảng thông số tài nguyên, quy trình cấu hình Security Group chuỗi liên kết (Chaining), DB Subnet Group đa vùng, RDS MySQL Multi-AZ, Web Server EC2 và sao lưu Snapshot.
  - **Tích hợp icon mũi tên điều hướng Sidebar cho Tuần 3:**
    - Khi có bài con 1.3.1, menu sidebar tự động kích hoạt icon mũi tên (`>`) và dấu tích xanh (`✓`) giống hệt Tuần 4 và Tuần 5. Menu con 1.3.1 thu gọn mặc định và mở rộng khi nhấp chuột.
  - **Tinh gọn trang tổng quan (Overview):**
    - **Tuần 1:** Cập nhật kết quả đạt được từ Thứ 2 đến Thứ 6 súc tích, thân thiện, nêu bật khái niệm đã học (IAM, VPC, S3, CloudWatch, EC2 Auto Scaling, Route 53, Migration).
    - **Tuần 2:** Cập nhật kết quả đạt được từ Thứ 2 đến Thứ 6 súc tích, thân thiện (Vận hành Lambda/CDK, Bảo mật SSO/KMS/WAF/GuardDuty, Độ tin cậy CI/CD, Tối ưu chi phí Savings Plans, Hiện đại hóa Serverless).
    - **Tuần 3:** Loại bỏ toàn bộ phần thực hành chi tiết dài và hình ảnh khỏi `_index`, thay bằng bảng tóm tắt súc tích, kèm hộp `notice tip` liên kết trực tiếp tới `1.3.1. Thực hành triển khai Amazon RDS`.
  - Kiểm thử Hugo build: 92 trang EN, 91 trang VI, 444 static files, 0 errors.

---

## 🛠️ Cấu hình & Tài nguyên AWS đã ghi nhớ (AWS Resources Log)

| Tài nguyên              | ID / Name                           | Thông số / Chi tiết                                                 | Ghi chú                                          |
| :---------------------- | :---------------------------------- | :------------------------------------------------------------------ | :----------------------------------------------- |
| **VPC**                 | `rds-vpc` (`vpc-0d0b88a31c814b1df`) | CIDR: 10.0.0.0/16, 2 AZs, 4 Subnets                                 | Đã khởi tạo phần 2.1                             |
| **Public Subnet**       | `rds-subnet-public1-us-east-1a`     | Auto-assign Public IP: Enabled                                      | Dành cho EC2 Web                                 |
| **Private Subnet**      | `rds-subnet-private1-us-east-1a`    | Private isolated subnet                                             | Dành cho RDS                                     |
| **EC2 SG**              | `ec2-sg` (`sg-0cec4d0fbfc6d4c41`)   | Inbound: Port 22 (SSH), Port 80 (HTTP)                              | Public Subnet                                    |
| **RDS SG**              | `rds-sg` (`sg-0331b33d6bf62d714`)   | Inbound: Port 3306 (MySQL) từ `ec2-sg`                              | Private Subnet                                   |
| **DB Subnet Group**     | `rds-subnet-group`                  | 2 AZs (`us-east-1a`, `us-east-1b`)                                  | Sẵn sàng cho RDS                                 |
| **RDS DB Instance**     | `db-instance`                       | MySQL Community, `db.m5.large`, Multi-AZ                            | Endpoint: `db-instance.cgnkaue6ib4x...`          |
| **Database Name**       | `fcaj`                              | Port: 3306                                                          | Username: `admin`                                |
| **EC2 Web Server**      | `web-server`                        | `t2.micro`, Amazon Linux 2023                                       | Đặt tại Public Subnet                            |
| **Lightsail DB**        | `Workshop-DB-Instance`              | MySQL (STANDARD $15), 1GB RAM, 2 vCPUs                              | Master DB: `dbWordPress`                         |
| **Lightsail DB User**   | `LightsailAdmin`                    | Password: (custom)                                                  | Tag: `dbname=dbWordPress`                        |
| **EC2 Web Server (CW)** | `Web-Server-Lab`                    | Amazon Linux 2023, CloudWatch Agent installed                       | Thu thập metrics & logs                          |
| **Log Group (CW)**      | `/aws/ec2/system-logs`              | Retention: 7 ngày, Metric Filter: `HTTP404Errors`                   | CloudWatch Logs Insights                         |
| **CloudWatch Alarm**    | `High-CPU-Utilization-Alarm`        | Threshold: CPU > 70%, 2 periods (1 min), SNS alert                  | Monitoring                                       |
| **AD Directory (R53)**  | `corp.example.com`                  | AWS Managed Microsoft AD Standard Edition                           | DNS Server On-premises                           |
| **Outbound Resolver**   | `r53-outbound-resolver`             | 2 IP Endpoints tại 2 Subnets khác nhau                              | Forward query về On-prem AD                      |
| **Inbound Resolver**    | `r53-inbound-resolver`              | 2 IP Endpoints tại 2 Subnets khác nhau                              | Ingest query từ On-prem lên AWS                  |
| **IAM Group (CLI)**     | `aws-cli`                           | Policy: `AdministratorAccess`                                       | Phục vụ bài AWS CLI                              |
| **IAM User 1 (CLI)**    | `aws-cli-user`                      | Member of `aws-cli` + CLI Access Key                                | Default profile                                  |
| **IAM User 2 (CLI)**    | `devops`                            | Member of `aws-cli` + CLI Access Key                                | devops profile                                   |
| **EC2 Bastion (CLI)**   | `aws-cli-instance`                  | `t3.micro`, Amazon Linux 2023, Key: `aws-cli-keypair`               | Quản trị viên SSH MobaXterm                      |
| **S3 Bucket (CLI)**     | `aws-cli-trangiabao-2026`           | S3 Standard Storage (Singapore)                                     | Test object storage                              |
| **SNS Topic (CLI)**     | `aws-cli`                           | ARN: `arn:aws:sns:ap-southeast-1:887086382708:aws-cli`              | Kênh gửi Email thông báo                         |
| **VPC (CLI Lab)**       | `vpc-07ebcfa7f5b9c659c`             | CIDR: `10.0.0.0/16` (Singapore)                                     | Tạo hoàn toàn bằng CLI                           |
| **Subnet (CLI Lab)**    | `subnet-03c90d43fb1f53b06`          | CIDR: `10.0.1.0/24` (Singapore `ap-southeast-1a`)                   | Tạo hoàn toàn bằng CLI                           |
| **IGW (CLI Lab)**       | `igw-006783ef67381e1d4`             | Attached to `vpc-07ebcfa7f5b9c659c`                                 | Cổng Internet cho VPC                            |
| **EC2 Automated**       | `i-03171455cd0278073`               | `t2.micro`, Private: `10.0.1.41`, Key: `MyKeyPair`                  | Khởi tạo qua run-instances                       |
| **Elastic IP (CLI)**    | `47.131.189.63`                     | `eipalloc-0f52955fe9fe8ad41`                                        | Cấp phát và gán cho EC2                          |
| **DynamoDB Table 1**    | `Music`                             | Partition: `Artist` (S), Sort: `SongTitle` (S)                      | Provisioned RCU=10, WCU=5 (`us-east-1`)          |
| **DynamoDB GSI**        | `AlbumTitle-index`                  | Partition: `AlbumTitle` (S), Projection: `ALL`                      | GSI cho bảng `Music` (`us-east-1`)               |
| **DynamoDB Table 2**    | `Movies`                            | Partition: `year` (N), Sort: `title` (S)                            | Provisioned RCU=10, WCU=10 (`ap-southeast-1`)    |
| **IAM User (DDB)**      | `AWS-FCAJ-DynamDB`                  | Policy: `AmazonDynamoDBFullAccess`                                  | Phục vụ CloudShell & Python SDK                  |
| **Sample Dataset**      | `moviedata.json`                    | 4.609 phim (3.7 MB), JSON format                                    | Nạp dữ liệu kiểm thử Query & Scan                |
| **VPC (ElastiCache)**   | `vpc-0fc9d5490a843944e`             | 3 Subnets (`1a`, `1b`, `1c`), IGW `my-igw`                          | Region `us-east-1`                               |
| **Subnet Group**        | `subnet-group`                      | 3 Subnets across `us-east-1a`, `1b`, `1c`                           | Phục vụ Redis Multi-AZ                           |
| **Security Group**      | `sg-06c03603fe1cca808`              | Inbound: Port 22 (SSH), Port 6379 (Redis)                           | Phục vụ EC2 và ElastiCache                       |
| **EC2 Redis Client**    | `redis-client`                      | `t2.micro`/`t3.micro`, AL2023, Python 3 + `redis-py`                | Chạy lệnh kiểm thử Redis                         |
| **Redis Cluster 1**     | `my-cluster-disable`                | Mode Disabled, 1 Node Group, Port 6379                              | Endpoint: `my-cluster-disable.1vblox.ng.0001...` |
| **Redis Cluster 2**     | `my-cluster-enable`                 | Mode Enabled, 2 Shards, Port 6379                                   | Config: `my-cluster-enable.1vblox.clustercfg...` |
| **Redis Cluster 3**     | `redis-disabled-sdk`                | Mode Disabled, tạo bằng Boto3 SDK                                   | Endpoint: `redis-disabled-sdk.1vblox.ng.0001...` |
| **Redis Cluster 4**     | `redis-enabled-sdk`                 | Mode Enabled, 2 Node Groups qua SDK                                 | Config: `redis-enabled-sdk.1vblox.clustercfg...` |
| **Redis Cluster 5**     | `redis-rbac-sdk`                    | Mode Disabled, TLS Encryption + RBAC                                | Endpoint: `master.redis-rbac-sdk.1vblox...`      |
| **RBAC User Group**     | `mygroup`, `mygroup2`               | User Groups quản lý quyền Redis RBAC                                | Gán vào cụm Redis có TLS                         |
| **RBAC Users**          | `myuser`, `default`                 | Mật khẩu: `MyStrongPasswordWithNumbers123`                          | Phân quyền truy cập kênh & key Redis             |
| **Service Quota**       | `L-34B43A08`                        | EC2 Spot: `All Standard (A,C,D,H,I,M,R,T,Z) Spot Instance Requests` | Vùng `us-east-1`, Account `887086382708`         |
| **Quota Value**         | `64 vCPUs`                          | Đã nâng thành công từ 32 lên 64 vCPUs (Miễn phí)                    | Effective trong 30 phút                          |
| **Support Case ID**     | `179257232100832`                   | Trạng thái: `Case Closed` / `Approved`                              | Basic Support Plan                               |

---

## 🔍 Bảng tra cứu sự cố & Khó khăn kỹ thuật đã giải quyết (Troubleshooting Memory Bank)

Phần này dùng để tra cứu ngay lập tức khi người dùng hỏi lại về các lỗi thực tế đã gặp và phương án khắc phục:

### 📌 Nhóm lỗi ElastiCache & Redis (Thứ 4 Tuần 5 - 14/10/2026):

1. **Không thấy IGW và Route Table bị lỗi Blackhole làm mất mạng:**
   - _Hiện tượng:_ Người dùng vào VPC không thấy Internet Gateway đâu, mở Route Table thấy dòng route trỏ ra ngoài bị báo `Blackhole`. EC2 Instance Connect không kết nối được và lệnh tải gói bị timeout.
   - _Nguyên nhân:_ IGW mặc định trước đó đã bị xóa hoặc tách khỏi VPC nhưng Route Table vẫn giữ nguyên route `0.0.0.0/0` trỏ vào ID cũ, gây ra hiện tượng định tuyến vào "lỗ đen" (Blackhole).
   - _Cách xử lý:_ Tạo một Internet Gateway mới đặt tên `my-igw`, đính kèm (Attach) vào VPC `vpc-0fc9d5490a843944e`. Sau đó vào Route Table xóa route Blackhole cũ và thêm route mới `0.0.0.0/0` trỏ tới `my-igw`.
2. **Lệnh `pip3` không tìm thấy (`-bash: pip3: command not found`):**
   - _Hiện tượng:_ Người dùng gõ `pip3 install redis` trên máy ảo EC2 thì terminal trả về `-bash: pip3: command not found`.
   - _Nguyên nhân:_ Máy ảo Amazon Linux 2023 chỉ cài bản Python 3 tối giản của hệ thống, chưa tích hợp sẵn trình quản lý gói `pip3`.
   - _Cách xử lý:_ Phải cài gói quản lý pip từ kho yum/dnf của Amazon bằng lệnh: `sudo dnf install -y python3-pip`.
3. **Lỗi thiếu thư viện `redis` (`ModuleNotFoundError: No module named 'redis'`):**
   - _Hiện tượng:_ Sau khi tạo file code Python và thực thi trên EC2, chương trình văng lỗi `ModuleNotFoundError: No module named 'redis'`.
   - _Nguyên nhân:_ Môi trường Python trên EC2 chưa được cài đặt driver `redis-py` để giao tiếp với Redis server.
   - _Cách xử lý:_ Thực hiện lệnh `pip3 install redis` để tải và cài đặt thư viện `redis` (phiên bản v8.1.0).
4. **Thư viện `rediscluster` trong tài liệu Workshop bị khai tử/lỗi thời:**
   - _Hiện tượng:_ Tài liệu gốc yêu cầu viết `from rediscluster import RedisCluster`. Khi chạy thì lỗi không import được hoặc không tìm thấy module.
   - _Nguyên nhân:_ Thư viện bên thứ ba `redis-py-cluster` đã bị deprecated (dừng phát triển từ lâu) và các tính năng Cluster đã được sáp nhập trực tiếp vào thư viện chính thức `redis`.
   - _Cách xử lý:_ Thay thế hoàn toàn bằng câu lệnh import chính thức của Redis: `from redis.cluster import RedisCluster`.
5. **Endpoint mẫu trong tài liệu Workshop là dạng placeholder (`xxx.yyy...`):**
   - _Hiện tượng:_ Người dùng copy code từ workshop thấy endpoint có dạng `xxx.yyy.clustercfg.zzz1.cache.amazonaws.com` nên thắc mắc tại sao dán vào không chạy được.
   - _Nguyên nhân:_ Đây là ký hiệu ví dụ của AWS, không phải endpoint thực tế của cụm vừa tạo.
   - _Cách xử lý:_ Lấy đúng **Configuration Endpoint** thực tế của cụm `my-cluster-enable` trên AWS Console (`my-cluster-enable.1vblox.clustercfg.use1.cache.amazonaws.com:6379`) để dán vào code.
6. **Code mẫu bài 4.3 (Strings) và 4.4 (Hash) bị cắt cụt, thiếu phần khởi tạo biến `redis`:**
   - _Hiện tượng:_ Chạy file `SetAndGetStrings.py` hoặc `SetAndGetHash.py` theo workshop báo lỗi `NameError: name 'redis' is not defined`.
   - _Nguyên nhân:_ Tác giả workshop giả định người dùng chạy trên môi trường Interactive Shell (nơi biến `redis` đã được kết nối từ bài trước) nên trong file code mẫu chỉ viết mỗi phần `redis.set()` hay `redis.hset()`, thiếu hoàn toàn đoạn khởi tạo kết nối.
   - _Cách xử lý:_ Bổ sung khối kết nối `redis = RedisCluster(host="...", port=6379, decode_responses=True)` vào đầu cả 2 file script.
7. **Xung đột kiểu dữ liệu Redis (`WRONGTYPE Operation against a key holding the wrong kind of value`):**
   - _Hiện tượng:_ Chạy bài 4.4 (SetAndGetHash) báo lỗi `WRONGTYPE Operation against a key holding the wrong kind of value`.
   - _Nguyên nhân:_ Ở bài 4.3, key tên `mykey` được lưu dữ liệu kiểu chuỗi (`String`). Sang bài 4.4, tài liệu lại dùng tiếp đúng key `mykey` đó để ghi cấu trúc bảng băm (`Hash`) bằng lệnh `hset`. Do key cũ chưa hết thời gian 60 giây TTL nên Redis từ chối ghi đè vì xung đột kiểu dữ liệu.
   - _Cách xử lý:_ Thêm lệnh xóa an toàn `redis.delete(keyName)` ở đầu bài 4.4 trước khi thực hiện `hset`.
8. **Code mẫu Pub/Sub (bài 4.5) thiếu lệnh import `from redis import Redis`:**
   - _Hiện tượng:_ Chạy `PubAndSub.py` báo `NameError: name 'Redis' is not defined`.
   - _Nguyên nhân:_ Workshop dùng `redis = Redis(...)` nhưng phần khai báo import ở đầu file chỉ có `import logging` và `import time`.
   - _Cách xử lý:_ Bổ sung `from redis import Redis`, đồng thời bọc khối vòng lặp vô hạn `while True` trong `try...except KeyboardInterrupt` để người dùng có thể bấm `Ctrl + C` dừng chương trình gọn gàng mà không văng lỗi unhandled exception.
9. **Không thể kết nối tới Redis từ máy tính cá nhân (Connection Timed Out):**
   - _Hiện tượng:_ Người dùng chạy code kết nối Redis trên máy local (VS Code / PyCharm / Terminal máy tính) thì bị treo và báo `Connection timed out`.
   - _Nguyên nhân:_ Mặc định cụm Amazon ElastiCache nằm trong Private VPC, không có Public IP và không định tuyến ra Internet để bảo vệ dữ liệu.
   - _Cách xử lý:_ Bắt buộc phải tạo một máy ảo EC2 Client (`redis-client`) nằm cùng VPC với ElastiCache, gán Security Group mở Port 6379, sau đó chạy toàn bộ code kiểm thử từ bên trong máy ảo EC2 này.
10. **Lỗi từ chối tạo Subnet Group hoặc Cluster do thiếu Availability Zones:**
    - _Hiện tượng:_ AWS Console báo lỗi `Each Node Group needs to have at least two distinct Availability Zones` hoặc nút tạo cluster bị mờ đi không cho ấn.
    - _Nguyên nhân:_ Cụm Redis bật Multi-AZ hoặc Cluster Mode Enabled yêu cầu bắt buộc các node/shard phải được phân bổ trên tối thiểu 2 AZs khác nhau. Subnet Group ban đầu chỉ có subnet ở 1 AZ.
    - _Cách xử lý:_ Khởi tạo đủ 3 Subnets tại 3 AZ riêng biệt (`us-east-1a`, `us-east-1b`, `us-east-1c`) và thêm toàn bộ vào `subnet-group`.
11. **Lỗi cú pháp Python trong file mẫu `ClusterModeDisabledWithRBAC.py` của Workshop:**
    - _Hiện tượng:_ Chạy code SDK tạo cluster có RBAC bị báo lỗi `SyntaxError: non-default argument follows default argument`.
    - _Nguyên nhân:_ Workshop định nghĩa hàm với tham số không có giá trị mặc định (`CacheSubnetName`) đặt phía sau các tham số có giá trị mặc định (`CacheNodeType='cache.t3.micro'`), vi phạm quy tắc cú pháp hàm của Python.
    - _Cách xử lý:_ Gán giá trị mặc định `CacheSubnetGroupName=None` cho tham số đó.
12. **Độ trễ truyền tải quyền IAM (IAM Propagation Delay):**
    - _Hiện tượng:_ Vừa đính kèm policy `AmazonElastiCacheFullAccess` cho user xong, chạy script Boto3 SDK tạo cluster ngay thì bị AWS từ chối với lỗi `AccessDeniedException`.
    - _Nguyên nhân:_ Cơ chế IAM của AWS có độ trễ truyền dữ liệu phân quyền trên phạm vi toàn cầu từ 15 đến 45 giây.
    - _Cách xử lý:_ Chờ khoảng 30 giây để quyền IAM đồng bộ hoàn tất trước khi chạy script SDK.

### 📌 Nhóm lỗi DynamoDB (Thứ 3 Tuần 5 - 13/10/2026):

1. **Lỗi sai chính tả tham số trong tài liệu gốc:**
   - _Hiện tượng:_ Gõ lệnh tạo bảng báo lỗi `Unknown options: --provided-throughput`.
   - _Nguyên nhân:_ Workshop viết sai chính tả `provided` thay vì `provisioned`.
   - _Cách xử lý:_ Sửa thành `--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5`.
2. **Lỗi IAM `AccessDeniedException` khi truy cập DynamoDB:**
   - _Hiện tượng:_ IAM User `AWS-FCAJ-DynamDB` chạy lệnh CLI hoặc Python SDK bị từ chối truy cập.
   - _Nguyên nhân:_ Mới tạo user chưa cấp quyền quản lý cơ sở dữ liệu.
   - _Cách xử lý:_ Gán policy `AmazonDynamoDBFullAccess` cho user qua IAM Console hoặc CLI.
3. **Lỗi trùng tên bảng `ResourceInUseException`:**
   - _Hiện tượng:_ Chạy lệnh `create-table` bảng `Music` báo bảng đã tồn tại.
   - _Nguyên nhân:_ Đã tạo bảng `Music` từ giao diện Web Console ở phần trước.
   - _Cách xử lý:_ Dùng lệnh `aws dynamodb describe-table --table-name Music` kiểm tra trạng thái và tái sử dụng bảng đang `ACTIVE`.
4. **Lỗi ký tự tàng hình Unicode Zero-Width (`\u200b`):**
   - _Hiện tượng:_ Lệnh CLI báo lỗi parser cú pháp `Expected: '=', received: ''` dù nhìn bằng mắt chuỗi lệnh hoàn toàn đúng.
   - _Nguyên nhân:_ Khi copy từ trang web HTML bị dính 2 ký tự khoảng trắng vô hình (`\u200b`) ngay sau cờ `--expression-attribute-values`.
   - _Cách xử lý:_ Dán vào text editor bật hiển thị hidden characters hoặc gõ tay lại đoạn tham số.
5. **AWS CLI v2 Pager tự động thoát lệnh (`~ $`):**
   - _Hiện tượng:_ Sau khi chạy lệnh DynamoDB xem output, nhấn phím hoặc xem hết trang thấy con trỏ văng ra ngoài shell `~ $`.
   - _Nguyên nhân:_ CLI v2 mặc định bật trình phân trang `less`. Nhấn phím `q` hoặc khi hết trang nó tự động kết thúc.
   - _Cách xử lý:_ Nhấn `q` bình thường, hoặc vô hiệu hóa vĩnh viễn pager bằng lệnh `export AWS_PAGER=""`.
6. **Lỗi khóa truy vấn GSI đang Backfilling:**
   - _Hiện tượng:_ Query GSI `AlbumTitle-index` ngay sau khi tạo bị lỗi `ValidationException: Cannot read from backfilling global secondary index`.
   - _Nguyên nhân:_ DynamoDB cần thời gian quét và sao chép dữ liệu ngầm vào index.
   - _Cách xử lý:_ Chờ 1–2 phút kiểm tra bằng `describe-table` cho đến khi `IndexStatus` chuyển từ `CREATING` sang `ACTIVE`.
7. **Lỗi dán nhầm code Python vào Windows CMD:**
   - _Hiện tượng:_ Người dùng dán code `import boto3...` thẳng vào CMD dẫn đến thông báo `is not recognized as an internal or external command`.
   - _Nguyên nhân:_ Command Prompt chỉ nhận lệnh của hệ điều hành, không phải môi trường Python interactive.
   - _Cách xử lý:_ Lưu mã nguồn vào file script `.py` và thực thi bằng lệnh `python <file>.py`.
8. **Môi trường CMD mặc định ở thư mục `C:\Windows\System32`:**
   - _Hiện tượng:_ Chạy `python MoviesLoadData.py` báo `No such file or directory`.
   - _Nguyên nhân:_ Mở CMD với quyền Admin nên thư mục làm việc mặc định là `System32`, trong khi code và `moviedata.json` nằm ở ổ đĩa `D:`.
   - _Cách xử lý:_ Chuyển thư mục bằng lệnh `cd /d D:\AWS\template_AWS\fcj-workshop-template-main`.
9. **Nghẽn throughput khi nạp dữ liệu lớn (`moviedata.json`):**
   - _Hiện tượng:_ Nạp 4.609 bộ phim vào bảng `Movies` bị chậm hoặc dính `ProvisionedThroughputExceededException`.
   - _Nguyên nhân:_ Bảng cấu hình chỉ có 10 WCU, không kịp xử lý lượng ghi dồn dập.
   - _Cách xử lý:_ Nạp mẫu một phần dữ liệu đại diện hoặc tạm thời nâng WCU lên cao hơn khi nạp.
10. **Lỗi xóa bảng trên AWS CloudShell `ResourceNotFoundException`:**
    - _Hiện tượng:_ Chạy `aws dynamodb delete-table --table-name Music` trên CloudShell bị lỗi `Table: Music not found`.
    - _Nguyên nhân:_ Bảng `Music` được tạo ở Region Bắc Virginia (`us-east-1`), nhưng AWS CloudShell mặc định chạy ở Singapore (`ap-southeast-1`).
    - _Cách xử lý:_ Thêm cờ Region chính xác: `aws dynamodb delete-table --table-name Music --region us-east-1`.

---

### 📌 Nhóm lỗi AWS CLI (Thứ 2 Tuần 5 - 12/10/2026):

1. **Lỗi thiếu Default Subnet khi tạo EC2:** VPC mặc định chưa có subnet ở AZ yêu cầu ➔ Tạo thủ công `subnet-01` (`172.31.100.0/24`) và bật Auto-assign Public IP.
2. **Lỗi MobaXterm SSH Connection Timed Out:** Do thiếu đường ra Internet ➔ Tạo Internet Gateway, gắn vào VPC và thêm route `0.0.0.0/0` trỏ tới `igw`.
3. **Lệnh CLI kiểm tra EC2 không ra kết quả:** CLI mặc định đọc sai Region ➔ Bổ sung cờ `--region us-east-1 --output table`.
4. **Lỗi tạo S3 Bucket `BucketAlreadyExists`:** Tên bucket bị trùng trên toàn cầu ➔ Đổi tên bucket duy nhất: `aws-cli-trangiabao-2026`.
5. **Lỗi giữ nguyên placeholder `bucket-name`:** Người dùng copy nguyên văn mẫu ➔ Thay bằng tên bucket thật.
6. **Lỗi xóa bucket không rỗng `BucketNotEmpty`:** S3 chặn xóa bucket còn chứa file ➔ Thêm cờ `--force`.
7. **Lỗi cú pháp SNS `Unknown options: Topic**`:\*\* Nhập sai định dạng ➔ Thay thế bằng ARN chính xác của Topic.
8. **Không nhận email thông báo SNS:** Nhập sai email thiếu ký tự và thư bị phân vào mục Spam ➔ Sửa lại email chuẩn và xác nhận đường link trong hộp thư Spam.
9. **IGW tạo qua CLI không thấy trên Web Console:** Console đang mở ở Region khác ➔ Chuyển Region trên web sang Singapore (`ap-southeast-1`).
10. **Lỗi `Resource.AlreadyAssociated` khi attach IGW:** IGW đã được gắn thành công trước đó ➔ Kiểm tra trạng thái VPC trước khi attach.
11. **Máy chủ EC2 tạo bằng CLI không có Public IP (`Address: null`):** Subnet chưa bật cấp IP động ➔ Cấp phát Elastic IP và chạy lệnh `associate-address` gán vào instance.
12. **Lỗi `NoCredentials` khi chạy `terminate-instances`:** Đang đứng trong session SSH của máy khách (không có AWS credentials) ➔ Gõ `exit` quay lại máy quản trị ban đầu.

### [2026-10-20] Đồng bộ Chuẩn hóa Quy tắc Mục tiêu Tuần sau Nối tiếp (Continuous Next-Week Objectives)

- **Dự án & Phạm vi:** Cập nhật trang tổng quan song ngữ \_index.vi.md và \_index.md cho toàn bộ các tuần từ Tuần 1 đến Tuần 5.
- **Tiến độ đã hoàn thành:**
  - Thiết lập quy tắc nối tiếp: Ở cuối mỗi tuần (Tuần N) luôn có mục ### Mục tiêu cho tuần sau (Tuần N+1): mô tả chính xác nội dung thực tế của tuần kế tiếp (Tuần N+1).
  - **Cuối Tuần 1:** Ghi chi tiết mục tiêu của **Tuần 2** (Tối ưu hóa hệ thống: Operations, Security, Reliability, Cost & Hiện đại hóa ứng dụng Serverless).
  - **Cuối Tuần 2:** Ghi chi tiết mục tiêu của **Tuần 3** (App Modernization, Containers, Data Analytics, và Thực hành chuyên sâu Amazon RDS).
  - **Cuối Tuần 3:** Ghi chi tiết mục tiêu của **Tuần 4** (Amazon Lightsail, Lightsail Container, EC2 Auto Scaling, Amazon CloudWatch, Hybrid DNS Route 53 Resolver).
  - **Cuối Tuần 4:** Ghi chi tiết mục tiêu của **Tuần 5** (AWS CLI v2, Amazon DynamoDB, Amazon ElastiCache Redis).
  - **Cuối Tuần 5:** Ghi chi tiết mục tiêu của **Tuần 6** (Tự động hóa IaC CloudFormation/CDK/Terraform, Quản trị bảo mật KMS & Secrets Manager, CI/CD Pipeline CodePipeline).
  - Dịch và đồng bộ 100% bản tiếng Anh \_index.md cho các Tuần 1, Tuần 2, Tuần 3, Tuần 4, Tuần 5.
  - Cập nhật quy chuẩn mới vào SKILL.md.
  - Kiểm thử Hugo build: 90 trang EN, 89 trang VI, 423 static files, 0 errors.

### [2026-10-20] Ghi nhớ Cẩm nang Trình bày Worklog Áp dụng cho các Tuần sau (Standard Presentation & Workflow Framework)

- **Mục đích:** Đảm bảo toàn bộ các tuần tiếp theo (Tuần 5 các ngày còn lại, Tuần 6 đến Tuần 12) tuân thủ nhất quán 100% phong cách thiết kế, trình bày kỹ thuật và quy trình nối tiếp.
- **5 Trụ cột Quy chuẩn Bắt buộc:**
  1. **Quy tắc Nối tiếp Mục tiêu Tuần sau (Continuous Next-Week Objectives):**
     - Hoàn thành bài thực hành Tuần N+1 ➔ Lập tức quay lại cuối trang `_index.vi.md` và `_index.md` của Tuần N cập nhật mục `### Mục tiêu cho tuần sau (Tuần N+1):` / `### Next Week's Objectives (Week N+1):` sao cho khớp tuyệt đối với thực tế đã làm.
  2. **Cấu trúc Trang Index Tuần Chuẩn mực:**
     - FrontMatter (`title`, `date`, `weight`, `chapter: false`, `pre: " <b> 1.X. </b> "`).
     - Hộp Notice Warning nhắc không sao chép nguyên văn.
     - Mục tiêu định hướng tuần (`### Mục tiêu tuần X:`).
     - Bảng kế hoạch tuần 5 cột (`Thứ`, `Công việc chi tiết`, `Ngày bắt đầu`, `Ngày hoàn thành`, `Nguồn tài liệu`).
     - Báo cáo kết quả tuần: Hộp Notice Tip trỏ link bài chi tiết + tóm tắt công việc.
     - Đường phân cách `---` và Mục tiêu tuần kế tiếp.
  3. **Cấu trúc Báo cáo Lab Ngày Step-by-Step Thực chiến (Không lý thuyết suông):**
     - FrontMatter chuẩn (`weight: Y`, `pre: " <b> 1.X.Y. </b> "`).
     - **🎯 Mục tiêu bài thực hành (Lab Objectives):** 3-5 gạch đầu dòng.
     - **📊 Bảng thông số tài nguyên (Provisioned Resource Specifications):** Bảng chi tiết VPC, Subnet, CIDR, SG, Port, Instance Type, Engine, Auth...
     - **Nội dung thực hành theo từng bước (`#### Bước Z: [Tên bước]`):** Thao tác console/CLI, bảng thông số điền, lệnh shell/code script hoàn chỉnh, ảnh chụp màn hình thực tế, hộp warning chỉ rõ cách khắc phục lỗi tại chỗ.
     - **🛠️ Ngân hàng sự cố kỹ thuật thực tế (Real-world Troubleshooting Bank):** Tối thiểu 8-12 lỗi (Hiện tượng -> Nguyên nhân gốc rễ -> Cách khắc phục -> Ảnh so sánh lỗi vs thành công).
     - **🧹 Dọn dẹp tài nguyên (Resource Cleanup):** Trình tự teardown an toàn.
  4. **Quản trị Tài sản Hình ảnh (Image Assets):**
     - Thư mục riêng: `static/images/1-Worklog/1.X-WeekX/1.X.Y-ten-bai/`.
     - Tên file không dấu, không khoảng trắng, dạng `module.step.png`.
     - Đường dẫn nhúng tuyệt đối: `/images/1-Worklog/...`.
  5. **Nguyên tắc Đa ngôn ngữ Độc lập (Bilingual):**
     - `.vi.md`: 100% Tiếng Việt chuẩn mực, link `/vi/...`.
     - `.md`: 100% Tiếng Anh học thuật/AWS, link `/...`.

### [2026-10-21] Hoàn thành phân tích ghi âm sự kiện Event 2: Tọa đàm cùng Dr. Werner Vogels (CTO Amazon)

- **Dự án & Phạm vi:** Cập nhật mục Sự kiện đã tham gia (`content/4-EventParticipated/4.2-Event2/`) dựa trên bản ghi âm dài 53 phút (`Thoại 006_1.m4a` / `audio_event.mp3`).
- **Thông tin sự kiện:**
  - **Tên:** Fireside Chat with Dr. Werner Vogels: The Renaissance Developer & Building at Scale.
  - **Thời gian:** 09:00 - 10:30, 02/10/2026.
  - **Địa điểm:** Tầng 26, Tòa nhà Bitexco Financial Tower, số 02 Hải Triều, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh.
  - **Diễn giả chính:** Dr. Werner Vogels (VP & CTO toàn cầu của Amazon.com).
  - **Thành phần tham dự:** AWS Heroes, AWS Community Builders, Cloud Engineers và Intern Builders.
- **Tiến độ đã hoàn thành:**
  - Chuyển đổi và nén file ghi âm phục vụ phân tích đa phương thức (FFmpeg 16kHz mono MP3).
  - Trích xuất toàn bộ các luận điểm cốt lõi, bài học lịch sử và triết lý kiến trúc:
    - **Lịch sử ra đời của DynamoDB:** Sự cố sập hệ thống RDBMS thương mại ngày 12/12 giáng sinh dưới chương trình free shipping $25; phân tích của Swami Sivasubramanian chỉ ra 70% truy vấn là Key-Value; ra đời bài báo Dynamo 2007 và dịch vụ DynamoDB.
    - **Operational Excellence & Tail Latency (P99.9):** Cảnh báo bẫy trung vị (Median); tối ưu cho P99.9 để 0.1% người dùng yếu thế nhất vẫn nhanh; văn hóa GameDays chủ động ngắt Data Center; bài học reconciliation đồng bộ dữ liệu khi DC bật lại.
    - **Cloud Economics:** Xóa bỏ hợp đồng phần cứng 5-10 năm và tiền cọc vô lý; mô hình Pay-as-you-go; khởi đầu đơn giản của S3 năm 2006.
    - **5 Phẩm chất của The Renaissance Developer:** Tính tò mò & học tập suốt đời (Assembly -> Rust); Tư duy hệ thống (System Thinking); Kỹ năng giao tiếp (Communicator - thấu hiểu bài toán nghiệp vụ); Tinh thần làm chủ (Ownership - "You own what you build", chịu trách nhiệm mã nguồn AI sinh ra); Kỹ sư hình chữ T (Polymath).
    - **Triết lý Trí tuệ nhân tạo (AI):** AI 70 năm tuổi; AI hoạt động như một Trình biên dịch (Compiler) thế hệ mới từ ngôn ngữ tự nhiên; con người giữ vai trò phán đoán (Judgment) và thấu cảm (Empathy); Working Backwards (PR/FAQ); "Xây dựng công nghệ vì con người, không phải vì công nghệ".
    - **Văn hóa Việt Nam:** Tặng quà phin cà phê truyền thống, trao đổi về văn hóa cà phê sữa đá và tinh thần nhiệt huyết của builders Việt Nam.
  - Tích hợp trọn vẹn 3 hình ảnh minh chứng thực tế lưu tại `static/images/4-EventParticipated/4.2-Event2/`:
    - `event2-proof-1.jpg`: Dr. Werner Vogels trên sân khấu Fireside Chat đối thoại cùng Solutions Architect Manager & Sr Prototyping Architect AWS Vietnam.
    - `event2-proof-2.png`: Ảnh lưu niệm tập thể toàn thể cộng đồng AWS Builders, AWS Heroes và intern cùng Dr. Werner Vogels tại văn phòng Bitexco lầu 26.
    - `event2-proof-3.jpg`: Nhóm thực tập sinh First Cloud Journey check-in trước khẩu hiệu Amazon "Invent and Simplify".
  - Khởi tạo đầy đủ bài viết song ngữ:
    - `content/4-EventParticipated/4.2-Event2/_index.vi.md` (100% Tiếng Việt, 149 dòng chi tiết, cấu trúc 12 phần + 3 ảnh minh chứng).
    - `content/4-EventParticipated/4.2-Event2/_index.md` (100% Tiếng Anh học thuật chuẩn AWS).
  - Cập nhật trang mục lục: `content/4-EventParticipated/_index.vi.md` và `_index.md`.
  - Kiểm thử giao diện trên trình duyệt và xác thực Hugo build thành công (92 trang EN, 91 trang VI, 447 static files, 0 errors).

### [2026-10-21] Hoàn thiện Blog 1: Giới thiệu Amazon ECS Gateway (Tính năng mới nhất 20/10/2026)

- **Dự án & Phạm vi:** Cập nhật mục Các bài blogs đã đăng (`content/3-BlogsPosted/3.1-Blog1/`).
- **Nguồn bài viết gốc:** [Introducing Amazon ECS Gateway: A fully-managed ingress solution for ECS services](https://aws.amazon.com/blogs/aws/introducing-amazon-ecs-gateway-a-fully-managed-ingress-solution-for-ecs-services/) trên AWS News Blog (Tác giả: Channy Yun, phát hành ngày 20/10/2026).
- **Tiến độ đã hoàn thành:**
  - Tải và đồng bộ banner chính thức: `static/images/3-BlogsPosted/3.1-Blog1/ecs-gateway-hero.png`.
  - Phân tích kiến trúc chuyên sâu:
    - **Nút thắt cổ chai truyền thống:** Quản lý Ingress phân mảnh (mỗi service 1 ALB, ACM cert, Route 53, WAF, Security Group).
    - **Mô hình phân tách trách nhiệm:** Platform Team cấu hình Gateway tập trung (Subnets, Security baseline, WAF Web ACL); Application Team tự phục vụ qua tham số `--gateway-connectors` mà không cần chuyên môn mạng.
    - **Tối ưu hóa FinOps:** Cho phép tối đa 25 microservices dùng chung 1 ALB qua host-based routing; tự động co giãn ALB và dọn dẹp khi service bị xóa, tiết kiệm đến 90% chi phí Load Balancer.
    - **Sơ đồ kiến trúc Mermaid & Bảng so sánh:** Phân tích chi tiết giữa cách làm truyền thống và ECS Gateway mới.
    - **Các lưu ý kỹ thuật:** Chế độ `awsvpc`, phân bổ Availability Zones, quản lý hạn mức `maxAlbCount` (default 10), và giám sát CloudWatch Metrics (`TargetGroup` & `LoadBalancer` dimensions).
  - Soạn thảo song ngữ hoàn chỉnh:
    - `content/3-BlogsPosted/3.1-Blog1/_index.vi.md` (100% Tiếng Việt).
    - `content/3-BlogsPosted/3.1-Blog1/_index.md` (100% Tiếng Anh học thuật).
  - Cập nhật trang mục lục `content/3-BlogsPosted/_index.vi.md` và `_index.md`: làm nổi bật Blog 1, đồng thời giữ nguyên cấu trúc thư mục Blog 2 và Blog 3 dự phòng theo yêu cầu.
  - Kiểm thử biên dịch Hugo thành công: 92 trang EN, 91 trang VI, 448 static files, 0 errors.

### [2026-10-27] Hoàn thiện Event 3: Buổi Meetup "First Cloud AI Journey" (24/10/2026)

- **Dự án & Phạm vi:** Cập nhật mục Các sự kiện đã tham gia (`content/4-EventParticipated/4.3-Event3/`).
- **Thông tin sự kiện:**
  - **Tên:** First Cloud AI Journey Meetup: Xu Hướng & Thực Tiễn Triển Khai Cloud & AI Agent.
  - **Thời gian:** 09:00 - 12:00, Sáng Thứ Bảy, 24/10/2026.
  - **Địa điểm:** Văn phòng AWS Việt Nam, Lầu 26, Tòa nhà Bitexco Financial Tower, số 02 Hải Triều, P. Bến Nghé, Quận 1, TP. Hồ Chí Minh.
  - **Đơn vị tổ chức:** First Cloud Journey (FCJ) phối hợp cùng AWS Community Builders và AWS Student Builder Groups.
  - **Thành phần tham dự:** Hơn 100 kỹ sư, Tech Leads, Cloud Architects, sinh viên và thực tập sinh.
- **Tiến độ đã hoàn thành:**
  - Thu thập, đồng bộ và chuẩn hóa toàn bộ 17 hình ảnh thực tế từ các thư mục `minh chung`, `person` và `to chuc` sang `static/images/4-EventParticipated/4.3-Event3/`:
    - `event3-minh-chung.jpg`: Ảnh selfie check-in thẻ đeo sự kiện tại văn phòng AWS lầu 26 Bitexco.
    - `event3-to-chuc-2.jpg` & `event3-to-chuc-7.jpg`: Ảnh lưu niệm tập thể toàn thể cộng đồng và khoảnh khắc vẫy tay chào bế mạc.
    - Trọn bộ ảnh các phiên diễn giả và slides kỹ thuật: `event3-to-chuc-1.jpg` đến `event3-to-chuc-6.jpg`, `event3-person-1.jpg` đến `event3-person-8.jpg`.
  - Phân tích và biên soạn chi tiết toàn diện 5 sessions chuyên sâu:
    1. **Session 1 (Anh Kiệt Trần - Revve AI):** Voice AI Contact Center tiếng Việt. 3 kiến trúc (Cascade, S2S, Full duplex S2S). 4 bài học: Turn detection tiếng Việt (79% vs 94%), chuẩn hóa text số ("500K" -> "năm trăm nghìn"), kiểm soát an toàn từng câu với Small Judge Model (lỗi từ 5/6 về 0/6), ngân sách độ trễ (~1.8s, LLM median 0.24s). Live demo phỏng vấn tuyển dụng Cloud Engineer bằng tiếng Việt mượt mà.
    2. **Session 2 (Anh Long Huỳnh - Styl Solution):** AWS Resource Access Manager (RAM). Giải quyết bài toán Multi-Account Challenge (chống phân mảnh và trùng lặp x3 chi phí Transit GW, Subnets, DNS rules, Licenses). Nguyên lý "Create once, share everywhere". Kết hợp bảo mật kép giữa IAM Resource Policy và Organization SCPs.
    3. **Session 3 (Anh Nguyễn Tuấn Thịnh - Styl Solution):** AWS Pentest with Security Agent. Shift-Left Security. Tự động hóa Static Code Analysis quét mã nguồn IaC Terraform trên GitLab/GitHub PR. Frontier Security Agent ứng dụng Amazon Bedrock suy luận tự chủ (Autonomous Reasoning) để pentest tự động trên SIT/UAT trước khi deploy production.
    4. **Session 4 (Anh Xuân An - HCMUTE):** Amazon Bedrock AgentCore. Ecosystem Diagram (App -> Agent Runtime -> Models). Chạy MicroVM độc lập trên EC2 Spot theo từng session ("Micro lives to serve a single session only") giúp tiết kiệm 70-90% chi phí máy chủ. Hệ thống bộ nhớ 2 tầng: Short-term đồng bộ và Long-term bất đồng bộ qua Vector Database.
    5. **Session 5 (Anh Kiều Nguyễn Đăng Khoa - Tech Lead ACB & Anh Danh Hoàng Hiệu Nghi - AWS Community Builder):** Kiro Crew - All-In-One AI Companion 24/7. Tự động sinh Artifacts (cào việc làm và vẽ biểu đồ trực quan trong chat). Quản trị Context Window qua cơ chế Auto Compact (70-90%) và tính năng Break down context bóc tách token. Quản lý Developer Storage và thiết lập Guardrails an toàn chống phá hoại hạ tầng hoặc rò rỉ secrets.
  - Soạn thảo song ngữ chuẩn mực:
    - [4.3-Event3/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/4-EventParticipated/4.3-Event3/_index.vi.md) (100% Tiếng Việt, tối ưu bộ 8 ảnh chất lượng cao chuyên nghiệp từ ban tổ chức + ảnh check-in cá nhân).
    - [4.3-Event3/\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/4-EventParticipated/4.3-Event3/_index.md) (100% Tiếng Anh học thuật/AWS Technical Writing).
  - Cập nhật trang mục lục `content/4-EventParticipated/_index.vi.md` và `_index.md`: Nâng số lượng sự kiện tham dự lên 3 events và bổ sung thông tin tóm tắt Event 3.
  - Cập nhật tiêu đề hiển thị trên menu sidebar (Frontmatter title): Đồng bộ định dạng với Event 2 thành `Event 3: First Cloud AI Journey Meetup (Cloud & AI Agent)` giúp thanh mục lục hiển thị đầy đủ tên sự kiện rõ ràng và chuyên nghiệp.
  - Kiểm thử biên dịch Hugo thành công: 94 trang EN, 93 trang VI, 465 static files, 0 errors.

### [2026-10-28] Cập nhật Blog 1: Enterprise Agentic Retrieval với Amazon Bedrock & AWS CDK (26/10/2026)

- **Dự án & Phạm vi:** Cập nhật mục Các bài blogs đã đăng (`content/3-BlogsPosted/3.1-Blog1/`).
- **Nguồn bài viết gốc:** [Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK](https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/) trên AWS Machine Learning Blog (Tác giả: Prabhakar Chandrasekaran & Siddhant Sahu, phát hành ngày 26/10/2026).
- **Lý do lựa chọn:** Người dùng chọn đề tài này thay thế cho ECS Gateway vì đây là đề tài cực kỳ gần gũi, thực tế và phù hợp làm đồ án cấp độ sinh viên (Đồ án tốt nghiệp / Capstone GenAI RAG).
- **Tiến độ đã hoàn thành:**
  - Tải và đồng bộ 3 hình ảnh minh họa chất lượng cao từ AWS Blog:
    - `static/images/3-BlogsPosted/3.1-Blog1/bedrock-agentic-rag-hero.png` (Hình kiến trúc luồng tổng quan).
    - `static/images/3-BlogsPosted/3.1-Blog1/bedrock-agentic-flow.png` (Sơ đồ tương tác Gateway & MCP tools).
    - `static/images/3-BlogsPosted/3.1-Blog1/bedrock-cloudwatch-dashboard.jpg` (Ảnh bảng điều khiển giám sát CloudWatch).
  - Phân tích kiến trúc chuyên sâu:
    - **Giới hạn của Naive/Classic RAG:** Cơ chế single retrieval - single generation thất bại với câu hỏi đa nguồn, không thể định tuyến ngữ nghĩa và thiếu khả năng tự hiệu chỉnh/second look.
    - **Kiến trúc Agentic Retrieval:** Đưa tác tử suy luận (Reasoning Agent) vào vòng lặp (Agentic Loop), tự phân tích câu hỏi, gọi công cụ MCP qua Bedrock AgentCore Gateway, truy xuất đa bước (multi-turn planning), và reranking bằng API `AgenticRetrieveStream`.
    - **Tính năng đột phá Managed Knowledge Base (Type: MANAGED):** AWS tự động quản lý toàn bộ ingestion, chunking, indexing và vector search. Loại bỏ hoàn toàn sự cần thiết của cụm OpenSearch Serverless (AOSS), triệt tiêu chi phí OCU đắt đỏ, chuyển sang mô hình serverless pay-as-you-go tối ưu cho sinh viên.
    - **Chuẩn Model Context Protocol (MCP):** Đóng gói mỗi Knowledge Base thành một công cụ độc lập, bảo mật phân quyền qua IAM.
    - **Observability với Amazon CloudWatch:** 7 tầng telemetry (Latency, Reasoning Steps, Tool Calls, Tokens, Relevance, Errors, Continuous Evaluation).
    - **Tự động hóa hoàn chỉnh bằng AWS CDK (Python):** 1 lệnh `cdk deploy --all` triển khai toàn bộ hệ thống.
  - Soạn thảo song ngữ 100%:
    - `content/3-BlogsPosted/3.1-Blog1/_index.vi.md` (100% Tiếng Việt).
    - `content/3-BlogsPosted/3.1-Blog1/_index.md` (100% Tiếng Anh học thuật/AWS Technical Writing).
  - Cung cấp sẵn khung chờ link bài đăng Facebook và hình ảnh chụp màn hình sau khi duyệt trên nhóm `AWS Study Group - First Cloud Journey`.
  - Cập nhật trang mục lục `content/3-BlogsPosted/_index.vi.md` và `_index.md` đồng bộ tóm tắt Blog 1.
  - Kiểm thử biên dịch Hugo thành công: 94 trang EN, 93 trang VI, 469 static files, 0 errors.

### [2026-10-28] Hoàn thiện Blog 1: AWS Continuum for Code Vulnerabilities (GA 22/10/2026) & Mô hình Draw.io An Ninh Tự Chủ

- **Dự án & Phạm vi:** Cập nhật mục Các bài blogs đã đăng (`content/3-BlogsPosted/3.1-Blog1/`).
- **Nguồn bài viết gốc:** [AWS Continuum for code vulnerabilities is now generally available](https://aws.amazon.com/blogs/aws/aws-continuum-for-code-vulnerabilities-is-now-generally-available/) trên AWS News Blog (Tác giả: Esra Kayabali - Principal Solutions Architect tại AWS, phát hành ngày 22/10/2026).
- **Lý do chuyển đổi:** Người dùng mong muốn một đề tài hoàn toàn mới mẻ, mang tầm vóc ngành công nghiệp điện toán đám mây và an ninh tự chủ (Frontier AI & Autonomous DevSecOps), thay vì chỉ dừng lại ở các bài viết nâng cấp tính năng thông thường hay đóng khung trong đề tài sinh viên.
- **Tiến độ đã hoàn thành:**
  - **Tải và tích hợp 4 hình ảnh Console chính thức từ AWS:**
    - `static/images/3-BlogsPosted/3.1-Blog1/continuum-overview.png` (Giao diện tổng quan dịch vụ AWS Continuum).
    - `static/images/3-BlogsPosted/3.1-Blog1/continuum-issues.png` (Danh sách các vấn đề an ninh và độ ưu tiên rủi ro).
    - `static/images/3-BlogsPosted/3.1-Blog1/continuum-risk-assessment.png` (Phân tích ma trận rủi ro và bằng chứng khai thác).
    - `static/images/3-BlogsPosted/3.1-Blog1/continuum-pr-github.png` (Pull Request tự động tạo trên GitHub kèm code fix và giải thích chi tiết).
  - **Thiết kế & Thẩm định Sơ đồ Kiến trúc Draw.io (10/10 Perfect Score):**
    - Đã hướng dẫn chi tiết quy chuẩn vẽ sơ đồ trên Draw.io với các AWS Shape Icons chính thức.
    - Phân chia bố cục làm 2 khối chính (AWS/group):
      - Khối 1: `Developer Environment (GitHub / GitLab)` chứa **Dev / Security Reviewer** (icon User), **Source Code Repository** (icon GitHub/Code), và **PR: Continuum fix** (icon Git/Document).
      - Khối 2: `AWS Cloud / Security Context` chứa **AWS Continuum** (icon Security Agent / Bedrock), **AWS Config & VPC Context** (icon Config/VPC), và **Isolated Sandbox (PoC)** (icon EC2/Sandbox).
    - Thẩm định 6 bước luồng dữ liệu chuẩn xác:
      1. `1. Scan Code`: Từ Repo sang AWS Continuum.
      2. `2. Read Cloud Context`: Mũi tên từ AWS Config sang AWS Continuum (Đọc ngữ cảnh cấu hình thực tế).
      3. `3. Trigger PoC Exploit`: Từ Continuum kích hoạt kiểm thử trong Isolated Sandbox.
      4. `4. Validated Evidence`: Sandbox trả về bằng chứng khai thác thực tế cho Continuum.
      5. `5. Auto Open PR`: Continuum tự động mở Pull Request lên Developer Environment.
      6. `6. Review & Merge`: Từ Dev / Security Reviewer phê duyệt và hợp nhất PR vào Repo (Human-in-the-loop).
    - Đường dẫn lưu file ảnh xuất từ Draw.io: `static/images/3-BlogsPosted/3.1-Blog1/continuum-architecture.png`.
  - **Soạn thảo Song ngữ Kỹ thuật Chuyên sâu:**
    - [3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) (100% Tiếng Việt, 4 phần phân tích chuyên sâu: Nút thắt DevSecOps truyền thống, Cơ chế đột phá Context Graph & Sandbox PoC, Human-in-the-loop qua GitHub PR, và Tầm nhìn tương lai).
    - [3.1-Blog1/\_index.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.md) (100% Tiếng Anh học thuật/AWS Technical Writing).
  - **Trang Mục lục [3-BlogsPosted/](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/):**
    - Cập nhật cả 2 bản `_index.vi.md` và `_index.md` giới thiệu nổi bật Blog 1 về AWS Continuum.
  - **Kịch bản Bài đăng Facebook Hoàn chỉnh:**
    - Soạn sẵn toàn văn bài post chia sẻ kỹ thuật chuẩn phong cách DevSecOps / Cloud Architect cho group [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj).
    - Đầy đủ hashtag: `#FirstCloudJourney #FCJ #AWSStudyGroup #AWSUserGroupVietnam #AWS #AWSContinuum #DevSecOps #CloudSecurity #GenerativeAI`.
    - Thiết kế sẵn khung chờ link bài viết và ảnh chụp màn hình minh chứng sau khi duyệt bài.
  - **Kiểm thử Hugo Build:**
    - `hugo -D`: 94 trang EN, 93 trang VI, 473 static files, **0 errors**, thời gian build ~0.95s.

### [2026-10-29] Tinh chỉnh Sơ đồ Draw.io & Đăng bài Blog 1 lên Cộng đồng Facebook (Chờ Admin Duyệt)

- **Dự án & Phạm vi:** Hoàn thiện khâu chia sẻ cộng đồng cho [Blog 1: AWS Continuum for Code Vulnerabilities](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/).
- **Tiến độ đã hoàn thành:**
  - **Phân tích Tỉ lệ vàng (Golden Ratio $\varphi \approx 1.618$):**
    - Làm rõ khái niệm toán học và ứng dụng thực tiễn trong thiết kế sơ đồ kiến trúc AWS Draw.io.
    - Khảo sát kích thước sơ đồ thực tế của Blog 1 (`1024 x 530 px`, tỉ lệ ~1.932 Widescreen), xác nhận đạt chuẩn thị giác lý tưởng trên slide 16:9 và trang web Hugo.
  - **Tinh chỉnh hoàn thiện Sơ đồ Draw.io:**
    - Hướng dẫn căn chỉnh và tách nhãn chữ: Khắc phục lỗi co cụm chữ tại `AWS Config & VPC Topology` (chia 3 tầng cân xứng) và `PR:Continuum fix` (gọn gàng, thẳng thớm trong container Developer Environment).
    - Sơ đồ hoàn chỉnh đạt điểm tối đa 10/10 với 6 bước rõ ràng, màu sắc phân nhóm chính xác (AWS Cloud, AWS Account, Managed Continuum, Dev Environment).
  - **Biên soạn & Tối ưu Bài viết Facebook:**
    - Tinh chỉnh nội dung theo phong cách trực diện, dễ hiểu, tránh thuật ngữ hàn lâm trừu tượng, nêu bật 3 nhiệm vụ cốt lõi: Quét code Git ➔ Đối chiếu hạ tầng thực tế AWS (VPC, IAM, Security Groups) ➔ Tự viết code sửa và mở sẵn PR trên Git cho Dev bấm Merge.
    - Tích hợp chuẩn hóa thuật ngữ chuyên ngành: _cấu hình mạng VPC, chính sách phân quyền IAM, và bề mặt phơi nhiễm Internet (Internet Exposure / Security Groups)_.
    - Đính kèm link bài viết gốc từ AWS News Blog và trọn bộ hashtag chiến dịch.
  - **Gửi bài đăng lên Cộng đồng:**
    - Người dùng đã nạp nội dung bài viết và đính kèm sơ đồ kiến trúc lên nhóm [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj).
    - Giải thích rõ cơ chế kiểm tra chính tả của trình duyệt (gạch đỏ không ảnh hưởng khi đăng) và cơ chế nhận diện Hashtag màu xanh của Facebook.
- **Trạng thái hiện tại:**
  - ⏳ **Đang chờ duyệt bài:** Bài viết đang trong hàng đợi kiểm duyệt (Pending Approval) của đội ngũ Admin nhóm Facebook AWS Study Group.
- **Kế hoạch tiếp theo ngay khi bài được duyệt:**
  1. Lấy URL bài viết chính thức dán vào file [3.1-Blog1/\_index.vi.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/content/3-BlogsPosted/3.1-Blog1/_index.vi.md) và `_index.md`.
  2. Chụp ảnh màn hình bài đăng đã được duyệt, lưu vào `static/images/3-BlogsPosted/3.1-Blog1/facebook-post-proof.png`.
  3. Chuyển sang triển khai nội dung Worklog Tuần 6 / Tuần 7.

### [2026-10-31] Đồng bộ Trạng thái Thực tế: Tuần 5 Thứ 6 Chưa có gì & Tuần 6 Không có gì
- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Người dùng xác nhận rõ ràng: "là tuần 5 thứ 6 chưa có gì và tuần 6 ko có gì".
  - Thứ 6 Tuần 5 hiện tại người dùng chưa làm bài nào cả. Tuần 6 người dùng cũng chưa học đến nên chưa có nội dung triển khai nào.
- **Tiến độ & Xử lý thực tế:**
  - **1. Tuần 5 (`content/1-Worklog/1.5-Week5/_index.vi.md` & `_index.md`):**
    - Đã xóa sạch thư mục bài viết 1.5.5 và ảnh tạm.
    - Dòng Thứ 6 trong bảng công việc để `*(Chưa thực hiện)*` / `*(Not yet scheduled)*`.
    - Phần kết quả tuần 5 chỉ có Thứ 2, Thứ 3, Thứ 4, Thứ 5. Hoàn toàn không có mục Thứ 6.
  - **2. Tuần 6 (`content/1-Worklog/1.6-Week6/_index.vi.md` & `_index.md`):**
    - Đã đưa về đúng template nguyên mẫu ban đầu (như các tuần chưa làm 7, 8, 9...), không tự ý viết trước các bài lab hay kết quả thực hành.
  - **3. Kiểm thử biên dịch Hugo:**
    - `hugo -D`: **94 trang EN, 93 trang VI, 509 static files, 0 errors, 0 warnings**.

### [2026-10-31] Hoàn thiện Worklog Thứ 6 Tuần 5: Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack

- **Dự án & Phạm vi:** Hoàn thiện bài thực hành bù Thứ 6 Tuần 5 (`content/1-Worklog/1.5-Week5/1.5.5-aws-lambda/`).
- **Nguồn tài liệu:** [Optimizing the system on AWS - Workshop 000022](https://000022.awsfcaj.com/).
- **Khu vực AWS & Tài nguyên thật:**
  - **AWS Account:** `887086382708`, IAM User: `trangiabao`, Region: `us-east-1` (N. Virginia).
  - **Mạng VPC:** `lambda-lab` (`10.0.0.0/16`), Public Subnet: `10.0.128.0/20` (`us-east-1a`).
  - **Nhóm bảo mật:** `lambda-lab` (Inbound Port 22 SSH & Port 80 HTTP).
  - **Máy ảo EC2:** `lambda-lab-instance` / `i-003cb6dbd0f4e5b31` (`t3.micro`, Amazon Linux 2023, Tag `environment_auto = true`).
  - **IAM Role:** `dc-common-lambda-role` (`AmazonEC2FullAccess`, `CloudWatchFullAccessV2`).
  - **Hàm Lambda:** `dc-common-lambda-auto-stop` và `dc-common-lambda-auto-start` (Runtime Python 3.14, Memory 128 MB, Env `environment_auto = true`).
  - **Lịch trình EventBridge:** Rate 9 hours (Stop) và Rate 8 hours (Start).
  - **ChatOps Slack:** Workspace `aws-lambda-labs`, Kênh `#notification`, App `Lambda-Notifier`, Webhook URL hoạt động thật.
- **Tiến độ đã hoàn thành:**
  - Chuẩn hóa và đồng bộ trọn bộ **18 ảnh chụp thực hành thực tế** của người dùng tại `static/images/1-Worklog/1.5-Week5/1.5.5-aws-lambda/` (`2.1.png` đến `6.3.png`).
  - Soạn thảo bài viết song ngữ chi tiết theo phong cách **Step-by-Step thực chiến**:
    - [1.5.5-aws-lambda.vi.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.5-aws-lambda/1.5.5-aws-lambda.vi.md) (100% Tiếng Việt, 9 bước thực hành, bảng tài nguyên, code Python Boto3 tối ưu hóa, 10 sự cố kỹ thuật thực tế & dọn dẹp tài nguyên).
    - [1.5.5-aws-lambda.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/1.5.5-aws-lambda/1.5.5-aws-lambda.md) (100% Tiếng Anh chuẩn mực).
  - **Đúc kết 10 sự cố thực tế & giải pháp:**
    1. Không thấy Security Group khi tạo EC2 (do chọn nhầm Default VPC thay vì VPC `lambda-lab`).
    2. Quên bật gán IP công khai (Auto-assign public IPv4) trong Subnet Public.
    3. Ngoại lệ `IncorrectInstanceState` khi chạy Lambda: Máy cũ `i-099b2108fbf1a9175` bị `Terminated` nhưng còn dính Tag `environment_auto=true` khiến bộ lọc quét nhầm. Đã khắc phục bằng cách tạo máy mới `i-003cb6dbd0f4e5b31` và bổ sung bộ lọc trạng thái máy `instance-state-name: ['running']` (cho Stop) và `['stopped']` (cho Start).
    4. Tràn bộ nhớ Lambda / Timeout khi xử lý nhiều tài nguyên.
    5. Thiếu biến môi trường `environment_auto` (mã lỗi 400).
    6. Lộ lọt Slack Webhook URL lên kho mã nguồn công khai (khuyến nghị dùng AWS Secrets Manager).
    7. Giới hạn tần suất gửi tin nhắn Slack API (HTTP 429 Rate Limiting).
    8. Lệch múi giờ UTC và giờ địa phương Việt Nam (UTC+7) trên EventBridge Scheduler.
    9. Rủi ro chi phí khi quên xóa tài nguyên lab (máy ảo EC2, IP công cộng IPv4 phụ phí $0.005/giờ, NAT Gateway).
    10. Lỗi phân quyền IAM Role khi gọi API Start/Stop Instances (`AccessDenied`).
  - Cập nhật trang tổng quan Tuần 5 ([\_index.vi.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.vi.md) và [\_index.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/content/1-Worklog/1.5-Week5/_index.md)).
  - Giữ nguyên trạng thái Tuần 6 trống đúng yêu cầu.
  - Kiểm thử Hugo build: **95 trang EN, 94 trang VI, 545 static files, 0 errors, 0 warnings**.

### [2026-11-01] Rà soát Toàn diện & Khắc phục Lỗi Kỹ thuật Dự án (System Audit & Fixes)

- **Bối cảnh & Chỉ đạo từ Người dùng:** Người dùng yêu cầu đánh giá toàn diện những điểm cần cải thiện của bài workshop/báo cáo, sau đó chỉ đạo sửa các lỗi kỹ thuật và cấu hình (bỏ qua ảnh đại diện cá nhân).
- **Tiến độ & Các hạng mục đã khắc phục triệt để:**
  1. **Khắc phục triệt để 38 ảnh bị lỗi 404 ở bài 1.5.1 AWS CLI:**
     - Đổi tên thư mục `static/images/1-Worklog/1.5-Week5/1.5.1-AWS CLI` thành `1.5.1-aws-cli` (chuẩn hóa chữ thường không dấu, dùng dấu gạch ngang).
     - Rà soát tự động toàn bộ 100% hình ảnh trong repo: **0 missing images**.
  2. **Dọn dẹp thư mục rác (Repo Cleanup):**
     - Đã xóa 2 thư mục thừa trong `static/images/1-Worklog/1.5-Week5/`: `1.5.5-static-website-hosting-s3/` (thư mục nháp cũ) và `1.5.6-AWS Lambda/` (ảnh thô trùng lặp với `1.5.5-aws-lambda`). Giảm dung lượng tĩnh từ 545 files xuống 480 files sạch đẹp.
  3. **Đồng bộ thông tin sinh viên Trang chủ Tiếng Việt (`content/_index.vi.md`):**
     - Đồng bộ chính xác thông tin tác giả thực tế (**Trần Gia Bảo**, SĐT: `0936674461`, Email: `trangiabao4461@gmail.com`, **FPT University**, kỳ thực tập `14/09/2026 - 14/12/2026`), loại bỏ hoàn toàn thông tin mẫu "Nguyễn Văn A".
     - Xóa hộp cảnh báo Warning mẫu trên cả 2 trang chủ EN và VI.
  4. **Khắc phục lỗi liên kết nội bộ 404 trong Mục 5 (Workshop S3 VPC Endpoint) & Mục 2 (Proposal):**
     - Sửa link `content/5-Workshop/5.3-S3-vpc/`: Chuyển `3.1-create-gwe/` và `3.2-test-gwe/` thành `5.3.1-create-gwe/` và `5.3.2-test-gwe/`.
     - Bổ sung menu điều hướng cho 4 subpages trong `content/5-Workshop/5.4-S3-onprem/`.
     - Xóa link trỏ vào file PDF không tồn tại (`budget_estimation.pdf`) trong `content/2-Proposal/`.
     - Rà soát tự động 100% liên kết nội bộ trong repo: **0 broken links**.
  5. **Cập nhật cấu hình tác giả Hugo (`config.toml`):**
     - Thay đổi `author = "thienlh@thienlu.com"` thành `author = "trangiabao4461@gmail.com"`.
  6. **Kiểm thử biên dịch Hugo:**
     - `hugo -D`: **95 trang EN, 94 trang VI, 480 static files, 0 errors, 0 warnings** (thời gian build siêu tốc ~2.0s).

### [2026-11-16] Chuẩn hóa Quy tắc Lịch học 1 bài/ngày & Thứ 6 Review/Project (Bắt đầu từ Tuần 1)

- **Bối cảnh & Chỉ đạo từ Người dùng:**
  - Người dùng thiết lập quy tắc tiến độ mới: **Từ Thứ 2 đến Thứ 5 mỗi ngày học đúng 1 nội dung / bài lab chất lượng**.
  - **Thứ 6 cố định làm ngày Review & Project:** Dành trọn vẹn để ôn tập, tổng kết kiến thức trong tuần và nghiên cứu, phát triển đồ án thực tập (Proposal / Project).
  - Các bài học vốn ở Thứ 6 theo giáo trình cũ sẽ được đẩy cuốn chiếu sang Thứ 2 tuần kế tiếp.
  - Người dùng yêu cầu chuẩn hóa ngay từ **Tuần 1**.
- **Tiến độ & Xử lý thực tế Tuần 1 (`content/1-Worklog/1.1-Week1/`):**
  - **Thứ 2 (14/09/2026):** Quản trị chi phí & Bảo mật định danh: AWS Budgets (000007) & AWS IAM (000002).
  - **Thứ 3 (15/09/2026):** Hạ tầng mạng cốt lõi: Amazon VPC (000003).
  - **Thứ 4 (16/09/2026):** Điện toán đám mây: Amazon EC2 (000004).
  - **Thứ 5 (17/09/2026):** Lưu trữ đối tượng & Web tĩnh: Amazon S3 (000057).
  - **Thứ 6 (18/09/2026):** Tổng kết, ôn tập review kiến thức Tuần 1 & Dành thời gian nghiên cứu, lập dàn ý Đề xuất dự án (Project Proposal).
  - Đã cập nhật song ngữ hoàn chỉnh cả `_index.vi.md` và `_index.md`.
  - Kiểm thử `hugo -D`: **95 trang EN, 94 trang VI, 0 errors, 0 warnings**.

- **Tiến độ & Xử lý thực tế Tuần 3 (`content/1-Worklog/1.3-Week3/`):**
  - **Thứ 2 (28/09/2026):** Hiện đại hóa ứng dụng với Serverless (000078, 000081, 000080).
  - **Thứ 3 (29/09/2026):** Dịch vụ Container: ECS, ECR, EKS (000067, 000126, 000071).
  - **Thứ 4 (30/09/2026):** Phân tích dữ liệu: Data Pipeline, EMR, Athena (000035, 000073, 000106).
  - **Thứ 5 (01/10/2026):** Thực hành chuyên sâu: Get Started with Amazon RDS (1.3.1).
  - **Thứ 6 (02/10/2026):** Tổng kết Tuần 3, Hoàn thiện Worklog 1.3.1 & Nghiên cứu Đề xuất dự án (Project Proposal).
  - Cập nhật song ngữ hoàn chỉnh cả `_index.vi.md` và `_index.md`.

- **Tiến độ & Tái cấu trúc Tuần 4 (`content/1-Worklog/1.4-Week4/`):**
  - **1.4.1 (Thứ 2 - 05/10/2026):** Triển khai Amazon Lightsail (13 ảnh).
  - **1.4.2 (Thứ 3 - 06/10/2026):** Triển khai Amazon Lightsail Container (11 ảnh).
  - **1.4.3 (Thứ 4 - 07/10/2026):** Tự động co giãn với EC2 Auto Scaling (44 ảnh).
  - **1.4.4 (Thứ 5 - 08/10/2026):** Giám sát với Amazon CloudWatch (33 ảnh).
  - **Thứ 6 (09/10/2026):** Tổng kết Tuần 4, Viết Worklog (1.4.1 - 1.4.4) & Làm Project (Proposal).
  - Bài thực hành Hybrid DNS (1.4.5 cũ) được chuyển cuốn chiếu sang Thứ 2 Tuần 5 thành **1.5.1**.
  - Cập nhật song ngữ hoàn chỉnh cả `_index.vi.md` và `_index.md`.

- **Tiến độ & Tái cấu trúc Tuần 5 (`content/1-Worklog/1.5-Week5/`):**
  - **1.5.1 (Thứ 2 - 12/10/2026):** Thiết lập Hybrid DNS với Route 53 Resolver (11 ảnh, chuyển từ 1.4.5 cũ).
  - **1.5.2 (Thứ 3 - 13/10/2026):** Thao tác dòng lệnh với AWS CLI (38 ảnh, đổi số từ 1.5.1 cũ).
  - **1.5.3 (Thứ 4 - 14/10/2026):** Làm việc với Amazon DynamoDB (32 ảnh, đổi số từ 1.5.2 cũ).
  - **1.5.4 (Thứ 5 - 15/10/2026):** Triển khai Amazon ElastiCache - Redis (27 ảnh, đổi số từ 1.5.3 cũ).
  - **Thứ 6 (16/10/2026):** Tổng kết Tuần 5, Viết Worklog (1.5.1 - 1.5.4) & Làm Project (Proposal).
  - Toàn bộ thư mục ảnh trong `static/images/1-Worklog/1.5-Week5/` được đồng bộ sang tiền tố số mới (`1.5.1-hybrid-dns`, `1.5.2-aws-cli`, `1.5.3-amazon-dynamodb`, `1.5.4-amazon-elasticache`).
  - Cập nhật song ngữ hoàn chỉnh cả `_index.vi.md` và `_index.md`.

- **Tiến độ & Tái cấu trúc Tuần 6 (`content/1-Worklog/1.6-Week6/`):**
  - **1.6.1 (Thứ 2 - 19/10/2026):** Quản lý và Nâng hạn mức tài nguyên với AWS Service Quotas (chuyển từ 1.5.4 cũ).
  - **1.6.2 (Thứ 3 - 20/10/2026):** Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (18 ảnh, chuyển từ 1.5.5 cũ).
  - **1.6.3 (Thứ 4 - 21/10/2026):** Quản trị Thẻ định danh và Nhóm tài nguyên AWS - Tags & Resource Groups (14 ảnh chuyển từ Week 14 sang `1.6.3-tags-and-resource-groups`).
  - **1.6.4 (Thứ 5 - 22/10/2026):** Giám sát hệ thống với Grafana & Amazon CloudWatch (Workshop 000029 - Getting started with Grafana basic, 18 ảnh trong `1.6.4-grafana-basic`).
  - **Thứ 6 (23/10/2026):** Tổng kết Tuần 6, Viết Worklog (1.6.1 - 1.6.4) & Làm Project (Proposal).
  - Đã chuyển giao và chuẩn hóa đầy đủ thư mục ảnh trong `static/images/1-Worklog/1.6-Week6/`.
  - Cập nhật song ngữ hoàn chỉnh cả `_index.vi.md`, `_index.md`, `1.6.3-tags-and-resource-groups.*`, `1.6.4-grafana-basic.*`.

- **Tiến độ & Tái cấu trúc Tuần 7 (`content/1-Worklog/1.7-Week7/`):**
  - **1.7.1 (Thứ 2 - 26/10/2026):** Giám sát chuyên sâu với Amazon CloudWatch - CloudWatch Advanced Workshop (24 ảnh trong `static/images/1-Worklog/1.7-Week7/1.7.1-cloudwatch-advanced/`, gồm CloudFormation stack, Metric Math, Search Expressions, Dynamic Labels, SSM Session Manager logger script, CloudWatch Logs Insights, Metric Filter `PythonAppErrors`, SNS Email alert, và Dashboard `ssmDashboard`).
  - **Thứ 3 (27/10/2026):** Giám sát tải & Tự động phản ứng sự cố với CloudWatch & SNS.
  - **Thứ 4 (28/10/2026):** Tham gia Sự kiện Công nghệ AWS Community & Chia sẻ Kiến trúc (Event 3 - 24/10 Review).
  - **Thứ 5 (29/10/2026):** Nghiên cứu Chuyên sâu & Biên soạn Bài viết Kỹ thuật Blog 1 (Cloud Migration Journey).
  - **Thứ 6 (30/10/2026):** Tổng kết Tuần 7, Viết Worklog & Làm Project (Proposal).
  - Cập nhật song ngữ hoàn chỉnh cả `_index.vi.md`, `_index.md`, `1.7.1-cloudwatch-advanced.*`.

- **Kiểm tra & Thẩm định Toàn diện (Verification & Audit):**
  - Chạy `scratch/verify_links.ps1`: **0 missing images** (Tất cả 100% hình ảnh trong mọi bài viết đều tồn tại chính xác trên disk).
  - Chạy `scratch/verify_internal_links.ps1`: **0 broken internal links** (Tất cả liên kết bài viết, trang mục lục và proposal đều hoạt động chính xác).
  - Chạy `hugo -D`: **102 trang EN, 101 trang VI, 536 static files, 0 errors, 0 warnings**.







