# Wrapper
------------------
Wrapper classes provide a way to use primitive data types (int, boolean, etc..) as objects.

| Primitive Data Type      | Wrapper Class |
| ----------- | ----------- |
| byte      | Byte       |
| short   | Short        |
| int      | Integer       |
| long   | Long        |
| float      | Float       |
| double   | Double        |
| boolean      | Boolean       |
| char   | Character        |

Sometimes you must use wrapper classes, 
e.g., when working with Collection objects, such as ArrayList, where primitive types cannot be used (the list can only store objects):

>  ArrayList<int> myNumbers = new ArrayList<int>();         // Invalid
>
>  ArrayList<Integer> myNumbers = new ArrayList<Integer>(); // Valid

------------------------------
  
the following methods are used to get the value associated with the corresponding wrapper object:
-  intValue()
-  byteValue()
-  shortValue()
-  longValue()
-  floatValue()
-  doubleValue()
-  charValue()
-  booleanValue()
  
```java
public class Main {
  public static void main(String[] args) {
    Integer myInt = 5;
    Double myDouble = 5.99;
    Character myChar = 'A';
    System.out.println(myInt.intValue());
    System.out.println(myDouble.doubleValue());
    System.out.println(myChar.charValue());
  }
}
```  
