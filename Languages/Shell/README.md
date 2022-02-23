# Shell Commands

--------------------

## Navigation Commands

*options* : modify the behavior of commands
**--** : long name version

**-** : short name version


**ls** : list files
-  **-a** : includes hidden files and directories
-  **-l** : lists in long format, as well as the file permissions
    -  **-al** : includes hidden files and directories
-  **-t** : orders files and directories by the time they were last modified
    - **alt** : includes hidden files 

**pwd** : print working directory / outputs the name of the directory you're currently in

**cd** : change directory
-  cd .. : move up one directory
-  cd ../.. : move up two directories

**mkdir** : make directory

**touch** : creates a new file inside a working directory ($ touch keyboard.txt)

**echo "Hello Command Line" >> hello_cli.txt** : create a file named hello_cli.txt and add *Hello Command Line* to that file

**cat** : view contents of individual file in terminal
-  cat hello_cli.txt : print the contents of the hello_cli.txt file to the terminal

------------------

## Copying, moving, and removing files and directories from the command line

**cp** : copies files or directories
-  *Copy contents of source file -> destination file*:
    -  cp source.txt destination.txt
- *Copy a file -> destination directory*: 
    -  cp source.txt destination/ 
- *Copy multiple files -> directory*:
    -  cp file1.txt file2.txt my_directory/

**mv** : moves a file without making a copy
-  *Move a file -> directory*:
    -  mv my_file.txt my_directory/
-  *Move multiple files -> directory*:
    -  mv my_file_1.txt my_file_2.txt my_directory/
-  *Rename a file*:
    -  mv file_origin.txt file_renamed.txt

**rm** : delete files and directories
-  *Remove a file*:
    -  rm unwanted_file.txt
-  *Remove a directory (and all of its child directories)*:
    -  rm -r unwanted_directory

------------------

## Input/Output Redirection

Through *redirection* you can direct input and the output of a command to and from other files and programs, and chain commands together in a pipeline

**echo** : accepts a standard input, and echoes back to the terminal a standard output

>  *standard input* (stdin), **information inputted into the terminal** through keyboard or input device
>  
>  *standard output* (stdout), **information outputted** after a process is run
>  
>  *standard error* (stderr), **error message outputted** by a failed process
>  

>  **redirection** *reroutes* stdin, stdout, and stderr *to* or *from a different location*

**>** : redirects a standard output to a file
-  Redirecting a string into a file
    -  echo "Hello" > hello.txt
    -  cat hello.txt
-  Redirect standard output of *cat deserts.txt* -> forests.txt
    -  cat deserts.txt > forests.txt
------------------

## Wildcards

Special characters like * to select groups of files
-  *Copy all files* in the current working directory into another directory
    -  cp * my_directory/
-  *Copy all files starting with "w" and ending with ".txt"* in the current working directory and copies them to my_directory/
    -  cp w*.txt my_directory/

------------------

## Helper Commands

**clear** : clear your terminal

*tab* : autocomplete your command

*up/down arrows* : cycle through previous commands