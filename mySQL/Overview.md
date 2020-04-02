Main Topics for Database Design
There are many different terms and concepts that you will learn throughout this chapter, but they all point to one very simple concept: Don't Repeat Data. If you can remember this one concept, the rest is just getting yourself familiar with the terminology.

Database Relationships
One to One
One to Many
Many to Many
Three (3) Forms of Normalization
MySQL Workbench
Data Types
What's the Point?
When we normalize our tables, we don't repeat data. This means that in the long run, we can use our storage space more efficiently. 

There's also another advantage we get by normalizing our tables and establishing relationships between them. We will learn later that the ids and the foreign keys serve as the glue between our tables. Using SQL, we can manipulate our tables and create the customized table that we need for the job at hand. 

By breaking out our data into different tables, we make each table be good at one thing: storing instances, or rows, of that data. Also if we separate our tables, our database becomes more modular. This means that we can create our own customized tables depending on the task at hand using SQL. 

We will learn this in the next chapter but it is crucial to understand that we are using the strategy of normalizing our tables and setting relationships between them because we want to save storage space; and also because it makes our database more modular so that we can create more variety of customized tables using SQL.