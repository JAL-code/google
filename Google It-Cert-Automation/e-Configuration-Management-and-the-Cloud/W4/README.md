Storing Data in the Cloud

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
