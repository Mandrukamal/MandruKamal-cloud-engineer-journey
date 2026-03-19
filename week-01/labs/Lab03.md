# Lab03 - VPC Architecture

## Building 

Your VPC (10.0.0.0/16)
├── Public Subnet  (10.0.1.0/24) ← EC2 lives here
└── Private Subnet (10.0.2.0/24) ← Database lives here
         │
    Internet Gateway
         │
      Internet

## Task - 1 - Create VPC (5 mins)

Go to → VPC → Your VPCs → Create VPC
Name       : kamal-dev-vpc
IPv4 CIDR  : 10.0.0.0/16
Tenancy    : Default

## Task - 2 - Create Subnets (10 mins)

Go to → Subnets → Create Subnet
Select     : kamal-dev-vpc

Subnet 1:
Name       : kamal-public-subnet
AZ         : ap-south-1a
CIDR       : 10.0.1.0/24

Subnet 2:
Name       : kamal-private-subnet
AZ         : ap-south-1b
CIDR       : 10.0.2.0/24

## Task - 3 - Create Internet Gateway (5 mins)

Go to → Internet Gateways → Create
Name       : kamal-igw
→ After creating, click Actions
→ Attach to VPC → select kamal-dev-vpc

## Task - 4 - Create Route Table (10 mins)

Go to → Route Tables → Create
Name       : kamal-public-rt
VPC        : kamal-dev-vpc

→ After creating:
→ Edit Routes → Add Route
Destination : 0.0.0.0/0
Target      : kamal-igw ← This is what makes it PUBLIC

→ Subnet Associations tab
→ Associate kamal-public-subnet with this route table

## Task - 5 - Launch EC2 in Public Subnet (10 mins)

Go to → EC2 → Launch Instance
Name            : kamal-public-ec2
AMI             : Amazon Linux 2023
Instance type   : t2.micro (free tier)
Key pair        : Create new → kamal-keypair
                  Download .pem file — SAVE IT!
Network         : kamal-dev-vpc
Subnet          : kamal-public-subnet
Auto-assign IP  : Enable
Security Group  : Create new
                  Allow SSH port 22
                  Source: My IP

## Task - 6 - Verify (5 mins)

→ Once EC2 is running check:
→ It has a Public IP address assigned ✅
→ It sits in kamal-public-subnet ✅
→ VPC shows kamal-dev-vpc ✅