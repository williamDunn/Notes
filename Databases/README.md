## What is a Database?

-  A structured set of data held in a computer

----------------------

#### Database Terminology

-  Field / Column (in a table)
-  View (the result set of a stored query on the data)

(RDBMS)
-  Table (a collection of data elements organised in terms of rows and columns)
-  Tuple / Record / Row (in a table)
-  Attribute / field / column (values in a row)

----------------------
**Primary Key**
-  unique identifier within a table

**Foreign Key**
-  is a primary key in another table

**Candidate Key**
-  Minimal set of attributes that can uniquely identify a tuple (eg., STUD_NO in STUDENT relation)

**Super Key**
-  The set of attributes that can uniquely identify a tuple (eg., STUD_NO, (STUD_NO, STUD_NAME), etc.)

----------------------
#### Normalized vs Denormalized

-Normalized DBs are designed to minimize redunency (duplicates)

-Denormalized DBs are designed to optimize read time

----------------------

#### SQL vs NoSQL Databases

-  SQL Databases are relational **|** NoSQL Databases are non-relational

#### Why use SQL vs NoSQL DBs

-  SQL = Organized
-  NoSQL = Easier to store different types of data

----------------------
#### Data Modeling

-  Relational Data Model
-  Entity Relationship Model

----------------------
## Database Schema
-  Structure Defining Around the Data of a DB

##### OR

-  Structure for Understanding the Data and their Corresponding Data Relationships

*(Data as in things like: tables, views, fields, relationships, indexes, etc.)*

-----------------------

#### Structure of the Schema is Dependant on the Platform/DB (MongoDB, Oracle, Microsoft, etc.)

##### 2 Types:

1) Schema on *Read*
-  For Unstructured Data (This is where structure is added to the query code)
- ie. Hadoop, MongoDB

2) Schema on *Write*
-  DBs that force structure as a condition before data is written
-  ie. SQL server?, etc.

----------------------
#### How Schema is Designed
-  How schema is designed influences behaviors in database

(Slow querying)
1) Series of Tables connected by primary keys
-  Likely for reading & writing singular records
-  ie. Salesforce

(Fast querying)
2) Central table connected to keys supplied by surrounding tables
-  Likely for a system that needs highlyu efficient read output
-  STAR Schema - ideal for high scal information delivery
