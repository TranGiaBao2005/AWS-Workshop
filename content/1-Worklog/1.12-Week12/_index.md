---
title: "Week 12 Worklog"
date: 2026-11-30
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 12 Objectives:

- Master **Modern Data Lake Architectures** on Amazon S3 and implement centralized, fine-grained access control using **AWS Lake Formation** (Workshop 000035).
- Automate serverless Extract, Transform, and Load (ETL) data pipelines at scale utilizing **AWS Glue** (Glue Crawlers, Data Catalog, and PySpark Visual Jobs), converting raw data into optimized columnar Apache Parquet format.
- Execute interactive, distributed serverless SQL queries against massive datasets via **Amazon Athena** (Workshop 000106) and explore real-time stream ingestion with **Amazon Kinesis Data Streams**.
- Author interactive business intelligence dashboards and operational reports with **Amazon QuickSight** (Workshop 000073) accelerated by SPICE in-memory engines.
- Investigate cloud data warehousing principles at petabyte scale using **Amazon Redshift** (Massively Parallel Processing - MPP architecture).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and engineering an end-to-end telemetry and cost analytics pipeline for the internship **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Data Lake (Part 1) - Governance with AWS Lake Formation:** <br>- Establishing S3 Data Lake tiered zones (Raw Zone, Processed Zone, Curated Zone). <br>- Registering S3 Data Lake storage locations and establishing unified governance. <br>- Configuring granular row-level and column-level access control policies. <br>- Optimizing lake storage structures with chronological partitioning strategies. | 11/30/2026 | 11/30/2026 | [Data Lake Fundamentals (000035)](https://000035.awsfcaj.com/) |
| **Tuesday** | **Data Lake (Part 2) - Serverless ETL Automation with AWS Glue:** <br>- Deploying Glue Crawlers to automatically infer schemas into the AWS Glue Data Catalog. <br>- Building visual data pipelines in Glue Studio to clean, cast, and filter records. <br>- Converting uncompressed CSV/JSON files into Snappy-compressed columnar Apache Parquet. <br>- Configuring event-driven ETL triggers executing on new S3 object arrivals. | 12/01/2026 | 12/01/2026 | [Cloud Journey - Data](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Wednesday** | **Interactive SQL Analytics with Athena & Real-Time Streams with Kinesis:** <br>- Configuring Athena Workgroups, output S3 buckets, and query execution guardrails. <br>- Authoring complex analytical aggregation queries optimized for Parquet partitions. <br>- Evaluating real-time ingestion pipelines using Amazon Kinesis Data Streams and Firehose. <br>- Benchmarking query latency and data scan volumes across storage formats. | 12/02/2026 | 12/02/2026 | [Amazon Athena Workshop (000106)](https://000106.awsfcaj.com/) |
| **Thursday** | **Visual BI Dashboards with Amazon QuickSight & Exploring Redshift:** <br>- Connecting QuickSight datasets to Athena tables leveraging high-speed SPICE engines. <br>- Authoring visual charts, KPIs, geographic distribution maps, and parameterized controls. <br>- Analyzing Amazon Redshift distributed clustering, distribution styles, and sort keys. <br>- Evaluating massive parallel query processing (MPP) patterns for large data warehouses. | 12/03/2026 | 12/03/2026 | [Amazon QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Friday** | **Week 12 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate Lake Formation, Glue ETL, Athena, Kinesis, QuickSight, and Redshift. <br>- **Worklog Completion:** Finalize bilingual Week 12 documentation and teardown lab resources. <br>- **Project Work:** Incorporate an analytics dashboard reflecting application telemetry into the Capstone Proposal. | 12/04/2026 | 12/04/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (11/30/2026) - Data Lake (Part 1): Governance via AWS Lake Formation

* **What did we learn today?**
  * **Multi-Tier S3 Data Lake Topology:**
    * *Raw Zone (Bronze):* Landing zone capturing immutable source logs and transactional extracts in native format (CSV, JSON).
    * *Processed Zone (Silver):* Cleaned, deduplicated, and transformed datasets stored in optimized columnar Parquet format.
    * *Curated Zone (Gold):* Highly aggregated, business-ready models powering executive BI and machine learning features.
  * **Centralized Governance Plane:** Replaced fragmented S3 bucket policies and IAM grants with centralized table and column permissions managed exclusively via Lake Formation.
  * **Cell-Level Access Security:**
    * *Column-Level Filtering:* Redacted sensitive personally identifiable information (e.g., credit card numbers and phone numbers) from general analytics roles.
    * *Row-Level Filtering:* Enforced geographical row filters ensuring regional branch analysts only access rows where `Region = 'APAC'`.
* **Encountered Challenges & Solutions:**
  * *Permission Precedence Conflicts (Direct IAM vs Lake Formation):* Analysts continued reading raw bucket objects despite revoked Lake Formation permissions. Root cause: The legacy `IAMAllowedPrincipals` group remained enabled in Data Catalog settings, bypassing Lake Formation checks. Solution: Removed `IAMAllowedPrincipals` from the catalog and routed all data access exclusively through Lake Formation security grants.

---

#### 📌 Tuesday (12/01/2026) - Data Lake (Part 2): Serverless ETL Pipelines via AWS Glue

* **What did we learn today?**
  * **Automated Cataloging via Glue Crawlers:** Crawled raw transaction directories on S3, discovering schemas, inferring data types, and publishing the `raw_orders` table definition into the AWS Glue Data Catalog in under 60 seconds.
  * **Visual Pipeline Authoring with Glue Studio:**
    * Chained processing nodes: S3 Raw Source ➔ ApplyMapping schema transformations ➔ Filter Null Records ➔ S3 Processed Target.
    * Transformed raw CSV files into columnar **Apache Parquet** format compressed with **Snappy**.
    * Measured efficiency: A 500MB raw CSV dataset compressed down to 72MB in Parquet, slashing storage footprints by 85%.
  * **Automated Partitioning Hierarchies:** Configured chronological target paths (`year=YYYY/month=MM/day=DD`), allowing query engines to prune partitions and avoid full-table scans.
* **Encountered Challenges & Solutions:**
  * *Timestamp Parsing Mismatches:* The `order_date` field formatted as `DD/MM/YYYY` was classified by the crawler as a `String`, breaking date-range SQL filters. Solution: Inserted a custom PySpark transform node utilizing `to_date()` to standardize the column to ISO `yyyy-MM-dd` before Parquet serialization.

---

#### 📌 Wednesday (12/02/2026) - Interactive SQL with Athena & Streaming with Kinesis

* **What did we learn today?**
  * **Serverless SQL Execution via Amazon Athena:** Configured Athena workgroups and dedicated query results staging at `s3://fcaj-athena-query-results/`. Executed ANSI SQL analytical queries against multi-million row datasets with zero provisioned database servers.
  * **FinOps Benchmarking on Query Telemetry:**
    * Benchmark results comparing a monthly revenue aggregation query:
      * Unpartitioned CSV table: Scanned **500MB** of data, query latency **4.8 seconds**.
      * Partitioned Parquet table: Scanned **6.2MB** of data, query latency **0.8 seconds**.
    * Scanned data volume decreased by over **98%**, directly translating to an equivalent 98% reduction in billable query costs ($5.00/TB scanned).
  * **Real-Time Stream Processing Principles:** Explored Amazon Kinesis Data Streams shard architectures and integrated Kinesis Data Firehose to buffer, compress, and dump streaming telemetry into S3 micro-batches.
* **Encountered Challenges & Solutions:**
  * *Athena Missing Newly Added Partitions:* Athena queries failed to return newly appended date partitions created by the Glue ETL job. Solution: Executed `MSCK REPAIR TABLE orders_parquet;` to update partition metadata, or configured **Partition Projection** in the Glue Catalog to infer dynamic date partitions programmatically.

---

#### 📌 Thursday (12/03/2026) - Visual Analytics via Amazon QuickSight & Redshift

* **What did we learn today?**
  * **Business Intelligence with Amazon QuickSight:**
    * Connected QuickSight directly to Athena data sources.
    * Cached datasets into the **SPICE (Super-fast, Parallel, In-memory Calculation Engine)** memory tier, enabling instantaneous dashboard interactions and drill-downs without incurring repeated Athena scan charges.
    * Built a production dashboard: Total Revenue KPIs, weekly order trend line graphs, product category breakdowns, and geographic heat maps.
  * **Amazon Redshift Data Warehouse Mechanics:**
    * Evaluated Massively Parallel Processing (MPP) architectures distributing query workloads across compute slices.
    * Evaluated distribution styles (`AUTO`, `EVEN`, `KEY`, `ALL`) to minimize data movement (shuffling) across nodes during heavy join operations.
* **Encountered Challenges & Solutions:**
  * *QuickSight S3 Access Denied Errors:* QuickSight failed to ingest Athena query outputs from S3. Root cause: QuickSight operates under a dedicated service role requiring explicit storage grants. Solution: Navigated to `Manage QuickSight` ➔ `Security & permissions`, granting read access to both the Data Lake and Athena results buckets.

---

#### 📌 Friday (12/04/2026) - Week 12 Review, Worklog Finalization & Capstone Analytics

* **What did we learn today?**
  * **End-to-End Data Pipeline Architecture:** Synthesized the complete data lifecycle: Ingestion (Kinesis/S3) ➔ Security Governance (Lake Formation) ➔ Transformation (Glue ETL) ➔ Distributed SQL (Athena) ➔ Executive Visualizations (QuickSight).
  * **Disciplined FinOps Cleanup:** Pruned temporary Glue Catalog tables, purged staging S3 data, and released unallocated SPICE capacity to avoid recurring monthly charges.
  * **Graduation Capstone Analytics Pipeline:** Built an automated telemetry pipeline ingesting application web access logs into Athena, publishing an executive QuickSight dashboard tracking error spikes (HTTP 5xx) and user traffic trends.
