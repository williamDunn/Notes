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


However when working with lists we should tell it what data types it should old - doesn't make sense to hold a list with a bunch of different types
To fix this we use "<>" to declare the type
i.e.

```
List<String> colors = new ArrayList<>();
```

to print a List, check the size, check if it contains a certain element
```
colors.add("blue");
colors.add("purple");
colors.add("yellow");

System.out.println(colors);
//returns [blue, purple, yellow]

System.out.println(colors.size());
//returns 3

System.out.println(colors.contains("yellow"));
//returns true

System.out.println(colors.contains("pink"));
//returns false
```

Looping through a list methods
```
//Using a for loop
for (String color : colors) 
{
	System.out.println(color);
}

//Using a for each
colors.forEach(System.out::println);


//traditional for i loop
//not preferred unless you need access to the index itself
for (int i = 0; i < colors.size(); i++)
{
	System.out.println(colors.get(i));
}
```
Returns:

blue

purple

yellow

----------
Creating an unmodifiable list
```
List<String> colorsUnmodifiable = List.of(
	"blue",
	"yellow"
);
```

if you try to add something to this list, you'll get an error because the list is immutable
