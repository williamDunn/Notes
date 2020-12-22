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
