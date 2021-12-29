# Sets
------------

-  A collection that contains no duplicate elements
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


System.out.println(balls.size());
//returns 3

balls.add(new Ball("blue"));
System.out.println(balls.size());
//returns 3 since it's a duplicate

//to remove an element use remove()
balls.remove(new Ball("red"));

//Can loop through using iterator or for each
balls.forEach(System.out::println);
```
