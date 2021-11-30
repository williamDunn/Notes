## SQL (Structured Query Language)
--------------------------------
#### What is it?
SQL is a language used specifically to do thing with data. Things like selecting certain data between given dates, updating a record that matches a certain criteria, etc.

--------------------------------
Standard SQL statement:

```
SQL commands:

Select:

From:

Where:
```
--------------------------------

##### Types of JOINs:

(Inner) JOIN:
-  Returns records *matching values* in *both tables*

FULL (outer) JOIN:
-  Returns *all* records *when there is a match in either table*

LEFT (outer) JOIN:
-  Returns *all records from left table*, & *matched records from right table*

RIGHT (outer) join:
-  Returns *all records from right table*, & *matched records from left table*
-  
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
#### Database Terminology
-  Table (Collection of Rows)
-  Field / Column (in a table)
-  Tuple / Row (in a table)
-  View (? Looking at data ?)
-  Index (? Finding data ?)
