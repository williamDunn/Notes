# Variables

Declaring a variable
```java
int a;
```

Initializing a variable
```java
int a = 10;
```

### Local Variables:
-  declared in methods, constructors, or blocks
    -  destroyed once it exits the method, constructor, or block
    -  only visible within / scope limited to the declared method, constructor, or block
-  there is no default values for local variables, so they should declared and initialized before first use
-  access modifiers cannot be used for local variables
```java
public class Test {

//age is a local variable, only existing within the scope of the method
   public void pupAge() {
      int age;
      age = age + 7;
      System.out.println("Puppy age is : " + age);
   }

   public static void main(String args[]) {
      Test test = new Test();
      test.pupAge();
   }
}
```

### Instance Variables:
-  declared in a class, but outside a method, constructor, or any block
-  instance variables are created when an objected is created with the use of keyword 'new' and destroyed when object is destroyed
    -  ie. variables of person class: age, name, etc.
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
```java
public class Employee {

   // this instance variable is visible for any child class.
   public String name;

   // salary  variable is visible in Employee class only.
   private double salary;

   // The name variable is assigned in the constructor.
   public Employee (String empName) {
      name = empName;
   }

   // The salary variable is assigned a value.
   public void setSalary(double empSal) {
      salary = empSal;
   }

   // This method prints the employee details.
   public void printEmp() {
      System.out.println("name  : " + name );
      System.out.println("salary :" + salary);
   }

   public static void main(String args[]) {
      Employee empOne = new Employee("Ransika");
      empOne.setSalary(1000);
      empOne.printEmp();
   }
}
```

### Class/Static Variables
-  declared with keyword 'static' in a class, but outside a method, constructor or a block
-  there would be only one copy of each class variable per class
-  rarely used other than being declared as *constants*
    - Constants are variables that are declared as public/private, final, and static
        -  constants variables never change from their intial value
-  created when the program starts and destroyed when the program stops
-  visibility is similar to instance variables
    - most static variables are declared public since they must be available for users of the class
- default values are same as instance variables
    - values can be assigned during the declaration or within the constructor
    - additionally, values can be assigned in special static initializer blocks
- can be accessed by calling with the class name
    - ie. ClassName.VariableName
- when declaring class variables as public static final, variable names must be in all upper case
    - if the static variables aren't public and final, naming syntax is the same as instance and local variables 
```java
public class Employee {

   // salary  variable is a private static variable
   private static double salary;

   // DEPARTMENT is a constant
   public static final String DEPARTMENT = "Development ";

   public static void main(String args[]) {
      salary = 1000;
      System.out.println(DEPARTMENT + "average salary:" + salary);
   }
}
```

(tutorialspoint.com/java/java_variable_types.htm)
