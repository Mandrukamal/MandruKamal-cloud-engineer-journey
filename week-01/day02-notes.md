## Serverless Computing
Definition: Serverless computing is building and running applications and services without managing servers.
# Key Features:
Serverless doesn't run idle resources so you pay what you need.
Automatic scaling
Pay-as-you-go pricing
Reduced operational complexity
Availability and fault tolerance built-in
# Popular Serverless Platforms:
AWS Lambda - per millisecond pricing, event-driven architectures, S3 or DynamoDB triggers, built-in logging and monitoring
Lambda offers per-millisecond pricing of the code being run.  Lambda can run your code on a schedule.  Lambda can run your code in response to events. However, Lambda supports multiple languages and provides high availability.
Azure Functions - integrates with Azure services, supports multiple programming languages, offers a consumption plan
Google Cloud Functions - lightweight, event-driven, supports HTTP triggers and background functions

## Containers orchestration

# Amazon ECS
a fully managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications using Docker on AWS.
# Amazon EKS 
a fully managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install and operate your own Kubernetes control plane or nodes.

Amazon ECS and Amazon EKS give you a centralized way of monitoring and controlling how you want your containers launched.
If you have in-house skills running Kubernetes, there is a fully managed Amazon EKS for you.
Amazon ECS and Amazon EKS are container orchestrating services that help you schedule the fleet of nodes running your containers.
Amazon ECS and Amazon EKS remove the complexity of standing up the infrastructure.