INSERT Basics
Now, let's go over how we can INSERT data. We can do this in two ways. One way is to manipulate the table directly using our MySQL Workbench and another way is to run direct SQL commands in the editor. 

Even if you are using the GUI to insert data, it is important to see what kind of SQL commands it is running. We are going to have to run INSERT statements using SQL commands later so it is important that we know how to INSERT data both ways.


Inserting Records
The SQL command pattern for INSERTing records is as follows:

INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value'); 