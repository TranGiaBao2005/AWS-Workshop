---
title: "Blogs Posted"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

This section indexes in-depth technical blogs and cloud architectural analyses published to the [AWS Study Group - First Cloud Journey](https://www.facebook.com/groups/awsstudygroupfcj) community.

---

### [3.1. Introducing AWS Continuum for Code Vulnerabilities](3.1-Blog1/)

- **Original Publication Source:** [AWS News Blog (October 22, 2026)](https://aws.amazon.com/blogs/aws/aws-continuum-for-code-vulnerabilities-is-now-generally-available/)
- **Author:** Esra Kayabali (Principal Solutions Architect at AWS)
- **Community Post Proof:** [View published post on AWS Study Group Facebook](https://www.facebook.com/groups/awsstudygroupfcj/posts/2319591015472524/)
- **Summary:** An in-depth architectural exploration of **AWS Continuum for code vulnerabilities**, generally available as of October 22, 2026. Continuum establishes an autonomous DevSecOps paradigm by constructing a bidirectional Context Graph merging repository source code with live AWS infrastructure telemetry (AWS Config, VPC routing, IAM). It actively validates exploitable vulnerabilities inside isolated sandboxes with reproducible proof-of-concept tests and leverages frontier AI models to synthesize code patches delivered directly as automated Pull Requests on GitHub/GitLab, upholding strict human-in-the-loop review controls.

---

### [3.2. Session Policies in Amazon EKS Pod Identity](3.2-Blog2/)

- **Core Topic:** Fine-grained least-privilege access management with inline session policies in Amazon EKS Pod Identity.
- **Summary:** Architectural analysis on narrowing pod-level IAM permissions dynamically without multiplying IAM roles. Eliminates over-permissioning risks, prevents IAM role limits exhaustion, and simplifies cluster governance.

---

### [3.3. Optimizing Performance and Cost with Amazon S3 Express One Zone](3.3-Blog3/)

- **Core Topic:** Single-digit millisecond latency data access with up to 50% lower request charges.
- **Summary:** Detailed exploration of Amazon S3 Express One Zone storage class for latency-sensitive cloud workloads including AI/ML model training, interactive big data analytics, and high-speed temporary caching.
