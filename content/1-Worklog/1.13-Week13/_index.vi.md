---
title: "Worklog Tuần 13"
date: 2026-12-07
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 13:

- Tiếp cận toàn diện hệ sinh thái **Trí tuệ nhân tạo tạo sinh (Generative AI)** trên AWS thông qua dịch vụ nền tảng được quản lý hoàn toàn **Amazon Bedrock**.
- Trải nghiệm và đánh giá thực nghiệm các mô hình nền tảng hàng đầu thế giới (**Foundation Models - FMs**): Anthropic Claude 3.5 Sonnet, Amazon Titan Text, Meta Llama 3 thông qua Bedrock Console Playground và Python Boto3 SDK.
- Nắm vững các kỹ thuật thiết kế câu lệnh chuyên sâu (**Prompt Engineering**: Zero-shot, Few-shot, Chain-of-Thought) và xây dựng kiến trúc **RAG (Retrieval-Augmented Generation)** với **Amazon Bedrock Knowledge Bases** tích hợp cơ sở dữ liệu véc-tơ Amazon OpenSearch Serverless.
- Xây dựng và triển khai tác nhân AI tự hành (**Amazon Bedrock Agents**) có khả năng tự động phân tích ý định, chia nhỏ bài toán và kích hoạt các hàm AWS Lambda (**Action Groups**) để xử lý dữ liệu thực tế.
- Khám phá chu trình phát triển học máy toàn diện (**MLOps**) với **Amazon SageMaker** (SageMaker Studio, JumpStart và Real-time Inference Endpoints).
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và tích hợp tính năng Trợ lý AI thông minh vào đồ án thực tập (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Khám phá Foundation Models & Amazon Bedrock:** <br>- Đăng ký quyền truy cập mô hình (Model Access: Claude 3.5 Sonnet, Titan, Llama 3). <br>- Kiểm thử độ trễ, ngữ cảnh (Context Window) và chi phí token trên Bedrock Playground. <br>- Lập trình gọi mô hình tạo sinh qua Python Boto3 SDK (`bedrock-runtime`). | 07/12/2026 | 07/12/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Thứ 3** | **Prompt Engineering & Kiến trúc RAG với Bedrock Knowledge Bases:** <br>- Tối ưu hóa kỹ thuật Prompt: System Prompts, Structured Outputs (JSON Schema). <br>- Khởi tạo Bedrock Knowledge Base liên kết nguồn dữ liệu tài liệu trên Amazon S3. <br>- Cấu hình mô hình nhúng véc-tơ (Titan Embeddings) và tìm kiếm ngữ nghĩa với OpenSearch. | 08/12/2026 | 08/12/2026 | [AWS Bedrock Guide](https://cloudjourney.awsfcaj.com/) |
| **Thứ 4** | **Xây dựng Trợ lý AI tự hành với Bedrock Agents & Action Groups:** <br>- Thiết lập Bedrock Agent với hướng dẫn chỉ dẫn chi tiết (Agent Instructions). <br>- Định nghĩa OpenAPI Schema và nhóm hành động (Action Groups) kết nối hàm AWS Lambda. <br>- Kiểm thử kịch bản hỏi đáp tự động truy xuất dữ liệu từ cơ sở dữ liệu RDS và trả lời người dùng. | 09/12/2026 | 09/12/2026 | [AWS Bedrock Agents](https://cloudjourney.awsfcaj.com/) |
| **Thứ 5** | **Huấn luyện và Triển khai mô hình Học máy với Amazon SageMaker:** <br>- Làm quen với giao diện Amazon SageMaker Studio và SageMaker Canvas (No-code ML). <br>- Triển khai các mô hình mã nguồn mở dựng sẵn thông qua SageMaker JumpStart. <br>- Cấu hình máy chủ suy luận thời gian thực (Real-time Inference Endpoint) và Auto Scaling. | 10/12/2026 | 10/12/2026 | [Amazon SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 13, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Bedrock, Prompting, RAG, Bedrock Agents và SageMaker. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 13 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp API Bedrock vào sản phẩm Capstone Project để hỗ trợ người dùng tự động. | 11/12/2026 | 11/12/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 13:

#### 📌 Kết quả Thứ 2 (07/12/2026) - Làm chủ Amazon Bedrock API:
* **Tích hợp API phi máy chủ:** Kết nối ứng dụng thành công với Amazon Bedrock thông qua thư viện Boto3 client `bedrock-runtime`, thực hiện gọi mô hình Claude 3.5 Sonnet với tham số nhiệt độ `temperature = 0.2` giúp câu trả lời chính xác, mạch lạc và bám sát ngữ cảnh.
* **Tối ưu hóa ngân sách Token:** So sánh chi phí giữa các mô hình, lựa chọn chiến lược phối hợp linh hoạt: sử dụng mô hình nhẹ Titan Text cho các tác vụ tóm tắt đơn giản và Claude 3.5 Sonnet cho các tác vụ suy luận phân tích logic phức tạp.

#### 📌 Kết quả Thứ 3 (08/12/2026) - Triển khai RAG với Bedrock Knowledge Bases:
* **Ngăn chặn hiện tượng ảo giác (Hallucination):** Tích hợp thành công kho tài liệu chính sách nội bộ vào Bedrock Knowledge Base. Khi người dùng đặt câu hỏi, mô hình tự động trích xuất các đoạn văn bản liên quan nhất làm ngữ cảnh tham chiếu, giúp câu trả lời đạt độ chính xác 100% kèm trích dẫn nguồn cụ thể.
* **Tự động hóa chuyển đổi véc-tơ:** Toàn bộ chu trình chunking tài liệu, tính toán vector embeddings và đánh chỉ mục trên Amazon OpenSearch Serverless được AWS quản lý tự động mà không cần can thiệp hạ tầng máy chủ.

#### 📌 Kết quả Thứ 4 (09/12/2026) - Trợ lý thông minh Bedrock Agents:
* **Khả năng tự hành thực thi tác vụ:** Khởi tạo thành công Agent có khả năng nhận yêu cầu từ người dùng bằng ngôn ngữ tự nhiên, tự động suy luận các bước thực hiện và gọi hàm AWS Lambda để truy vấn trực tiếp bảng dữ liệu kiểm tra trạng thái dịch vụ.
* **Xử lý hội thoại đa vòng (Multi-turn Conversation):** Quản lý trạng thái phiên làm việc (Session State) tự nhiên, duy trì mạch ngữ cảnh thông suốt mà không cần lưu trữ trạng thái thủ công trên máy chủ ứng dụng.

#### 📌 Kết quả Thứ 5 (10/12/2026) - Khám phá Amazon SageMaker:
* **Triển khai mô hình nhanh chóng:** Triển khai thử nghiệm mô hình phân loại văn bản mã nguồn mở thông qua giao diện SageMaker JumpStart chỉ với 1 cú nhấp chuột lên máy chủ `ml.m5.large`.
* **Sẵn sàng cho môi trường sản xuất:** Thiết lập điểm cuối suy luận có độ trễ dưới 50ms, tích hợp chính sách co giãn theo số lượng yêu cầu xử lý trên giây (InvocationsPerInstance).
