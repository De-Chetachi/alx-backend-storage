#nosql
not only sql(structured query language)
does not use the tabular schema of rows and table found in rdbms
strengths
  storing unstructured date eg
	user and session data, chat, messaging, log data
	time serioes data like IoT and device data
	large objects eg video and images

# types / categories
key-value data stores - high-speed read and write processing of non transactional data, value can be any binary object eg text, video etc, values are accessed via a key. suitable for applications that deal with high-velocity, non-transactional data

Document stores: stores self-describing json, xml and bbson documents, similar to key-value but in this case the value is a document that stores all data related to a specific key.

Wide-column stores: stores data in tables with rows and cols similar to rdbms but names and formats of cols can vary from row to row across the table. group colums of related data together hence a query can retrieve related data in a single operation.

Graph stores: uses graph structure to store, map and query relationships, index-free adjacency, adjacent elements are linked together without using index


Multi-model databases leverages a combination of the four types described and can support a wider range of apps


#advantages
Scalability: (the ability of a product to function efficiiently as its users grow) uses a horizontal scale-out method that makes it easier to reduce or add capacity

Performance: enterprises can improve performance by simply adding commodity resources.

High Availability: masterless achitecture that automatically distributes data equally among multiple resources so the application is redundant.

Global Availability: automatically replicates data across multiple servers, data centers, cloud resources, it minimizes latency and consistent user experience irrespective of user location


Flexible Data Modeling
