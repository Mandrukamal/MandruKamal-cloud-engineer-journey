### Lab02 - IAM Hands-On (45 mins)

## Task 1 — Create an IAM user:

Username: kamal-dev-user
Access: AWS Console access
No admin permissions yet

## Task 2 — Create a policy:

Service: S3
Actions: GetObject, ListBucket only
Resource: your bucket ARN

## Task 3 — Attach and test:

Attach policy to your user
Login as that user
Verify you can LIST the bucket
Verify you CANNOT delete anything
That's least privilege in action!