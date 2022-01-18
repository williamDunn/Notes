# JavaScript
-  is a single threaded language
  -  Single threaded means it has only one call stack. Whatever is on the top of the call stack is run first. In the above program, functions are run sequentially

#### Can you do OOP in JavaScript?
-  Yes. Because it supports inheritance through prototyping as well as properties and methods

-------------------------------

#### Variables
-  "Defined": has value/initialized
-  "Not Defined": a variable accessed before defining
-  "Undefined": a variable that is defined but not initialized (i.e. no value assigned before accessing)
-  "Null": empty or non-existent value

#### Global Object Property
- NaN (Not-A-Number)
  - Checks if value not a number

----------------------------

### Methods

#### Array Methods
-  filter()
  - creates a new array filled with elements that pass a test provided by a function
  - does not execute the function for empty elements
  - does not change the original array
- reduce()
  - executes a reducer function for array element
  - returns a single value: the function's accumulated result
  - does not execute the function for empty array elements
  - does not change the original array 

setTimeout()
-  The setTimeout() method calls a function after a number of milliseconds.

Syntax

```js
let timeout;

function myFunction() {
  timeout = setTimeout(alertFunc, 3000);
}

function alertFunc() {
  alert("Hello!");
}
```

-------------------------------

#### Hoisting
-  Hoisting is JavaScript's default behavior of moving all declarations to the top of the current scope (to the top of the current script or the current function).

-  JavaScript declarations are hoisted
  -  In JavaScript, a variable can be declared after it has been used.

---------------------------------

### Async
-  When you execute something synchronously, you wait for it to finish before moving on to another task. When you execute something asynchronously, you can move on to another task before it finishes.

#### Async/Await keywords
-  async makes a function return a Promise
-  await makes a function wait for a Promise

Syntax

```js
async function myFunction() {
  return "Hello";
}
```
