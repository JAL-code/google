+Storing Data in the Cloud

Two types of storage: 

    Traditional storage technologies, like block storage.
    Newer technologies, like object or blob storage.

Block storage in the Cloud acts almost exactly like a hard drive. The operating system of the virtual machine will create and manage a file system on top of the block storage just as if it were a physical drive.  These are virtual disks, so we can easily move the data around.  We can migrate the information on the disk to a different location, attach the same disk image to other machines, or create snapshots of the current state.

Persistent storage is used for instances that are long lived, and need to keep data across reboots and upgrades.

On the flip side, ephemeral storage is used for instances that are only temporary, and only need to keep local data while they're running.

In typical Cloud setups, each VM has one or more disks attached to the machine. The data on these disks is managed by the OS and can't be easily shared with other VMs.  To share data across instances, you might want to look into some *shared file system solutions,* that Cloud providers offer using the platform as a service model.  Data can be accessed through network file system protocols like NFS or CIFS. You can connect many different instances or containers to the same file system with no programming required.

Block storage and shared file systems work fine when you're managing servers that need to access files.

Blob storage is good to store application data for/as objects  Object storage lets you place in retrieve objects in a storage bucket.  Generic files can include items like photos or videos.  They are encoded and stored on disk as binary data.  These files are commonly called blobs, which comes from *binary large object,* and as we called out, these blobs are stored in locations known as *buckets.

Everything that you put into a storage bucket has a unique name.  There is no file system.
If you want that object back, you simply ask for it by name.  However, you will need to use an API or special utilities that can interact with the specific object store that you're using.

Most Cloud providers offer databases as a service.
    SQL 
    NoSQL.

SQL databases, also known as relational, use the traditional database format and query language.  Data is stored in tables with columns and rows that can be indexed, and we retrieve the data by writing SQL queries.  They are typically chosen when migrating an existing application to the Cloud.

NoSQL databases offer a lot of advantages related to scale.  They can be distributed across tons of machines and are super fast when retrieving results.  You need to use a specific API provided by the database.  Also, usage requires the need to rewrite the portion of the application that accesses the DB.  You'll also have to choose a *storage class*.
Variables like performance, availability, or how often the data is accessed will affect the monthly price.

Important factors: throughput, IOPS, and latency.

Throughput is the amount of data that you can read and write in a given amount of time.  Throughput of one gigabyte per second for reading and 100 megabytes per second for writing.

IOPS or input/output operations per second measures how many reads or writes you can do in one second, no matter how much data you're accessing.  Each read or write operation has some overhead.

Latency is the amount of time it takes to complete a read or write operation.  This takes into account the impact of IOPS, throughput and the particulars of the specific service.

Read latency is sometimes reported as the time it takes a storage system to start delivering data after a read request has been made, also known as *time to first byte.*

write latency is typically measured as the amount of time it takes for a write operation to complete.

Choosing the storage class to use, you might come across terms like hot and cold.
    
    Hot data is accessed frequently and stored in hot storage. Hot storage back ends are usually built using solid state disks, which are generally faster than the traditional spinning hard disks.
choose to keep the last one year of data in hot storage.

    After a year, you can move your data to cold storage where you can still get to it, but it will be slower and possibly costs more to access.
    
+Load Balancing

To handle loads:

Get more than one machine or container running our service.
To horizontally scale our service to handle more work, distribute instances geographically to get closer to our users.
Backup instances to keep the service running if one or more of the other instances fail.
Use orchestration tools and techniques to make sure that the instances are repeatable.
With our replicated machines, we'll want to distribute the requests across instances.

What is load balancing? 

Look at a round robin DNS.  Round robin is a really common method for distributing tasks. Like handing out cookies the party.  Every user gets one cookie.  Then the server gives everyone a second serving 
until all of the treats are gone.

To translate a URL like my service.example.com into an IP address, we use the DNS protocol or domain name system.  Just like the example above, Clients are served in turn.
The URL always gets translated into exactly the same IP address.  For a DNS to use round robin, it'll give each client asking for the translation a group of IP addresses in a different order.
The clients will then pick one of the addresses.  If an attempt fails, the client will jump to another address.

First, you can't control which addresses get picked by the clients.  And you can't stop the clients from reaching out to your service.

DNS records are cached by the clients and other servers.  Change the list of addresses for the instances, you'll have to wait until all of the DNS records that were cached by the clients expire.

We can set up a server as a dedicated load balancer.  The machine that acts as a proxy between the clients and the servers.  It directs them to the selected back-end server.

Say your service needs to keep track of the actions that a user has taken up till now. In this case, you'll want your load balancer to use sticky sessions.
Using sticky sessions means all requests from the same client always go to the same back end server.

Load balancers are great because you can configure them to check the health of the backend servers. If a back-end server is unhealthy, the load balancer will stop sending new requests to it to keep only healthy servers in the pool.

Cool feature of cloud infrastructure is how easily we can add or remove machines from a pool of servers providing a service.  Adding a new machine to the pool is as easy as creating the instance. And then letting the load balancer know that it can now route traffic to it.
manually creating and adding the instance or when our services under heavy load, we can just let the auto scaling feature do it.

How to make sure that clients connect to the servers that are closest to them?

Geo DNS and GeoIP.

Most Cloud providers offer it as part of their services making it much easier to have a geographically distributed service.  There are some providers dedicated to bringing the contents of your services as close to the user as possible. These are the content delivery networks or CDNs.
network of physical hosts that are geographically located as close to the end user as possible.  Often in the same data center as the users Internet service provider.  Caching content super close to the user.

Video's are stored in the closest CDN server. That way, when a second user in the same region requests the same video, it's already cached in a server that's pretty close and it can be downloaded extra fast.

+Change Management

Change management: How to keep the service running and make changes in a controlled and safe ways.  Lets us keep innovating while our services keep running.

Step one in improving the safety of our changes, we have to make sure they're well-tested.
Running unit tests and integration tests, and then running these tests whenever there's a change.

CI means the software is built, uploaded and tested constantly.
Continuous integration, or CI, A continuous integration system will build and test our code every time there's a change.
Service runs even for changes that are being reviewed.  This in necessary before they're merged into the main branch.
open source CI system like Jenkins, or if you use GitHub, you can use its Travis CI integration.

Now you can use continuous deployment, or CD, to automatically deploy the results of the build or build artifacts.
Continuous deployment lets you control the deployment with rules.
    
    configure our CD system to deploy new builds only when all of the tests have passed successfully.

    configure our CD to push to different environments based on some rules.

The service should have a test environment separate from the production environment.  Validate that changes work correctly before they affect users.

Environment means everything needed to run the service.  

    the machines and networks used for running the service
    the deployed code
    the configuration management
    the application configurations
    the customer data

Production, usually shortened to prod, is the real environment, the ones users see and interact with.

The test environment needs to be similar enough to prod that we can use them to check our changes work correctly. You could have your CD system configured to push new changes to the test environment.
Check that the service is still working correctly there, and then manually tell your deployment system to push those same changes to production.

For example, you might have your CD system push all new changes to a development or dev environment, then have a separate environment called pre-prod, which only gets specific changes after approval.
And only after a thorough testing, these changes get pushed to pro.  You want to deploy it to one of those testing or development environments to make sure it works correctly before you ship it to prod.
These environments need to be as similar to prod as possible, built and deployed in the same way.

In A/B testing, some requests are served using one set of code and configuration, A, and other requests are served using a different set of of code and configuration, B.

Deploy one instance group in your A configuration and a second instance group in your B configuration. Then by changing the configuration of the load balancer, you can direct different percentages of inbound requests to those two configurations.  Add basic monitoring, to compare A or B performances.  Becareful though, the value of A/B testing can be lost to A/B debugging.

Remember what we discussed in an earlier course about post-mortems. We learn from failure and we build the new knowledge into our change management.

Can I have one of my change management systems look for problems like that in the future? 
Can I add a test or a rule to my unit tests, my CI/CD system, or my service health checks to prevent this kind of failure in the future?
