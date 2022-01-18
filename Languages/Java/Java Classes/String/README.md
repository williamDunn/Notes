# Strings

>  String greeting = "Hello";

String Class is Immutable

String methods
-  length():  the length of a string
-  toUpperCase()
-  toLowerCase()
-  indexOf():  returns the index (the position) of the first occurrence of a specified text in a string (including whitespace)
>  Java counts positions from zero.
>  
>  0 is the first position in a string, 1 is the second, 2 is the third ...
>  
>  String txt = "Please locate where 'locate' occurs!";
>  
>  System.out.println(txt.indexOf("locate")); // Outputs 7

-  

https://www.w3schools.com/java/java_ref_string.asp

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
