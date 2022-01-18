### Spring MVC
-  A Web MVC Framework for building web applications
-  Contains lots of configuration files for various capabilities
-  it is an HTTP oriented web application development framework

The Spring Web model-view-controller (MVC) framework is designed around a DispatcherServlet that handles all the HTTP requests and responses

Following is the sequence of events corresponding to an incoming HTTP request to DispatcherServlet


-  After receiving an HTTP request, DispatcherServlet consults the HandlerMapping to call the appropriate Controller.

-  The Controller takes the request and calls the appropriate service methods based on used GET or POST method. The service method will set model data based on defined business logic and returns view name to the DispatcherServlet.

-  The DispatcherServlet will take help from ViewResolver to pickup the defined view for the request.

-  Once view is finalized, The DispatcherServlet passes the model data to the view which is finally rendered on the browser.
