# Big-O
--------
What is it?

Big-O notation is simply how programmers talk about algorithms. It's determined by how a function responds to different inputs, how much slower is something if we input 1000 vs 1?

- You'd read O(n) as "Order of N"

Why is it important?

Types of Big-O Notation:

O(1) - Constant Time
- Always take the same amount of time to be executed
- Best case scenario for a function
----------------
O(n) - Linear Time Complexity
- The time it takes to execute the algorithm is directly proprtional to the input size *n*
---------------
O(log n) - Logarithmic Time Complexity
- The time it takes to run the algorithm is proportional to the logarithm of the input size *n*
---------------
O(n^2) - Quadratic Time Complexity
- The time it takes to execute is proportional to the square of the input size
    - For example, if we wanted to find everyone combinition of [1, 2, 3] we'd get back [(1,1) (1,2), (1,3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    - This is an O(n^2) function because for every number in the array we have to do n more operations
----------------
