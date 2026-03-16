## AWS Cloud databases
AWS offers a variety of managed database services to support different use cases and workloads. 
These services are designed to be scalable, reliable, and secure, allowing you to focus on your applications rather than managing infrastructure.
Breaking free from traditional database management, AWS Cloud databases provide a range of features and benefits

8 database types: 

1. Relational Databases
Usecases:
- Online transaction processing (OLTP)
- Data warehousing
- Content management systems (CMS)
AWS Services:
- Amazon RDS (Relational Database Service)
- Amazon Aurora
- Amazon Redshift

2. Key-Value Databases
Usecases:
- Session management
- Shopping cart data
- Real-time analytics
AWS Services:
- Amazon DynamoDB

3. In-Memory Databases
Usecases:
- Caching
- Real-time analytics
- Session management
AWS Services:
- Amazon ElastiCache
- Amazon MemoryDB for Redis

4. Document Databases
Usecases:
- Content management
- Catalogs
- User profiles
AWS Services:
- Amazon DocumentDB
5. Wide column Databases
Usecases:
- IoT data
- Time-series data
- Event logging
AWS Services:
- Amazon Keyspaces

6. Graph Databases
Usecases:
- Social networks
- Recommendation engines
- Fraud detection
AWS Services:
- Amazon Neptune

7. Time-Series Databases
Usecases:
- IoT data
- DevOps monitoring
- Financial market data
AWS Services:
- Amazon Timestream

8. Ledger Databases
Usecases:
- Financial transactions
- Supply chain tracking
- Identity verification
AWS Services:
- Amazon QLDB (Quantum Ledger Database)

AWS Service: 

## Amazon Aurora
Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. 
It offers up to five times the performance of standard MySQL databases and three times the performance of standard PostgreSQL databases. Aurora is designed for high availability and durability, with automatic backups and replication across multiple Availability Zones.

## Amazon RDS (Relational Database Service)
Amazon RDS is a managed relational database service that supports multiple database engines, including MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server. 
It automates tasks such as backups, patching, and scaling, making it easier to manage relational databases in the cloud.
Launch database in the Multi-AZ deployment for high availability.
The service will launch the primary and standby databases in different Availability Zones and set up synchronous replication of data and failover strategy. 
If the primary database goes down, the standby picks up the traffic.

## Amazon Redshift
Amazon Redshift is a fully managed data warehouse service that allows you to analyze large amounts of data using SQL and your favorite business intelligence tools. It is optimized for online analytical processing (OLAP) and can handle petabyte-scale data warehousing.

### Key - Value database

## Amazon DynamoDB (NoSQL)
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. 
It is designed for applications that require low-latency data access and can handle large amounts of traffic. DynamoDB supports both key-value and document data models.
With DynamoDB, you can achieve single-digit millisecond performance at any scale.
It is a fully managed, serverless, nonrelational database.
DynamoDB is a great choice when you're looking for seamless database scalability. DynamoDB will automatically scale to meet demand.
DynamoDB is also an excellent choice for workloads that involve working with databases, flexible schemas, and high throughput (with many read/write requests). 

Usecase - using Amazon DynamoDB for running Leaderboard would be a good use case.

### In-memory database

## Amazon ElastiCache
Amazon ElastiCache is a fully managed in-memory data store service that supports Redis and Memcached. 
It is designed to improve the performance of web applications by caching frequently accessed data, reducing the load on backend databases.
Unlock microsecond latency.
Scalable caching service.

## Amazon MemoryDB
Amazon MemoryDB is a fully managed, Redis-compatible, in-memory database service. 
It is designed for use cases that require microsecond read and low-latency write access to data.

### Document database

## Amazon DocumentDB
Amazon DocumentDB is a fully managed document database service that is compatible with MongoDB. 
It is designed for applications that require a flexible schema and the ability to store and query JSON-like documents.

### Graph database

## Amazon Neptune
Amazon Neptune is a fully managed graph database service that supports both property graph and RDF graph models. 
It is designed for applications that require complex relationships and connections between data points, such as social networks and recommendation engines.

### Wide column database

## Amazon Keyspaces
Amazon Keyspaces is a fully managed Apache Cassandra-compatible database service. It is designed for applications that require high availability and scalability, with the ability to handle large amounts of data across multiple regions.

### Time series database

## Amazon Timestream
Amazon Timestream is a fully managed time series database service designed for IoT and operational applications. 
It is optimized for storing and analyzing time-stamped data, making it easy to collect, store, and query time series data at scale.

### Ledger database

## Amazon QLDB
Amazon QLDB (Quantum Ledger Database) is a fully managed ledger database service that provides a transparent, immutable, and cryptographically verifiable transaction log. 
It is designed for use cases that require a centralized, authoritative data source with a complete history of changes, such as financial transactions and supply chain tracking.

### Benefits of AWS Cloud databases
- Fully managed: AWS takes care of database management tasks such as backups, patching, and scaling.
- Scalability: Easily scale your database up or down based on demand.
- High availability: AWS provides built-in redundancy and failover capabilities to ensure your database is always available.
- Security: AWS offers a range of security features, including encryption, access control, and network isolation.
