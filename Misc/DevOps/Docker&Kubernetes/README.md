#### Docker
-  Sole purpose of Docker is to make sure code executes under the exact same environment in production, testing, and during development

###### pros:
*  portability
*  performance (containers don't require an OS, so they leave a smaller footprint in turn making them faster to create and quicker to start. - a virtual machine, an alternative to containers, requires an OS.
*  agility (portability & performance can make your development process more agile and responsive)
*  isolation (a docker container that contains one of your applications also includes the relevant versions of any supporting software. && Different docker containers are totally independent of eachother meaning you can have multiple 'images' of your application in different states that work)
*  Scalability (you can create new containers if demand for your application requires them)

#### Kubernetes
-  A Kubernetes Cluster is a set of nodes that run containerized applications

###### pros:
*  Interacts with several groups of containers (able to manage more cluster at the same time)
*  Self-monitoring (constantly checks health of nodes and containers)
*  Horizontal scaling (allows you to scale rseources horizonatlly as well as vertically, easily and quickly)
*  Automates rollouts and rollbacks
*  Automates varioua manual processes (controlling which server will host the container, how it will be launched, etc.)
*  Container balancing (calculates the best location when placing containers)
*  Storage orchestration (moutns and add storage system of your choice to run apps)
*  Provides additional services (security, networking, and storage services)
*  Run everywhere (open source tool that gives you the freedom to take advantage of on-premises, hybrid, or public cloud infrastructure)
