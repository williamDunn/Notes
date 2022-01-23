# Python (.py)

-  an interpreted high-level general-purpose programming language

**Used for**:
-  web development (server-side),
-  software development,
-  mathematics,
-  system scripting.

**Can do**:

-  Python can be used alongside software to create workflows.
-  Python can connect to database systems. It can also read and modify files.
-  Python can be used to handle big data and perform complex mathematics.
-  Python can be used for rapid prototyping, or for production-ready software development.

---------------------
**Commenting out code**:
```python
# Use a hashtag

"""
This is a comment
written in
more than just one line
"""
```

**How to print**:
```python
print("Hello world!")
```

**Creating a variable**:
``python
x = 5
y = "John"
print(x)
print(y)
``

-  Variables do not need to be declared with any particular **type**
    - variables can even change type after they've been set 
 
``python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
``

#### Tuple

-  Tuple items are ordered, unchangeable/immutable, and allow duplicate values.
-  Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

#### List

-  List items are ordered, changeable, and allow duplicate values.
-  List items are indexed, the first item has index [0], the second item has index [1] etc.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

#### Range

-  The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

**Syntax**
range(start, stop, step) 

```python
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
for n in x:
  print(n) 
```
