# After Every VPC Lab:

Step 1 → EC2 Instances
         EC2 → Instances → Select → 
         Instance State → Terminate

Step 2 → NAT Gateway (if created)
         VPC → NAT Gateways → Select → 
         Actions → Delete
         ⚠️ Wait until fully deleted before next step

Step 3 → Release Elastic IPs (if created)
         VPC → Elastic IPs → Select → 
         Actions → Release
         ⚠️ Elastic IPs cost money if not released!

Step 4 → Internet Gateway
         VPC → Internet Gateways → Select →
         Actions → Detach from VPC first →
         Then Actions → Delete

Step 5 → Subnets
         VPC → Subnets → Select each →
         Actions → Delete

Step 6 → Route Tables (custom ones only)
         VPC → Route Tables → Select →
         Actions → Delete
         ⚠️ Never delete the MAIN route table

Step 7 → Security Groups (custom ones only)
         VPC → Security Groups → Select →
         Actions → Delete
         ⚠️ Never delete the DEFAULT security group

Step 8 → Finally delete the VPC itself
         VPC → Your VPCs → Select →
         Actions → Delete

# 3 Golden Rules of Cleanup:

Rule 1 → Always delete in ORDER — resources
         inside first, VPC last

Rule 2 → NAT Gateway + Elastic IP = MONEY
         Delete these FIRST and FAST

Rule 3 → When in doubt — go to AWS Billing
         Dashboard and check for any
         unexpected charges

# Pro Tip — The Nuclear Option:

If you ever feel lost during cleanup, go to:

AWS Console → Resource Groups & Tag Editor
→ Tag Editor → Search all resources
→ See everything running in your account
→ Delete anything you don't recognize
