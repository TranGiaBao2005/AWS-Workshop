---
title: "Proposal"
date: 2026-10-02
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# IoT Weather Platform for Lab Research
## A Unified AWS Serverless Solution for Real-Time Weather Monitoring

### 1. Executive Summary
The **IoT Weather Platform** automates real-time weather telemetry collection, storage, and analysis for laboratory research. Supporting 5 initial weather stations and scaling seamlessly to 10–15 stations, the system pairs Raspberry Pi edge nodes and ESP32 sensor arrays transmitting over MQTT with a fully **AWS Serverless** cloud backend. This design minimizes operational overhead, keeps recurring cloud spend under $1/month, and enforces authenticated access for 5 research members via **Amazon Cognito**.

---

### 2. Problem Statement

#### Current Challenges
Existing standalone weather stations rely on manual data extraction, which becomes error-prone as station counts grow. Without centralized ingestion and storage, researchers cannot monitor live anomalies or query clean historical datasets for modeling, while commercial third-party IoT platforms carry high subscription costs and unnecessary complexity for a small research team.

#### Proposed Solution
An end-to-end serverless telemetry pipeline built natively on AWS:
- **Ingestion:** **AWS IoT Core** receives X.509-authenticated MQTT payloads from Raspberry Pi edge gateways.
- **Processing & Storage:** **AWS Lambda** and **Amazon API Gateway** process incoming events, while **Amazon S3** separates raw payloads (Raw Data Lake) from curated datasets (Processed Bucket).
- **Cataloging & ETL:** **AWS Glue Crawlers** maintain schema metadata and **AWS Glue ETL Jobs** clean and transform records for downstream analysis.
- **Dashboard & Authentication:** **AWS Amplify** hosts a **Next.js** web dashboard protected by **Amazon Cognito**.

#### Benefits & Return on Investment (ROI)
The platform eliminates manual station polling and produces a clean, queryable historical dataset for AI/ML weather research. Estimated monthly AWS expenditure is **$0.70 USD/month** (**$8.40 USD/year** via the AWS Pricing Calculator). Because edge sensors and Raspberry Pi units are already available in the lab, the project achieves break-even within 6–12 months through saved engineering hours.

---

### 3. Solution Architecture

The architecture decouples edge telemetry collection from serverless cloud ingestion, ETL processing, and dashboard visualization:

![IoT Weather Station Architecture](/images/2-Proposal/edge_architecture.jpeg)

![IoT Weather Platform Architecture](/images/2-Proposal/platform_architecture.jpeg)

#### AWS Services Used
- **AWS IoT Core:** Ingests MQTT sensor streams from 5 stations (scalable to 15).
- **AWS Lambda:** Validates incoming telemetry and triggers scheduled ETL workflows (2 functions).
- **Amazon API Gateway:** Exposes secure HTTP endpoints for the web dashboard.
- **Amazon S3:** Provides durable object storage across two buckets (Raw Data Lake & Processed Analytics Bucket).
- **AWS Glue:** Runs Crawlers for Data Catalog indexing and serverless ETL jobs for data normalization.
- **AWS Amplify:** Hosts and continuously deploys the Next.js frontend application.
- **Amazon Cognito:** Manages user authentication and restricts dashboard access to 5 authorized lab accounts.

#### Component Design
- **Edge Layer:** Temperature, humidity, rainfall, and wind-speed sensors wired to ESP32 microcontrollers; Raspberry Pi edge gateways run Docker containers to filter noisy readings and publish ~1 MB/day/station over Wi-Fi MQTT.
- **Ingestion Layer:** AWS IoT Core Message Broker and IoT Rules route incoming payloads directly to S3 and Lambda.
- **Storage & ETL Layer:** Raw JSON/CSV records land in the S3 Raw Bucket; AWS Glue Crawlers and ETL jobs transform and store analytics-ready data in the S3 Processed Bucket.
- **Presentation & Auth Layer:** Next.js on AWS Amplify renders real-time charts and historical trends, gated by Amazon Cognito User Pools.

---

### 4. Technical Implementation

#### Implementation Phases
1. **Phase 1 – Edge Validation & Architecture Design:** Verify ESP32–Raspberry Pi sensor acquisition, containerize the local MQTT publisher with Docker, and finalize the AWS Serverless blueprint.
2. **Phase 2 – Cost Modeling & Feasibility Audit:** Benchmark monthly resource consumption in the AWS Pricing Calculator and configure AWS Budgets alerts.
3. **Phase 3 – Architectural Optimization:** Offload full-stack rendering tasks to Next.js on AWS Amplify to minimize redundant Lambda invocations and batch Glue ETL schedules.
4. **Phase 4 – Cloud Deployment & End-to-End Testing:** Provision AWS resources using AWS CDK/SDK, connect all 5 edge stations to AWS IoT Core, verify Glue ETL outputs, and validate the live dashboard.

---

### 5. Timeline & Milestones

- **Pre-Internship Preparation:** Audit existing weather station hardware and define research telemetry schemas.
- **Month 1 (Weeks 1 – 4):** Establish core AWS networking, IAM security baselines, S3 storage buckets, CloudWatch monitoring, and edge container setups.
- **Month 2 (Weeks 5 – 8):** Configure database/caching patterns, CLI/Lambda/IaC automation, and the AWS IoT Core ➔ S3 ingestion pipeline.
- **Month 3 (Weeks 9 – 12):** Integrate AWS Glue ETL jobs, deploy the Next.js dashboard on AWS Amplify with Cognito authentication, run end-to-end validation, and defend the project.

---

### 6. Budget Estimation

Detailed cost breakdown on the **[AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01)**:

| AWS Service | Estimated Monthly Usage | Monthly Cost (USD) |
| :--- | :--- | :---: |
| **AWS Lambda** | ~1,000 requests/month, 512 MB ephemeral storage (covered by Free Tier) | $0.00 |
| **Amazon S3 Standard** | ~6 GB storage, 2,100 PUT/GET requests, 1 GB scanned | $0.15 |
| **Data Transfer** | 1 GB Inbound, 1 GB Outbound | $0.02 |
| **AWS Amplify** | Next.js web hosting (256 MB memory, ~500 ms request duration) | $0.35 |
| **Amazon API Gateway** | ~2,000 HTTP API requests/month | $0.01 |
| **AWS Glue ETL Jobs** | 2 DPUs on scheduled batch runs | $0.02 |
| **AWS Glue Crawlers** | 1 Crawler updating Data Catalog partitions | $0.07 |
| **AWS IoT Core (MQTT)** | 5 edge devices, ~45,000 MQTT messages/month | $0.08 |
| **Total Cloud Spend** | **Monthly / Annual (12-Month) Projection** | **$0.70 / month ($8.40 / year)** |

*(One-time hardware value for Raspberry Pi 5 and sensor kits is approximately $265, utilizing existing laboratory equipment).*

---

### 7. Risk Assessment & Mitigation

| Risk Scenario | Impact | Likelihood | Mitigation & Contingency Plan |
| :--- | :---: | :---: | :--- |
| **Wi-Fi / Network Outage at Edge Stations** | Medium | Medium | Docker containers buffer sensor readings locally on the Raspberry Pi SD card and replay queued MQTT messages upon reconnection. |
| **Sensor Drift or Hardware Failure** | High | Low | Apply range sanity checks inside edge/Lambda ingestion logic and maintain spare ESP32/sensor modules in the lab. |
| **Unexpected AWS Cost Spikes** | Medium | Low | Enforce AWS Budgets alerts at 80% and 100% thresholds, throttle Glue job schedules, and manage stack lifecycles via CloudFormation/CDK. |

---

### 8. Expected Outcomes

- **Technical Improvements:** 100% automated real-time weather ingestion, ETL normalization, and web visualization across 5 stations—ready to scale to 10–15 stations without architectural rework.
- **Long-Term Research Value:** A clean, multi-month historical weather dataset on Amazon S3 supporting future machine learning and environmental forecasting projects.
