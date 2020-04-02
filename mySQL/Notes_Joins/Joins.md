Joining Tables
Remember foreign keys from the last chapter? We now get to put them to use! We JOIN two tables on the ids that match each other. This means that we can't JOIN tables together that don't have a relationship with each other (e.g. One to One, One to Many, Many to Many). A foreign key in a table matches up directly with an id in another table. Let's take a peek at what this looks like.

Go ahead and download the  morepractice.sql and follow along with the video.


Here is another example:

One to One
SELECT * FROM customers 
JOIN addresses ON addresses.id = customers.address_id;

Screen-Shot-2013-10-09-at-8.56.44-AM

0Bw6pb7

One to Many
SELECT * FROM orders 
JOIN customers ON customers.id = orders.customer_id;

Screen-Shot-2013-10-09-at-8.57.06-AM

SdHYDDl

Many to Many
SELECT * FROM orders 
JOIN items_orders ON orders.id = items_orders.order_id 
JOIN items ON items.id = items_orders.item_id;

Screen-Shot-2013-10-09-at-8.57.35-AM

zu3hsWo


The above examples are using a JOIN, also referred to as INNER JOIN. However, there may be times where you would want to use a different type of JOIN. Imagine that in the  One to Many relationship above there was a customer that had not yet placed an order. There wouldn't be a customer_id listed in the orders table. If we wanted to get the results of all the customers orders including the customers that hadn't yet placed an order we would have to use a LEFT JOIN. See the visual representations of what you can expect to be included when using different types of joins.

Grouping Results
In the previous section, we saw how we could use functions to manipulate a single value in a single row. With GROUP BY, we will group multiple rows together, by performing a function to combine the values of those rows. Because this results in a single result for the group, it will combine those grouped rows into a single resultant row. 

As you can imagine, there are many different ways that we might combine multiple values into a result. Below are a list of the most common ones, often called Grouping Functions or Aggregate Functions.  

Aggregate Functions

Screen-Shot-2013-10-08-at-11.17.10-PM