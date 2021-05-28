Week 1, Quiz 1.

Modern IT is moving more and more towards Cloud-based solutions and having a solid background in how to manage them will be even more critical for IT professionals in the future.

What is scale?
What is configuration management?
You can treat code as infrastructure?
What are the benefits and challenges of moving services to the Cloud?

First what is a Site Reliablity Engineer?

1. focused on the reliability and maintainability of large system
2. scale support as the service grows  (Be samll but mighty!)
3. Collab with partner teams on reliability aspsets of new features. (scheduling email)
4. Write software and tools to help automate system management.
5. Do research or architectural design for new projects.
6. On-call rotation for the service support. Take charge of fixing tickets or if unable to fix, find the right team member.

Scale: 

How do you define scale? Start asking these questions.

will adding more servers increase the capacity of the service?
How are new servers prepared, installed, and configured?
How quickly can you set up new computers to get them ready to be used?
Could you deploy a hundred servers with the same IT team that you have today?
Or would you need to hire more people to get it done faster?
Would all the deployed servers be configured exactly the same way?

In short, a scalable system is a flexible one.  Being able to scale what we do means that we can keep achieving larger impacts with the same amount of effort when a system scales.
(1) Can rapidly hire new employees, with an onboarding process that can scale as needed.
(2) Applying the latest security policies and patches
(3) Making sure users' needs still get addressed all 
(4) More and more users join the network without new support staff to back the core team.
(5) Use automation as an essential tool for keeping up with the infrastructure needs of a growing business.
For example, we could deploy a whole new server by running a single command and letting the automation take care of the rest.
We could also create a batch of user accounts with all the necessary permissions based on data already stored in the database, eliminating all human interaction.

Configuration Management (CM) is an automation techique.  In this class our CM will use Puppet, the current industry standard for configuration management.  Qwiklabs which is an environment that allows you to test your code on a virtual machine running in the Cloud.

By manually deploying the installation and configuring the computer, we see that we're using unmanaged configuration.
current operating system and the applications installed to any necessary configuration files or policies, including anything else that's relevant for the server to do its job.
When you work in IT, you're generally in charge of the configuration of a lot of different devices, not just servers. Network routers printers and even smart home devices can have configuration that we can control.
a network switch might use a config file to set up each of its ports.
It means using a configuration management system to handle all of the configuration of the devices in your fleet, also known as nodes.
define a set of rules that have to be applied to the nodes you want to manage and then have a process that ensures that those settings are true on each of the nodes.
Configuration management systems aim to solve this scaling problem.
because the system will deploy the configuration automatically no matter how many devices you're managing.
Instead, you edit the configuration management rules and then let the automation apply those rules in the affected machines.
systematic, repeatable way.
Being repeatable is important because it means that the results will be the same on all the devices.
some application
to be very insecure.
add rules to your configuration management system to improve the settings on all computers.
It will continue to monitor the configuration going forward.
user changes the settings on their machine, the configuration management tooling will detect this change and reapply the settings you defined in code.
Puppet, Chef, Ansible, and CFEngine.
Think bare metal or virtual machines, like the laptops or work stations that employees use at a company.
Cloud integration allowing them to manage resources in Cloud environments like Amazon EC2, Microsoft Azure, or the Google Cloud platform, and the list doesn't stop there.
platform specific tools, like SCCM and Group Policy for Windows.
specific environments, even when they aren't as flexible as the others.
Puppet because it's the current industry standard for configuration management.
selecting a configuration management system is a lot like deciding on a programming language or version control system.

When using a configuration management system, we write rules that describe how the computers in our fleet should be configured.
Components of CM:
 - We can model the behavior of our IT infrastructure in  files that can be processed by automatic tools.
 - Version control system tracking to record all changes.  Can help answer questions like who, when, and why. Revert changes.

Infrastructure as Code or IaC:
You are using Infrastructure as Code when all of the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.  This is combined with automatic tooling to actually get the nodes provisioned and managed.

you can very quickly deploy a new device if something breaks down.
The principals of Infrastructure as Code are commonly applied in cloud computing environments, where machines are treated like interchangeable resources, instead of individual computers. 
from servers to laptops, or even workstations in a small IT department.
One valuable benefit of this process is that the configuration applied to the device doesn't depend on a human remembering to follow all the necessary steps.
deployment consistent.
Since the configuration of our computers is stored in files, those files can be added to a VCS.
an audit trail of changes
quickly rollback if a change was wrong,
others reviewed our code to catch errors and distribute knowledge,
improves collaboration with the rest of the team,
easily check out the state of our infrastructure by looking at the rules that are committed.
ability to easily see what configuration changes were made and roll back to a known good state is super important.
I've had my fair share of outages caused by an innocent-looking change with unintended side effects.
On top of that, having the rules stored in files means that we can also run automated tests on them.
In a complex or large environment, treating your IT Infrastructure as Code can help you deploy a flexible scalable system.
To sum all of this up, managing your Infrastructure as Code it means that your fleet of nodes are consistent, versioned, reliable, and repeatable.
machines are treated as replaceable resources that can be deployed on-demand through the automation.
Performing an action like adding more servers to handle an increase in requests is just a possible first step. There are other things that we might need to take into account, such as the amount of traffic that network can handle or the load on the back end servers like databases.
