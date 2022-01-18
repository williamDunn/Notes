# Lambda Expressions

-  A lambda expression is a short block of code which takes in parameters and returns a value. 
-  Lambda expressions are similar to methods, but they do not need a name and they can be implemented right in the body of a method.

https://www.w3schools.com/java/java_lambda.asp

--------------------

### Syntax:

The simplest lambda expression contains a single parameter and an expression:

>  parameter -> expression

To use more than one parameter, wrap them in parentheses:

>  (parameter1, parameter2) -> expression

Expressions are limited. They have to immediately return a value, and they cannot contain variables, assignments or statements such as if or for. In order to do more complex operations, a code block can be used with curly braces. If the lambda expression needs to return a value, then the code block should have a return statement.

>  (parameter1, parameter2) -> { code block }

--------------------

Code Examples:

```
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(5);
    numbers.add(9);
    numbers.add(8);
    numbers.add(1);
    numbers.forEach( (n) -> { System.out.println(n); } );
  }
}
```



```
interface StringFunction {
  String run(String str);
}

public class Main {
  public static void main(String[] args) {
    StringFunction exclaim = (s) -> s + "!";
    StringFunction ask = (s) -> s + "?";
    printFormatted("Hello", exclaim);
    printFormatted("Hello", ask);
  }
  public static void printFormatted(String str, StringFunction format) {
    String result = format.run(str);
    System.out.println(result);
  }
}
```
