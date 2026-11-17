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
- Tự động hóa quy trình trích xuất, chuyển đổi và nạp dữ liệu (ETL) phi máy chủ quy mô lớn với **AWS Glue** (Glue Crawlers, Data Catalog và PySpark Jobs).
- Thực thi các câu lệnh truy vấn SQL tương tác trực tiếp trên dữ liệu phi cấu trúc lưu trữ tại S3 bằng **Amazon Athena** (Workshop 000106) và tiếp cận xử lý luồng dữ liệu thời gian thực với **Amazon Kinesis Data Streams**.
- Xây dựng hệ thống báo cáo phân tích thông minh và bảng điều khiển trực quan (**Business Intelligence - BI**) với **Amazon QuickSight** (Workshop 000073).
- Nghiên cứu kiến trúc kho dữ liệu đám mây quy mô Petabyte với **Amazon Redshift** (Serverless vs Provisioned Cluster).
- Dành trọn vẹn ngày Thứ 6 tổng kết kiến thức, hoàn thiện hồ sơ Worklog và xây dựng luồng phân tích dữ liệu chuyên sâu (Data Analytics Pipeline) cho đồ án (**Capstone Project Proposal**).

---

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| :--- | :--- | :---: | :---: | :--- |
| **Thứ 2** | **Xây dựng Hồ dữ liệu tập trung với AWS Lake Formation:** <br>- Đăng ký S3 Data Lake Location và cấu hình quản trị phân quyền dữ liệu tập trung. <br>- Thiết lập kiểm soát truy cập chi tiết tới từng hàng và từng cột (Row/Column-level Security). <br>- Tối ưu hóa chi phí lưu trữ hồ dữ liệu với cơ chế phân vùng Partitioning. | 30/11/2026 | 30/11/2026 | [Data Lake Fundamentals (000035)](https://000035.awsfcaj.com/) |
| **Thứ 3** | **Tự động hóa chu trình ETL phi máy chủ với AWS Glue:** <br>- Khởi chạy Glue Crawler tự động quét dữ liệu và tạo bảng trong AWS Glue Data Catalog. <br>- Xây dựng Glue Studio Visual ETL Pipeline làm sạch và chuẩn hóa dữ liệu. <br>- Chuyển đổi định dạng tệp từ thô (CSV/JSON) sang định dạng cột tối ưu (Apache Parquet). | 01/12/2026 | 01/12/2026 | [Cloud Journey - Data](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Thứ 4** | **Truy vấn dữ liệu với Amazon Athena & Xử lý luồng Kinesis:** <br>- Thiết lập Athena Workgroup và cấu hình vị trí lưu trữ kết quả truy vấn trên S3. <br>- Viết các truy vấn phân tích SQL tổng hợp phức tạp tối ưu chi phí với Parquet. <br>- Tiếp cận cơ chế thu thập dữ liệu thời gian thực với Amazon Kinesis Data Streams. | 02/12/2026 | 02/12/2026 | [Amazon Athena Workshop (000106)](https://000106.awsfcaj.com/) |
| **Thứ 5** | **Trực quan hóa BI với Amazon QuickSight & Khám phá Redshift:** <br>- Kết nối Amazon QuickSight với nguồn dữ liệu Amazon Athena qua SPICE in-memory engine. <br>- Thiết kế các biểu đồ phân tích tương tác trực quan (Interactive Dashboards) và chia sẻ an toàn. <br>- Tìm hiểu kiến trúc MPP (Massively Parallel Processing) của Amazon Redshift. | 03/12/2026 | 03/12/2026 | [Amazon QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Thứ 6** | **Tổng kết Tuần 12, Viết Worklog & Làm Project:** <br>- **Tổng kết kiến thức:** Hệ thống hóa toàn bộ kiến thức Data Lake, Glue, Athena, Kinesis, QuickSight và Redshift. <br>- **Làm Worklog:** Chuẩn hóa bài viết báo cáo Worklog Tuần 12 song ngữ và dọn dẹp tài nguyên thử nghiệm. <br>- **Làm Project:** Tích hợp Dashboard phân tích dữ liệu hiệu năng và chi phí vào Đề xuất đồ án (Proposal). | 04/12/2026 | 04/12/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Kết quả đạt được tuần 12:

#### 📌 Kết quả Thứ 2 (30/11/2026) - Xây dựng Hồ dữ liệu với Lake Formation:
* **Quản trị dữ liệu tập trung:** Đăng ký vị trí lưu trữ S3 vào AWS Lake Formation, thay thế hàng chục chính sách S3 Bucket Policy và IAM Policy rời rạc bằng một bảng phân quyền kiểm soát tập trung (Centralized Permissions Grant).
* **Bảo mật dữ liệu nhạy cảm:** Triển khai thành công bộ lọc dữ liệu cấp hàng và cấp cột (Cell-level Security), cho phép các nhóm phân tích khác nhau chỉ nhìn thấy các trường thông tin được phép mà không làm lộ dữ liệu định danh cá nhân (PII).

#### 📌 Kết quả Thứ 3 (01/12/2026) - ETL phi máy chủ với AWS Glue:
* **Tự động nhận diện lược đồ:** Glue Crawler tự động phân tích hàng nghìn tệp dữ liệu thô trên S3, suy diễn kiểu dữ liệu và tự động cập nhật Schema vào AWS Glue Data Catalog.
* **Tối ưu hóa hiệu năng & Chi phí:** Chuyển đổi toàn bộ tập dữ liệu từ CSV sang định dạng Parquet kèm nén Snappy, giúp giảm 85% dung lượng lưu trữ đĩa và tăng tốc độ quét dữ liệu lên gấp 5 lần.

#### 📌 Kết quả Thứ 4 (02/12/2026) - Phân tích dữ liệu với Amazon Athena:
* **Truy vấn tức thì không máy chủ:** Thực thi các câu lệnh SQL ANSI tiêu chuẩn trên tập dữ liệu hàng chục triệu bản ghi trong chưa đầy 3 giây mà không cần phải khởi chạy hay quản trị bất kỳ máy chủ cơ sở dữ liệu nào.
* **Tối ưu hóa chi phí truy vấn:** Nhờ định dạng cột Parquet và cơ chế phân vùng Partition Projection, lượng dữ liệu quét (Data Scanned) giảm từ 10GB xuống còn 120MB cho mỗi lượt truy vấn, giúp tiết kiệm hơn 98% chi phí truy vấn trên Athena.

#### 📌 Kết quả Thứ 5 (03/12/2026) - Báo cáo thông minh với Amazon QuickSight:
* **Tăng tốc phân tích dữ liệu với SPICE:** Nạp dữ liệu vào công cụ tính toán trong bộ nhớ siêu nhanh SPICE (Super-fast, Parallel, In-memory Calculation Engine), mang lại trải nghiệm tương tác với đồ thị mượt mà tức thì.
* **Bảng điều khiển kinh doanh toàn diện:** Thiết kế thành công Dashboard trực quan hiển thị các chỉ số kinh doanh quan trọng (KPIs, xu hướng doanh thu theo thời gian, bản đồ phân bố địa lý và tỷ lệ chuyển đổi).
