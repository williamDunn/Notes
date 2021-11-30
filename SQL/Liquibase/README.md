#### Liquibase Basics
-------------------------------

## What is Liquibase for?
-  Automates Database Schema Changes / Automatically updates a database

-------------------------------

## How to use Liquibase
1) Add Liquibase to your project (by dependency injection)
2) Implement database migration (AKA updating the schema/database)
  a. Get DB connection
    -  Getting DB connection depends on your environment & tech stack
  b. Initialize Liquibase
  c. Run the update
