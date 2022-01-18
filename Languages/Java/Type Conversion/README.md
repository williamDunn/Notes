# Type Conversion in Java
-------------------------

### Double to int - Type Casting
```
public class DoubleToIntExample1
{  
  public static void main(String args[])
  {  
    double d=10.5;  
    int i=(int)d;  
    System.out.println(i);  
  }
}  
```

### Convert int/double/float/Object to String

-  String.valueOf()
-  Integer.toString()
```
long i = 9993939399L;           //L is the suffix for long  
String s = String.valueOf(i);   //Now it will return "9993939399"  
```
```
long i = 9993939399L;  
String s = Long.toString(i);    //Now it will return "9993939399"  
```

-------------------------------

### Converting StringBuilder Object to String (& Reversing the String)

```
public class ObjectToStringExample2
{  
  public static void main(String args[])
  {  
    String s="hello";  
    StringBuilder sb=new StringBuilder(s);  
    sb.reverse();  
    String rev=sb.toString();                       //converting StringBuilder to String  
    System.out.println("String is: "+s);  
    System.out.println("Reverse String is: "+rev);  
  }
}  
```
