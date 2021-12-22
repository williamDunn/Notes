# Stack
------------

-  The Stack class represents a last-in-first-out (LIFO) stack of objects.

-  It extends class Vector with 5 operations that allow a vector to be treated as a stack.
    -  The usual **push()** and **pop()** operations are provided, 
    -  as well as a method to **peek()** at the top item on a the stack
    -  a method to test for whether the stack is empty **empty()**
    -  and a method to search the stack for an item and discover how far it is from the top

```
Stack<Integer> stack = new Stack<>();

stack.push(1);
stack.push(2);
stack.push(3);

//returns the element at the top of the stack (3)
System.out.println(stack.peek());

//returns 3 (the size)
System.out.println(stack.size());

//returns whats at the top of the stack but also removes it
System.out.println(stack.pop());

//returns false (since its not empty)
System.out.println(stack.empty());
```

