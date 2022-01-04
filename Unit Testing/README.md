Using JUnit for Unit Testing
----------------------------

1. JUnit is included with eclipse, but if using something other than Eclipse, may need to install from junit.org
2. In Eclipse, right click on your project, choose Build Path and New Source Folder
    -  Name the folder test, and click Finish
3. Right-click on the project, choose New / JUnit Test Case
    -  Change the source folder to test
    -  Give new class a name (like PrimeTest)
    -  When prompted, choose to add JUnit to the classpath
4. Write the test case method
    -  Should start with @Test
    -  public void testname()
        -  Common naming convention:
        -  MethodName_WhatIsBeingTested_ExpectedBehavior
    -  Commonly use assertEquals to test outcome, but there are other options as well
    -  If an exception is expected:
        -  @Test(expected=IndexOutOfBoundsException.class)
    -  Code needed to run before each test, to do setup:
        -  @Before
        -  public void setup() throws Exception {...}
