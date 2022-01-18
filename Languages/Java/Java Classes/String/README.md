# Strings

>  String greeting = "Hello";

String Class is Immutable

String methods
-  length():  the length of a string
-  toUpperCase()
-  toLowerCase()
-  indexOf():  returns the index (the position) of the first occurrence of a specified text in a string (including whitespace)
>  Java counts positions from zero - 0 is the first position in a string, 1 is the second, 2 is the third ...
```
String txt = "Please locate where 'locate' occurs!";
System.out.println(txt.indexOf("locate")); // Outputs 7
```

String Concatenation
-  The + operator can be used between strings to combine them. This is called concatenation:
```
System.out.println(firstName + " " + lastName);
```
-  You can also use the concat() method to concatenate two strings:
```
System.out.println(firstName.concat(lastName));
```

https://www.w3schools.com/java/java_strings.asp

https://www.w3schools.com/java/java_ref_string.asp

-----------------------------------------

## Parsing a String

```
// Java program to Convert a String
// to a Character array using Naive Approach
  
import java.util.*;
  
public class GFG {
  
    public static void main(String args[])
    {
        String str = "GeeksForGeeks";
  
        // Creating array of string length
        char[] ch = new char[str.length()];
  
        // Copy character by character into array
        for (int i = 0; i < str.length(); i++) {
            ch[i] = str.charAt(i);
        }
  
        // Printing content of array
        for (char c : ch) {
            System.out.println(c);
        }
    }
}
```

```
// Java program to Convert a String
// to a Character array using toCharArray()
  
import java.util.*;
  
public class GFG {
  
    public static void main(String args[])
    {
  
        String str = "GeeksForGeeks";
  
        // Creating array and Storing the array
        // returned by toCharArray()
        char[] ch = str.toCharArray();
  
        // Printing array
        for (char c : ch) {
            System.out.println(c);
        }
    }
}
```

```
public class StringTest {
    public static void main(String args []){
        String source1 = "March032021";
        String [] returnedArray1 = source1.split("\\d+");
        for(String str1 :  returnedArray1){
            System.out.println(" Output1 : "+str1);
        }
        String source2 = "950-003-123-900-456 : 11 _343-1 789----";
        String [] returnedArray2 = source2.split("-",4);
        for(String str2 :  returnedArray2){
            System.out.println(" Output2 : "+str2);
        }

    }
}

```

-----------------------------------------

## StringBuilder Class
-  Alternative to string class (along with StringBuffer)
-  creates a mutable sequence of characters
-  The StringBuilder class provides no guarantee of synchronization whereas the StringBuffer class does

**Constructors in Java StringBuilder:** 
 

-  StringBuilder(): Constructs a string builder with no characters in it and an initial capacity of 16 characters.
     
-  StringBuilder(int capacity): Constructs a string builder with no characters in it and an initial capacity specified by the capacity argument.
     
-  StringBuilder(CharSequence seq): Constructs a string builder that contains the same characters as the specified CharSequence.
     
-  StringBuilder(String str): Constructs a string builder initialized to the contents of the specified string. 


https://www.geeksforgeeks.org/stringbuilder-class-in-java-with-examples/
