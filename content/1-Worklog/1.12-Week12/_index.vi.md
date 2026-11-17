---
title: "Worklog Tuần 12"
date: 2026-11-30
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Mục tiêu tuần 12:

- Khám phá kiến trúc **Hồ dữ liệu hiện đại (Modern Data Lake Architecture)** trên Amazon S3 và thiết lập quản trị phân quyền dữ liệu tập trung với **AWS Lake Formation** (Workshop 000035).
- Tự động hóa quy trình trích xuất, chuyển đổi và nạp dữ liệu (ETL) phi máy chủ quy mô lớn với **AWS Glue** (Glue Crawlers, Data Catalog và PySpark Jobs), chuyển đổi dữ liệu thô sang định dạng cột tối ưu Apache Parquet.
- Thực thi các câu lệnh truy vấn SQL tương tác trực tiếp trên dữ liệu lớn bằng **Amazon Athena** (Workshop 000106) và tiếp cận xử lý luồng dữ liệu thời gian thực với **Amazon Kinesis Data Streams**.
- Xây dựng hệ thống báo cáo phân tích thông minh và bảng điều khiển trực quan (**Business Intelligence - BI**) với **Amazon QuickSight** (Workshop 000073) được tăng tốc bởi bộ nhớ đệm SPICE.
- Nghiên cứu kiến trúc kho dữ liệu đám mây quy mô Petabyte với **Amazon Redshift** (Massively Parallel Processing - MPP).
- Dành ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và xây dựng luồng phân tích dữ liệu chuyên sâu (Data Analytics Pipeline) cho đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Data Lake (Phần 1) - Quản trị Hồ dữ liệu với AWS Lake Formation:** <br>- Thiết lập các phân vùng hồ dữ liệu trên S3 (Raw Zone, Processed Zone, Curated Zone). <br>- Đăng ký S3 Data Lake Location và cấu hình quản trị phân quyền tập trung. <br>- Thiết lập kiểm soát truy cập chi tiết tới từng hàng và từng cột (Row/Column-level Security). <br>- Tối ưu hóa chi phí lưu trữ hồ dữ liệu với cơ chế phân vùng Chronological Partitioning. | 30/11/2026 | 30/11/2026 | [Data Lake Fundamentals (000035)](https://000035.awsfcaj.com/) |
| **Thứ 3** | **Data Lake (Phần 2) - Tự động hóa chu trình ETL phi máy chủ với AWS Glue:** <br>- Khởi chạy Glue Crawler tự động quét dữ liệu và tạo bảng trong AWS Glue Data Catalog. <br>- Xây dựng kịch bản Glue Studio Visual ETL làm sạch, chuẩn hóa và xử lý kiểu dữ liệu. <br>- Chuyển đổi định dạng tệp từ thô (CSV/JSON) sang định dạng cột Apache Parquet nén Snappy. <br>- Lập lịch kích hoạt ETL tự động dựa trên sự kiện có tệp mới tải lên S3 (Event-Driven ETL). | 01/12/2026 | 01/12/2026 | [Cloud Journey - Data](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Thứ 4** | **Truy vấn phân tán với Amazon Athena & Xử lý luồng Kinesis:** <br>- Thiết lập Athena Workgroups và cấu hình vị trí lưu trữ kết quả truy vấn trên S3. <br>- Viết các truy vấn phân tích SQL tổng hợp phức tạp tối ưu chi phí trên Parquet partitions. <br>- Tiếp cận cơ chế thu thập dữ liệu luồng thời gian thực với Amazon Kinesis Data Streams. <br>- Đánh giá hiệu năng và chi phí quét dữ liệu (Data Scanned) trên Athena. | 02/12/2026 | 02/12/2026 | [Amazon Athena Workshop (000106)](https://000106.awsfcaj.com/) |
| **Thứ 5** | **Báo cáo kinh doanh với Amazon QuickSight & Khám phá Redshift:** <br>- Kết nối Amazon QuickSight với nguồn dữ liệu Athena qua SPICE in-memory engine. <br>- Thiết kế các biểu đồ phân tích tương tác trực quan (KPIs, xu hướng thời gian, Heatmaps). <br>- Tìm hiểu kiến trúc xử lý song song khối lượng lớn (MPP) của kho dữ liệu Amazon Redshift. <br>- Phân tích bảng phân bổ dữ liệu (Distribution Styles) và Sort Keys trên Redshift. | 03/12/2026 | 03/12/2026 | [Amazon QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 12, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Data Lake, Glue, Athena, Kinesis, QuickSight và Redshift. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 12 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp Dashboard phân tích dữ liệu hiệu năng và chi phí vào Đề xuất đồ án (Proposal). | 04/12/2026 | 04/12/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Chi tiết nội dung học tập và kết quả đạt được mỗi ngày:

#### 📌 Thứ 2 (30/11/2026) - Data Lake (Phần 1): Quản trị Hồ dữ liệu với AWS Lake Formation

* **Ta học được những gì hôm nay?**
  * **Kiến trúc Hồ dữ liệu đa tầng (Multi-tier S3 Data Lake):**
    * *Raw Zone (Bronze):* Vùng chứa dữ liệu gốc nguyên trạng chưa qua xử lý được đẩy về từ các nguồn giao dịch (CSV, JSON logs).
    * *Processed Zone (Silver):* Dữ liệu đã được làm sạch, loại bỏ bản ghi trùng lặp và chuyển sang định dạng nén Parquet.
    * *Curated Zone (Gold):* Dữ liệu tổng hợp chất lượng cao sẵn sàng cho các báo cáo BI và mô hình học máy.
  * **Tập trung hóa bảo mật với AWS Lake Formation:** Thay thế các chính sách phân quyền rời rạc giữa S3 Bucket Policy và IAM Policy bằng một mặt bằng quản trị duy nhất (Unified Governance). Đăng ký S3 Data Lake Location và cấp quyền truy cập cơ sở dữ liệu dựa trên danh tính người dùng hoặc nhóm phân tích.
  * **Bảo vệ dữ liệu nhạy cảm cấp độ ô (Cell-level Security):**
    * *Column-level filtering:* Ẩn các cột nhạy cảm như số thẻ tín dụng, số điện thoại đối với nhóm Data Analyst thông thường.
    * *Row-level filtering:* Chỉ cho phép quản lý chi nhánh xem các dòng dữ liệu thuộc vùng địa lý của họ (`Region = 'APAC'`).
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi xung đột phân quyền kép (Lake Formation vs IAM Direct Access):* Người dùng đã bị thu hồi quyền trong Lake Formation nhưng vẫn đọc được tệp trực tiếp từ S3. Nguyên nhân: Mặc định nhóm IAM vẫn sở hữu quyền `s3:GetObject` trên bucket và cài đặt mặc định `IAMAllowedPrincipals` vẫn đang bật trong Data Catalog Settings. Cách xử lý: Xóa nhóm `IAMAllowedPrincipals` khỏi Data Catalog và chỉ định tuyến toàn bộ quyền truy cập thông qua Lake Formation Permissions.

---

#### 📌 Thứ 3 (01/12/2026) - Data Lake (Phần 2): Chu trình ETL phi máy chủ với AWS Glue

* **Ta học được những gì hôm nay?**
  * **Tự động suy diễn Schema với AWS Glue Crawler:** Cấu hình Crawler quét qua thư mục `s3://fcaj-datalake-raw/ecommerce/`, tự động nhận diện cấu trúc tệp CSV, định kiểu dữ liệu cho từng cột và tạo bảng `raw_orders` trong Glue Data Catalog chỉ trong vòng chưa đầy 60 giây.
  * **Xây dựng kịch bản ETL trực quan với AWS Glue Studio:**
    * Kéo thả các nút xử lý: Nguồn S3 Raw ➔ Ánh xạ kiểu dữ liệu (ApplyMapping) ➔ Lọc bản ghi rỗng (Filter Nulls) ➔ Đích S3 Processed.
    * Chuyển đổi định dạng tệp từ CSV sang **Apache Parquet** đi kèm thuật toán nén **Snappy**.
    * Kết quả đo lường: Tập dữ liệu 500MB CSV sau khi chuyển đổi chỉ còn 72MB Parquet (tiết kiệm 85% dung lượng lưu trữ).
  * **Cơ chế phân vùng tự động (Partitioning):** Cấu hình đường dẫn đầu ra phân vùng theo cấu trúc ngày tháng `year=YYYY/month=MM/day=DD`, giúp các công cụ truy vấn sau này chỉ quét đúng thư mục cần thiết thay vì duyệt toàn bộ dữ liệu.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi không khớp kiểu dữ liệu ngày tháng (Schema Mismatch):* Cột `order_date` trong CSV có định dạng `DD/MM/YYYY` bị Crawler suy diễn thành kiểu chuỗi `String` thay vì `Timestamp`, khiến các câu lệnh truy vấn thời gian bị sai. Cách xử lý: Trong Glue Studio, thêm bước `Custom Transform` sử dụng hàm `to_date()` của PySpark để ép kiểu về chuẩn `yyyy-MM-dd` trước khi lưu vào Parquet.

---

#### 📌 Thứ 4 (02/12/2026) - Truy vấn phân tán với Amazon Athena & Xử lý luồng Kinesis

* **Ta học được những gì hôm nay?**
  * **Truy vấn SQL phi máy chủ tương tác với Amazon Athena:** Khởi tạo Athena Workgroup, cấu hình thư mục lưu kết quả truy vấn tại `s3://fcaj-athena-query-results/`. Athena đọc trực tiếp siêu dữ liệu từ Glue Data Catalog, cho phép thực thi các câu lệnh SQL ANSI chuẩn trên hàng triệu dòng dữ liệu lưu trữ tại S3.
  * **Tối ưu hóa kinh tế FinOps trên Athena:**
    * So sánh hiệu quả truy vấn: Cùng một câu lệnh tính tổng doanh thu theo tháng:
      * Trên bảng CSV chưa phân vùng: Quét **500MB** dữ liệu, thời gian thực thi **4.8 giây**.
      * Trên bảng Parquet đã phân vùng: Quét vỏn vẹn **6.2MB** dữ liệu, thời gian thực thi **0.8 giây**.
    * Lượng dữ liệu quét giảm hơn **98%**, đồng nghĩa với việc chi phí truy vấn giảm tương ứng 98% (Athena tính phí $5.00 trên mỗi TB dữ liệu quét).
  * **Tiếp cận xử lý luồng với Amazon Kinesis Data Streams:** Tìm hiểu kiến trúc Shard-based của Kinesis, cơ chế đưa dữ liệu thời gian thực (Real-time Clickstream Logs) vào Kinesis Data Firehose để tự động gom cụm và ghi thành các tệp nén trên S3.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi Athena không nhận ra các phân vùng mới tạo:* Sau khi Glue Job nạp thêm thư mục `day=02`, câu lệnh `SELECT *` trên Athena không trả về dữ liệu ngày mới. Nguyên nhân: Bảng chưa được cập nhật siêu dữ liệu phân vùng. Cách xử lý: Chạy câu lệnh `MSCK REPAIR TABLE orders_parquet;` hoặc kích hoạt tính năng **Partition Projection** trong cấu hình bảng của Glue Catalog.

---

#### 📌 Thứ 5 (03/12/2026) - Trực quan hóa dữ liệu với Amazon QuickSight & Khám phá Redshift

* **Ta học được những gì hôm nay?**
  * **Trực quan hóa dữ liệu với Amazon QuickSight:**
    * Kết nối QuickSight với nguồn dữ liệu Amazon Athena.
    * Nạp dữ liệu vào công cụ tính toán trong bộ nhớ siêu nhanh **SPICE (Super-fast, Parallel, In-memory Calculation Engine)**, giúp tăng tốc độ phản hồi đồ thị khi người dùng tương tác lọc dữ liệu mà không tốn thêm chi phí truy vấn Athena.
    * Xây dựng một Dashboard kinh doanh hoàn chỉnh: Biểu đồ KPI Tổng doanh thu, đồ thị đường xu hướng đơn hàng theo tuần, biểu đồ tròn cơ cấu ngành hàng và bản đồ phân bố đơn hàng theo vị trí địa lý.
  * **Kiến trúc kho dữ liệu đám mây Amazon Redshift:**
    * Tìm hiểu kiến trúc xử lý song song khối lượng lớn (Massively Parallel Processing - MPP) và lưu trữ dạng cột (Columnar Storage) của Redshift.
    * Phân tích các kiểu phân bổ dữ liệu (Distribution Styles: `AUTO`, `EVEN`, `KEY`, `ALL`) nhằm giảm thiểu việc di chuyển dữ liệu giữa các node tính toán (Data Shuffling) khi thực hiện các phép JOIN phức tạp.
* **Khó khăn gặp phải & Cách xử lý:**
  * *Lỗi QuickSight không có quyền truy cập S3 Bucket:* Khi nạp dữ liệu từ Athena vào QuickSight báo lỗi `Access Denied to S3 bucket`. Nguyên nhân: QuickSight chạy trên một IAM Role hệ thống riêng của dịch vụ. Cách xử lý: Vào mục `Manage QuickSight` ➔ `Security & permissions` ➔ Đánh dấu chọn cấp quyền đọc cho đúng S3 Data Lake Bucket và S3 Athena Output Bucket.

---

#### 📌 Thứ 6 (04/12/2026) - Tổng kết Tuần 12, Viết Worklog & Xây dựng Analytics cho Đồ án

* **Ta học được những gì hôm nay?**
  * **Bức tranh tổng thể về Data Analytics trên AWS:** Kết nối hoàn chỉnh chuỗi giá trị dữ liệu từ Thu thập (Kinesis/S3) ➔ Quản trị bảo mật (Lake Formation) ➔ Xử lý chuyển đổi (Glue ETL) ➔ Truy vấn phân tích (Athena) ➔ Trực quan hóa ra quyết định (QuickSight).
  * **Dọn dẹp tài nguyên:** Hủy các bảng test trong Glue Catalog, xóa dữ liệu tạm trên S3 và hủy tài nguyên SPICE không dùng để tránh phát sinh chi phí duy trì hàng tháng.
  * **Phát triển Bảng điều khiển phân tích cho Đồ án Capstone:** Xây dựng luồng phân tích tự động thu thập nhật ký truy cập (Access Logs) của ứng dụng đồ án, xử lý qua Athena và xuất bản Dashboard theo dõi tỷ lệ lỗi HTTP 5xx cùng xu hướng người dùng thực tế trên QuickSight.
