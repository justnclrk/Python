Continuing from our previous example of customers and addresses tables where one customer can only have one address...

Screen-Shot-2013-10-04-at-1.38.16-PM

We now want our customers to be able to order items from us. To add our orders table, it will require us to define a different relationship. Each customer is able to have multiple orders, but each order can only belong to one customer

Screen-Shot-2013-10-04-at-1.38.53-PM

Since one customer can have many orders for any given user we call this a One to Many Relationship.

graph_2

What Can We Do with SQL
Notice how the foreign key and the id of the table that we want to combine act as the glue. We can join different tables using SQL. Once again, we will learn how to do this later on but it is important to know that we are setting up these relationships so that we can create customized tables like the illustration below by using SQL to join different tables on the foreign key and the primary id.

SdHYDDl

Examples
One-to-Many is probably the most common relationship you'll encounter while making web applications. Often times a One-to-One relationship is actually much more similar to a One-to-Many. Below are a few examples:

Messages and Comments - One Comment belongs to one Message, but one Message can have many Comments.
States and Cities - One City is only in one State, but one State can have many Cities.
Customers and Orders - One Order only has one Customer, but one Customer can have many Orders.