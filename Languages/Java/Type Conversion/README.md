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

### Convert Integer/Double/Float/Character/Object to String

-  String.valueOf()
```
double d = 12.3;
String s = String.valueOf(d);  
```
-  Double.toString()
```
double d = 89.7;  
String s = Double.toString(d);  
```

### String to Double/Float/Integer

-  Double.parseDouble()
```
String s = "23.6";  
double d = Double.parseDouble("23.6");  
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