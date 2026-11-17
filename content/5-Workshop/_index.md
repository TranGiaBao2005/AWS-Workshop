---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Secure Hybrid Access to Amazon S3 via VPC Endpoints

#### Architecture Objectives
In hybrid cloud production environments, routing data transfers between on-premises datacenters and **Amazon S3** over the public internet introduces unnecessary latency, compliance risks, and data exposure. This workshop deploys a zero-trust network routing solution using two types of **VPC Endpoints**:

1. **Gateway VPC Endpoint (AWS VPC Workloads):** Routes traffic from EC2 instances to Amazon S3 directly using VPC route tables, requiring zero public IP assignment, NAT Gateway, or Internet Gateway (IGW).
2. **Interface VPC Endpoint / AWS PrivateLink (On-Premises Workloads):** Provisions dedicated private IP addresses (Elastic Network Interfaces - ENIs) inside the VPC, enabling on-premises servers to communicate with S3 over an IPsec Site-to-Site VPN tunnel or AWS Direct Connect.

```
[On-Premises Data Center] 
       │ (IPsec VPN / Direct Connect)
       ▼
[AWS Transit Gateway] 
       ▼
[Interface Endpoint (ENI Private IP)] ────(AWS PrivateLink)────► [Amazon S3]
                                                                      ▲
[Cloud VPC EC2] ─────(Route Table: Gateway Endpoint)─────────────────┘
```

#### Workshop Roadmap

1. [5.1 Workshop Overview & Topology](5.1-Workshop-overview/) — Dual-VPC architecture connecting Cloud VPC and simulated On-Premises VPC.
2. [5.2 Prerequisites & Environment Provisioning](5.2-Prerequiste/) — Deploy base infrastructure via AWS CloudFormation and configure IAM policies.
3. [5.3 Accessing S3 from VPC via Gateway Endpoint](5.3-S3-vpc/) — Configure prefix list route tables and verify private 1GB payload transfers with AWS Systems Manager.
4. [5.4 Accessing S3 from On-Premises via Interface Endpoint](5.4-S3-onprem/) — Configure StrongSwan VPN routing, Interface Endpoints, and Route 53 Resolver conditional DNS forwarding.
5. [5.5 Restricting Access with VPC Endpoint Policies](5.5-Policy/) — Apply resource-level IAM policies to restrict endpoint access strictly to designated buckets.
6. [5.6 Resource Cleanup & Cost Governance](5.6-Cleanup/) — De-provision Private Hosted Zones, Resolver rules, endpoints, and CloudFormation stacks to avoid recurring idle costs.
