# REST APIs
--------------------------------
## API – Application Programming Interface
-	Application: Any one or many “programs” or functionality coming together to be used by an end-user towards a need or a purpose 
-	Interface: An endpoint of an application that an end-user can interact with
    -	human – software interaction
     - You loaded a search engine, Google’s homepage. You are met with an interface. You’re already served a resource: the search form, logo and all. You type text into   the input area and click ‘search’. Congratulations, you’ve interacted with the interface, you’ve sent data to it. Now it returns you new resources, web pages that are listed based on your search term.
-	Programming Interface: Is only different at one endpoint compared to the interface, you. It’s for different programs to interact with each other, not humans.
    -	To make this interaction process more universal, HTTP methods were introduced into web APIs. That “universal” behavior made what’s now called REST API. These API ends are usually token-authenticated, especially if they allow operations besides retrieving data.

--------------------------------
## HTTP methods used in REST APIs:
-	GET:
    -	Retrieve a resource/data
    -	GET /user/1 or GET /users
-	PUT:
    -	Replaces a resource completely (even if it doesn’t exist)
    -	PUT /user/1 or PUT /user if it’s an insert
-	PATCH:
    -	Updates a resource (only for existent resources, unlike PUT it won’t create if there’s no such resource)
    -	POST /user/1
-	POST:
    -	Create a resource
    -	POST /user
-	DELETE:
    -	Deletes a resource
    -	DELETE /user/1

CRUD – Create (POST or PUT), Read(GET), Update(PUT or PATCH), Delete(DELETE)

In general, created resources return an ID (resource identifier) for you
-	Update and delete operations require such an ID
-	For listing it can be optional (GET a specific resource or refer to it’s container to get all resources)

--------------------------
## RESTful System

REST is just a particular description of how an interface should work: all of the requests and operations that a program should be able to make when it’s using your site, how they ideally should work.

**6 guiding constraints** that restrict the way the server can process and respond to client requests
•	By doing this, the system gains desirable non-functional properties (performance, scalability, simplicity, modifiability, portability, reliability, & visibility)

1.	**Client-Server Architecture**
-	TL;DR: Server manages the data, client accesses it
-	Main principle = separation of concerns between client and server
      -	Separating the UI concerns from the data storage concerns improves portability of the UI across multiple platforms
      -	Improves scalability by simplifying the server components
      -	Most significant to the Web is that the separation allows the components to evolve independently – thus supporting the internet scale requirement of multiple organizational domains
2.	**Statelessness**
-	TL;DR: the API cannot hold state
-	In a client-server interaction, state is made up of intrinsic state and extrinsic state. 
      -	Intrinsic state, or resource state, is stored on the server and consists of information that is independent of the server’s context, thereby making it sharable to all clients of the server
      -	Extrinsic state, or application state, is stored on each client and consists of info that is dependent on the server’s context and therefore cannot be shared
-	Clients	are responsible for passing application state to the server when it needs it, by storing application state on the client rather than on the server makes the communication stateless
3.	**Cacheability**
-	TL;DR: Responses must be defined as cacheable or non-cacheable
-	Clients and intermediaries can cache responses (responses must define themselves as either cacheable or non-cacheable to prevent clients from providing stale or inappropriate data
-	Well-managed caching can eliminate some client-server interactions, thus improving scalability and performance.
4.	**Layered System**
-	The API can be made up of several other APIs and servers but this information must be hidden to the client
•	A client can’t ordinarily tell if it is connected directly to the end server or to an intermediary, so if a proxy or load balancer is placed between the client and server, it won’t affect their communications.
o	Servers can call multiple other servers to generate a response to the client
•	Intermediary servers can improve system scalability by enabling load balancing and providing shared caches. Security can also be added as a layer to separate business logic from security logic. 
5.	**Code on demand** (optional)
-	The API can be used to retrieve code/logic
•	Servers can temporarily extend or customize the functionality of a client by transferring executable code (compiled components such as Java applets, or client-side scripts such as JavaScript
6.	**Uniform Interface**
-	TL;DR: Manipulation and identification of resources using URIs (I can PATCH request   API/user/user_id to update a specific user in one of my APIs)
•	It simplifies and decouples the architecture, enabling each to part evolve independently
•	4 constraints that make up a uniform interface:
1.	Resource Identification in requests (i.e. URIs in RESTful web services)
	The resources themselves are conceptually separate from the representations returned to the client
	For example, the server could send data from its database as HTML, XML, or JSON – none of which are the server’s internal representation
2.	Resource manipulation through representations
	When a client holds a representation of a resource, including any metadata attached, it has enough info to modify or delete the resource’s state
3.	Self-descriptive messages
	Each message includes enough info to describe how to process the message (i.e. which parser to invoke can be specified by a media type)
4.	Hypermedia as the engine of application state (HATEOAS)
	Having accessed an initial URI for the REST app- like a human Web user accessing the home page of a website – a REST client should then be able to use server provided links dynamically to discover all the available resources it needs
	As access proceeds, the server responds with text that includes hyperlinks to other resources that are currently available
	There is no need for the client to be hard coded with information regarding the structure or dynamics of the application

