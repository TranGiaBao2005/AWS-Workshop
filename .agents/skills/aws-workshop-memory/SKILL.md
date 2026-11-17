---
name: aws-workshop-memory
description: >-
  Lưu trữ và đọc lại toàn bộ bộ nhớ tiến trình làm việc (Worklog, bài học, trạng thái dự án, cấu hình RDS/EC2/VPC, lịch sử trò chuyện) của dự án AWS Workshop. Dùng skill này khi người dùng yêu cầu xem lại lịch sử, đọc bộ nhớ, hoặc khôi phục trạng thái làm việc sau khi tắt/mở lại ứng dụng.
---

# AWS Workshop Memory & Context Tracker

Skill này dùng để lưu trữ và quản lý toàn bộ bộ nhớ làm việc và lịch sử trao đổi của dự án **AWS Workshop**, giúp giữ nguyên tiến độ, thông số cấu hình, lịch sử thực hành và nội dung học tập để không bị mất khi tắt ứng dụng hoặc chuyển phiên làm việc.

---

## 📂 Cấu trúc Lưu trữ Skill (`my-skill/`)

```text
.agents/skills/aws-workshop-memory/
├── SKILL.md                          # File hướng dẫn chính & frontmatter
├── references/                       # Bộ nhớ dữ liệu, bảng thông số & lịch sử
│   ├── memory.md                     # Nhật ký bộ nhớ công việc & tài nguyên AWS
│   └── conversation_history.md       # Lịch sử trò chuyện chi tiết & các quyết định
└── assets/                           # Sơ đồ kiến trúc & hình ảnh tài liệu
    └── arc.png                       # Sơ đồ kiến trúc Amazon RDS (Public/Private Subnet)
```

---

## 🎯 Khi nào sử dụng

- **Khôi phục trạng thái (Restore Context):** Khi mở lại dự án hoặc bắt đầu phiên chat mới, agent sử dụng skill này để nắm ngay toàn bộ lịch sử và trạng thái công việc hiện tại.
- **Đọc bộ nhớ / Lịch sử trò chuyện:** Khi người dùng yêu cầu _"đọc bộ nhớ"_, _"xem lịch sử trò chuyện"_, _"xem tiến độ"_, _"kiểm tra lịch sử làm việc"_.
- **Cập nhật ghi nhớ:** Khi hoàn thành bài thực hành mới, hoàn thiện Worklog tuần, hoặc thêm thông số AWS.

---

## 📌 Bộ nhớ Trạng thái Hiện tại (Current Project Memory)

### 1. Thông tin Dự án & Quy trình

- **Tên dự án:** AWS Workshop - Get Started with Amazon RDS (Hugo Template)
- **Đường dẫn local:** `d:\AWS\template_AWS\fcj-workshop-template-main`
- **Quy trình làm việc:** AI làm Co-pilot gợi ý/viết code ➔ Người dùng kiểm tra & phê duyệt.

### 2. Tiến độ Worklog (Mốc hiện tại: Tháng 10/2026)

- **Phạm vi làm việc:**
  - Hoàn thiện việc điền lộ trình từ **Cloud Journey mới (`cloudjourney.awsfcaj.com`)**, bổ sung trọn bộ hình ảnh kết quả thực tế cho từng ngày từ Thứ 2 đến Thứ 6 và đồng bộ toàn bộ link tài liệu tham khảo workshop cho **Week 1, Week 2, và Week 3**.
  - Hoàn thiện và chuẩn hóa toàn bộ 5 ngày của **Week 4** sang phong cách Step-by-Step thực chiến:
    - 1.4.1 (Amazon Lightsail): 13 bước, 13 ảnh.
    - 1.4.2 (Lightsail Container): 11 bước, 11 ảnh.
    - 1.4.3 (EC2 Auto Scaling): 44 bước, 44 ảnh.
    - 1.4.4 (Amazon CloudWatch): 33 bước, 33 ảnh.
    - Thứ 6: Tổng kết Tuần 4, Hoàn thiện Worklog (1.4.1 - 1.4.4) & Làm Project (Proposal).
  - Hoàn thành trọn vẹn 5 ngày của **Week 5** (`content/1-Worklog/1.5-Week5/`):
    - 1.5.1 (Hybrid DNS): 11 bước, 11 ảnh (chuyển từ 1.4.5 cũ).
    - 1.5.2 (AWS CLI): 38 bước, 38 ảnh, 12 khó khăn thực tế (chuyển từ 1.5.1 cũ).
    - 1.5.3 (Amazon DynamoDB): 32 bước, 32 ảnh, 10 khó khăn thực tế (chuyển từ 1.5.2 cũ).
    - 1.5.4 (Amazon ElastiCache - Redis): 26 bước thực hành, 27 ảnh, 12 khó khăn thực tế (chuyển từ 1.5.3 cũ).
    - Thứ 6: Tổng kết Tuần 5, Hoàn thiện Worklog (1.5.1 - 1.5.4) & Làm Project (Proposal).
  - Trạng thái **Tuần 6 Worklog** (`content/1-Worklog/1.6-Week6/`):
    - Mốc thời gian: 19/10/2026 - 23/10/2026.
    - 1.6.1 (Thứ 2 - 19/10/2026): Quản lý và Nâng hạn mức tài nguyên với AWS Service Quotas.
    - 1.6.2 (Thứ 3 - 20/10/2026): Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (18 ảnh).
    - 1.6.3 (Thứ 4 - 21/10/2026): Quản trị Thẻ định danh và Nhóm tài nguyên AWS - Tags & Resource Groups (14 ảnh).
    - 1.6.4 (Thứ 5 - 22/10/2026): Giám sát hệ thống với Grafana & Amazon CloudWatch (Workshop 000029, 18 ảnh).
    - Thứ 6: Tổng kết Tuần 6, Hoàn thiện Worklog (1.6.1 - 1.6.4) & Làm Project (Proposal).
    - Hoàn tất 100% song ngữ Việt - Anh.
  - Trạng thái **Tuần 7 Worklog** (`content/1-Worklog/1.7-Week7/`):
    - Mốc thời gian: 26/10/2026 - 30/10/2026.
    - 1.7.1 (Thứ 2 - 26/10/2026): Giám sát chuyên sâu với Amazon CloudWatch - CloudWatch Advanced Workshop (24 ảnh: CloudFormation, Metric Math, Search Expressions, Dynamic Labels, SSM Session Manager logger script, Logs Insights regex, Metric Filter `PythonAppErrors`, SNS Email alert, Dashboard `ssmDashboard`).
    - Thứ 3 (27/10/2026): Giám sát tải & Tự động phản ứng sự cố với CloudWatch & SNS.
    - Thứ 4 (28/10/2026): Tham gia Sự kiện Công nghệ AWS Community (Event 3 Review).
    - Thứ 5 (29/10/2026): Nghiên cứu Chuyên sâu & Biên soạn Bài viết Kỹ thuật Blog 1.
    - Thứ 6 (30/10/2026): Tổng kết Tuần 7, Viết Worklog & Làm Project (Proposal).
    - Hoàn tất 100% song ngữ Việt - Anh.
  - **Kiểm định chất lượng Hugo:** 102 trang EN, 101 trang VI, 536 static files, 0 missing images, 0 broken links.
    - 1.6.1 (Thứ 2): AWS Service Quotas (nâng quota Spot vCPU lên 64, xử lý case AWS Support, chuyển từ 1.5.4 cũ).
    - 1.6.2 (Thứ 3): Tối ưu hóa Chi phí Amazon EC2 với AWS Lambda & Thông báo Slack (9 bước, 18 ảnh, chuyển từ 1.5.5 cũ).
    - 1.6.3 (Thứ 4): Giám sát với Grafana & CloudWatch (Workshop 000029 - Getting started with Grafana basic).
    - Thứ 5: Mở rộng Giám sát & Quản trị Vận hành Đám mây (CloudWatch Advanced).
    - Thứ 6: Tổng kết Tuần 6, Hoàn thiện Worklog & Làm Project (Proposal).
- **Nội dung hoàn thành Tuần 5 - Thứ 2 (12/10/2026):**
  - Bài thực hành: **Thao tác dòng lệnh với AWS CLI** (Workshop 000011).
  - Khởi tạo trọn bộ 38 hình ảnh thực hành tại `static/images/1-Worklog/1.5-Week5/1.5.1-aws-cli/`.
  - Soạn thảo song ngữ chuẩn mực: `1.5.1-aws-cli.vi.md` và `1.5.1-aws-cli.md`.
  - Cập nhật trang tổng quan `_index.vi.md` và `_index.md`.
  - Đúc kết chi tiết 12 khó khăn kỹ thuật thực tế gặp phải và cách giải quyết triệt để.
- **Nội dung hoàn thành Tuần 5 - Thứ 3 (13/10/2026):**
  - Bài thực hành: **Làm việc với Amazon DynamoDB** (Workshop 000060).
  - Khởi tạo và chuẩn hóa trọn bộ 32 hình ảnh thực hành tại `static/images/1-Worklog/1.5-Week5/1.5.2-amazon-dynamodb/` (`2.1.png` đến `3.2.9.png`).
  - Nạp và xử lý bộ dữ liệu mẫu `moviedata.json` (4.609 bản ghi phim).
  - Viết và kiểm thử 9 script Python Boto3 SDK thao tác với DynamoDB (`MoviesCreateTable.py`, `MoviesItemOps01` đến `04`, `MoviesLoadData.py`, `MoviesQuery01.py`, `MoviesScan.py`, `MoviesDeleteTable.py`).
  - Soạn thảo song ngữ chuẩn mực: `1.5.2-amazon-dynamodb.vi.md` và `1.5.2-amazon-dynamodb.md`.
  - Cập nhật trang tổng quan `_index.vi.md` và `_index.md`.
  - Đúc kết chi tiết 10 khó khăn kỹ thuật thực tế gặp phải.
- **Nội dung hoàn thành Tuần 5 - Thứ 4 (14/10/2026):**
  - Bài thực hành: **Amazon ElastiCache - Redis** (Workshop 000061).
  - Khởi tạo và đồng bộ trọn bộ 27 hình ảnh thực hành tại `static/images/1-Worklog/1.5-Week5/1.5.3-amazon-elasticache/` (`2.1.png` đến `4.6.png`).
  - Khởi tạo hạ tầng mạng: VPC 3 AZs (`us-east-1a`, `1b`, `1c`), Subnet Group `subnet-group`, SG mở port 22 & 6379, Internet Gateway `my-igw`, định tuyến loại bỏ Blackhole.
  - Máy ảo EC2 client `redis-client` cài đặt Python 3 và thư viện `redis` v8.1.0.
  - Triển khai thành công 5 cụm Redis: `my-cluster-disable`, `my-cluster-enable`, `redis-disabled-sdk`, `redis-enabled-sdk`, `redis-rbac-sdk`, `redis-enabled-rbac-sdk`.
  - Quản trị RBAC User Groups: `mygroup`, `mygroup2`, Users: `myuser`, `default`.
  - Viết và chạy thành công các chương trình tương tác Redis: `ConnectClusterModeDisabled.py`, `ConnectClusterModeEnabled.py`, `SetAndGetStrings.py`, `SetAndGetHash.py`, `PubAndSub.py`.
  - Soạn thảo song ngữ Step-by-Step chuẩn mực: `1.5.3-amazon-elasticache.vi.md` và `1.5.3-amazon-elasticache.md`.
  - Cập nhật trang tổng quan `_index.vi.md` và `_index.md`.
  - Phân tích chi tiết và đưa ảnh minh chứng cho sự cố khi chưa tạo User Group (`UserGroupNotFoundFault`) và kết quả thành công sau khi tạo `UserAndUserGroups.py` (`4.1.1.1.png`, `4.1.3.png`, `4.1.3.1.png`).
  - Đúc kết chi tiết 12 sự cố kỹ thuật thực tế.
- **Hoàn thành Event 3 (24/10/2026):**
  - Sự kiện: **First Cloud AI Journey Meetup** tại Lầu 26 Bitexco Financial Tower.
  - Tích hợp 17 hình ảnh chuẩn hóa (selfie check-in, ảnh tập thể toàn cộng đồng, trọn bộ 5 sessions kỹ thuật).
  - Soạn thảo song ngữ chi tiết 5 sessions: Voice AI tiếng Việt (Revve AI), AWS RAM multi-account (Styl Solution), Shift-Left Security & AI Pentesting (Styl Solution), Bedrock AgentCore MicroVM Spot & Memory (HCMUTE), Kiro Crew Companion (ACB & AWS Community Builder).
  - Soạn thảo song ngữ `4.3-Event3/_index.vi.md` và `_index.md`, cập nhật trang mục lục `4-EventParticipated`.
  - Hugo build: 94 trang EN, 93 trang VI, 465 static files, 0 errors.
- **Hoàn thành Blog 1 (28/10 - 29/10/2026):**
  - Đề tài chính thức: **AWS Continuum for Code Vulnerabilities Is Now Generally Available** (AWS News Blog - 22/10/2026 GA).
  - Tích hợp 4 ảnh console chính thức từ AWS: `continuum-overview.png`, `continuum-issues.png`, `continuum-risk-assessment.png`, `continuum-pr-github.png`.
  - Thiết kế và thẩm định sơ đồ kiến trúc Draw.io: Đạt điểm 10/10 với đầy đủ 6 bước (Scan Code, Read Cloud Context, Trigger PoC Exploit, Validated Evidence, Auto Open PR, Review & Merge) phân bố chuẩn trong 2 nhóm hạ tầng (`AWS Cloud / Security Context` và `Developer Environment GitHub/GitLab`). Đích lưu: `static/images/3-BlogsPosted/3.1-Blog1/continuum-architecture.png`.
  - Soạn thảo song ngữ chuẩn mực: `3.1-Blog1/_index.vi.md` (100% Tiếng Việt) và `3.1-Blog1/_index.md` (100% Tiếng Anh học thuật), cập nhật trang mục lục `3-BlogsPosted`.
  - **Đã đăng bài lên cộng đồng Facebook (29/10/2026):** Đã tinh chỉnh bài viết trực diện, chuyên nghiệp, gắn link blog và nộp lên nhóm [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj). Hiện tại đang ở trạng thái **⏳ Chờ Admin duyệt bài**.
  - Tích hợp sẵn khung chờ link bài đăng Facebook và hình ảnh minh chứng sau khi duyệt.
  - Hugo build: 94 trang EN, 93 trang VI, 473 static files, 0 errors.

### 3. Đã xử lý Cấu hình Hugo & Rà soát Toàn diện (01/11/2026)

- Đã khắc phục tiến trình Hugo server chạy ngầm trên port 1313 (http://localhost:1313/vi/1-worklog/1.3-week3/).
- Đã chuẩn hóa thuộc tính `weight` từ 1 đến 12 cho tất cả các folder `1.1-Week1` ➔ `1.12-Week12` để hiển thị đúng thứ tự trên thanh Sidebar.
- Đã chuẩn hóa tên thư mục `1.5.1-aws-cli`, phục hồi toàn bộ 38 ảnh hiển thị thành công (0 missing images).
- Đã đồng bộ thông tin sinh viên thực tế (Trần Gia Bảo) trên trang chủ Tiếng Việt (`_index.vi.md`) và cập nhật tác giả `config.toml`.
- Đã sửa triệt để các liên kết nội bộ 404 trong Mục 5 (5.3 và 5.4) và Mục 2 (0 broken links).
- Hugo build hiện tại: 95 trang EN, 94 trang VI, 480 static files, 0 errors, 0 warnings.

### 4. Cẩm nang Quy chuẩn Trình bày Worklog Áp dụng cho các Tuần sau (Presentation & Workflow Framework)

Quy chuẩn này là kim chỉ nam bắt buộc phải tuân thủ nghiêm ngặt khi tạo mới hoặc cập nhật bất kỳ tài liệu Worklog nào (từ Tuần 5 trở đi và toàn bộ các tuần tương lai):

#### 4.1. Quy tắc Nối tiếp Mục tiêu Tuần sau (Continuous Next-Week Objectives Workflow)

- **Nguyên lý cuốn chiếu:** Khi hoàn thành bất kỳ bài thực hành của **Tuần N+1**, agent/developer bắt buộc phải quay lại cuối trang tổng quan `_index.vi.md` và `_index.md` của **Tuần N** để cập nhật mục:
  - Bản tiếng Việt: `### Mục tiêu cho tuần sau (Tuần N+1):`
  - Bản tiếng Anh: `### Next Week's Objectives (Week N+1):`
- **Yêu cầu nội dung:** Phải phản ánh chính xác 100% các chủ đề, dịch vụ và bài lab thực tế đã hoàn thành ở Tuần N+1. Nhờ đó, người đọc khi theo dõi từ Tuần 1 ➔ Tuần 2 ➔ Tuần 3 ➔ Tuần 4 ➔ Tuần 5 ➔ Tuần 6... luôn thấy lộ trình nối tiếp mạch lạc và không có độ vênh thông tin.
- **Bản đồ nối tiếp đã thiết lập:**
  - Cuối **Tuần 1**: Ghi chi tiết mục tiêu của **Tuần 2** (Tối ưu hóa: Operations, Security, Reliability, Cost & Serverless).
  - Cuối **Tuần 2**: Ghi chi tiết mục tiêu của **Tuần 3** (App Modernization, Containers, Data Analytics & Lab Amazon RDS).
  - Cuối **Tuần 3**: Ghi chi tiết mục tiêu của **Tuần 4** (Amazon Lightsail, Containers, EC2 Auto Scaling, CloudWatch, Hybrid DNS).
  - Cuối **Tuần 4**: Ghi chi tiết mục tiêu của **Tuần 5** (AWS CLI v2, Amazon DynamoDB, Amazon ElastiCache Redis).
  - Cuối **Tuần 5**: Ghi chi tiết mục tiêu của **Tuần 6** (Tự động hóa IaC CloudFormation/CDK, AWS KMS, Secrets Manager, CI/CD Pipeline).
  - Khi hoàn thành **Tuần 6**: Cập nhật mục tiêu **Tuần 7** vào cuối Tuần 6, và đồng bộ lại nếu Tuần 6 có sự thay đổi thực tế.

#### 4.2. Cấu trúc Chuẩn mực của Trang Tổng quan Tuần (`_index.vi.md` & `_index.md`)

Mỗi trang `_index` của tuần phải tuân thủ đúng thứ tự cấu trúc sau:

1. **FrontMatter:**
   ```yaml
   ---
   title: "Worklog Tuần X" # EN: "Week X Worklog"
   date: YYYY-MM-DD
   weight: X
   chapter: false
   pre: " <b> 1.X. </b> "
   ---
   ```
2. **Hộp cảnh báo tham khảo (Notice Warning):**
   ```markdown
   {{% notice warning %}}
   ⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
   {{% /notice %}}
   ```
3. **Mục tiêu tuần X:** 2-3 gạch đầu dòng định hướng chiến lược của tuần.
4. **Bảng công việc trong tuần (5 cột chuẩn):**
   `| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |`
   - Mỗi ô Công việc phải có tên in đậm và các gạch đầu dòng `<br>- Chi tiết nhiệm vụ`.
   - Nguồn tài liệu dẫn link Markdown chuẩn tới Workshop AWS tương ứng.
5. **Kết quả đạt được tuần X:**
   - Với mỗi ngày có bài thực hành chi tiết, bắt buộc phải có hộp Tip dẫn link:
     ```markdown
     {{% notice tip %}}
     👉 **Báo cáo thực hành chi tiết:** Toàn bộ thông số cấu hình, các bước thực hiện và trọn bộ [N] hình ảnh minh chứng được trình bày ngăn nắp tại: **[1.X.Y. Tên bài](1.X.Y-slug/)**.
     {{% /notice %}}
     ```
   - Đi kèm các gạch đầu dòng tóm tắt các hạng mục công việc đã làm được.
6. **Đường phân cách:** `---`
7. **Mục tiêu cho tuần sau (Tuần X+1):** Cấu trúc cây thư mục markdown với các gạch đầu dòng chi tiết nội dung tuần tiếp theo.

#### 4.3. Cấu trúc Chuẩn mực của Bài Báo cáo Chi tiết Ngày (`1.X.Y-ten-bai.vi.md` & `1.X.Y-ten-bai.md`)

Tuyệt đối **không copy nguyên tài liệu lý thuyết dài dòng** vào bài viết. Phải tuân theo phong cách **Step-by-Step thực chiến**:

1. **FrontMatter:**
   ```yaml
   ---
   title: "1.X.Y. Tên bài thực hành"
   date: YYYY-MM-DD
   weight: Y
   chapter: false
   pre: " <b> 1.X.Y. </b> "
   ---
   ```
2. **🎯 Mục tiêu bài thực hành (Lab Objectives):** Nêu rõ 3-5 kết quả kỹ thuật cụ thể mà bài lab hướng tới.
3. **📊 Bảng tổng hợp thông số tài nguyên đã triển khai (Provisioned Resource Specifications):**
   - Bảng tổng hợp rõ ràng: `| Thành phần / Tài nguyên | Tên định danh (Name/ID) | Thông số kỹ thuật / Cấu hình chi tiết | Mục đích / Ghi chú |`
   - Ghi rõ: VPC CIDR, Subnets, Security Groups, Inbound/Outbound Ports, Instance Types, AMI, DB Engines, Storage Classes, Auth Modes, User Groups...
4. **Các bước thực hành Step-by-Step có số thứ tự rõ ràng (`#### Bước Z: [Tên bước]`):**
   Mỗi bước bắt buộc phải cung cấp đủ:
   - **Thao tác:** Đường dẫn menu trên AWS Console hoặc môi trường CLI.
   - **Bảng/Danh sách thông số:** Giá trị nhập liệu chính xác từng trường.
   - **Khối lệnh / Mã nguồn (nếu có):** Code hoàn chỉnh, có giải thích dòng lệnh, không viết code cụt hoặc để biến placeholder `xxx.yyy`.
   - **Ảnh minh chứng:** Nhúng ảnh chụp màn hình thực tế tương ứng với bước đó.
   - **Sự cố & Xử lý tại chỗ (nếu có):** Hộp `{{% notice warning %}}` hoặc `{{% notice tip %}}` chỉ rõ lỗi phát sinh và cách vượt qua.
5. **🛠️ Ngân hàng sự cố kỹ thuật thực tế & Cách khắc phục triệt để (Real-world Troubleshooting Bank):**
   - Tổng hợp 8-12 sự cố kỹ thuật thực tế gặp phải trong suốt quá trình làm bài.
   - Trình bày theo format 3 yếu tố:
     - **Hiện tượng (Symptom):** Thông báo lỗi chính xác, mã lỗi (`Exception`, `Fault`, `Error`).
     - **Nguyên nhân cốt lõi (Root Cause):** Giải thích bản chất kỹ thuật (IAM, Security Group, Route Table, Version mismatch, Type collision...).
     - **Giải pháp & Minh chứng (Solution & Proof):** Từng bước khắc phục và dẫn ảnh minh chứng so sánh trước vs sau khi sửa (Error ➔ Fix ➔ Success).
6. **🧹 Dọn dẹp tài nguyên (Resource Cleanup):**
   - Hướng dẫn thứ tự xóa tài nguyên an toàn theo đúng chiều phụ thuộc (tránh lỗi `DependencyViolation`) để không phát sinh chi phí ngoài ý muốn trên AWS.

#### 4.4. Quy chuẩn Quản lý Hình ảnh (Image Assets)

- Thư mục lưu trữ hình ảnh: `static/images/1-Worklog/1.X-WeekX/1.X.Y-ten-bai/`.
- Tên ảnh chuẩn hóa không dấu, không chứa khoảng trắng (ví dụ: `step-1.png`, `4.1.3.1.png`).
- Đường dẫn nhúng trong markdown phải bắt đầu bằng `/images/1-Worklog/...` (đường dẫn tuyệt đối từ root của Hugo tĩnh).
- Tuyệt đối không xóa hoặc ghi đè làm mất ảnh của các bài trước.

#### 4.5. Nguyên tắc Đa Ngôn Ngữ Tách Biệt Tuyệt Đối (Strict Bilingual Separation)

- File `.vi.md`: **100% Tiếng Việt** chuẩn mực kỹ thuật (link nội bộ trỏ tới `/vi/...`).
- File `.md`: **100% Tiếng Anh** chuẩn AWS Technical Writing (link nội bộ trỏ tới `/...`).
- Tuyệt đối KHÔNG bao giờ copy chèn nội dung tiếng Việt sang file `.md` tiếng Anh hoặc ngược lại.

---

## 🔗 Liên kết tài liệu bộ nhớ

- 📄 [SKILL.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/SKILL.md)
- 📝 [memory.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/references/memory.md)
- 💬 [conversation_history.md](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/references/conversation_history.md)
- 🖼️ [arc.png](file:///d:/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/aws-workshop-memory/assets/arc.png)
