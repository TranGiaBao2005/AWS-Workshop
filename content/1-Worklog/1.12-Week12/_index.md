---
title: "Week 12 Worklog"
date: 2026-11-30
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 12 Objectives:

- Master **Modern Data Lake Architectures** on Amazon S3 and implement centralized governance with fine-grained access control using **AWS Lake Formation** (Workshop 000035).
- Automate serverless Extract, Transform, and Load (ETL) data pipelines at scale utilizing **AWS Glue** (Glue Crawlers, Data Catalog, and PySpark Visual Jobs).
- Execute high-performance, serverless distributed SQL queries against unstructured and semi-structured S3 data via **Amazon Athena** (Workshop 000106) and explore real-time stream ingestion with **Amazon Kinesis**.
- Develop interactive, self-service business intelligence dashboards using **Amazon QuickSight** (Workshop 000073) powered by SPICE in-memory engines.
- Investigate cloud data warehousing at petabyte scale using **Amazon Redshift** (Massively Parallel Processing - MPP architecture).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and engineering an end-to-end data pipeline for the internship **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Centralized Data Lake Governance with AWS Lake Formation:** <br>- Registering S3 Data Lake storage locations and establishing unified governance. <br>- Configuring granular row-level and column-level access control policies. <br>- Optimizing lake storage structures with chronological partitioning strategies. | 11/30/2026 | 11/30/2026 | [Data Lake Fundamentals (000035)](https://000035.awsfcaj.com/) |
| **Tuesday** | **Serverless ETL Automation with AWS Glue:** <br>- Deploying Glue Crawlers to automatically infer schemas into the AWS Glue Data Catalog. <br>- Building visual data pipelines in Glue Studio to clean and standardize raw records. <br>- Converting uncompressed CSV/JSON files into optimized columnar Apache Parquet format. | 12/01/2026 | 12/01/2026 | [Cloud Journey - Data](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Wednesday** | **Interactive SQL Analytics with Amazon Athena & Kinesis Streams:** <br>- Configuring Athena Workgroups, output S3 buckets, and query execution guardrails. <br>- Authoring complex analytical aggregation queries optimized for Parquet partitions. <br>- Evaluating real-time ingestion pipelines using Amazon Kinesis Data Streams. | 12/02/2026 | 12/02/2026 | [Amazon Athena Workshop (000106)](https://000106.awsfcaj.com/) |
| **Thursday** | **Business Intelligence Dashboards with Amazon QuickSight & Redshift:** <br>- Connecting QuickSight datasets to Athena tables leveraging high-speed SPICE engines. <br>- Authoring visual charts, KPIs, geographic distribution maps, and parameterized controls. <br>- Analyzing Amazon Redshift distributed clustering, distribution keys, and sort keys. | 12/03/2026 | 12/03/2026 | [Amazon QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Friday** | **Week 12 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate Lake Formation, Glue ETL, Athena, Kinesis, QuickSight, and Redshift. <br>- **Worklog Completion:** Finalize bilingual Week 12 documentation and teardown lab resources. <br>- **Project Work:** Incorporate an analytics dashboard reflecting application telemetry into the Capstone Proposal. | 12/04/2026 | 12/04/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 12 Achievements:

#### 📌 Monday (11/30/2026) - Data Lake Governance with Lake Formation:
* **Unified Security Plane:** Enforced central access permissions across S3 buckets via Lake Formation, replacing fragmented bucket policies with unified role-based grants.
* **Sensitive Data Redaction:** Configured cell-level filters to restrict access to Personally Identifiable Information (PII) columns, ensuring compliance across multi-disciplinary analytics teams.

#### 📌 Tuesday (12/01/2026) - Serverless ETL with AWS Glue:
* **Automated Cataloging:** Ingested multi-format raw files from S3 using Glue Crawlers, populating table definitions and partitions into the Glue Data Catalog automatically.
* **Storage Optimization:** Transformed tabular raw CSVs into Snappy-compressed Apache Parquet format, reducing data storage requirements by 85% and significantly accelerating downstream query I/O.

#### 📌 Wednesday (12/02/2026) - Serverless Queries via Amazon Athena:
* **Zero Infrastructure Overhead:** Executed complex analytical queries across millions of records without provisioning, managing, or scaling database instances.
* **FinOps Optimization:** By leveraging partitioned columnar Parquet data, reduced the scanned volume per query from 10GB down to 120MB, slashing query costs by over 98%.

#### 📌 Thursday (12/03/2026) - Visual Analytics with Amazon QuickSight:
* **Ultra-Fast Visualizations:** Ingested analytical data into the SPICE in-memory engine, achieving sub-second interactive graph rendering and filter responses.
* **Executive Dashboards:** Designed an executive summary board highlighting key business metrics, traffic trends, and regional usage patterns with role-based dashboard sharing.
