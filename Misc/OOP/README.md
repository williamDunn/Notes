# Object Oriented Programming (OOP)

-  Classes and objects are the two main aspects of object-oriented programming

-  a class is a template for objects, and an object is an instance of a class.
      -  When the individual objects are created, they inherit all the variables and methods from the class.


**Advantage of OOP** (over precedural progamming)

-  OOP is faster and easier to execute
-  OOP provides a clear structure for the programs
-  OOP reduces boilerplate code, and makes the code easier to maintain, modify and debug
-  OOP makes it possible to create full reusable applications with less code and shorter development time

-----------------------------------
There are **4 basic OOP concepts**:
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism

-----------------------------------

# Abstraction

-  Data abstraction is the process of hiding certain details and showing only essential information to the user

* Simple things to represent complexity
    * Simple: objects, classes, variables, method(parameters)
    * Complexity: How a method is implemented, Calculations to perform to create a result


i.e., Calling a method, don't need to worry about the code in the method
    
**How to achieve Abstraction:**

-  Abstraction can be achieved with either abstract classes or interfaces


--------------------------------------------------------------------------------------------------------------------

# Encapsulation
- The meaning of encapsulation is to make sure that "sensitive" data is hidden from users

**Why?**
-  Better control of class attributes and methods
      -  Class attributes can be made **read-only** (if you only use the get method), or **write-only** (if you only use the set method)
-  Flexible: the programmer can change one part of the code without affecting other parts
-  **Increased security of data**

To achieve encapsulation you must:
-  Getters & Setters
-  declare class variables/attributes as private ( AKA encapsulating our properties within the object)

```
public class Person {
  private String name; // private = restricted access

  // Getter
  public String getName() {
    return name;
  }

  // Setter
  public void setName(String newName) {
    this.name = newName;
  }
}

```
--------------------------------------------------------------------------------------------------------------------

# Inheritance
* Allows you to create new classes that share attributes and methods of existing classes

-  It is useful for **code reusability**: reuse attributes and methods of an existing class when you create a new class.
-  Ability to add more functionality when needed through child class

>  Notes:
>  -  To inherit from a class, use the *extends* keyword.
>     -  If you don't want other classes to inherit from a class, use the final keyword
>     
>  Terminology:
>  -  subclass (child) - the class that inherits from another class
>  -  superclass (parent) - the class being inherited from
    
--------------------------------------------------------------------------------------------------------------------    
    
# Polymorphism
* Objects of different types can be accessed through the same interface (with it's own independent implementations)
    * Method overriding
         -  Overriding means 2 methods with the same method name and parameters
    * Method overloading
         -  Overloading occurs when 2 or more methods in one class have the same name but different parameters
