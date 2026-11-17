# AI Writing Patterns & Vocabulary Replacement Catalog

Tài liệu này chứa toàn bộ cơ sở dữ liệu mẫu câu AI (AI-isms), từ vựng rập khuôn và quy tắc chuyển đổi sang văn phong kỹ sư thực chiến cho cả **Tiếng Anh** và **Tiếng Việt**.

---

## 1. Bảng Chuyển đổi Từ vựng Tiếng Anh (English Vocabulary Tiers)

### Tier 1A: Từ vựng Đậm mùi AI (LLM Frequency Markers - Flag ngay khi xuất hiện)

| Từ AI hay dùng | Thay thế tự nhiên | Ví dụ chỉnh sửa |
| :--- | :--- | :--- |
| `delve` / `delve into` | explore, examine, look at, inspect, review | ❌ Delve into the VPC architecture.<br>✅ Review the VPC setup. |
| `tapestry` | mix, collection, combination, system | ❌ A rich tapestry of microservices.<br>✅ A combination of Lambda functions and queues. |
| `testament` / `testament to` | proof of, shows that, proves, demonstrates | ❌ A testament to high availability.<br>✅ Proves the failover works. |
| `beacon` | guide, standard, model | ❌ Acts as a beacon for best practices.<br>✅ Follows the AWS Well-Architected Framework. |
| `multifaceted` | complex, varied, having multiple parts | ❌ A multifaceted approach.<br>✅ An approach covering both VPC and IAM. |
| `intricate` | detailed, complex | ❌ Intricate configurations.<br>✅ Complex routing rules. |
| `embark` / `embark on` | start, begin, set up, launch | ❌ Embark on this lab.<br>✅ Start setting up the cluster. |
| `harness` | use, utilize, apply | ❌ Harness the power of DynamoDB.<br>✅ Use DynamoDB on-demand capacity. |
| `realm` | area, domain, service scope | ❌ In the realm of cloud monitoring.<br>✅ In CloudWatch metrics. |
| `pivot` | switch, change, move | ❌ Pivot to using Redis.<br>✅ Switch from Memcached to Redis. |
| `plethora` | many, several, a number of | ❌ A plethora of IAM roles.<br>✅ Multiple IAM roles. |
| `nuance` / `nuanced` | detail, subtlety, difference | ❌ Nuanced security settings.<br>✅ Specific Security Group port rules. |
| `cornerstone` | foundation, core, key component | ❌ S3 is the cornerstone of storage.<br>✅ S3 is the primary storage layer. |

---

### Tier 1B: Từ ngữ Rườm rà & Trang trọng Hóa (Wordiness & Inflated Formality)

| Cụm từ rườm rà | Thay thế súc tích |
| :--- | :--- |
| `in order to` | **to** |
| `utilize` / `utilization` | **use** |
| `leverage` | **use**, **rely on** |
| `facilitate` | **help**, **allow**, **support** |
| `commence` | **start**, **begin** |
| `implement` *(khi nói về cấu hình đơn giản)* | **set up**, **configure**, **build** |
| `due to the fact that` | **because**, **since** |
| `at this point in time` | **now**, **currently** |
| `with regard to` / `in terms of` | **regarding**, **for**, *(hoặc viết thẳng vào chủ ngữ)* |

---

### Tier 2: Từ ngữ Tiếp thị Doanh nghiệp (Corporate Buzzwords)

| Thuật ngữ sáo rỗng | Cách diễn đạt kỹ thuật thực tế |
| :--- | :--- |
| `robust` | reliable, resilient, fault-tolerant, tested |
| `seamless` / `seamlessly` | directly, without downtime, automatically |
| `cutting-edge` | modern, latest, current |
| `game-changer` | significant improvement, reduced latency by 40% |
| `streamline` | simplify, automate, speed up |
| `synergy` | integration, connection |
| `holistic` | end-to-end, full-stack, comprehensive |

---

## 2. Bảng Chuyển đổi Văn phong Tiếng Việt (Vietnamese AI-ism Catalog)

### Mẫu câu sáo rỗng thường gặp trong Báo cáo thực tập tiếng Việt

| Mẫu câu AI tiếng Việt | Vấn đề | Cách viết lại của Kỹ sư thực chiến |
| :--- | :--- | :--- |
| *"Trong bối cảnh công nghệ thông tin ngày càng bùng nổ hiện nay..."* | Mở bài sáo rỗng, học thuộc lòng, không mang lại thông tin. | **Đi thẳng vào đề:** *"Báo cáo này trình bày quá trình cấu hình kiến trúc Amazon RDS Multi-AZ và xử lý failover tự động."* |
| *"Đóng vai trò vô cùng quan trọng / then chốt trong..."* | Cường điệu hóa, lặp đi lặp lại ở mọi bài viết. | **Nói rõ vai trò cụ thể:** *"VPC cô lập máy chủ cơ sở dữ liệu khỏi internet, chỉ mở cổng 3306 cho Web Server nội bộ."* |
| *"Là minh chứng rõ nét cho sức mạnh của..."* | Tâng bốc công nghệ như nhân viên bán hàng. | **Nêu số liệu/kết quả đo đạc:** *"Kiểm thử thực tế cho thấy cơ chế Multi-AZ chuyển đổi dự phòng trong vòng 65 giây mà không làm mất dữ liệu."* |
| *"Không thể phủ nhận rằng việc tối ưu hóa..."* | Lời dẫn gián tiếp, thiếu tự tin, rườm rà. | **Khẳng định trực tiếp:** *"Cấu hình Auto Scaling giúp hệ thống tự động giảm từ 4 instance xuống 1 instance vào ban đêm để tiết kiệm 60% chi phí."* |
| *"Mang lại trải nghiệm liền mạch và tối ưu nhất..."* | Quảng cáo chung chung, vô nghĩa về mặt kỹ thuật. | **Chỉ rõ tiêu chí kỹ thuật:** *"Giảm thời gian phản hồi API từ 350ms xuống 45ms nhờ cache dữ liệu trên Amazon ElastiCache."* |
| *"Tóm lại, thông qua bài thực hành này, em đã gặt hái được..."* | Kết bài rập khuôn của học sinh cấp 2. | **Tổng kết hành động & bài học:** *"Kết quả: Đã dựng xong hạ tầng, cấu hình đầy đủ Alert. Khó khăn: Gặp lỗi Subnet Group thiếu AZ, đã xử lý bằng cách thêm subnet `us-east-1c`."* |

---

## 3. Các Cấu trúc Câu Rập khuôn cần Loại bỏ (Structural AI Tells)

### 3.1. Quy tắc 3 vế cân đối (The Rule of Three)
- **Dấu hiệu:** AI luôn cố gắng nhồi nhét đúng 3 tính từ hoặc 3 mệnh đề song song để nghe có vẻ nhịp nhàng.
  - ❌ *"Hệ thống đảm bảo tính an toàn, linh hoạt và hiệu quả cao."*
  - ❌ *"A fast, reliable, and secure cloud solution."*
- **Khắc phục:** Chọn đúng tính chất kỹ thuật quan trọng nhất hoặc mô tả bằng thông số cụ thể:
  - ✅ *"Hệ thống chạy trên VPC riêng biệt và phân quyền IAM theo nguyên tắc tối thiểu."*
  - ✅ *"The cluster maintained 99.9% uptime during stress testing."*

### 3.2. Mở bài tâng bốc & Nhắc lại câu hỏi (Sycophantic Echo & Grand Openers)
- **Dấu hiệu:** Mở đầu bài viết bằng việc khen ngợi chủ đề hoặc nhắc lại toàn bộ câu hỏi.
  - ❌ *"Việc giám sát hệ thống là một đề tài vô cùng thú vị và thiết yếu trong mọi dự án điện toán đám mây..."*
- **Khắc phục:** Đi thẳng vào mục tiêu thực tế của bài:
  - ✅ *"Bài viết này hướng dẫn cài đặt Grafana và tích hợp CloudWatch Data Source để theo dõi CPU và Memory của dàn EC2."*

### 3.3. Nhượng bộ giả tạo (The False Concession)
- **Dấu hiệu:** Dùng cấu trúc: *"Mặc dù X có nhược điểm Y, nhưng không thể phủ nhận rằng Z là giải pháp hoàn hảo..."*
- **Khắc phục:** Phân tích kỹ thuật khách quan:
  - ✅ *"Amazon DynamoDB có chi phí thấp khi tải thấp, nhưng khi lượng truy vấn đột biến, cần cấu hình On-Demand Mode để tránh bị throttling."*

### 3.4. Nghiện dấu gạch ngang dài (Em-dash Addiction `—`)
- **Dấu hiệu:** AI chèn dấu gạch ngang liên tục vào giữa câu để tạo khoảng lặng giả tạo.
- **Khắc phục:** Dùng dấu phẩy bình thường, ngắt thành 2 câu ngắn, hoặc dùng dấu ngoặc đơn giải thích.
