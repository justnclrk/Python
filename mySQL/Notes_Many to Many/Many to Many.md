We have a table that keeps track of each of the orders the customer placed but we haven't created a way to keep track of the items they are ordering.

Screen-Shot-2013-10-07-at-3.39.23-PM

Here we created an items table to hold the name and description of each item that the customer can order.

Screen-Shot-2013-10-07-at-4.21.19-PM

Since each order can have many different items and those same items can show up in many different orders, we have to use a different type of relationship to connect orders to items. Orders can have many items and items can have many orders, so we call this a Many to Many Relationship.

In a Many to Many relationship, we create a connector table that has both the order_id and the item_id so that we can determine all the items in a particular order.

Screen-Shot-2013-10-07-at-4.26.47-PM

Here is how we can visualize this kind of relationship:

graph_3

If you want to include the items_orders records in the graph, it may look like this:

graph_4

What Can We Do with SQL

zu3hsWo

Examples
Many-to-Many is often the most confusing type of relationship for lots of people, but if you make sure to talk-out the relationship out loud, you'll quickly find if it works or not. Remember, anytime you have a Many-to-Many, it will require some sort of joining table! Check out the below examples and use how we describe the relationship as a guide:

Users and Interests - One User can have many Interests, one Interest can be applied to many Users.
Actors and Movies - One Movie can have many Actors, one Actor can be in many Movies.
Businesses and Cities - One Business can be spread across many Cities, one City can be home to many Businesses.