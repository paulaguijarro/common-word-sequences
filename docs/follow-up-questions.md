# Follow up questions

* What are the steps needed to have this program (or any application) ready for production?

Use multi-thread and asynchronous tools to improve the way we handle operations.
Instrument the code for logging, this will help to monitor our application and help during troubleshooting.
Build a CI/CD pipeline to deliver the application to production.
Provision of the infrastructure we will be using to host/run the application (decide between using servers or a serverless architecture)
Using gitops: create infrastructure as code, so we can automate the process of provisioning the infrastructure.

* What would be the advantages or disadvantages of having a program like this running in a distributed system with a container-orchestration platform?

An advantage of using a container-orchestration platform like EKS, AKS or GKE, is that we can take advantage of all the performance, scalability of these cloud providers' infrastructure without having to manage the infrastructure. We will only need to worry about selecting the right server types for running their workloads.
But, having a managed or hosted Kubernetes cluster will be too expensive and overkill for hosting this simple application, so I will discard this option.
AWS Fargate or AWS lambda would be an option to consider to run the code without managing servers.

* How would you scale this if you needed to support millions of requests simultaneously?

Monitor the application and make a capacity plan to know how many requests we can handle so we can prepare our infrastructure accordingly.
In case of being using instances, create an autoscaling group and use a load balancer in front of our servers to distribute the requests between the group of instances.
Use a cache for the results of the requests to reduce the load on the servers.
