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

```
go build fileName.go
```

ls (list files) command to see original Go program and executable file

```
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
