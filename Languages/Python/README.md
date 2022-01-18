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
