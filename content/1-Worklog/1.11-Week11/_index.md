---
title: "Week 11"
date: 2026-11-23
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Objectives for Week 11:

- Architect a **Modern Data Lake** on Amazon S3 governed centrally by **AWS Lake Formation** (Workshop 000035) and serverless **AWS Glue** ETL pipelines converting raw data into Apache Parquet.
- Optimize interactive SQL analytics with **Amazon Athena** (Workshop 000106), explore streaming with **Amazon Kinesis**, build BI dashboards in **Amazon QuickSight** (Workshop 000073), and study **Amazon Redshift** MPP warehousing.
- Master **Generative AI** services on AWS via **Amazon Bedrock** (Foundation Models, Boto3 Runtime API, Prompt Engineering, RAG Knowledge Bases, and Bedrock Agents) alongside MLOps workflows on **Amazon SageMaker**.
- Dedicate Friday to consolidating weekly learnings, updating bilingual Worklogs, cleaning up expensive AI/Data resources, and integrating analytics/GenAI into the **Capstone Project**.

---

### Tasks to be implemented this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Data Lake Governance (AWS Lake Formation) & Serverless ETL (AWS Glue):** <br>- Structure S3 Data Lake zones (Raw, Processed, Curated) and enforce row/column-level access in Lake Formation. <br>- Run Glue Crawlers to infer table schemas into the Glue Data Catalog. <br>- Build Glue Studio ETL jobs converting CSV/JSON into Snappy-compressed Apache Parquet partitioned by `year/month/day`. | 23/11/2026 | 23/11/2026 | [Data Lake (000035)](https://000035.awsfcaj.com/) & [Data Analytics](https://cloudjourney.awsfcaj.com/6-dataandanalytic/) |
| **Tuesday** | **Amazon Athena Analytics, Kinesis Streams, QuickSight BI & Amazon Redshift:** <br>- Configure Athena Workgroups and benchmark Data Scanned reductions between raw CSV and partitioned Parquet. <br>- Study real-time ingestion architectures with Amazon Kinesis Data Streams and Data Firehose. <br>- Connect Amazon QuickSight (SPICE) for KPI dashboards and examine Redshift MPP distribution styles. | 24/11/2026 | 24/11/2026 | [Athena (000106)](https://000106.awsfcaj.com/) & [QuickSight (000073)](https://000073.awsfcaj.com/) |
| **Wednesday** | **Amazon Bedrock Foundation Models, Prompt Engineering & RAG Architecture:** <br>- Evaluate Foundation Models (Claude, Amazon Titan, Llama) and invoke APIs via Python Boto3 `bedrock-runtime`. <br>- Apply System Prompts, Few-shot prompting, Chain-of-Thought, and JSON Schema enforcement. <br>- Architect RAG with Bedrock Knowledge Bases, Titan Embeddings, and OpenSearch Serverless vector search. | 25/11/2026 | 25/11/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Thursday** | **Autonomous Bedrock Agents & MLOps with Amazon SageMaker:** <br>- Define OpenAPI 3.0 schemas and Lambda Action Groups powering Bedrock Agents (ReAct + Guardrails). <br>- Explore Amazon SageMaker Studio, JumpStart, and Real-time Inference Endpoints with Auto Scaling. <br>- Enforce strict FinOps teardown procedures for GPU/CPU endpoints and vector collections. | 26/11/2026 | 26/11/2026 | [Amazon Bedrock & SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Friday** | **Week 11 Review, Worklog & Project:** <br>- **Knowledge Synthesis:** Connect Data Analytics pipelines and Generative AI architectures end-to-end. <br>- **Worklog & Cleanup:** Finalize bilingual Week 11 documentation and delete OpenSearch/SageMaker test resources. <br>- **Capstone Project:** Integrate observability analytics and GenAI assistant capabilities into the project design. | 27/11/2026 | 27/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily Learning Details & Results:

#### 📌 Monday (23/11/2026) - Data Lake Governance (AWS Lake Formation) & AWS Glue ETL

* **What did I learn today?**
  * **Multi-Tier S3 Data Lake & Cell-Level Security:** Partitioned S3 into *Raw*, *Processed*, and *Curated* zones, using AWS Lake Formation to centralize permissions and apply column masking (hiding PII) plus row-level filters by region.
  * **Serverless ETL with AWS Glue:** Automated schema discovery via Glue Crawlers and authored Glue Studio ETL jobs converting CSV datasets into Snappy-compressed **Apache Parquet** organized by `year=YYYY/month=MM/day=DD`, drastically shrinking storage footprint.
* **Challenges & Resolutions:**
  * *`IAMAllowedPrincipals` bypass & date schema mismatches:* Revoked default `IAMAllowedPrincipals` on the Glue Catalog so Lake Formation governs access exclusively, and applied PySpark `to_date()` transformations to normalize `yyyy-MM-dd` timestamps before Parquet output.

---

#### 📌 Tuesday (24/11/2026) - Amazon Athena, Kinesis, QuickSight BI & Amazon Redshift

* **What did I learn today?**
  * **FinOps Query Optimization on Amazon Athena:** Transitioning from unpartitioned CSV to partitioned Parquet cut Data Scanned by >90%, directly reducing per-TB query charges ($5/TB) and cutting query latency sharply.
  * **Streaming, BI & MPP Warehousing:** Studied **Kinesis Data Streams/Firehose** for real-time telemetry ingestion; connected **Amazon QuickSight** with **SPICE** in-memory caching for responsive dashboards without repeated Athena scans; reviewed **Amazon Redshift** MPP architecture and Distribution Styles (`AUTO`, `KEY`, `EVEN`, `ALL`).
* **Challenges & Resolutions:**
  * *Missing new partitions in Athena & QuickSight S3 `Access Denied`:* Executed `MSCK REPAIR TABLE` (or enabled Partition Projection) to register partitions, and granted explicit S3 bucket read access under `Manage QuickSight -> Security & permissions`.

---

#### 📌 Wednesday (25/11/2026) - Amazon Bedrock Foundation Models & RAG Architecture

* **What did I learn today?**
  * **Unified Model Access via Bedrock Runtime API:** Tuned inference parameters (`temperature`, `top_p`, `max_tokens`) and invoked foundation models cleanly via Python Boto3 without provisioning GPU servers:
    ```python
    import json, boto3
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": "Analyze 3 security benefits of AWS KMS."}]
    }
    resp = bedrock.invoke_model(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body=json.dumps(payload)
    )
    ```
  * **Prompt Engineering & RAG Knowledge Bases:** Combined structured prompting (System Prompts, Few-shot, Chain-of-Thought) with Bedrock Knowledge Bases (S3 documents ➔ Titan Text Embeddings v2 ➔ OpenSearch Serverless) to deliver grounded, citation-backed responses with minimal hallucination.
* **Challenges & Resolutions:**
  * *`Model access not granted` & OpenSearch Data Access Policy failures:* Requested model activation under Bedrock `Model access` and added the Knowledge Base IAM Role to the OpenSearch Serverless Data Access Policy.

---

#### 📌 Thursday (26/11/2026) - Amazon Bedrock Agents & MLOps with Amazon SageMaker

* **What did I learn today?**
  * **Autonomous Execution with Bedrock Agents:** Applied ReAct reasoning loops paired with OpenAPI 3.0 schemas and AWS Lambda **Action Groups** to fetch live operational state safely, reinforced with **Bedrock Guardrails** against prompt injection (aligning directly with the AgentCore Deep-Dive Workshop).
  * **End-to-End MLOps with Amazon SageMaker:** Explored Data Wrangler, SageMaker Studio, JumpStart one-click pre-trained deployments, and Real-time Inference Endpoints with `InvocationsPerInstance` Target Tracking Auto Scaling.
* **Challenges & Resolutions:**
  * *Agent Lambda invocation errors & zero default GPU quotas:* Added resource-based permission for `bedrock.amazonaws.com` via `aws lambda add-permission`; used CPU `ml.m5.large` for functional validation or requested Service Quotas increases when GPU instances are needed.

---

#### 📌 Friday (27/11/2026) - Week 11 Review, Worklog & Project Integration

* **What did I learn today?**
  * **End-to-End Data & AI Value Chain:** Unified S3 Data Lakes (Lake Formation, Glue, Athena, QuickSight) with production-ready Generative AI capabilities (Bedrock RAG, Agents, SageMaker).
  * **Strict AI FinOps Cleanup:** Deleted OpenSearch Serverless collections and SageMaker endpoints immediately after validation to prevent costly OCU and hourly compute accruals.
  * **Preparing for Week 12:** Finalized core architecture deliverables and demo scope ahead of the final internship week.
