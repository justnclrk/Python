UPDATE Basics
We can UPDATE our database in two ways as well. Once again, it is important to pay attention to the SQL commands that are being run even if we just use the GUI because we will have to run UPDATE commands later in the bootcamp. Try updating your table both ways.


Updating Records
The SQL command pattern for updating/editing records is as follows:

UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)
IMPORTANT: if WHERE condition is not added to the UPDATE statement, the changes will be applied to every record in the table.