---
name: avoid-ai-writing
description: >-
  Audit, clean, and rewrite content to remove AI writing patterns ("AI-isms"), inflated corporate jargon, formulaic structures, and generic machine phrasing. Use when asked to "remove AI-isms", "clean up AI writing", "make this sound less like AI", "edit writing to sound human", or when writing/polishing technical blogs, worklogs, proposals, and self-evaluations. Supports rewrite, detect-only, and edit-in-place modes with bilingual (EN & VI) pattern detection and technical voice calibration.
---

# Avoid AI Writing (Agent Skill)

Skill này giúp rà soát, phát hiện và viết lại (rewrite) nội dung nhằm loại bỏ hoàn toàn các **"mùi AI" (AI-isms / AI Smells)**, sáo rỗng, hoa mỹ giả tạo, biến bài viết thành văn phong **kỹ sư thực chiến (grounded, authentic, natural, action-oriented)**.

---

## 🎯 Khi nào sử dụng

Kích hoạt skill này khi:
1. Người dùng yêu cầu: *"xóa mùi AI"*, *"làm bài này tự nhiên hơn"*, *"viết như người thật"*, *"tránh văn phong ChatGPT"*, *"audit AI writing"*, *"make this sound human"*.
2. Soạn thảo hoặc biên tập các phần quan trọng:
   - **Worklog hàng ngày / Báo cáo tuần:** Loại bỏ văn giải thích lý thuyết chung chung, tập trung vào thao tác thực tế và xử lý lỗi.
   - **Technical Blog (`3-BlogsPosted`):** Tăng tính trải nghiệm thực tế, loại bỏ giọng văn dịch máy.
   - **Đề xuất dự án (`2-Proposal`):** Tăng tính khả thi và sức thuyết phục kỹ thuật.
   - **Tự đánh giá (`6-Self-Evaluation`):** Giữ giọng văn tự sự chân thành của sinh viên thực tập.

---

## ⚙️ 3 Chế độ Hoạt động (Operation Modes)

1. **Rewrite Mode (Mặc định):**
   - Đọc văn bản nguồn, phát hiện các mẫu AI, và viết lại toàn bộ theo phong cách tự nhiên của kỹ sư.
   - Tóm tắt ngắn gọn những điểm đã lược bỏ/chỉnh sửa.

2. **Detect-Only Mode:**
   - Kiểm tra và đánh giá văn bản (Chấm điểm mức độ AI từ 0 đến 100, trong đó 0 là 100% tự nhiên, 100 là đậm đặc AI).
   - Liệt kê chi tiết các câu, từ vựng và cấu trúc vi phạm (phân loại theo mức độ P0, P1, P2) mà **không làm thay đổi file**.

3. **Edit-in-Place Mode:**
   - Chỉnh sửa trực tiếp trên file Markdown được chỉ định.
   - **Bảo toàn 100%** code blocks, cấu hình, liên kết, bảng số liệu và Hugo frontmatter.

---

## 🚨 Thang mức độ nghiêm trọng (Severity Tiers)

- **P0 — Credibility Killers (Sát thủ uy tín - Phải sửa ngay):**
  - Mở bài triết lý đao to búa lớn (*"Trong kỷ nguyên số bùng nổ hiện nay...", "In today's fast-paced digital world..."*).
  - Tâng bốc công nghệ lộ liễu (*"minh chứng cho sự vượt trội", "testament to the power of cloud"*).
  - Lời mở đầu máy móc của chatbot (*"Chắc chắn rồi! Dưới đây là bài viết...", "Certainly! Here is..."*).

- **P1 — Obvious AI Smells (Mùi AI đặc trưng - Cần làm sạch trước khi nộp):**
  - Từ vựng AI kinh điển (Tier 1A): `delve`, `tapestry`, `testament`, `beacon`, `multifaceted`, `intricate`, `embark`, `harness`, `realm`...
  - Quy tắc 3 vế cân đối (Rule of three): *"nhanh chóng, an toàn và tối ưu"*, *"fast, reliable, and secure"*.
  - Đoạn kết luận sáo rỗng: *"Tóm lại, thông qua bài lab này...", "In conclusion, by leveraging..."*.

- **P2 — Stylistic Polish (Gọt giũa độ tinh gọn):**
  - Từ vựng rườm rà (Tier 1B): `in order to` ➔ `to`, `utilize` ➔ `use`, `leverage` ➔ `use`, `facilitate` ➔ `help/allow`.
  - Tiếng Việt: *"đóng vai trò then chốt"* ➔ *"cần thiết/quan trọng"*, *"không thể phủ nhận rằng"* ➔ *(bỏ hẳn)*.
  - Lạm dụng từ nối học thuật: `Moreover`, `Furthermore`, `Hơn nữa`, `Bên cạnh đó` lặp lại liên tục ở đầu mỗi đoạn.

---

## 🛡️ Nguyên tắc Bảo toàn Kỹ thuật (Preservation Rules)

**TUYỆT ĐỐI KHÔNG BAO GIỜ THAY ĐỔI:**
1. Khối mã nguồn (` ```bash `, ` ```python `, ` ```yaml `...) và inline code (` `aws s3 cp` `).
2. Tên tài nguyên kỹ thuật, Service name (Amazon EC2, Amazon RDS, AWS Lambda, VPC, CloudWatch...).
3. Thông số mạng, IP, CIDR block (`10.0.0.0/16`), Port, ARN, IAM role name.
4. YAML frontmatter của bài viết (title, weight, date...).
5. Cú pháp shortcodes của Hugo (`{{< ... >}}`).

---

## 🎙️ Voice Profiles (Hồ sơ Giọng văn)

- **`technical` (Ưu tiên số 1 cho dự án AWS này):** Ngắn gọn, chính xác, định lượng cụ thể, tập trung vào hành động kỹ sư (Cấu hình gì ➔ Thông số nào ➔ Kết quả ra sao ➔ Gặp lỗi gì ➔ Khắc phục thế nào).
- **`professional`:** Rõ ràng, trang nhã, không dùng từ ngữ quảng cáo hay tâng bốc.
- **`casual`:** Gần gũi, như một kỹ sư đang chia sẻ kinh nghiệm nội bộ với đồng nghiệp.
- **`blunt`:** Cực kỳ trực diện, không có từ đệm, chỉ có sự thật và hành động.

Chi tiết về từ điển thay thế và mẫu câu xem tại:
- [references/patterns.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/avoid-ai-writing/references/patterns.md)
- [references/voice-profiles.md](file:///d:/tool/AWS/template_AWS/fcj-workshop-template-main/.agents/skills/avoid-ai-writing/references/voice-profiles.md)
