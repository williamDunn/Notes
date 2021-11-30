## Liquibase Basics
-------------------------------

#### What is Liquibase for? 
-  CI/CD
-  Automates Database Schema Changes / Automatically updates a database

-------------------------------

#### How to use Liquibase
A. Add Liquibase to your project (by dependency injection)

B. Implement database migration (AKA updating the schema/database)
  1) Get DB connection

    -  Getting DB connection depends on your environment & tech stack

  2) Initialize Liquibase

  3) Run the update

-------------------------------

#### Integrating Liquibase into Spring Boot Application (Easy)
-  Just add the Liquibase core to your classpath
```
<dependency>
  <groupId> org.liquibase </groupId>
  <artifactId> liquibase-core </artifactId>
  <version> 3.5.3 </version>
</dependency>
```
--------------------------------

#### 2 Mechanisms Liquibase uses to *Track, Version, & Deploy* changes to your DB
1) Changelogs
2) Tracking Tables
