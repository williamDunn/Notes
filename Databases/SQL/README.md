## SQL (Structured Query Language)
--------------------------------
#### What is it?
SQL is a language used specifically to do things with data. Things like selecting certain data between given dates, updating a record that matches a certain criteria, etc.

--------------------------------
Standard SQL statement:

```
SQL commands:

Select:

From:

Where:
```
--------------------------------

#### Types of JOINs:

(Inner) JOIN:
-  Returns records *matching values* in *both tables*

FULL (outer) JOIN:
-  Returns *all* records *when there is a match in either table*

LEFT (outer) JOIN:
-  Returns *all records from left table*, & *matched records from right table*

RIGHT (outer) join:
-  Returns *all records from right table*, & *matched records from left table*

------------------------------
#### SQL Stored Procedure:

-  SQL statement(s) that were created & stored in the DB
###### Pros:
-  Anyone can use,
-  Updateable,
-  ? Flexible Parameters ?

Example:

```
CREATE PROCEDURE *Name*
AS
Select *
From *TableName*
GO;
```

```
EXEC *NAME*
```

------------------------------
#### SQL Index

-  A SQL index is used to retrieve data from a database very fast
    -  they're small, fast, and optimized for quick lookups
-  quick lookup table for finding records users need to search frequently
-  Very useful for connecting relational tables and searching large tables
-  Indexing a table or view is one of the best ways to improve the performance of queries and applications

Creating an index
```
CREATE INDEX idx_pname
ON Persons (LastName, FirstName); 
```

Deleting an index (in SQL server)
```
DROP INDEX table_name.index_name; 
```

------------------------------
