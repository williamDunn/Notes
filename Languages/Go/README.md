# Go (Golang)

-  An open sourced programming language designed by Google employees

Purpose of **Go**:
-  make it faster and easier to develop

Advantages:
-  Has modern features (such as garbage colletion)
-  Takes advantage of multi-core computer capabilities with built-in concurrency support

-------------------

## Compiling .go files

(in our command prompt) type

```console
go build fileName.go
```

ls (list files) command to see original Go program and executable file

```console
ls
```
>  fileName fileName.go

to execute the file, call

```
./fileName
```

## Running .go files

use the *go run* command - combines both the compilation and execution of code
-  unlike *go build*, *go run* will NOT create an executable file in our current folder

```
go run fileName.go
```

----------------------

## Basic Go Structure

```
(1)package main 
 
(2)import "fmt" 
 
(3)func main () {
  fmt.Println("Hello World") 
}
```
## 1

*Package Declaration*: every Go program starts with one
-  the package declaration informs the compiler whether to create an executable or library
  -  a library doesn't outright run/execute code - it is a collection of code that can be used in other programs
```
package main
```
Programs that have the package declaration *package main* will create an executable file

  

Go generally ignores blank lines (whitespace - new lines, spaces, and tabs)

  
## 2

*Import statement*: the *import* keyword allows us to bring in and use code from other packages
-  package name must be enclosed with double quotes "
```
import "fmt"
```
we only import the packages we need, in turn our program runs faster

  

**Packages serve important roles in Go**
-  they group related code together
-  allow code to be reusable
-  make it easier to maintain

## 3

function : a reusable block of code
-  a *main* function is special, a file that has a *package main* declaration will automatically run the *main* function
```
func main () {
    fmt.Println("Hello World") 
}
```

-------------------------------

## Importing multiple packages

We can add multiple *import* statements

```go
import "package1"
import "package2"
```

or

we can use a single import and a pair of parentheses that contain our packages

```go
import (
  "package1"
  "package2"
)
```
