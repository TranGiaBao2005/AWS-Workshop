---
title: "Tuần 11"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 11:

- Thiết kế **Hồ dữ liệu hiện đại (Modern Data Lake)** trên Amazon S3 với phân quyền tập trung **AWS Lake Formation** (Workshop 000035) và chu trình ETL phi máy chủ **AWS Glue** chuyển đổi sang định dạng cột Apache Parquet.
- Thực thi truy vấn phân tích tối ưu chi phí với **Amazon Athena** (Workshop 000106), tiếp cận xử lý luồng **Amazon Kinesis**, trực quan hóa BI với **Amazon QuickSight** (Workshop 000073) và kiến trúc kho dữ liệu **Amazon Redshift**.
- Làm chủ hệ sinh thái **Trí tuệ nhân tạo tạo sinh (Generative AI)** trên AWS với **Amazon Bedrock** (Foundation Models, Boto3 Runtime API, Prompt Engineering, RAG Knowledge Bases & Bedrock Agents) và khám phá MLOps với **Amazon SageMaker**.
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện Worklog, kiểm toán dọn dẹp tài nguyên AI/Data và tích hợp phân tích + GenAI vào **Capstone Project**.

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Hồ dữ liệu (AWS Lake Formation) & Chu trình ETL phi máy chủ (AWS Glue):** <br>- Quy hoạch phân vùng S3 Data Lake (Raw, Processed, Curated) và phân quyền chi tiết hàng/cột trên Lake Formation. <br>- Chạy Glue Crawler suy diễn Schema vào Glue Data Catalog. <br>- Xây dựng Glue Studio ETL chuyển đổi CSV/JSON sang Apache Parquet nén Snappy có phân vùng theo ngày (`year/month/day`). | 23/11/2026 | 23/11/2026 | [Data Lake (000035)](https://000035.awsfcaj.com/) & [Data Analytics](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Thứ 3** | **Truy vấn Amazon Athena, Luồng Kinesis, QuickSight BI & Amazon Redshift:** <br>- Thiết lập Athena Workgroups, đối chiếu chi phí Data Scanned giữa CSV thô và Parquet phân vùng. <br>- Tìm hiểu kiến trúc thu thập luồng thời gian thực Amazon Kinesis Data Streams / Firehose. <br>- Kết nối Amazon QuickSight (SPICE) xây dựng Dashboard KPI và nghiên cứu kiến trúc MPP của Redshift. | 24/11/2026 | 24/11/2026 | [Athena (000106)](https://000106.awsfcaj.com/) & [QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Thứ 4** | **Amazon Bedrock Foundation Models, Prompt Engineering & Kiến trúc RAG:** <br>- Khảo sát Foundation Models (Claude, Amazon Titan, Llama) và lập trình gọi API qua Python Boto3 `bedrock-runtime`. <br>- Áp dụng System Prompts, Few-shot, Chain-of-Thought và JSON Schema Enforcement. <br>- Thiết kế RAG với Bedrock Knowledge Bases, Titan Embeddings và cơ sở dữ liệu véc-tơ OpenSearch Serverless. | 25/11/2026 | 25/11/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Thứ 5** | **Trợ lý tự hành Bedrock Agents & Chu trình MLOps với Amazon SageMaker:** <br>- Định nghĩa OpenAPI 3.0 Schema và Action Groups kết nối Bedrock Agent với AWS Lambda (ReAct loop + Guardrails). <br>- Khám phá Amazon SageMaker Studio, JumpStart và triển khai Real-time Inference Endpoint kèm Auto Scaling. <br>- Kiểm soát chặt chi phí GPU/CPU Endpoints và quy trình tắt endpoint ngay sau khi kiểm thử. | 26/11/2026 | 26/11/2026 | [Amazon Bedrock & SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 11, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa chuỗi xử lý Data Analytics và kiến trúc Generative AI trên AWS. <br>- **Làm Worklog:** Chuẩn hóa báo cáo Worklog Tuần 11 song ngữ và kiểm toán xóa OpenSearch/SageMaker thử nghiệm. <br>- **Làm Project:** Tích hợp luồng phân tích log/dữ liệu và trợ lý AI vào kiến trúc Capstone Project. | 27/11/2026 | 27/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (23/11/2026) - Quản trị Hồ dữ liệu AWS Lake Formation & ETL với AWS Glue

* **Ta học được những gì hôm nay?**
  * **Kiến trúc Hồ dữ liệu 3 tầng & Phân quyền cấp ô (Cell-level Security):** Chia vùng S3 thành *Raw Zone* (dữ liệu gốc), *Processed Zone* (đã làm sạch, định dạng Parquet) và *Curated Zone* (sẵn sàng cho BI/ML). Sử dụng AWS Lake Formation quản trị phân quyền tập trung theo cột (ẩn PII) và theo hàng (lọc theo khu vực địa lý).
  * **Chu trình ETL phi máy chủ với AWS Glue:** Dùng Glue Crawler suy diễn bảng vào Glue Data Catalog, sau đó chạy Glue Studio ETL chuyển đổi CSV sang **Apache Parquet** nén **Snappy** kèm phân vùng `year=YYYY/month=MM/day=DD` giúp giảm đáng kể dung lượng lưu trữ.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Xung đột phân quyền `IAMAllowedPrincipals` & sai kiểu ngày tháng:* Gỡ bỏ nhóm mặc định `IAMAllowedPrincipals` khỏi Glue Catalog để áp dụng quyền Lake Formation triệt để; dùng hàm `to_date()` trong PySpark ép chuẩn `yyyy-MM-dd` trước khi xuất Parquet.

---

#### 📌 Thứ 3 (24/11/2026) - Truy vấn Amazon Athena, Kinesis, QuickSight & Redshift

* **Ta học được những gì hôm nay?**
  * **Tối ưu FinOps khi truy vấn với Amazon Athena:** Chuyển từ bảng CSV thô sang Parquet có phân vùng giúp cắt giảm trên 90% dung lượng dữ liệu quét (Data Scanned), đồng nghĩa giảm tương ứng chi phí truy vấn ($5/TB) và tăng tốc phản hồi SQL.
  * **Dữ liệu luồng, BI & Data Warehouse:** Nắm rõ vai trò **Kinesis Data Streams/Firehose** cho dữ liệu thời gian thực; kết nối **Amazon QuickSight** với bộ nhớ đệm **SPICE** để vẽ biểu đồ KPI mà không gọi lại Athena liên tục; tìm hiểu kiến trúc xử lý song song MPP và Distribution Styles (`AUTO`, `KEY`, `EVEN`, `ALL`) của **Amazon Redshift**.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Athena không thấy phân vùng mới & QuickSight bị `Access Denied` vào S3:* Chạy `MSCK REPAIR TABLE` (hoặc bật Partition Projection) để nạp partition mới; cấp quyền đọc S3 Data Lake & Athena Output Bucket trong phần `Manage QuickSight -> Security & permissions`.

---

#### 📌 Thứ 4 (25/11/2026) - Amazon Bedrock Foundation Models & Kiến trúc RAG

* **Ta học được những gì hôm nay?**
  * **Tích hợp Foundation Models qua Bedrock Runtime API:** Điều chỉnh tham số sinh văn bản (`temperature`, `top_p`, `max_tokens`) và gọi mô hình thông qua Python Boto3 SDK mà không cần quản trị hạ tầng GPU:
    ```python
    import json, boto3
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": "Phân tích 3 ưu điểm bảo mật của AWS KMS."}]
    }
    resp = bedrock.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body=json.dumps(payload)
    )
    ```
  * **Prompt Engineering & RAG với Bedrock Knowledge Bases:** Kết hợp System Prompts, Few-shot, Chain-of-Thought với kiến trúc RAG (tài liệu S3 ➔ Titan Text Embeddings v2 ➔ OpenSearch Serverless Vector Store) giúp câu trả lời bám sát nguồn tài liệu kèm trích dẫn (Citations), hạn chế ảo giác (Hallucination).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi `Model access not granted` & OpenSearch thiếu Data Access Policy:* Kích hoạt quyền sử dụng model trong mục `Model access` trên Bedrock Console và bổ sung IAM Role của Knowledge Base vào Data Access Policy của OpenSearch Serverless.

---

#### 📌 Thứ 5 (26/11/2026) - Bedrock Agents & Chu trình MLOps với Amazon SageMaker

* **Ta học được những gì hôm nay?**
  * **Tác tử tự hành với Amazon Bedrock Agents:** Vận dụng chu trình suy luận ReAct (Reasoning + Acting) kết hợp OpenAPI 3.0 Schema và **Action Groups** gọi AWS Lambda truy vấn dữ liệu động, bảo vệ bằng **Bedrock Guardrails** chống Prompt Injection và rò rỉ dữ liệu nhạy cảm (liên hệ trực tiếp kiến trúc học tại Sự kiện AgentCore Deep-Dive).
  * **Chu trình MLOps với Amazon SageMaker:** Khám phá quy trình từ Data Wrangler ➔ SageMaker Studio ➔ JumpStart (triển khai nhanh mô hình dựng sẵn) ➔ Real-time Inference Endpoints kèm Target Tracking Auto Scaling theo chỉ số `InvocationsPerInstance`.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Agent không gọi được Lambda & hạn mức GPU mặc định bằng 0:* Chạy `aws lambda add-permission` cho principal `bedrock.amazonaws.com` để cấp quyền `lambda:InvokeFunction`; sử dụng dòng CPU `ml.m5.large` cho bài kiểm thử hoặc gửi yêu cầu tăng Service Quotas khi cần GPU.

---

#### 📌 Thứ 6 (27/11/2026) - Tổng kết Tuần 11, Viết Worklog & Tích hợp Đồ án

* **Ta học được những gì hôm nay?**
  * **Liên kết chuỗi giá trị Data & AI trên AWS:** Nắm vững luồng dữ liệu hoàn chỉnh từ Data Lake (Lake Formation/Glue/Athena/QuickSight) tới tầng ứng dụng trí tuệ nhân tạo (Bedrock RAG, Bedrock Agents, SageMaker).
  * **Kiểm soát chi phí FinOps cho tài nguyên AI:** Xóa sạch các OpenSearch Serverless Collections và SageMaker Endpoints ngay sau khi thử nghiệm xong để tránh phí duy trì OCU/giờ rất cao.
  * **Chuẩn bị cho Tuần 12 (Bảo vệ Đồ án):** Hoàn tất tích hợp các thành phần kiến trúc trọng tâm, chốt phạm vi demo và chuẩn bị bước vào tuần tổng kết cuối kỳ.

---

### Mục tiêu cho tuần sau (Tuần 12 - Tuần cuối kỳ thực tập):

* **Đóng gói hồ sơ & Xuất bản mã nguồn:** Rà soát toàn bộ 11 tuần Worklog, Proposal, Blogs, Events và mã nguồn trên GitHub.
* **Thuyết trình & Bảo vệ Capstone Project:** Thiết kế Slide, diễn tập Demo trực tiếp và bảo vệ trước Hội đồng Mentor FCAJ.
* **Dọn dẹp tài nguyên ($0 Audit) & Tổng kết thực tập:** Thực hiện Cloud Teardown theo chiều phụ thuộc, hoàn tất Tự đánh giá (`6-Self-evaluation`) và tiếp thu phản hồi Mentor.
