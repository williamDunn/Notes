# Big-O / Time Complexity
--------
https://www.bigocheatsheet.com/

https://towardsdatascience.com/essential-programming-time-complexity-a95bb2608cac

### What is it?

-  **Big O notation** is the language programmers use for **describing how long an algorithm takes to run*
    -  With big O notation **we express the runtime in terms of how quickly it grows relative to the input**, as the input gets arbitrarily large. 
        -  how a function responds to different inputs - how much slower is something if we input 1000 vs 1
        1)  how quickly the runtime goes
        2)  relative to input
        3)  as the input gets arbitrarily large

-  It's about figuring out the approximate worst-case performance of doing something

-  You'd read O(n) as "Order of N"

## Types of Big-O Notation:

1)  O(1) - **Constant** time
2)  O(log n) - **Logarithmic** time
3)  O(n) - **Linear** time
4)  O(n^2) - **Quadratic** time
5)  O(2^n) - **Exponential** time

<img src="timeComplexityExplained.png" height="250">

---------------------

### O(1) - Constant Time
-  **Best case scenario for a function**
-  Always takes the same amount of time to be executed no matter how big the input
    -  The input array could be 1 item or 1,000 items, but this method would still just require one "step."

```java
public static void printFirstItem(int[] items) {
    System.out.println(items[0]);
}
```

----------------
### O(n) - Linear Time
- **Time** it takes **to execute** the **algorithm** is **directly proprtional to the input size** *n*
- Checking an array 1 by 1, the time directly corresponds to the amount of items in the array
    -  If the array has 10 items, we have to print 10 times. If it has 1,000 items, we have to print 1,000 times.


```java
public static void printAllItems(int[] items) {
    for (int item : items) {
        System.out.println(item);
    }
}
```

---------------
### O(log n) - Logarithmic Time
-  The **time** it takes **to run** the **algorithm** is **proportional to** the **logarithm of the input size** *n*
-  Generally associated with **Divide and Conquer algorithms**
---------------
### O(n^2) - Quadratic Time
-  The **time** it takes **to execute** is **proportional to** the **square of the input size** *n*
    -  i.e., if we wanted to find everyone combinition of [1, 2, 3] we'd get back [(1,1) (1,2), (1,3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        -  This is an O(n^2) function because for every number in the array we have to do *n* more operations

```java
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
### O(2^n) - Exponential Time
-  Should be **avoided**
-  **Growth rate doubles** with **each addition to the input** *n*
-  Usually seen in brute force algorithms
----------------

# Calculating time complexity

**Drop the constants**
-  O(2n), we just call O(n)
-  O(1 + n / 2 + 100) we just call O(n)

>  Why can we get away with this? For big O notation we're looking at what happens as n gets arbitrarily large. As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect. 

(Sometimes the constants matter - If we have a script that takes 5 hours to run, an optimization that divides the runtime by 5 might not affect big O, but it still saves you 4 hours of waiting)

**Drop the Less Significant Terms**
- Even if our runtime is O(n+n^2), we just call it O(n^2). Even if it was O(n^2 / 2 + 100n), it would still be O(n^2)

Similarly:
-  O(n^3 + 50n^2 + 10000) is O(n^3)
-  O((n + 30) ??? (n + 5)) is O(n^2)

>  We can get away with this because the less significant terms quickly become, well, less significant as n gets big. 

--------------------

# Space Complexity

Sometimes we want to optimize for using less memory instead of (or in addition to) using less time

-  simply look at the total size (relative to the size of the input) of any new variables we're allocating


This method takes O(1) space (we use a fixed number of variables): 

```java
public static void sayHiNTimes(int n) {
    for (int i = 0; i < n; i++) {
        System.out.println("hi");
    }
}
```
This method takes O(n) space (the size of hiArray scales with the size of the input): 

```java
public static String[] arrayOfHiNTimes(int n) {
    String[] hiArray = new String[n];
    for (int i = 0; i < n; i++) {
        hiArray[i] = "hi";
    }
    return hiArray;
}
```

**Usually when we talk about space complexity, we're talking about additional space**, so we don't include space taken up by the inputs. For example, this method takes constant space even though the input has *n* items: 

```java
public static int getLargestItem(int[] items) {
    int largest = Integer.MIN_VALUE;
    for (int item : items) {
        if (item > largest) {
            largest = item;
        }
    }
    return largest;
}
```
