# Arrays 101
------------

Time Complexitity:
O(N)

-  Fixed size
-  Fast for data retrieval
-  Compact memory usage (if size is known)
-  Delete operation very hard

<img src="screenshot.png" height="200">


```
String[] colors = new String[5];

colors[0] = "purple";
colors[1] = "blue";

System.out.println(Arrays.toString(colors));
System.out.println(colors[4]);
```
returns:

[purple, blue, null, null, null]

```
System.out.println(colors[0]);
System.out.println(colors[1]);
System.out.println(colors[2]);
System.out.println(colors[3]);
System.out.println(colors[4]);
```
returns:

purple

blue

null

null

null

```
colors[2] = "yellow";
System.out.println(Arrays.toString(colors));
```
returns: 

[purple, blue, yellow, null, null]
