---
title: "Week 13 Worklog"
date: 2026-12-07
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 13 Objectives:

- Explore the **Generative AI** ecosystem on AWS leveraging the fully managed **Amazon Bedrock** foundation service.
- Experiment with and benchmark top-tier **Foundation Models (FMs)**: Anthropic Claude 3.5 Sonnet, Amazon Titan Text, and Meta Llama 3 via the Bedrock Playground and Python Boto3 SDK (`bedrock-runtime`).
- Master advanced **Prompt Engineering** techniques and architect enterprise **Retrieval-Augmented Generation (RAG)** systems using **Amazon Bedrock Knowledge Bases** backed by Amazon OpenSearch Serverless vector stores.
- Design, configure, and deploy autonomous **Amazon Bedrock Agents** capable of intent parsing, task decomposition, and invoking backend **Action Groups** via AWS Lambda.
- Survey the end-to-end Machine Learning lifecycle (**MLOps**) using **Amazon SageMaker** (SageMaker Studio, JumpStart, and Real-time Inference Endpoints).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and embedding a production GenAI Assistant into the **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Foundation Models & Amazon Bedrock API Integration:** <br>- Managing model access permissions (Claude 3.5 Sonnet, Titan Text, Llama 3). <br>- Benchmarking latency, context windows, and token consumption on Bedrock Playground. <br>- Programmatic invocation via Python Boto3 SDK using `bedrock-runtime` client. | 12/07/2026 | 12/07/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Tuesday** | **Prompt Engineering & RAG Architecture with Bedrock Knowledge Bases:** <br>- Advanced prompting: System instructions, few-shot examples, and JSON Schema enforcement. <br>- Provisioning Bedrock Knowledge Bases connected to document stores on Amazon S3. <br>- Configuring vector embeddings (Amazon Titan) and semantic search via OpenSearch Serverless. | 12/08/2026 | 12/08/2026 | [AWS Bedrock Guide](https://cloudjourney.awsfcaj.com/) |
| **Wednesday** | **Autonomous AI Agents with Bedrock Agents & Action Groups:** <br>- Defining agent personas, multi-step reasoning instructions, and guardrails. <br>- Specifying OpenAPI specs and Action Groups wired to backend AWS Lambda functions. <br>- Testing automated query execution against database records and returning formatted answers. | 12/09/2026 | 12/09/2026 | [AWS Bedrock Agents](https://cloudjourney.awsfcaj.com/) |
| **Thursday** | **End-to-End Machine Learning with Amazon SageMaker:** <br>- Exploring SageMaker Studio notebooks and SageMaker Canvas no-code environments. <br>- Deploying pre-trained foundation models via SageMaker JumpStart. <br>- Provisioning real-time inference endpoints with Target Tracking auto scaling policies. | 12/10/2026 | 12/10/2026 | [Amazon SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Friday** | **Week 13 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate Bedrock APIs, Prompting, RAG Knowledge Bases, and Agents. <br>- **Worklog Completion:** Finalize bilingual Week 13 documentation and teardown lab resources. <br>- **Project Work:** Integrate Bedrock APIs into the Capstone Project backend to provide intelligent AI assistance. | 12/11/2026 | 12/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 13 Achievements:

#### 📌 Monday (12/07/2026) - Mastering the Bedrock Runtime API:
* **Serverless Model Consumption:** Seamlessly invoked Claude 3.5 Sonnet using the AWS Python SDK with low-temperature configurations (`temperature = 0.2`) to deliver deterministic, factual responses.
* **Token Cost Engineering:** Established a tiered routing model: dispatching lightweight conversational queries to cost-efficient Amazon Titan models while preserving advanced reasoning tasks for Claude 3.5 Sonnet.

#### 📌 Tuesday (12/08/2026) - Grounded RAG with Knowledge Bases:
* **Hallucination Prevention:** Linked an enterprise knowledge repository on S3 to Bedrock Knowledge Bases. Queries automatically retrieve the most relevant semantic document chunks as ground truth, delivering 100% verifiable responses with exact source citations.
* **Managed Vector Pipeline:** Automated text chunking, embedding generation via Titan Multimodal/Text models, and vector indexing on OpenSearch Serverless with zero vector database cluster management.

#### 📌 Wednesday (12/09/2026) - Autonomous Workflows with Bedrock Agents:
* **Autonomous Task Execution:** Configured an AI Agent that parses complex human prompts, breaks them down into sub-tasks, and invokes AWS Lambda Action Groups to query live database backends.
* **Multi-Turn Context Tracking:** Managed continuous conversation sessions natively via Bedrock session IDs without having to persist conversational history manually in application databases.

#### 📌 Thursday (12/10/2026) - MLOps with Amazon SageMaker:
* **One-Click Model Hosting:** Deployed a pre-trained sentiment analysis model using SageMaker JumpStart onto an `ml.m5.large` instance in under 5 minutes.
* **Production-Grade Serving:** Configured real-time endpoints with autoscaling triggers based on concurrent request volumes, ensuring low latency (under 50ms) across varying load conditions.
