Import/Export DB
Note: We will be mostly creating our own database/ERD and forward engineering into a database.

You may use MySQL Workbench in exporting and importing database (SQL) files.

(Note: Mac users should make sure to use version 6.3.9 or higher.)

Using MySQL Workbench
Import:

Copy the SQL commands from the .sql file that you wish to import. Paste the copied contents to MySQL Workbench query window and click the bolt icon.

2DZiSHp

Upon successful run of your query, refresh the Schemas section (on the left side of Workbench) and your newly imported database will appear.

You may also use the Data Import/Restore option on Workbench to import database.

Export:
Click the Data Export option on your Workbench and choose the database/schema you wish to export.

workbench-export

Choose the Export to Self-contained file option. Be sure to indicate file name (don't forget to add .sql as the file extension) and specify the path to where you are saving the exported SQL file.

workbench-export2

Then click Start Export. This will generate a .sql file which contains MySQL commands to duplicate the database you created.