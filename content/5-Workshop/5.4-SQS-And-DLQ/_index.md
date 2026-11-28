---
title : "Amazon SQS & DLQ Setup"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

In this section, we set up asynchronous processing with **Amazon SQS** for AI question generation and validation jobs (15–45 seconds per job), consisting of a **Dead-Letter Queue** (`exammaker-dev-ai-jobs-dlq`) and a **Main Queue** (`exammaker-dev-ai-jobs`) configured with a **300-second visibility timeout**, **20-second Long Polling**, and a **Redrive Policy (`maxReceiveCount = 3`)**.

#### Section Contents

1. [5.4.1. Create Dead-Letter Queue — DLQ (Figure 8)](5.4.1-Create-DLQ/)
2. [5.4.2. Create Main Queue (Figure 9)](5.4.2-Create-Main-Queue/)
3. [5.4.3. Verify 2 SQS Queues (Figure 10)](5.4.3-Verify-Queues/)
