---
title: "Bản đề xuất"
date: 2026-10-02
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# IoT Weather Platform for Lab Research
## Giải pháp AWS Serverless hợp nhất cho giám sát thời tiết thời gian thực

### 1. Tóm tắt điều hành
Nền tảng **IoT Weather Platform** được thiết kế nhằm tự động hóa việc thu thập, lưu trữ và phân tích dữ liệu thời tiết theo thời gian thực. Hệ thống hỗ trợ từ 5 trạm quan trắc ban đầu và có khả năng mở rộng lên 10–15 trạm, sử dụng thiết bị biên Raspberry Pi kết hợp vi điều khiển ESP32 truyền dữ liệu cảm biến qua giao thức MQTT. Toàn bộ tầng xử lý và lưu trữ trên đám mây vận hành theo kiến trúc **AWS Serverless** để tối ưu chi phí, giảm công sức vận hành thủ công và kiểm soát truy cập tập trung cho 5 thành viên nhóm nghiên cứu thông qua **Amazon Cognito**.

---

### 2. Tuyên bố vấn đề

#### Vấn đề hiện tại
Các trạm thời tiết đơn lẻ hiện yêu cầu thu thập dữ liệu thủ công, khó đồng bộ khi tăng số lượng trạm. Việc thiếu một kho dữ liệu tập trung khiến nhóm nghiên cứu không thể theo dõi chỉ số theo thời gian thực hoặc chuẩn bị tập dữ liệu sạch cho các bài toán phân tích, trong khi các nền tảng IoT thương mại của bên thứ ba lại có chi phí duy trì cao và dư thừa tính năng so với quy mô phòng lab.

#### Giải pháp đề xuất
Xây dựng đường ống dữ liệu tự động hoàn toàn trên AWS:
- **Tiếp nhận dữ liệu:** **AWS IoT Core** nhận bản tin MQTT từ các trạm biên Raspberry Pi.
- **Xử lý & Lưu trữ:** **AWS Lambda** và **Amazon API Gateway** xử lý luồng sự kiện; **Amazon S3** lưu trữ tách biệt vùng dữ liệu thô (Raw Data Lake) và vùng dữ liệu đã chuẩn hóa (Processed Bucket).
- **Danh mục & ETL:** **AWS Glue Crawlers** lập chỉ mục schema và **AWS Glue ETL Jobs** làm sạch, chuyển đổi dữ liệu phục vụ phân tích.
- **Giao diện & Bảo mật:** **AWS Amplify** triển khai ứng dụng giao diện **Next.js**, kết hợp **Amazon Cognito** xác thực và giới hạn quyền truy cập cho thành viên nội bộ.

#### Lợi ích và hoàn vốn đầu tư (ROI)
Giải pháp loại bỏ thao tác chép dữ liệu thủ công ở từng trạm, đồng thời tạo ra tập dữ liệu lịch sử đồng nhất phục vụ huấn luyện mô hình học máy. Chi phí vận hành đám mây ước tính chỉ khoảng **0,70 USD/tháng** (**8,40 USD/năm** theo AWS Pricing Calculator), tận dụng lại phần cứng cảm biến sẵn có tại phòng lab nên đạt điểm hòa vốn trong vòng 6–12 tháng vận hành.

---

### 3. Kiến trúc giải pháp

Hệ thống sử dụng kiến trúc phi máy chủ (Serverless) kết nối từ tầng thiết bị biên Raspberry Pi lên AWS Cloud:

![IoT Weather Station Architecture](/images/2-Proposal/edge_architecture.jpeg)

![IoT Weather Platform Architecture](/images/2-Proposal/platform_architecture.jpeg)

#### Dịch vụ AWS sử dụng
- **AWS IoT Core:** Tiếp nhận gói tin MQTT bảo mật bằng chứng chỉ X.509 từ 5 trạm biên (mở rộng tối đa 15 trạm).
- **AWS Lambda:** Xử lý bản tin đến, kiểm tra ngưỡng dữ liệu và kích hoạt tác vụ ETL (2 hàm).
- **Amazon API Gateway:** Cung cấp REST/HTTP endpoints cho giao diện web truy xuất dữ liệu.
- **Amazon S3:** Lưu trữ dữ liệu thô (Data Lake) và dữ liệu đã qua xử lý (2 S3 Buckets).
- **AWS Glue:** Glue Crawler tự động cập nhật Data Catalog; Glue ETL Job chuẩn hóa dữ liệu định kỳ.
- **AWS Amplify:** Lưu trữ và tự động triển khai (CI/CD) giao diện điều khiển viết bằng Next.js.
- **Amazon Cognito:** Quản lý định danh và cấp phát JWT token cho tối đa 5 tài khoản nghiên cứu viên.

#### Thiết kế thành phần
- **Thiết bị biên (Edge Layer):** Cảm biến đo nhiệt độ, độ ẩm, lượng mưa, tốc độ gió kết nối ESP32; Raspberry Pi chạy Docker lọc nhiễu dữ liệu cục bộ trước khi đẩy qua MQTT (~1 MB/ngày/trạm).
- **Tầng tiếp nhận (Ingestion Layer):** AWS IoT Core Message Broker và IoT Rules định tuyến gói tin vào S3/Lambda.
- **Tầng lưu trữ & xử lý (Storage & ETL Layer):** S3 Raw Bucket lưu bản ghi gốc; Glue Crawler & ETL chuyển đổi dữ liệu sạch sang S3 Processed Bucket.
- **Tầng trình diễn & xác thực (Presentation & Auth Layer):** Next.js trên AWS Amplify hiển thị biểu đồ thời gian thực, bảo vệ bởi Amazon Cognito User Pool.

---

### 4. Triển khai kỹ thuật

#### Các giai đoạn triển khai
1. **Giai đoạn 1 – Thiết kế kiến trúc & Chuẩn hóa thiết bị biên:** Kiểm tra kết nối ESP32 – Raspberry Pi, đóng gói dịch vụ thu thập dữ liệu bằng Docker và hoàn thiện sơ đồ kiến trúc AWS Serverless.
2. **Giai đoạn 2 – Ước tính chi phí & Kiểm chứng khả thi:** Lập bảng dự toán chi tiết trên AWS Pricing Calculator, thiết lập AWS Budgets cảnh báo chi phí.
3. **Giai đoạn 3 – Tối ưu hóa kiến trúc:** Tận dụng khả năng xử lý phía server của Next.js trên Amplify để giảm số lượt gọi hàm Lambda không cần thiết và gộp chu kỳ chạy Glue ETL.
4. **Giai đoạn 4 – Phát triển, Kiểm thử & Vận hành:** Triển khai hạ tầng bằng AWS CDK/SDK, kết nối 5 trạm biên lên AWS IoT Core, kiểm thử luồng ETL và nghiệm thu dashboard.

---

### 5. Lộ trình & Mốc triển khai

- **Chuẩn bị trước thực tập:** Rà soát phần cứng trạm thời tiết cũ và xác định yêu cầu dữ liệu của phòng lab.
- **Tháng 1 (Tuần 1 – Tuần 4):** Nắm vững hạ tầng mạng, bảo mật IAM, lưu trữ S3, giám sát CloudWatch và chuẩn bị môi trường thiết bị biên.
- **Tháng 2 (Tuần 5 – Tuần 8):** Thiết lập cơ sở dữ liệu, tự động hóa bằng AWS CLI/Lambda/IaC và xây dựng luồng tiếp nhận IoT Core ➔ S3.
- **Tháng 3 (Tuần 9 – Tuần 12):** Tích hợp Glue ETL, hoàn thiện giao diện Next.js trên AWS Amplify + Cognito, kiểm thử toàn trình và bảo vệ đồ án.

---

### 6. Ước tính ngân sách

Chi tiết bảng tính chi phí trên **[AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01)**:

| Hạng mục dịch vụ | Cấu hình ước tính | Chi phí / tháng (USD) |
| :--- | :--- | :---: |
| **AWS Lambda** | ~1.000 requests/tháng, 512 MB bộ nhớ tạm (nằm trong Free Tier) | $0.00 |
| **Amazon S3 Standard** | ~6 GB lưu trữ, 2.100 PUT/GET requests, 1 GB dữ liệu quét | $0.15 |
| **Data Transfer** | 1 GB Inbound, 1 GB Outbound | $0.02 |
| **AWS Amplify** | Hosting Next.js (256 MB RAM, thời gian phản hồi ~500 ms) | $0.35 |
| **Amazon API Gateway** | ~2.000 HTTP API requests/tháng | $0.01 |
| **AWS Glue ETL Jobs** | 2 DPUs chạy theo lịch gộp định kỳ | $0.02 |
| **AWS Glue Crawlers** | 1 Crawler cập nhật danh mục bảng | $0.07 |
| **AWS IoT Core (MQTT)** | 5 thiết bị biên, ~45.000 bản tin MQTT/tháng | $0.08 |
| **Tổng chi phí Cloud** | **Ước tính hàng tháng / cả năm (12 tháng)** | **$0.70 / tháng ($8.40 / năm)** |

*(Chi phí phần cứng ban đầu cho bộ Raspberry Pi 5 và cụm cảm biến khoảng $265 trả một lần, tận dụng thiết bị sẵn có của phòng lab).*

---

### 7. Đánh giá rủi ro & Phương án giảm thiểu

| Rủi ro | Mức độ ảnh hưởng | Xác suất | Giải pháp giảm thiểu & Dự phòng |
| :--- | :---: | :---: | :--- |
| **Gián đoạn kết nối mạng Wi-Fi tại trạm biên** | Trung bình | Trung bình | Bộ chứa Docker trên Raspberry Pi lưu đệm (buffer) dữ liệu cục bộ và tự động gửi bù khi có mạng trở lại. |
| **Hỏng hoặc sai lệch chỉ số cảm biến** | Cao | Thấp | Bổ sung bước kiểm tra ngưỡng hợp lệ (sanity check) tại Lambda/Edge và dự phòng sẵn linh kiện cảm biến thay thế. |
| **Phát sinh chi phí AWS vượt dự toán** | Trung bình | Thấp | Cấu hình AWS Budgets cảnh báo ở ngưỡng 80% & 100%, giới hạn tần suất chạy Glue Crawler/ETL và dọn dẹp tài nguyên bằng IaC. |

---

### 8. Kết quả kỳ vọng

- **Hiệu quả kỹ thuật:** Tự động hóa 100% chu trình thu thập – làm sạch – hiển thị dữ liệu thời tiết từ 5 trạm biên với độ trễ thấp, sẵn sàng mở rộng lên 10–15 trạm mà không cần thay đổi kiến trúc.
- **Giá trị sử dụng lâu dài:** Xây dựng kho dữ liệu thời tiết chuẩn hóa trên Amazon S3 phục vụ các đề tài nghiên cứu học máy và phân tích môi trường trong các học kỳ tiếp theo.
