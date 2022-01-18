# Multithreading

What is multithreading?
-  Multithreading is an important programming concept
-  Multithreading is the ability to have multiple threads executing concurrently. While each thread shares the same process resources, they operate independently of each other

Difference between a process and thread?
-  A process is a single application or program, whereas a thread is a subprocess within that application or program
-  Each process has its own address space in memory; threads share their address space

Why use multithreading?
-  Since each thread runs concurrently, multithreading makes efficient use of the CPU. You can have background processes running while the application receives user input. Also, tasks can execute faster since each thread runs independently

Thread States:
-  New
-  Runnable
-  Running
-  Waited/Blocked
-  Dead/Termianted
    - (Once a thread is dead it cannot be restarted) 

Synchronization
-  Synchronization forces threads to run one at a time to prevent a race condition or multiple threads trying to perform the same task

Why use a synchronization block?
-  A synchronized block allows you to designate a particular portion of a method as synchronized. That is, only a single thread will be allowed to run until it completes, prioritizing that thread above others

Synchronous vs Asynchronous
-  Synchronous programming is when a single thread is assigned a single task
-  Asynchronous programming is when a single task is shared between multiple threads


Multithreading at the CPU level / What is context switching?
-  Context switching is where the current state of a thread or process is stored so the execution of that thread can be resumed at a later time
    -  This enables a single CPU to manage multiple threads or processes

Thread Starvation
-  Thread starvation is when there is insufficient CPU capacity to execute a thread
    -  This can happen with low-priority threads, or threads that are demoted in favor of other threads
-  Useful to know when code debugging

Deadlock
-  Deadlock is a problem that can cause code to stall
-  A deadlock situation is where multiple threads are waiting on each other to release CPU resources so they can run
    -  This can happen when:
        -   a single thread has exclusive priority but needs resources from a waiting thread, or all the threads are depending on one another to release needed resources


Creating a thread (in Java)
-  by implementing the Runnable interface on a class and creating a thread object
-  or create a class that extends the thread class

Killing a thread
-  There isn't a direct way to kill a thread (in Java)
-  Dies when finishes executing 
-  To manually kill a thread
    -  you can use a Volatile boolean variable within a thread that will throw an exception when triggered from another thread 
