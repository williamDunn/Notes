# Infrastructure as Code (IAC)

-  The **idea behind IAC** is that you write and execute code to *define*, *deploy*, *update*, and *destroy* your infrastructure

>  A key insight of DevOps is that you can manage almost *everything* in code
>  -  i.e., *servers*, *databases*, *networks*, *log files*, *application configuration*, *documentation*, *automated tests*, *deployment processes*, and so on.

--------------------------

# Five broad categories of IAC tools:
1.  **Ad hoc scripts**
2.  **Configuration management tools**
3.  **Server templating tools**
4.  **Orchestration tools**
5.  **Provisioning tools**

---------------------------

## Ad Hoc Scripts
-  Great for small, one-off tasks
-  The most straightforward approach to automating anything
    -  You take *whatever task you were doing manually*, *break it down into descrete steps*, *use a scripting language to define each of those steps in code*, and *execute that script on your server*

>  Advantage/disadvantage:
>  
>  -  You can use popular, general purpose programming languages and you can write the code however you want

>  Because of this, programmers end up writing custom code in their own different style and methods, which then becomes difficult to read due to a lack of structure
