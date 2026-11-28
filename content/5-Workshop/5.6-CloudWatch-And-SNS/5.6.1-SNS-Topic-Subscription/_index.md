---
title : "Create SNS Topic & Email Subscription"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.6.1. </b> "
---

#### Step 1: Create the `exammaker-dev-alerts` SNS Topic

1. Open **Amazon SNS** in `ap-southeast-1` → select **Topics → Create topic**.
2. Configure:
  * *Type:* `Standard`
  * *Name:* `exammaker-dev-alerts`
  * *Display name:* `ExamMakerAlert` (Max message size: `256` KiB)
3. Click **Create topic**.

![Create Amazon SNS Topic exammaker-dev-alerts](/images/5-Workshop/5.6-CloudWatch-And-SNS/13.png)

#### Step 2: Subscribe Operations Team Emails

1. Inside the `exammaker-dev-alerts` topic, click **Create subscription**.
2. Select **Protocol:** `Email` and enter the engineering team email addresses (**4 email subscribers**).
3. Click **Confirm subscription** in each confirmation email so the status transitions to `Confirmed`.

![Subscribe engineering emails to the SNS topic](/images/5-Workshop/5.6-CloudWatch-And-SNS/13.2.png)
