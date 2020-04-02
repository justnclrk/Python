DELETE Basics
You can DELETE your records as well. 

If you are getting an error regarding SQL SAFE UPDATES, run the following command to let MySQL Workbench know that you know what you are doing and you want to DELETE stuff from the database.

SET SQL_SAFE_UPDATES = 0;

Deleting Records
The SQL command pattern for deleting/removing records is as follows:

DELETE FROM table_name WHERE condition(s)
IMPORTANT: if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.