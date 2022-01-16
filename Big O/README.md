# Big-O
--------
https://www.bigocheatsheet.com/

#### What is it?

-  Big O notation is the language we use for talking about how long an algorithm takes to run
    -  With big O notation we express the runtime in terms of how quickly it grows relative to the input, as the input gets arbitrarily large. 
        1)  how quickly the runtime goes
        2)  relative to input
        3)  as the input gets arbitrarily large

-  Big-O notation is simply how programmers describe algorithms

- It's determined by how a function responds to different inputs - how much slower is something if we input 1000 vs 1

- It's about figuring out the approximate worst-case performance of doing something

- You'd read O(n) as "Order of N"

#### Types of Big-O Notation:

##### O(1) - Constant Time
- Always take the same amount of time to be executed no matter how big our input
- Best case scenario for a function

```
public static void printFirstItem(int[] items) {
    System.out.println(items[0]);
}
```
This method runs in O(1) time relative to its input. The input array could be 1 item or 1,000 items, but this method would still just require one "step."

----------------
##### O(n) - Linear Time
- The time it takes to execute the algorithm is directly proprtional to the input size *n*
- If we were to check an array 1 by 1, the time to check would correspond directly to the amount of items in the array

```
public static void printAllItems(int[] items) {
    for (int item : items) {
        System.out.println(item);
    }
}
```
This method runs in O(n) time, where n is the number of items in the array. If the array has 10 items, we have to print 10 times. If it has 1,000 items, we have to print 1,000 times.

---------------
##### O(log n) - Logarithmic Time Complexity
- The time it takes to run the algorithm is proportional to the logarithm of the input size *n*
---------------
##### O(n^2) - Quadratic Time
- The time it takes to execute is proportional to the square of the input size
    - For example, if we wanted to find everyone combinition of [1, 2, 3] we'd get back [(1,1) (1,2), (1,3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    - This is an O(n^2) function because for every number in the array we have to do n more operations

```
public static void printAllPossibleOrderedPairs(int[] items) {
    for (int firstItem : items) {
        for (int secondItem : items) {
            System.out.println(firstItem + ", " + secondItem);
        }
    }
}
```
Here we're nesting two loops. If our array has n items, our outer loop runs n times and our inner loop runs n times for each iteration of the outer loop, giving us n^2 total prints. Thus this method runs in O(n^2) time. If the array has 10 items, we have to print 100 times. If it has 1,000 items, we have to print 1,000,000 times.

----------------

### Calculating time complexity

**Drop the constants**
-  O(2n), we just call O(n)
-  O(1 + n / 2 + 100) we just call O(n)

>  Why can we get away with this? For big O notation we're looking at what happens as n gets arbitrarily large. As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect. 

**Drop the Less Significant Terms**
- Even if our runtime is O(n+n^2), we just call it O(n^2). Even if it was O(n^2 / 2 + 100n), it would still be O(n^2)

Similarly:
-  O(n^3 + 50n^2 + 10000) is O(n^3)
-  O((n + 30) ∗ (n + 5)) is O(n^2)

>  We can get away with this because the less significant terms quickly become, well, less significant as n gets big. 
