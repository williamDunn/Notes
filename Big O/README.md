# Big-O
--------
#### What is it?

- Big-O notation is simply how programmers describe algorithms

- It's determined by how a function responds to different inputs - how much slower is something if we input 1000 vs 1

- It's about figuring out the approximate worst-case performance of doing something

- You'd read O(n) as "Order of N"

#### Why is it important?

#### Types of Big-O Notation:

##### O(1) - Constant Time
- Always take the same amount of time to be executed no matter how big our input
- Best case scenario for a function
----------------
##### O(n) - Linear Time Complexity
- The time it takes to execute the algorithm is directly proprtional to the input size *n*
- If we were to check an array 1 by 1, the time to check would correspond directly to the amount of items in the array

---------------
##### O(log n) - Logarithmic Time Complexity
- The time it takes to run the algorithm is proportional to the logarithm of the input size *n*
---------------
##### O(n^2) - Quadratic Time Complexity
- The time it takes to execute is proportional to the square of the input size
    - For example, if we wanted to find everyone combinition of [1, 2, 3] we'd get back [(1,1) (1,2), (1,3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    - This is an O(n^2) function because for every number in the array we have to do n more operations
----------------
#### How do you calculate Big-O?
