SQL
For any relational database like MySQL, you will interact with it using SQL. In the previous chapter, we learned how to design a schema for our data: we set up the collections that we needed, and we set up the relationships among tables. Now we will see the importance of relationships, and how to use SQL to adjust the data in any way we can imagine.



SQL stands for Structured Query Language, which is a programming language designed for managing data in relational databases. SQL statements are used to perform tasks; they can SELECT data, SELECT data WHERE some conditions are true, INSERT data, UPDATE data, DELETE data, and JOIN different tables together. As we go over all of the basic SQL commands, be patient. You will be learning a domain-specific language, unrelated to languages you may have previously seen. However, mastering SQL is the key to mastering the database component of your application.

Database and SQL
We will install and run a MySQL server on our operating system to connect first to MySQL Workbench, and later our web applications. This will be a database server, which will be listening for connections on localhost (just like our Flask web servers). Also like our web servers, our MySQL server will be assigned a port number. After we install and configure MySQL, we will then connect to our database from MySQL Workbench via localhost and whichever port our MySQL server is using.

Installation (Mac)
We will use the homebrew package manager to install and initialize the required MySQL software.  If you haven't yet installed homebrew, you may refer back to the installation steps from earlier in the course.

All of the listed steps below are commands you will run in your Terminal.
Use homebrew to install MySQL.
brew install mysql
Use homebrew to start your MySQL Server as a  "service", meaning it will run in the background and allow connections.
brew services start mysql
Now with MySQL installed, you have access to some new command line tools. Run the following command to set the MySQL root user's password to "root".
mysqladmin -u root password "root"
mysql -u root -p
Installation (Windows 10)
Download the required MySQL software from the MySQL website Choose the MySQL Installer MSI Option.
Follow the installer guidelines, with the following considerations:
Choose the password "root" for your root user password
For "Windows Service" make sure you have the "Configure MySQL Server as a Windows Service" and "Start the MySQL Server at System Startup" options selected.

The installer will configure your Windows system to run the MySQL Server automatically on startup, listening on the default port 3306, as well as establish the required environment variables to run MySQL tools from a Windows shell

Open a MySQL shell from CMD/PowerShell to make sure everything is working correctly:

mysql -u root -p and enter "root" when prompted

Troubleshooting:
Problem: Running mysql in CMD/PowerShell gives the following error: 'mysql' is not recognized...

Solution: Make sure you have an Environment Variable PATH to your MySQL executables. Likely to be in C:\\Program Files\MySQL\MySQL Server 5.7\bin

Connecting to MySQL Server
Now that you have installed, configured, and started a MySQL server on our operating system, we can now connect to it with MySQL Workbench.

Open up MySQL Workbench, which will bring up a main menu showing your different DB connections. Most of you will only have one, unless you have added more.  Select the wrench icon to test and configure your connections.

Here you will notice the Hostname: 127.0.0.1 (the IP address for localhost), Port, and Username. Here you can change the port number if your MySQL server is on a different port. Test the connection with the button at the bottom of this menu.





Changing your Port
If you wish to change the port on the MySQL server, you can do so by adding a configuration file to a specific directory path depending on your OS.  If you do change your port here, make sure that your connection settings in MySQL Workbench also reflects this change.

Let's say we wanted to change the port our server is listening on to 3307 (instead of the default 3306). Create a file named my.cnf (the name is important), and add the following text:

[client]
port = 3307
[mysqld]
port = 3307
Make sure this file gets saved to one the following directories, depending on your OS

Mac/Linux: /etc/my.cnf
Windows: C:\MySQL\MySQLServer\my.cnf
When the file is saved, you will need to restart your MySQL server to reflect this change

Mac
brew services restart mysql
Windows
NET STOP MYSQL
NET START MYSQL
Privacy Policy