### Lists and ArrayList

-  An ordered collection (aka sequence)
-  Allows duplicates
-  Not fixed in size like arrays
-  Fast for data retrivals
-  Various implementations
    -  ArrayList
    -  Stack
    -  Vector
    -  Others

-------------------

A list can contain multiple data types
i.e.

```
List colors = new ArrayList();
		
    //if you want to add values to your list
    colors.add("blue");
    colors.add("purple");

    colors.add(1);
    colors.add(new Object());

    System.out.println(colors);
```
Returns:
[blue,purple, 1, java.lang.Object@6b71769e]

