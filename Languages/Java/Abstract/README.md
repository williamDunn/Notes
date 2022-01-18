# Abstraction

-  Data abstraction is the process of hiding certain details and showing only essential information to the user.

**Abstraction can be achieved with either abstract classes or interfaces**

-  An abstract class allows you to create functionality that can subclasses can implement or override
-  An interface allows you to define functionality, not implement it

**1 Abstract Class, Multiple Interfaces**
-  A class can extend only one abstract class
-  A class can implement multiple interfaces


--------------------

# Abstract Class/Methods

### Why And When To Use Abstract Classes and Methods?

**To achieve security** - hide certain details and only show the important details of an object.

---------------------

-  **Abstract class**: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).
-  **Abstract method**: can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from).

---------------------

If a class has even one abstract class in it, it becomes an abstract class

An abstract method belongs to an abstract class, and it does not have a body. The body is provided by the subclass:

```
// Abstract class
abstract class Animal {
  // Abstract method (does not have a body)
  public abstract void animalSound();
  // Regular method
  public void sleep() {
    System.out.println("Zzz");
  }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```

---------------------------------------------

# Interfaces

-  An interface is a completely "abstract class" that is used to group related methods with empty bodies

```
// interface
interface Animal {
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
}
```

--------------

**What's the use of an interface?**

Java does not support "multiple inheritance" (a class can only inherit from one superclass). 

However, it can be achieved with interfaces, because the class can implement multiple interfaces. 

>  Note: To implement multiple interfaces, separate them with a comma (see example below).


**Multiple Interfaces & Implementation**:

```
interface FirstInterface {
  public void myMethod(); // interface method
}

interface SecondInterface {
  public void myOtherMethod(); // interface method
}

class DemoClass implements FirstInterface, SecondInterface {
  public void myMethod() {
    System.out.println("Some text..");
  }
  public void myOtherMethod() {
    System.out.println("Some other text...");
  }
}

class Main {
  public static void main(String[] args) {
    DemoClass myObj = new DemoClass();
    myObj.myMethod();
    myObj.myOtherMethod();
  }
}
```

>  Notes:
>  
>   -  Like **abstract classes**, interfaces **cannot** be used to create objects (in the example above, it is not possible to create an "Animal" object in the MyMainClass)
>   -  Interface methods do not have a body - the body is provided by the "implement" class
>   -  On implementation of an interface, you must override all of its methods
>   -  Interface methods are by default *abstract* and *public*
>   -  Interface attributes are by default *public*, *static* and *final*
>   -  An interface cannot contain a constructor (as it cannot be used to create objects)
