# Networking

## Amazon Virtual Private Cloud (VPC)
Connecting to the resources running in the cloud.
End users connect to the applications deployed in the cloud.
VPC is a private network space that allows you to launch AWS resources in a logically isolated virtual network that you define.
More than one VPC can be created within a single AWS account.

### Private network
A private network is a virtual network that is isolated from other VPC or remote networks. ex: isolating production and development environments.
Can control the traffic flow in and out of amazon VPC and resources within it.
Can also control how to connect the VPC with other networks, such as on-premises data centers or other VPCs.
It allows you to securely connect your AWS resources to each other and to your on-premises network.

### Custom access controls and security settings for your resource
You can define custom access controls and security settings for your resources within a VPC. 
This includes configuring security groups, network access control lists (ACLs), and route tables to control inbound and outbound traffic to your resources.

# Amazon Route 53
Highly available and scalable Domain Name System (DNS) web service.
Route 53 will perform three main functions:
1. Domain registration
2. DNS routing
3. Health checking
DNS translates domain names into IP addresses, allowing users to access applications and services using human-readable names.
Can able to purchase and manage domain names and configure DNS settings for those domains.
Has multiple routing policies to control how traffic is directed to your resources.

## Benefits of Route 53
Reliable and highly available DNS service.
Scalable to handle large volumes of DNS queries.
Flexible routing policies to control traffic flow.
Integrated with other AWS services for seamless management.
Reduced latency for end users, enhancing application availability and ensuring compliance with regulatory requirements.

# Use Cases for Route 53
Manage network traffic globally.
Build highly available and fault-tolerant applications.
Set up private DNS for your applications.

# Elastic Load Balancing (ELB)
ELB is the load balancer service that automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses.
ELB automatically distributes incoming application traffic across multiple targets and virtual appliances in one or more Availability Zones (AZs).
It serves as single point of contact for your applications, improving availability and fault tolerance.