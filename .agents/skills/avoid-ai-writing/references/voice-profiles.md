# Voice Profiles & Before/After Calibration

Tài liệu này định nghĩa chi tiết các hồ sơ giọng văn (Voice Profiles) và cung cấp các ví dụ thực tế Trước (Before) và Sau (After) khi chuẩn hóa cho tài liệu kỹ thuật AWS.

---

## 1. Bốn Hồ sơ Giọng văn (Voice Profiles)

### 🎙️ 1. Technical Profile (Mặc định cho AWS Workshop)
- **Đặc trưng:** Ngắn gọn, trung thực, chú trọng số liệu, lệnh CLI, log output, tên service AWS chuẩn xác và cách khắc phục sự cố.
- **Từ ngữ:** Dùng thuật ngữ kỹ thuật tiêu chuẩn (VPC peering, latency, IOPS, cold start, retry logic...).
- **Cấm kỵ:** Các phép so sánh ví von hoa mỹ ("như một ngọn hải đăng", "nhịp đập trái tim của hệ thống").

### 🎙️ 2. Professional Profile
- **Đặc trưng:** Trang nhã, khách quan, trung tính, phù hợp cho báo cáo chính thức nộp lên Ban Giám Hiệu hoặc Khách hàng doanh nghiệp.
- **Từ ngữ:** Rõ ràng, ngữ pháp chuẩn mực, không dùng từ lóng hay tiếng lóng internet.

### 🎙️ 3. Casual Profile
- **Đặc trưng:** Giống như một kỹ sư viết blog cá nhân hoặc ghi chú cho đồng đội trong team dự án.
- **Từ ngữ:** Có thể dùng cách xưng hô thân mật ("mình", "anh em"), chia sẻ thẳng thắn những lỗi ngớ ngẩn thường gặp.

### 🎙️ 4. Blunt Profile
- **Đặc trưng:** Cắt bỏ 100% từ đệm và từ nối. Chỉ ghi lại sự kiện: Hiện trạng ➔ Vấn đề ➔ Hành động ➔ Kết quả.
- **Phù hợp cho:** Post-mortem sự cố, Bảng tổng hợp lỗi, Báo cáo tiến độ Standup hàng ngày.

---

## 2. Các Ví dụ Chuyển đổi Thực chiến (Before & After)

### Ví dụ 1: Mô tả bài lab AWS Lambda tự động tắt EC2 (Worklog Tuần 6)

❌ **BEFORE (Văn phong AI sáo rỗng):**
> Trong kỷ nguyên điện toán đám mây hiện nay, việc tối ưu hóa chi phí đóng vai trò then chốt quyết định sự thành bại của doanh nghiệp. Để giải quyết bài toán nan giải này, bài thực hành ngày hôm nay sẽ đưa chúng ta delve into sức mạnh vượt trội của AWS Lambda kết hợp cùng Amazon EventBridge và Slack Webhook. Đây là một giải pháp toàn diện, linh hoạt và liền mạch, không chỉ giúp tự động hóa quy trình quản lý tài nguyên mà còn là minh chứng rõ nét cho kiến trúc Serverless hiện đại.

✅ **AFTER (Văn phong Kỹ sư - Technical Profile):**
> Bài thực hành này thiết lập luồng tự động tắt các máy ảo EC2 môi trường Dev ngoài giờ làm việc (sau 19:00 hàng ngày) bằng AWS Lambda (Python 3.12, runtime Boto3 SDK) và Amazon EventBridge cron schedule. Sau khi hoàn thành thao tác StopInstances, Lambda sẽ gửi thông báo trạng thái kèm Instance ID trực tiếp về kênh `#aws-cost-alerts` trên Slack thông qua Incoming Webhook. Cấu hình này giúp giảm khoảng 60% chi phí chạy máy ảo nhàn rỗi mỗi tháng.

---

### Ví dụ 2: Mục "Khó khăn gặp phải & Bài học kinh nghiệm" (Lessons Learned)

❌ **BEFORE (Văn phong AI khuôn mẫu):**
> Trong suốt quá trình triển khai bài thực hành, bản thân em đã phải đối mặt với không ít thách thức và khó khăn đa chiều. Tuy nhiên, bằng sự nỗ lực không ngừng nghỉ và tinh thần học hỏi, em đã biến những thách thức đó thành cơ hội quý báu để nâng cao năng lực chuyên môn. Qua đó, em nhận thấy việc nắm vững kiến trúc mạng VPC là vô cùng quan trọng và cần thiết để kiến tạo nên những hệ thống đám mây bền vững trong tương lai.

✅ **AFTER (Văn phong Kỹ sư - Technical Profile):**
> **Các sự cố kỹ thuật gặp phải và cách khắc phục:**
> 1. **Lỗi Subnet Group không hợp lệ trên ElastiCache:** Hệ thống báo lỗi `CacheSubnetGroupNotAllowed` do nhóm subnet chỉ có 1 Availability Zone (`us-east-1a`). Khắc phục: Bổ sung thêm private subnet ở `us-east-1b` và `us-east-1c` theo đúng yêu cầu tối thiểu 2 AZs của Redis replication group.
> 2. **Lỗi kết nối Redis CLI Timeout:** Từ máy client không kết nối được tới endpoint cluster qua port 6379. Kiểm tra Security Group phát hiện rule Inbound mới chỉ mở cho IP public của người quản trị chứ chưa mở cho SG của máy client. Khắc phục: Thêm Inbound rule cho phép port 6379 với Source là `sg-xxxx (EC2-Client-SG)`.

---

### Ví dụ 3: Bản Đề xuất Dự án Thực tập (Project Proposal)

❌ **BEFORE (Văn phong AI tâng bốc):**
> Đề xuất dự án này là một sáng kiến mang tính đột phá nhằm tái định hình trải nghiệm người dùng thông qua việc khai thác tối đa sức mạnh của trí tuệ nhân tạo và điện toán đám mây. Dự án hứa hẹn sẽ mở ra một kỷ nguyên mới trong quản lý cơ sở dữ liệu, mang lại sự kết hợp hài hòa giữa hiệu năng vượt trội và tính bảo mật tuyệt đối.

✅ **AFTER (Văn phong Kỹ sư - Technical Profile):**
> Đề án đề xuất xây dựng hệ thống Ngân hàng Đề thi và Đánh giá Tự động (AI Exam Bank) phục vụ sinh viên khối ngành kỹ thuật. Hệ thống áp dụng kiến trúc Serverless trên AWS (API Gateway, AWS Lambda, DynamoDB) kết hợp mô hình ngôn ngữ lớn để tự động phân tích độ khó câu hỏi và chống trùng lặp. Mục tiêu: Giảm 70% thời gian biên soạn đề thi của giảng viên và duy trì thời gian phản hồi kiểm tra dưới 200ms với chi phí hạ tầng ước tính dưới \$30/tháng.
