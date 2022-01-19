# Spring Framework Basics

-  Provides patterns and structure in your java application

-------------------------

### Three Major Things the Spring Framework Provides

1)  **Managing object lifecycles and dependencies** for components & services in your code through the use of **application context** and **dependency injection**
-  Spring creates and manages (Singleton) object instances
    - Also connects these objects together the way you want it
      -  The way it works is by having every class declare the dependencies it needs
          - Spring will look at the declaration and inject those dependencies to make sure that every object has references to all the other instances they require (called **dependency injection**)
2)  Spring offers various **Data Access APIs and mechanisms** for:

    a)  Connectivity
    
    b)  Querying
    
    c)  Transaction Management
    
    d)  Etc.
    
-  Replaces the standard Java way of database connectivity using JDBC (Java database connectivity)

3)  Web framework called **Spring MVC**
-  Let's you easily create (dynamic) web applications and REST APIs using the same Spring application model and dependency injection concepts

-------------------------

### Dependency Injection (sometimes called 'Dependency Inversion')

It's a way in which you **decouple** the conventional dependency relationships between objects
