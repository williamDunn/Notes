# Data Structures

What are data structures?
- Simply ways of organizing data

Why are they used?
- Organizes, manages, and stores data

Types of data structures:

Linear vs Non-linear
--------------------
**Linear** data elements are arranged sequentially or linearly where the elements are attached to its previous and next adjacent
- Array, Stack, Queue, Linked List
    - In linear data structure, single level is involved. Therefore, we can traverse all the elements in single run only.
    - Applications of linear data structures are mainly in application software development.

**Non-linear** data elements are not arranged sequentially or linearly
- Graphcs, trees
    - In a non-linear data structure, single level is not involved. Therefore, we can’t traverse all the elements in single run only. Non-linear data structures are not easy to implement in comparison to linear data structure. It utilizes computer memory efficiently in comparison to a linear data structure.
    - Applications of non-linear data structures are in Artificial Intelligence and image processing

Java Collection
---------------
-  List
-  Set
-  Map


In Place vs Out of Place
------------------------
-  An **in-place method** modifies data structures or objects outside of its own stack frame ↴ (i.e.: stored on the process heap or in the stack frame of a calling function). Because of this, the changes made by the method remain after the call completes. 
-  An **out-of-place method** doesn't make any changes that are visible to other methods. Usually, those methods copy any data structures or objects before manipulating and changing them. 


```
public static void squareArrayInPlace(int[] intArray) {

    for (int i = 0; i < intArray.length; i++) {
        intArray[i] *= intArray[i];
    }

    // NOTE: no need to return anything - we modified
    // intArray in place
}

public static int[] squareArrayOutOfPlace(int[] intArray) {

    // we allocate a new array with the length of the input array
    int[] squaredArray = new int[intArray.length];

    for (int i = 0; i < intArray.length; i++) {
        squaredArray[i] = (int) Math.pow(intArray[i], 2);
    }

    return squaredArray;
}
```

Benefits of **In-Place**:
-  Working in-place is a good way to save time and space. 
    -  An in-place algorithm avoids the cost of initializing or copying data structures, and it usually has an O(1) space cost. 

Can Cause side effects:
-  Your input is "destroyed" or "altered," which can affect code outside of your method

Benefits of **Out-of-Place**:
-  Generally, out-of-place algorithms are considered safer because they avoid side effects

>  You should only use an in-place algorithm if you're space constrained or you're positive you don't need the original input anymore, even for debugging
