---
title : "Clean up"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

This guide covers the complete teardown procedure for all **AI Exam Maker** infrastructure resources in the **`ap-southeast-1` (Singapore)** region after the final presentation and grading, ensuring zero unexpected background charges.

{{% notice info %}}
**Operational Note (if only pausing overnight before the demo day):**
When you only choose `Stop temporarily` on **Amazon RDS (`exammaker-dev-pg`)**, AWS keeps the stopped state for a maximum of **7 days** and will **automatically restart the database after 7 days**, resuming hourly billing. Therefore, once the course is finished, you must execute the **complete Cleanup procedure** in the dependency order below.
{{% /notice %}}

---

#### Step 1: Empty and Delete Storage S3 Buckets

Amazon S3 does not allow deleting a non-empty bucket directly, so each bucket must be emptied (`Empty`) before deletion (`Delete`):

1. Open **Amazon S3** → in the left navigation pane, select **General purpose buckets** `(1)`.
2. Select the 2 project buckets in the `ap-southeast-1` region one by one `(2)` (including the static frontend bucket and the backend release artifacts bucket).
3. Click **Empty** `(3)` → enter `permanently delete` to remove all objects and versions inside.
4. Return to the bucket list, select the bucket again, and click **Delete** `(4)` to permanently remove the bucket.

![Empty and Delete S3 Buckets](/images/5-Workshop/5.6-Cleanup/4.png)

---

#### Step 2: Delete Amazon RDS PostgreSQL Database & Check Snapshots

1. Open **Aurora and RDS** → in the left navigation pane, select **Databases** `(1)`.
2. Select the **`exammaker-dev-pg`** instance `(2)` *(Note: if `Deletion protection` was enabled before the demo, click **Modify** → uncheck *Enable deletion protection* → select *Apply immediately* before deleting)*.
3. Click **Actions** `(3)` → select **Delete** `(4)`.

![Select Delete on Amazon RDS PostgreSQL](/images/5-Workshop/5.6-Cleanup/5a.png)

4. In the **Delete exammaker-dev-pg instance** confirmation dialog:
   - **Uncheck** `Create final snapshot` (avoids $0.095/GB-month snapshot storage fees).
   - **Uncheck** `Retain automated backups` (prevents retaining billable automated backups after deletion).
   - Type `delete me` into the confirmation field and click **Delete**.

![Confirm RDS deletion without final snapshot or automated backups](/images/5-Workshop/5.6-Cleanup/5a1.png)

{{% notice warning %}}
**Additional Check (Manual Snapshots):** Manual snapshots created before major migrations or recovery drills **are not automatically deleted** when the DB instance is removed. After the step above, go to **Snapshots → Manual tab** in the left menu and delete any remaining project snapshots via **Actions → Delete snapshot**.
{{% /notice %}}

---

#### Step 3: Terminate EC2 Instance & Check Unattached EBS Volumes

1. Open **EC2** → in the left navigation pane, select **Instances** `(1)`.
2. Check the **`aem-exammaker-ec2`** (`t4g.small`) instance `(2)`.
3. Click **Actions** (or **Instance state**) `(3)` → select **Terminate (delete) instance** `(4)`.

![Select Terminate on EC2 instance aem-exammaker-ec2](/images/5-Workshop/5.6-Cleanup/6a.png)

4. In the **Terminate (delete) instance** confirmation dialog, verify the default notice stating that the root EBS volume (`30 GiB gp3`) will be automatically deleted with the instance, then click **Terminate (delete)**.

![Confirm EC2 termination along with root EBS volume](/images/5-Workshop/5.6-Cleanup/6a1.png)

{{% notice warning %}}
**Additional Check (Unattached EBS Volumes):** Once the EC2 instance transitions completely to `Terminated`, open **Elastic Block Store → Volumes** in the left menu and filter by `Volume state = Available` (detached volumes not attached to any instance). If any `Available` volumes remain, select **Actions → Delete volume** to avoid $0.096/GB-month storage charges.
{{% /notice %}}

---

#### Step 4: Release Static Elastic IP Address — *Most Important*

AWS charges **$0.005/hour (~$3.65/month)** for every Public IPv4 / Elastic IP address allocated to an account, even after the associated EC2 instance has been terminated.

1. In the **EC2** console, scroll down the left menu to **Network & Security → Elastic IPs** `(1)`.
2. Check the project's **`aem-exammaker-eip`** address `(2)` (ensure this is performed after terminating or disassociating from EC2).
3. Click **Actions** `(3)` → select **Release Elastic IP addresses** `(4)` → click **Release** to return the IP address to AWS.

![Release Elastic IP aem-exammaker-eip](/images/5-Workshop/5.6-Cleanup/7.png)

---

#### Step 5: Audit High-Cost Network Resources & Clean Up Supporting Services

1. **Verify Zero Load Balancers & NAT Gateways:**
   - Check **EC2 → Load Balancing → Load Balancers** to confirm the list is empty (`0 load balancers`).
   - Check **VPC → NAT gateways** to confirm the list is empty (`0 NAT gateways` — adhering to the $200 budget-optimized architecture).

![Verify zero Load Balancers in ap-southeast-1](/images/5-Workshop/5.6-Cleanup/8b.png)

2. **Clean Up Remaining Configuration & Monitoring Services (Account Hygiene):**
   - **Amazon Route 53 (if using an AWS Hosted Zone):** open **Hosted zones**, delete the project's custom `A`/`CNAME` records, and delete the Hosted Zone (avoiding the fixed **$0.50/month/zone** maintenance fee).
   - **Amazon CloudWatch & SNS:** delete the `/exammaker/dev/app` Log Group, delete the 10 `exammaker-dev-*` Alarms, and delete the `exammaker-dev-alerts` SNS Topic.
   - **Amazon SQS:** delete the 2 queues `exammaker-dev-ai-jobs` and `exammaker-dev-ai-jobs-dlq`.
   - **Amazon Cognito:** delete the `exammaker-dev-users` User Pool.
   - **AWS Systems Manager Parameter Store:** delete configuration parameters under `/exammaker/dev/*` and `/exammaker-ops/dev/*`.
   - **IAM & VPC:** delete the project IAM roles (`aem-exammaker-ec2-role`, `aem-github-*-deploy-role`) and delete the `aem-demo-vpc` VPC (associated free Subnets, Route Tables, Internet Gateway, and Security Groups will be removed along with the VPC).
   - **Final Verification:** after 24 hours, open **AWS Billing and Cost Management → Bills** to confirm no services continue accruing hourly charges.
