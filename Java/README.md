#### Variables

Declaring a variable
```
int a;
```

Initializing a variable
```
int a = 10;
```

Local Variables:
-  declared in methods, constructors, or blocks
    -  destroyed once it exits the method, constructor, or block
    -  only visible within / scope limited to the declared method, constructor, or block
-  there is no default values for local variables, so they should declared and initialized before first use
-  access modifiers cannot be used for local variables

Instance Variables:
-  declared in a class, but outside a method, constructor, or any block
-  created when an objected is created with the use of keyword 'new' and destroyed when object is destroyed
-  can be declared in class level before or after use
-  access modifiers can be g iven for instance variables
-  instance variables visible for all methods, constructor and block in the class
    -  recommende to make these variables private (access level)
        -  visibility for subclasses can be given for these variables with the use of access modifiers
-  instance variables have default values
    -  values can be assigned during declarion or within constructor
-  can be accessed directly by calling the variable name inside the class
    -  however, within stat methods (when instance variables are given accessibility), they should be called using the fully qualified name
        -  ObjectReference.VariableName
--------------------------------
#### Abstract Class vs Interface

##### Abstract Class
-  Used for Common Properties

##### Interface
-  Used for Common Methods


<img src="abstractVsInterface.PNG" height="300">

--------------------------------
#### Enumerations

Use Enums where there's a fixed range of values that a variable can be
-  A static variable won't inforce that it must be one of those values, whereas an Enum would

--------------------------------
#### Private vs Public vs Protected

##### Private 
-  only class in which it is declared can see it

##### Package Private 
-  Can only be seen and used by the package in which it is declared (this is the default in Java)

##### Public 
-  Everyone can see it

##### Protected 
-   Package Private + can be seen by subclasses or package members
