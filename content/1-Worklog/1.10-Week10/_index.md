---
title: "Week 10 Worklog"
date: 2026-11-16
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

![Cloud Journey Roadmap](/images/1-Worklog/Cloud-Journey-1.png)

### Week 10 Objectives:

- Master the **Event-Driven Architecture (EDA)** paradigm and modern asynchronous distributed system design patterns on AWS.
- Architect, publish, and secure enterprise API endpoints using **Amazon API Gateway** (REST APIs, HTTP APIs, Lambda Authorizers, CORS, and Throttling).
- Implement decoupled microservices and burst-load smoothing via resilient message queues using **Amazon Simple Queue Service (Amazon SQS)** (Standard vs FIFO, Dead-Letter Queues - DLQ).
- Establish pub/sub messaging patterns and intelligent cross-account event routing utilizing **Amazon SNS** and **Amazon EventBridge**.
- Orchestrate complex, multi-step distributed business workflows with automated state transitions, error handling, and retries via **AWS Step Functions (State Machines)**.
- Dedicate Friday to synthesizing technical competencies, finalizing bilingual Worklog documentation, and integrating asynchronous queuing patterns into the **Capstone Project Proposal**.

---

### Tasks to be Carried Out This Week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :---: | :---: | :--- |
| **Monday** | **Enterprise API Management & Protection with Amazon API Gateway:** <br>- Comparing REST APIs vs HTTP APIs and implementing optimal endpoint types. <br>- Configuring routes, HTTP methods, CORS policies, and direct AWS Lambda integrations. <br>- Establishing Usage Plans, API Keys, and token bucket Rate Limiting to prevent DDoS. | 11/16/2026 | 11/16/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Tuesday** | **System Decoupling & Asynchronous Buffering with Amazon SQS:** <br>- Provisioning high-throughput Standard Queues vs strictly ordered FIFO Queues. <br>- Configuring Visibility Timeout, Message Retention, and Long Polling optimizations. <br>- Designing Dead-Letter Queues (DLQ) with redrive policies for automated error isolation. | 11/17/2026 | 11/17/2026 | [Serverless Workshop (000078)](https://000078.awsfcaj.com/) |
| **Wednesday** | **Pub/Sub Messaging & Event Orchestration with SNS & EventBridge:** <br>- Implementing the Fanout pattern: Subscribing multiple independent SQS queues to an SNS topic. <br>- Establishing default and custom event buses within Amazon EventBridge. <br>- Crafting JSON-based event pattern rules to enable content-based message filtering. | 11/18/2026 | 11/18/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Thursday** | **Distributed Workflow Orchestration with AWS Step Functions:** <br>- Authoring visual state machines via Workflow Studio using Amazon States Language (ASL). <br>- Orchestrating Task, Choice, Parallel, and Wait states across decoupled services. <br>- Implementing resilient error catching and exponential backoff retry policies. | 11/19/2026 | 11/19/2026 | [Cloud Journey - Modernize](https://cloudjourney.awsfcaj.com/4-modernize/) |
| **Friday** | **Week 10 Review, Worklog Completion & Project Work:** <br>- **Knowledge Review:** Consolidate API Gateway, SQS queues, SNS pub/sub, EventBridge, and Step Functions. <br>- **Worklog Completion:** Finalize bilingual Week 10 documentation and teardown lab resources. <br>- **Project Work:** Integrate asynchronous SQS buffering and Step Functions orchestration into the Capstone Proposal. | 11/20/2026 | 11/20/2026 | [FCAJ Roadmap](https://cloudjourney.awsfcaj.com/) |

---

### Week 10 Achievements:

#### 📌 Monday (11/16/2026) - API Security via Amazon API Gateway:
* **Production API Hardening:** Deployed a high-performance HTTP API acting as the unified entry point for backend microservices. Enforced strict CORS headers and validated JWT bearer tokens via custom Lambda Authorizers.
* **Traffic Shaping:** Enforced a Usage Plan with a steady-state rate limit of 100 requests/sec and a burst limit of 200 requests, safeguarding downstream database services against traffic surges.

#### 📌 Tuesday (11/17/2026) - Asynchronous Decoupling with Amazon SQS:
* **Load Leveling:** Introduced message queuing between the user-facing web ingestion layer and heavy compute consumers, smoothing spiky traffic patterns and preventing cascading application failures.
* **Fault Isolation via DLQ:** Configured a Dead-Letter Queue with a `maxReceiveCount` of 3. Poison messages and malformed payloads are automatically routed to the DLQ, preserving pipeline throughput without dropping business records.

#### 📌 Wednesday (11/18/2026) - Event Distribution with SNS & EventBridge:
* **Decoupled Fanout Topology:** Published atomic order events to an Amazon SNS topic that concurrently fan out to billing, inventory, and analytics SQS subscribers, maintaining clean separation of concerns.
* **Declarative Filtering:** Applied EventBridge rule patterns to inspect incoming JSON attributes, ensuring subscriber services only process events strictly relevant to their business domain.

#### 📌 Thursday (11/19/2026) - Workflow Orchestration with AWS Step Functions:
* **Visual State Machine:** Engineered a multi-step order execution pipeline (Inventory Reservation -> Payment Capture -> Fulfillment -> Notification) with transparent visual execution tracking on the AWS Console.
* **Fault-Tolerant Resilience:** Built automated retry policies with randomized exponential backoff jitter, effectively neutralizing transient network drops and downstream API rate limits.
