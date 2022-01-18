# MVC (Model View Controller)
-----------------------------
What is MVC? 

MVC is an architectural pattern that separates an application into 3 components: **Model, View, Controller**


#### Model

Model represents the shape of the data
- Model objects store data retrieve from the database

#### View

View is the user interface
- Displays model data to the user and also enables them to modify them
- View in ASP.NET MVC is HTML, CSS, & some special syntax that makes it easy to communicate with the model & the controller

#### Controller

Handles the user requests
- The user uses the view & raises an HTTP request, which is handled by the controller
- Controller processes the request & the returns the appropriate view as a response
