## Simple Storage Service (S3)
Amazon Simple Storage Service (Amazon S3) is a fully managed, serverless, low-cost, object-level storage service.
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. 
It is designed to store and retrieve any amount of data from anywhere on the web. 
S3 is commonly used for backup and restore, archiving, big data analytics, and as a data lake for machine learning.

# Amazon S3 Storage Classes
Amazon S3 offers a range of storage classes that you can choose from based on your workload's data access, resiliency, and cost requirements.

# Amazon S3 Standard
Amazon S3 Standard is designed for general-purpose storage of frequently accessed data. It offers high durability, availability, and performance. 
It is ideal for a wide range of use cases, including websites, content distribution, mobile applications, and big data analytics.

# Amazon S3 Intelligent-Tiering
Amazon S3 Intelligent-Tiering is designed to optimize costs for data with unknown or changing access patterns. 
It automatically moves data between two access tiers (frequent and infrequent) when access patterns change, without performance impact or operational overhead.
Delivers millisecond latency for frequently accessed data while optimizing costs for infrequently accessed data.

# Amazon S3 Standard-IA
Amazon S3 Standard-IA (Infrequent Access) is designed for data that is less frequently accessed but requires rapid access when needed. 
It offers lower storage costs compared to S3 Standard, making it ideal for long-term storage, backups, and disaster recovery.
High durability, High throughput, and low latency for rapid access to infrequently accessed data.
Low per GB storage cost compared to S3 Standard.

# Amazon S3 One Zone-IA
Amazon S3 One Zone-IA (Infrequent Access) is designed for data that is less frequently accessed but requires rapid access when needed. 
It offers lower storage costs compared to S3 Standard-IA, making it ideal for long-term storage, backups, and disaster recovery.
Amazon S3 Standard with a low per GB storage cost compared to S3 Standard-IA.

# More Amazon S3 Storage Classes

# Amazon S3 Glacier
Amazon S3 Glacier is designed for data archiving and long-term backup. It offers low-cost storage for data that is rarely accessed and can tolerate retrieval in milliseconds to several hours. 
It is ideal for use cases such as digital preservation, compliance archives, and media asset archiving.

# Amazon S3 Glacier Deep Archive
Amazon S3 Glacier Deep Archive is the lowest-cost storage class for data archiving. It is designed for data that is rarely accessed and can tolerate retrieval times of 12 hours or more. 
It is ideal for long-term data retention and compliance use cases.
Data that can be accessed once or twice a year.

# Amazon S3 Outposts
Amazon S3 Outposts is a fully managed storage service that extends S3's capabilities to on-premises environments. 
It is designed for workloads that require low-latency access to data stored on-premises while still benefiting from S3's scalability and durability.

# Amazon S3 Glacier Flexible Retrieval
Amazon S3 Glacier Flexible Retrieval is designed for data archiving and long-term backup. It offers low-cost storage for data that is rarely accessed and can tolerate retrieval in minutes to several hours. 
It is ideal for use cases such as digital preservation, compliance archives, and media asset archiving.

# Benefits of Amazon S3 Storage.
Highly durable storage with 99.999999999% (11 9's) durability.
Support for event triggers and notifications.

# Amazon S3 Usecases
Backup and restore - Amazon S3 Glacier
- Meet Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) and Compliance requirements.
Archiving - Amazon S3 Glacier Deep Archive
Big data analytics - Amazon S3 Standard
Data lake for machine learning - Amazon S3 Standard
Content distribution - Amazon S3 Standard
Media hosting - Amazon S3 Standard
Static website hosting - Amazon S3 Standard
Run Cloud-native applications - Amazon S3 Standard

## Other AWS Storage Services
Amazon Elastic Block Store (EBS) - Block storage for Amazon EC2 instances.
# Important points about EBS
EBS volumes are automatically replicated within their Availability Zone to protect against hardware failures.
Incremental snapshots allow you to back up only the changes made since the last snapshot, reducing storage costs.
EBS volumes can be attached to any running EC2 instance in the same Availability Zone.
EBS supports both SSD and HDD storage options for different use cases.
EBS volumes can be resized without downtime.

Amazon Elastic File System (EFS) - Fully managed file storage for use with Amazon EC2.
# Important points about EFS
- EFS provides a scalable and elastic file storage solution that grows and shrinks automatically as you add or remove files.
- EFS is designed to be highly available and durable, with data stored across multiple Availability Zones.
- EFS supports the NFS protocol, making it easy to integrate with existing applications that rely on file storage.

Amazon FSx - Fully managed file systems for Windows and Lustre.

# Important points about FSx
- FSx for Windows File Server provides a fully managed Windows file system with support for SMB protocol.
- FSx for Lustre is designed for high-performance workloads and is optimized for fast processing of large datasets.
- Both FSx options are integrated with other AWS services, making it easy to build and deploy applications.
