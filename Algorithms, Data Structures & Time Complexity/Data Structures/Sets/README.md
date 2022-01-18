# Sets
------------
-  A set is like a hash map except it only stores keys, without values
    -  Sets often come up when we're tracking groups of items
         -  nodes we've visited in a graph
         -  characters we've seen in a string
         -  or colors used by neighboring nodes. 
     -  Usually, we're interested in whether something is in a set or not.
-  In Java, sets are called "hash sets." 
    -  They're implemented using hash maps—each member of the set is a key in the hash map with a dummy value that gets ignored.
-  contains no duplicate elements
    -  At most, one null element
-  Not ordered


-  Implementations:
    -  TreeSet
        -  Preserves order, and is backed by a tree map
    -  HashSet 
        -  Backed by hash map

```
Set<Ball> balls = new HashSet<>();

balls.add(new Ball("blue"));
System.out.println(balls);

balls.add(new Ball("yellow"));
System.out.println(balls);

balls.add(new Ball("red"));
System.out.println(balls);


System.out.println(balls.size());  //returns 3


balls.add(new Ball("blue"));
System.out.println(balls.size());  //returns 3 since it's a duplicate


balls.remove("red");  //to remove an element use remove()


balls.contains("red");   // false


//Can loop through using iterator or for each

balls.forEach(System.out::println);
```
