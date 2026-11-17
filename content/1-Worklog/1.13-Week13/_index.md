---
title: "Week 13 Worklog"
date: 2026-12-07
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 13 Objectives:

- Master the **Generative AI** ecosystem on AWS utilizing the fully managed serverless foundation model platform **Amazon Bedrock**.
- Dedicate **two full deep-dive days (Monday & Tuesday)** to hands-on AI engineering: from programmatic Foundation Model invocation via the Python Boto3 SDK (`bedrock-runtime`) to advanced **Prompt Engineering** and enterprise **Retrieval-Augmented Generation (RAG)** systems powered by Amazon Bedrock Knowledge Bases and Amazon OpenSearch Serverless.
- Architect and deploy autonomous **Amazon Bedrock Agents** capable of natural language intent parsing, multi-step task decomposition, and invoking backend **Action Groups** via AWS Lambda.
- Survey the end-to-end Machine Learning lifecycle (**MLOps**) using **Amazon SageMaker** (SageMaker Studio, JumpStart, and autoscaled Real-time Inference Endpoints).
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and embedding a production GenAI Assistant into the **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **GenAI (Part 1) - Foundation Models & Bedrock Runtime API:** <br>- Managing model access permissions (Claude 3.5 Sonnet, Amazon Titan, Meta Llama 3). <br>- Benchmarking parameters on Bedrock Playground: `temperature`, `top_p`, `max_tokens`. <br>- Programmatic invocation via Python Boto3 SDK (`bedrock-runtime`). <br>- Analyzing inference latency profiles and designing token cost control tiers. | 12/07/2026 | 12/07/2026 | [AWS Generative AI](https://cloudjourney.awsfcaj.com/) |
| **Tuesday** | **GenAI (Part 2) - Prompt Engineering & RAG with Bedrock Knowledge Bases:** <br>- Mastering prompt methodologies: System Prompts, Few-shot Examples, Chain-of-Thought, JSON Schema. <br>- Provisioning Bedrock Knowledge Bases connected to document stores on Amazon S3. <br>- Configuring vector embeddings (Amazon Titan) and semantic search via OpenSearch Serverless. <br>- Testing RetrieveAndGenerate workflows to eliminate hallucinations with source citations. | 12/08/2026 | 12/08/2026 | [AWS Bedrock Guide](https://cloudjourney.awsfcaj.com/) |
| **Wednesday** | **Autonomous AI Agents with Bedrock Agents & Action Groups:** <br>- Defining agent personas, multi-step reasoning guidelines, and guardrails. <br>- Specifying OpenAPI 3.0 schemas and Action Groups wired to backend AWS Lambda functions. <br>- Testing automated query execution against database records and returning formatted answers. <br>- Managing multi-turn conversation session states. | 12/09/2026 | 12/09/2026 | [AWS Bedrock Agents](https://cloudjourney.awsfcaj.com/) |
| **Thursday** | **End-to-End Machine Learning Lifecycle with Amazon SageMaker:** <br>- Exploring SageMaker Studio developer environments and SageMaker Canvas (No-code ML). <br>- Deploying pre-trained foundation models via SageMaker JumpStart. <br>- Provisioning real-time inference endpoints hosted on `ml.m5.large` instances. <br>- Establishing Target Tracking autoscaling policies responding to invocation traffic. | 12/10/2026 | 12/10/2026 | [Amazon SageMaker](https://cloudjourney.awsfcaj.com/) |
| **Friday** | **Week 13 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate Bedrock APIs, Prompting, RAG Knowledge Bases, and SageMaker. <br>- **Worklog Completion:** Finalize bilingual Week 13 documentation and teardown lab resources. <br>- **Project Work:** Integrate Bedrock APIs into the Capstone Project backend to provide intelligent AI assistance. | 12/11/2026 | 12/11/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (12/07/2026) - GenAI (Part 1): Foundation Models & Bedrock Runtime API

* **What did we learn today?**
  * **Foundation Model Landscape on Amazon Bedrock:** Evaluated how Bedrock provides a unified serverless API accessing industry-leading models with zero GPU cluster administration:
    * *Anthropic Claude 3.5 Sonnet:* State-of-the-art model for complex logical reasoning, code analysis, and architectural synthesis.
    * *Amazon Titan Text:* Lightweight, low-latency, and cost-effective model for extraction and summarization.
    * *Meta Llama 3:* Versatile, open-weights foundational model for general-purpose tasks.
  * **Inference Parameter Tuning on the Bedrock Playground:**
    * `Temperature (0.0 - 1.0)`: Set to `0.2` for deterministic technical tasks requiring strict factual accuracy; set to `0.8` for creative brainstorming.
    * `Top P (0.0 - 1.0)`: Controlled token candidate probability mass, shaping semantic diversity.
    * `Max Tokens`: Capped maximum completion output length to prevent run-away token generation costs.
  * **SDK Integration via Python Boto3:**
    ```python
    import json
    import boto3

    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    prompt_payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.2,
        "messages": [
            {"role": "user", "content": "Analyze 3 core security benefits of AWS KMS."}
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
* **Encountered Challenges & Solutions:**
  * *`AccessDeniedException` on Model Invocation:* API calls failed with `Model access not granted`. Root cause: Newly provisioned AWS accounts must explicitly request access to third-party model providers. Solution: Navigated to `Model access` within the Amazon Bedrock Console, submitted the access request for Claude 3.5 Sonnet, which was approved within minutes.

---

#### 📌 Tuesday (12/08/2026) - GenAI (Part 2): Prompt Engineering & RAG Architecture

* **What did we learn today?**
  * **Advanced Prompt Engineering Disciplines:**
    * *System Prompts:* Assigned an authoritative engineering persona (`"You are an AWS Principal Solutions Architect..."`), enforcing concise, deterministic technical prose.
    * *Few-shot Examples:* Provided canonical input/output pairs to establish strict schema patterns.
    * *Chain-of-Thought:* Instructed the model to reason through intermediate deductions (`"Think step-by-step before concluding"`), measurably improving algorithmic problem-solving accuracy.
    * *JSON Schema Enforcement:* Constrained model outputs to valid JSON structures, enabling seamless downstream parsing via `JSON.parse()`.
  * **Architecting Enterprise RAG with Bedrock Knowledge Bases:**
    1. Staged internal architecture runbooks and standard operating procedures (PDF/DOCX) in S3 bucket `fcaj-kb-docs-887086382708`.
    2. Provisioned an Amazon Bedrock Knowledge Base utilizing the `Amazon Titan Text Embeddings v2` model.
    3. AWS automatically provisioned a serverless vector store on **Amazon OpenSearch Serverless**, automating document chunking (300 tokens, 20% overlap) and vector indexing.
    4. Validated `RetrieveAndGenerate` workflows: User queries retrieve the most semantically relevant text chunks as factual ground truth injected into the Claude 3.5 prompt context, eliminating hallucinations and attaching direct source citations.
* **Encountered Challenges & Solutions:**
  * *OpenSearch Serverless Data Access Rejection:* Knowledge Base creation failed with `Cannot write to OpenSearch vector collection`. Solution: Appended the Bedrock execution IAM role to the OpenSearch Serverless **Data Access Policy** with `aoss:CreateCollectionItems` and `aoss:DescribeCollectionItems` permissions.

---

#### 📌 Wednesday (12/09/2026) - Autonomous AI Agents via Bedrock Agents & Action Groups

* **What did we learn today?**
  * **Autonomous ReAct Reasoning Loops:** Mastered how Bedrock Agents use the ReAct (Reasoning + Acting) pattern to parse multi-step user prompts, determine missing parameters, invoke external APIs, and synthesize natural language answers.
  * **Engineering Action Groups Integrated with AWS Lambda:**
    * Authored an OpenAPI 3.0 YAML specification describing an `/check-order-status` endpoint accepting an `orderId` parameter.
    * Developed an AWS Lambda function querying live DynamoDB/RDS tables and returning structured JSON records.
    * Linked the Action Group to the Bedrock Agent.
  * **Live Conversational Validation:** Prompting *"What is the current status of order #FCJ-9921?"* caused the agent to recognize the intent, extract the ID, invoke Lambda, and return: *"Order #FCJ-9921 has been fulfilled and is in transit, with estimated delivery tomorrow."*
* **Encountered Challenges & Solutions:**
  * *Agent Invocation Permission Denied:* The Bedrock console reported `Agent failed to invoke action group`. Root cause: The target Lambda function lacked resource-based policy authorization for the Bedrock service principal. Solution: Executed `aws lambda add-permission --function-name MyAgentFunction --principal bedrock.amazonaws.com --action lambda:InvokeFunction`.

---

#### 📌 Thursday (12/10/2026) - MLOps Lifecycle Management with Amazon SageMaker

* **What did we learn today?**
  * **End-to-End Machine Learning Lifecycle:** Navigated the full pipeline: Data preparation (Data Wrangler) ➔ Model authoring (SageMaker Studio) ➔ Distributed training (Training Jobs) ➔ Production serving (Inference Endpoints).
  * **Rapid Deployment with SageMaker JumpStart:** Evaluated open-weights models in JumpStart, launching an open-source text classifier onto an `ml.m5.large` instance in under 5 minutes.
  * **Real-time Serving & Target Tracking Elasticity:**
    * Benchmarked inference response times, recording low-latency performance (P95 latency < 45ms).
    * Configured Target Tracking scaling policies on `InvocationsPerInstance`, ensuring compute instances scale out automatically during traffic spikes and scale in during idle hours.
* **Encountered Challenges & Solutions:**
  * *Insufficient Compute Quota on GPU Instances:* Launching an `ml.g5.2xlarge` instance failed with `ResourceLimitExceeded`. Root cause: Default AWS accounts possess zero default quota for GPU-accelerated instances. Solution: Selected general-purpose CPU instance `ml.m5.large` for functional validation and submitted a Service Quota limit increase request.

---

#### 📌 Friday (12/11/2026) - Week 13 Review, Worklog Finalization & Capstone AI Integration

* **What did we learn today?**
  * **Generative AI Maturity Model Synthesis:** Mapped architectural choices across the abstraction spectrum: from zero-infrastructure serverless consumption (Bedrock APIs, Knowledge Bases, Agents) to fully customized model hosting and training (SageMaker).
  * **FinOps Resource Decommissioning:** Decommissioned the SageMaker real-time inference endpoint (`ml.m5.large`) immediately after validation to stop hourly compute billing, and deleted test OpenSearch Serverless vector collections.
  * **Graduation Capstone AI Assistant Integration:** Integrated Bedrock Claude 3.5 Sonnet and Knowledge Base APIs into the web frontend of the Capstone Project, providing automated conversational support for user order tracking and policy inquiries.
