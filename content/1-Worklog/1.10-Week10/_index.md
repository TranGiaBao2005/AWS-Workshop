---
title: "Week 10 Worklog"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 10 Objectives:

- Master the **Event-Driven Architecture (EDA)** paradigm and modern asynchronous distributed design patterns on AWS.
- Architect, manage, and harden production-grade API endpoints using **Amazon API Gateway** (RESTful APIs, HTTP APIs, custom Lambda Authorizers, traffic shaping with Throttling & Usage Plans).
- Implement service decoupling and load-leveling buffers using resilient queues via **Amazon Simple Queue Service (Amazon SQS)** (Workshop 000078), performing deep-dive architectural comparisons between Standard and FIFO queues while isolating malformed payloads via Dead-Letter Queues (DLQ).
- Establish pub/sub broadcasting and intelligent cross-domain event routing via **Amazon SNS** and **Amazon EventBridge**.
- Orchestrate resilient, distributed business state machines with automated error catching and retries using **AWS Step Functions**.
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and embedding asynchronous messaging pipelines into the **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Enterprise API Management & Hardening with API Gateway:** <br>- Comparing REST APIs vs HTTP APIs (features, latency profiles, unit economics). <br>- Configuring resources, HTTP methods, CORS policies, and direct Lambda integrations. <br>- Authoring custom Lambda Authorizers to validate JSON Web Tokens (JWT). <br>- Implementing Usage Plans, API Keys, and Token Bucket rate limiting. | 11/16/2026 | 11/16/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Tuesday** | **System Decoupling & Asynchronous Queuing with Amazon SQS:** <br>- Evaluating high-throughput Standard Queues vs strictly ordered FIFO Queues. <br>- Optimizing poll efficiency and reducing costs via Long Polling (`ReceiveMessageWaitTimeSeconds = 20s`). <br>- Tuning Visibility Timeout parameters to prevent concurrent duplicate message processing. <br>- Establishing Dead-Letter Queues (DLQ) with redrive policies for fault isolation. | 11/17/2026 | 11/17/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Wednesday** | **Pub/Sub Messaging & Event Orchestration with SNS & EventBridge:** <br>- Constructing the Fanout pattern: Subscribing multiple independent SQS queues to one SNS topic. <br>- Deploying default and custom event buses within Amazon EventBridge. <br>- Crafting declarative JSON event patterns to filter and route events based on payload attributes. | 11/18/2026 | 11/18/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thursday** | **Distributed Workflow Orchestration with AWS Step Functions:** <br>- Visualizing state machines in Workflow Studio using Amazon States Language (ASL). <br>- Combining Task, Choice (branching logic), Parallel, and Wait states. <br>- Configuring automated fault resilience with exponential backoff retries and catch blocks. | 11/19/2026 | 11/19/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Friday** | **Week 10 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate API Gateway, SQS queues, SNS topics, EventBridge, and Step Functions. <br>- **Worklog Completion:** Finalize bilingual Week 10 documentation and teardown lab resources. <br>- **Project Work:** Integrate asynchronous SQS buffering and Step Functions orchestration into the Capstone Proposal. | 11/20/2026 | 11/20/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Daily In-Depth Learning Outcomes & Key Takeaways:

#### 📌 Monday (11/16/2026) - Enterprise API Hardening via Amazon API Gateway

* **What did we learn today?**
  * **Architectural Trade-Offs: REST API vs HTTP API:**
    * *HTTP API:* Optimized for sub-millisecond overhead (up to 60% latency reduction), streamlined configuration, and over 70% cost savings compared to REST APIs, with native OIDC/OAuth2 authorization support.
    * *REST API:* Feature-complete enterprise gateway supporting Usage Plans, API Keys, request/response data mapping templates, AWS WAF integration, and private VPC interface endpoints.
  * **Token Authentication with Lambda Custom Authorizers:** Developed a serverless authorizer inspecting incoming `Authorization: Bearer <JWT>` headers. The function validates cryptographic signatures, generating an IAM policy document (`Effect: Allow`) granting resource execution only upon successful token validation.
  * **Traffic Shaping & Throttling Guards:** Implemented the token bucket algorithm enforcing a steady-state rate limit of 100 requests/sec with a burst buffer of 200 requests. When requests exceed limits, the gateway returns HTTP `429 Too Many Requests`, safeguarding downstream database connections.
* **Encountered Challenges & Solutions:**
  * *Browser CORS Restrictions:* Frontend single-page applications were blocked by browser cross-origin security. Root cause: Missing `OPTIONS` pre-flight handlers and CORS headers. Solution: Enabled CORS on the API Gateway console, ensuring standard headers (`Access-Control-Allow-Origin: '*'`, `Access-Control-Allow-Headers: 'Content-Type,Authorization'`) were injected into all response schemas.

---

#### 📌 Tuesday (11/17/2026) - Decoupling & Reliable Queuing with Amazon SQS

* **What did we learn today?**
  * **Comparing Core Message Queue Modalities:**
    * *Standard Queue:* Provides virtually limitless transactional throughput and at-least-once delivery semantics, suitable for decoupled workloads tolerant of occasional out-of-order execution.
    * *FIFO Queue:* Strictly enforces first-in, first-out ordering and exactly-once processing using `MessageDeduplicationId` hashes and logical serialization via `MessageGroupId`.
  * **FinOps Optimization with Long Polling:** Replaced Short Polling with Long Polling (`ReceiveMessageWaitTimeSeconds = 20`), keeping connections open until messages arrive, eliminating millions of empty empty-receive API calls and slashing SQS billable requests by over 80%.
  * **Visibility Timeout Management:** Tuned `VisibilityTimeout = 30s`. When Worker A leases a message, it is hidden from other concurrent workers. If Worker A succeeds, it issues `delete_message`. If the worker crashes, the message reappears after 30 seconds for Worker B, ensuring zero message loss.
  * **Fault Isolation with Dead-Letter Queues (DLQ):** Attached `orders-dlq` to the main queue with `maxReceiveCount = 3`. Malformed payloads causing processing exceptions are automatically moved to the DLQ after 3 failed attempts, keeping the main processing line unblocked.
* **Encountered Challenges & Solutions:**
  * *Duplicate Processing from Premature Visibility Expiry:* Heavy worker tasks taking 45 seconds caused SQS to assume worker failure at the 30-second mark, redelivering the message to a second worker and generating duplicate database writes. Solution: Implemented heartbeat calls inside the worker logic invoking `change_message_visibility` to extend the processing lease dynamically.

---

#### 📌 Wednesday (11/18/2026) - Event Distribution with Amazon SNS & EventBridge

* **What did we learn today?**
  * **The Fanout Distribution Topology:** Created an Amazon SNS Topic `order-created-topic` with three independent SQS queue subscribers (`billing-queue`, `inventory-queue`, and `shipping-queue`). A single published order event fans out concurrently, allowing all three domains to process payloads in parallel without knowing about each other.
  * **Enterprise Event Bus via Amazon EventBridge:** Explored the structural advantages of EventBridge for content-based message filtering directly on incoming JSON payload keys.
  * **Declarative Filtering Rules:** Authored an Event Pattern rule to route high-value transactions ($1,000+) directly into an accelerated audit workflow:
    ```json
    {
      "source": ["ecommerce.orders"],
      "detail-type": ["OrderCreated"],
      "detail": {
        "amount": [{ "numeric": [">=", 1000] }]
      }
    }
    ```
* **Encountered Challenges & Solutions:**
  * *SQS Subscribers Not Receiving SNS Messages:* Subscriptions were active but subscriber queues remained empty. Root cause: SQS queue Access Policies lacked explicit permissions allowing the SNS Topic ARN to perform `sqs:SendMessage`. Solution: Updated the SQS resource-based access policy to authorize the SNS topic principal.

---

#### 📌 Thursday (11/19/2026) - Visual Workflow Orchestration with AWS Step Functions

* **What did we learn today?**
  * **Declarative State Machines via Workflow Studio:** Decoupled business orchestration logic from application runtimes, modeling workflows using the Amazon States Language (ASL).
  * **State Flow Coordination:**
    * *Task State:* Invokes AWS Lambda functions or publishes messages to Amazon SQS.
    * *Choice State:* Evaluates branching logic based on runtime JSON values (e.g., verifying customer account balances).
    * *Parallel State:* Concurrently executes independent sub-workflows (e.g., triggering billing and dispatching email notifications simultaneously).
  * **Resilience & Fault Recovery:** Integrated automated `Retry` blocks configured with exponential backoff (`BackoffRate = 2.0`), coupled with `Catch` handlers to initiate compensating transaction rollbacks when encountering unrecoverable errors.
* **Encountered Challenges & Solutions:**
  * *State Input/Output JSON Path Mismatches:* State executions failed because previous Lambda responses returned deeply nested structures, causing subsequent Choice states to evaluate empty paths. Solution: Standardized state contracts using JSONPath filters: `InputPath`, `ResultPath`, and `OutputPath` to shape payloads cleanly across state transitions.

---

#### 📌 Friday (11/20/2026) - Week 10 Review, Worklog Finalization & Capstone Architecture Integration

* **What did we learn today?**
  * **Serverless Architectural Synthesis:** Connected the end-to-end event-driven chain: client ingestion (API Gateway) ➔ load leveling (SQS) ➔ event fanout (SNS/EventBridge) ➔ resilient business orchestration (Step Functions).
  * **Clean Teardown Practices:** Terminated temporary Step Functions state machines, deleted experimental SQS queues, and detached test API Gateway endpoints to avoid ongoing account charges.
  * **Graduation Capstone Integration:** Architected asynchronous order ingestion and transaction processing state machines for the Capstone Project, eliminating synchronous inter-service blocking and single points of failure.
