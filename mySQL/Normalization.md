What is Normalization?
Database normalization is simply a convention for splitting large tables of data into smaller separate tables with the primary goal being to not repeat data. Why is this so important? Let's say that you wear a watch so you can check the time, because it's very important for you to know what the current time is. Would wearing eight watches make it easier? No way! Now we have eight conflicting accounts of what the proper time is. Worse yet, if we ever want to update the time, we'd have to do it for every watch independently. That's not very efficient!

You can apply a similar concept to database design. If we want to store a user's email address, we'd want to store it in only one place. Then, if we ever need to refer to it again, we'd simply use the id. The id will never change, so even if we update the user's email address, none of the other connections we defined in our database will be damaged. Neat!

Below are the three main rules of database normalization. You should use these as a guide for designing your ERDs. Always remember, however, that they are common convention, and not absolute rules. It is possible to take normalization to an extreme. For example, a simple address field. One state can have many cities, one city can have many streets, one street can have many buildings, one building can have many apartments, one apartment can have many residents... and so on. Yikes, that can get really crazy really quick! In the next sections, you'll learn more about why this type of complexity can be inefficient, especially for simple assignments.

First Form

Each Column in your table can only have 1 value.

Ex. You should not have an address column in your table that lists the address, city, state, and zip, all separated by commas.

Second Form
Each Column in your table that is not a key (primary or foreign) must have unique values.

Ex. If you have a movies table with a categories column, you should not have a category repeated more than once.

Third Form
You cannot have a non-key column that is dependent on another non-key column.

Ex. If you have a books table with columns publisher_name and publisher_address, the publisher_address and publisher_name should be separated into a separate table and linked to books with a foreign key. The publisher_address is dependent on the publisher_name and neither column is a key column.