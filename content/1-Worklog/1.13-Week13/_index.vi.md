---
title: "Tuần 13"
date: 2026-12-07
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 13:

- Tiếp cận toàn diện hệ sinh thái **Trí tuệ nhân tạo tạo sinh (Generative AI)** trên AWS thông qua dịch vụ nền tảng được quản lý hoàn toàn **Amazon Bedrock**.
- Dành **2 ngày chuyên sâu (Thứ 2 & Thứ 3)** làm chủ từ lập trình gọi mô hình nền tảng (**Foundation Models**) qua SDK đến kỹ thuật kiến tạo câu lệnh chuyên nghiệp (**Prompt Engineering**) và xây dựng kiến trúc tìm kiếm tăng cường truy xuất **RAG (Retrieval-Augmented Generation)** với cơ sở dữ liệu véc-tơ Amazon OpenSearch Serverless.
- Xây dựng và triển khai tác nhân AI tự hành (**Amazon Bedrock Agents**) có khả năng phân tích ý định, chia nhỏ bài toán và gọi hàm AWS Lambda (**Action Groups**) để truy vấn dữ liệu kinh doanh thực tế.
- Khám phá chu trình phát triển học máy toàn diện (**MLOps**) với **Amazon SageMaker** (SageMaker Studio, JumpStart và Real-time Inference Endpoints).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và tích hợp tính năng Trợ lý AI thông minh vào đồ án thực tập (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **GenAI (Phần 1) - Khám phá Foundation Models & Bedrock Runtime API:** <br>- Đăng ký quyền truy cập mô hình (Claude 3.5 Sonnet, Amazon Titan, Meta Llama 3). <br>- Kiểm thử trên Bedrock Playground: Điều chỉnh tham số `temperature`, `top_p`, `max_tokens`. <br>- Lập trình gọi mô hình tạo sinh qua Python Boto3 SDK (`bedrock-runtime`). <br>- Phân tích độ trễ phản hồi (Inference Latency) và chiến lược tối ưu ngân sách Token. | 07/12/2026 | 07/12/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Thứ 3** | **GenAI (Phần 2) - Prompt Engineering & RAG với Bedrock Knowledge Bases:** <br>- Làm chủ kỹ thuật Prompt: System Prompts, Few-shot Examples, Chain-of-Thought, JSON Schema. <br>- Khởi tạo Bedrock Knowledge Base liên kết kho tài liệu chính sách trên S3. <br>- Cấu hình mô hình nhúng Titan Embeddings và cơ sở dữ liệu véc-tơ OpenSearch Serverless. <br>- Kiểm thử truy vấn Semantic Search loại bỏ hoàn toàn hiện tượng ảo giác (Hallucination). | 08/12/2026 | 08/12/2026 | [AWS Bedrock Guide](https://cloudjourney.awsfcaj.com/) |
| **Thứ 4** | **Xây dựng Trợ lý AI tự hành với Bedrock Agents & Action Groups:** <br>- Thiết lập Bedrock Agent với hướng dẫn chỉ dẫn chi tiết (Agent Persona & Instructions). <br>- Định nghĩa OpenAPI 3.0 Schema và nhóm hành động (Action Groups) kết nối hàm AWS Lambda. <br>- Kiểm thử kịch bản tự động truy xuất trạng thái đơn hàng từ CSDL RDS và phản hồi người dùng. <br>- Quản lý phiên hội thoại đa vòng (Multi-turn Conversation State). | 09/12/2026 | 09/12/2026 | [AWS Bedrock Agents](https://cloudjourney.awsfcaj.com/) |
| **Thứ 5** | **Huấn luyện và Triển khai mô hình Học máy với Amazon SageMaker:** <br>- Khám phá môi trường phát triển SageMaker Studio và SageMaker Canvas (No-code ML). <br>- Triển khai các mô hình mã nguồn mở dựng sẵn thông qua SageMaker JumpStart. <br>- Cấu hình máy chủ suy luận thời gian thực (Real-time Endpoint) trên dòng máy `ml.m5.large`. <br>- Thiết lập chính sách tự động co giãn Endpoint theo số lượng request xử lý. | 10/12/2026 | 10/12/2026 | [Amazon SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 13, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Bedrock, Prompting, RAG, Bedrock Agents và SageMaker. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 13 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp API Bedrock vào sản phẩm Capstone Project để hỗ trợ người dùng tự động. | 11/12/2026 | 11/12/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (07/12/2026) - GenAI (Phần 1): Khám phá Foundation Models & Bedrock Runtime API

* **Ta học được những gì hôm nay?**
  * **Hệ sinh thái mô hình nền tảng trên Amazon Bedrock:** Tìm hiểu cách Bedrock cung cấp quyền truy cập thống nhất (Unified API) tới các mô hình hàng đầu mà không cần quản lý cụm GPU phức tạp:
    * *Anthropic Claude 3.5 Sonnet:* Mô hình mạnh mẽ nhất cho các tác vụ suy luận logic, phân tích mã nguồn và giải quyết bài toán phức tạp.
    * *Amazon Titan Text:* Mô hình nhẹ, độ trễ thấp và chi phí siêu tiết kiệm cho các tác vụ tóm tắt, trích xuất thực thể.
    * *Meta Llama 3:* Mô hình mã nguồn mở linh hoạt và đa năng.
  * **Khảo nghiệm các tham số điều khiển trên Playground:**
    * `Temperature (0.0 - 1.0)`: Đặt `0.2` cho các tác vụ kỹ thuật cần câu trả lời chính xác, mang tính quyết định; đặt `0.8` cho các tác vụ sáng tạo nội dung.
    * `Top P (0.0 - 1.0)`: Lựa chọn phân bố xác suất từ vựng, giúp kiểm soát độ đa dạng ngữ nghĩa.
    * `Max Tokens`: Giới hạn độ dài đầu ra để ngăn chặn phản hồi dài dòng lãng phí chi phí.
  * **Lập trình tích hợp qua Python Boto3 SDK:**
    ```python
    import json
    import boto3

    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    prompt_payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.2,
        "messages": [
            {"role": "user", "content": "Phân tích 3 ưu điểm bảo mật của AWS KMS."}
        ]
    }
    response = bedrock.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(prompt_payload)
    )
    response_body = json.loads(response.get("body").read())
    print(response_body["content"][0]["text"])
    ```
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi từ chối quyền truy cập mô hình (`AccessDeniedException`):* Gọi API báo `Model access not granted`. Nguyên nhân: Mặc định tài khoản AWS mới chưa được kích hoạt quyền truy cập các mô hình bên thứ ba. Cách xử lý: Truy cập vào mục `Model access` trên Amazon Bedrock Console, gửi yêu cầu kích hoạt (Request model access) cho Claude 3.5 Sonnet và chờ được phê duyệt trong vài phút.

---

#### 📌 Thứ 3 (08/12/2026) - GenAI (Phần 2): Prompt Engineering & Kiến trúc RAG

* **Ta học được những gì hôm nay?**
  * **Nâng tầm kỹ thuật Prompt Engineering:**
    * *System Prompts:* Định hình vai trò chuyên gia (`"Bạn là Kiến trúc sư giải pháp trưởng của AWS..."`), quy định giọng văn kỹ thuật, ngắn gọn và trung thực.
    * *Few-shot Examples:* Cung cấp 2-3 ví dụ mẫu chuẩn về định dạng đầu vào và đầu ra mong muốn.
    * *Chain-of-Thought:* Yêu cầu mô hình suy luận từng bước (`"Hãy suy nghĩ từng bước trước khi đưa ra kết luận"`) để tăng độ chính xác của logic toán học và thuật toán.
    * *JSON Schema Enforcement:* Ép mô hình trả về đúng định dạng JSON hợp lệ để hệ thống backend có thể `JSON.parse()` an toàn.
  * **Xây dựng giải pháp RAG với Bedrock Knowledge Bases:**
    1. Tải bộ tài liệu quy trình vận hành và tài liệu kỹ thuật của dự án (PDF/DOCX) lên S3 Bucket `fcaj-kb-docs-887086382708`.
    2. Khởi tạo Knowledge Base trên Bedrock, chọn mô hình nhúng `Amazon Titan Text Embeddings v2`.
    3. AWS tự động khởi tạo cơ sở dữ liệu véc-tơ không máy chủ **Amazon OpenSearch Serverless**, tự động cắt nhỏ văn bản (Chunking size: 300 tokens, 20% overlap) và lập chỉ mục véc-tơ ngữ nghĩa.
    4. Kiểm thử tính năng `RetrieveAndGenerate`: Khi người dùng đặt câu hỏi kỹ thuật, hệ thống tự động tìm kiếm các đoạn văn bản có độ tương đồng ngữ nghĩa cao nhất, đính kèm vào prompt gửi cho Claude 3.5 Sonnet làm ngữ cảnh (Context), giúp câu trả lời đạt độ chính xác 100% kèm trích dẫn nguồn văn bản (Citations), triệt tiêu hoàn toàn hiện tượng chém gió / bịa chuyện (Hallucination).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi OpenSearch Serverless thiếu Data Access Policy:* Quá trình tạo Knowledge Base bị lỗi `Cannot write to OpenSearch vector collection`. Cách xử lý: Kiểm tra và bổ sung IAM Role của Bedrock vào phần **Data Access Policy** của OpenSearch Serverless với đầy đủ quyền `aoss:CreateCollectionItems` và `aoss:DescribeCollectionItems`.

---

#### 📌 Thứ 4 (09/12/2026) - Trợ lý AI tự hành với Bedrock Agents & Action Groups

* **Ta học được những gì hôm nay?**
  * **Cơ chế suy luận tự hành của Bedrock Agents:** Hiểu rõ cách Agent sử dụng chu trình suy luận ReAct (Reasoning + Acting) để phân tích câu hỏi người dùng, tự xác định xem cần những thông tin gì, tự động gọi API phù hợp và tổng hợp kết quả trả lời.
  * **Xây dựng Action Group tích hợp AWS Lambda:**
    * Định nghĩa OpenAPI 3.0 Schema dạng YAML mô tả endpoint `/check-order-status` nhận tham số `orderId`.
    * Viết hàm Lambda Backend bằng Python nhận sự kiện từ Agent, truy vấn trực tiếp bảng Amazon DynamoDB hoặc Amazon RDS và trả về thông tin trạng thái đơn hàng.
    * Kết nối Action Group vào Bedrock Agent.
  * **Kiểm thử thực tế kịch bản hội thoại:** Khi người dùng nhắn: *"Kiểm tra giúp tôi đơn hàng #FCJ-9921 hiện đang ở đâu?"*, Agent tự động nhận diện ý định, trích xuất mã đơn hàng, gọi hàm Lambda và phản hồi tự nhiên: *"Đơn hàng #FCJ-9921 của bạn đã được xuất kho và đang trên đường vận chuyển, dự kiến giao vào ngày mai."*
* **Khó khăn gặp phải & Cách xử lý:**
  * *Agent không gọi được hàm Lambda:* Giao diện chat báo lỗi `Agent failed to invoke action group`. Nguyên nhân: Hàm Lambda thiếu quyền Resource-based Policy cho phép Bedrock gọi qua hành động `lambda:InvokeFunction`. Cách xử lý: Chạy lệnh `aws lambda add-permission --function-name MyAgentFunction --principal bedrock.amazonaws.com --action lambda:InvokeFunction`.

---

#### 📌 Thứ 5 (10/12/2026) - Chu trình MLOps với Amazon SageMaker

* **Ta học được những gì hôm nay?**
  * **Khám phá nền tảng Amazon SageMaker:** Tìm hiểu toàn bộ chu trình phát triển học máy từ Chuẩn bị dữ liệu (Data Wrangler) ➔ Xây dựng mô hình (SageMaker Studio) ➔ Huấn luyện mô hình (Training Jobs) ➔ Đóng gói và triển khai suy luận (Inference Endpoints).
  * **Trải nghiệm SageMaker JumpStart:** Truy cập kho thư viện mô hình mã nguồn mở dựng sẵn (Pre-trained Foundation Models). Triển khai thử nghiệm mô hình phân loại văn bản chỉ với 1 cú nhấp chuột lên máy chủ suy luận `ml.m5.large`.
  * **Cấu hình Real-time Inference Endpoint & Auto Scaling:**
    * Kiểm thử gửi dữ liệu JSON kiểm tra tốc độ phản hồi đạt độ trễ cực thấp (P95 latency < 45ms).
    * Thiết lập chính sách Target Tracking Auto Scaling theo dõi chỉ số `InvocationsPerInstance`, tự động nhân bản số lượng máy chủ suy luận khi số lượng request tăng vọt.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi hết hạn mức máy chủ suy luận (Insufficient Quota):* Khởi tạo máy chủ `ml.g5.2xlarge` báo lỗi `ResourceLimitExceeded`. Nguyên nhân: Tài khoản Free Tier mặc định có hạn mức GPU bằng 0. Cách xử lý: Chọn dòng máy chủ CPU `ml.m5.large` để thực hành kiểm thử chức năng hoặc gửi yêu cầu nâng Service Quotas trên AWS Support.

---

#### 📌 Thứ 6 (11/12/2026) - Tổng kết Tuần 13, Viết Worklog & Tích hợp GenAI vào Đồ án

* **Ta học được những gì hôm nay?**
  * **Hệ thống hóa năng lực Trí tuệ nhân tạo thế hệ mới trên AWS:** Làm chủ bộ công cụ từ mức tiêu thụ dịch vụ API phi máy chủ (Bedrock Runtime, Knowledge Bases, Agents) đến mức kiểm soát chuyên sâu hạ tầng học máy (SageMaker).
  * **Kiểm toán dọn dẹp tài nguyên AI an toàn:** Xóa bỏ ngay các máy chủ suy luận SageMaker Endpoint (`ml.m5.large`) sau khi kiểm thử xong để tránh bị tính phí tính toán liên tục theo giờ, xóa các bộ sưu tập OpenSearch Serverless thử nghiệm.
  * **Tích hợp Trợ lý AI vào Đồ án Capstone:** Hoàn thiện tích hợp API Bedrock vào giao diện Web của Đề xuất đồ án, mang đến tính năng Trợ lý thông minh hỗ trợ giải đáp chính sách và tư vấn đơn hàng tự động cho người dùng.

