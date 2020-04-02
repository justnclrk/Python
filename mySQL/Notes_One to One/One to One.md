Consider the following table customers:

Screen-Shot-2013-10-04-at-12.26.01-PM.png

Although each customer can only have one address, it would seem more fitting and better organized if we separate out the address and put it in its own table. We can then keep better track of specific information about a given address without the fear of our table getting too large to manage.

Screen-Shot-2013-10-04-at-1.33.06-PM

Don't worry, we'll continue to explore foreign keys throughout this chapter!

Screen-Shot-2013-10-04-at-12.27.10-PM

Since each address that we have can only belong to a single customer and each customer can only have one address, we call this a One to One Relationship.

We can visualize the relationship between the customer and address records like this:

graph_1

Note that the existence of a relationship can be optional, like having a customer record that has no related address record.

What Can We Do with SQL
Even though we split up our tables into two different tables, we can combine them into one using SQL. No need to know how to do this yet, but it is important to see how a table can be joined as long as there is a foreign key that references another table's id. We'll cover actual SQL syntax in the next chapter.

0Bw6pb7.gif

Examples of One-to-One
The easiest way to check to see if your relationship makes sense for your data is to simply talk through the relationship out loud. Remember that relationships go in two directions. For example, one address has only one ZIP code, but one ZIP code can have many addresses, thus making it a different type of relationship. Check out some of the sample One-to-One relationships below:

Customers and Credit Cards - Every Customer has one Credit Card, every Credit Card belongs to one Customer.
User and Email - Every User has one Email Address, every Email Address has one User.
Product and Image - Every Product has an Image, every Image is of a Product.