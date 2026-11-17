---
title : "Testing Gateway Endpoint Connectivity"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.3.2 </b> "
---

#### 1. Provision an Amazon S3 Bucket

1. Open the [Amazon S3 Management Console](https://s3.console.aws.amazon.com/s3/home?region=us-east-1).
2. Click **Create bucket**.

![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)

3. Configure General Settings:
   - **Bucket name:** Enter a globally unique name (e.g., `fcj-hybrid-s3-test-<your-name>`).
   - **AWS Region:** `us-east-1` (US East - N. Virginia).

![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)

4. Retain all default security configurations (Block all public access enabled). Scroll to the bottom and click **Create bucket**.

![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png)    

5. Verify that the bucket status is confirmed in the S3 bucket list.

![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)

---

#### 2. Establish Session Manager Shell to EC2

1. In the AWS console search bar, type **Systems Manager** and open the service.

![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)

2. From the left navigation menu, locate **Node Management** and select **Session Manager**.

![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)

3. Click **Start session** and select the EC2 instance named **`Test-Gateway-Endpoint`**.

> [!NOTE]
> This EC2 instance runs in an isolated private subnet of `VPC Cloud` with zero public IP addresses and no Internet Gateway. The interactive terminal functions entirely over private Systems Manager interface endpoints.

![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)

4. A new browser tab opens with the shell prompt: `sh-4.2$` (or `ssm-user@ip-10-0-x-x`).

![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)

---

#### 3. Generate 1GB Test Payload and Upload via AWS CLI

1. Switch to the `ssm-user` home directory:
   ```bash
   cd ~
   pwd
   ```

![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)

2. Generate a 1GB test file using the `fallocate` utility:
   ```bash
   fallocate -l 1G testfile.xyz
   ls -lh testfile.xyz
   ```

![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)

3. Upload the payload to the S3 bucket via AWS CLI (replace `<your-bucket-name>` with your actual bucket name):
   ```bash
   aws s3 cp testfile.xyz s3://<your-bucket-name>
   ```

![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)

The upload finishes rapidly over the AWS internal software-defined network.

---

#### 4. Confirm Upload in S3 Console

1. Return to the Amazon S3 Console and click your bucket name.
2. Under the **Objects** tab, verify that `testfile.xyz` (1.0 GB) is stored successfully.

![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)

---

#### 5. Technical Validation Summary

The successful 1GB file transmission validates that VPC Cloud routes traffic to Amazon S3 strictly over the private AWS backbone via the **Gateway VPC Endpoint (`s3-gwe`)**. No NAT Gateway or Internet Gateway is traversed, ensuring maximum throughput, zero egress data charges across the public internet, and robust network isolation.
