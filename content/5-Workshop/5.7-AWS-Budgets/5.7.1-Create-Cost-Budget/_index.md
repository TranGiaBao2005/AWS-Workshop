---
title : "Create $200.00 Quarterly Cost Budget"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.7.1. </b> "
---

#### Step 1: Choose Advanced Cost Budget Setup

1. Open **AWS Billing and Cost Management → Budgets → Create budget**.
2. Select `Customize (advanced)` → `Cost budget - Recommended`.

![Select Customize advanced and Cost budget](/images/5-Workshop/5.7-AWS-Budgets/16.png)

#### Step 2: Set Budget Name & $200.00 Quarterly Amount

* *Budget name:* `exammaker-200usd-budget`
* *Period:* `Quarterly`
* *Budget renewal type:* `Recurring budget`
* *Budgeting method:* `Fixed`
* *Budgeted amount:* `$200.00`

![Configure exammaker-200usd-budget with $200.00 quarterly ceiling](/images/5-Workshop/5.7-AWS-Budgets/16.2.png)

#### Step 3: Scope All AWS Services & Aggregate by `Unblended costs`

* *Budget scope:* `All AWS services (Recommended)`
* *Aggregate costs by:* `Unblended costs` (measures gross consumption before AWS Credits are applied, giving accurate visibility into real burn rate).

![Select All AWS services scope and Unblended costs aggregation](/images/5-Workshop/5.7-AWS-Budgets/16.3.png)
