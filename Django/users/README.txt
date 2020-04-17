Assignment: Users
Create a new app called 'user_login'. Create a new model called 'User' that has the following fields/attributes

Please do the following:

Create a new model called 'User' with the information above.
Successfully create and run the migration files

Using the shell...

Know how to retrieve all users.
User.objects.all()

Know how to get the last user.
User.objects.last()

Create a few records in the users.
User.objects.create(first_name="Justin", last_name="Clark", email_address="justlookin213@gmail.com", age="28")
User.objects.create(first_name="Steve", last_name="Clark", email_address="thecat@gmail.com", age="4")
User.objects.create(first_name="Scarlet", last_name="Stoolman", email_address="ayedog@gmail.com", age="5")

Know how to get the first user.
User.objects.first()

Know how to get the users sorted by their first name (order by first_name DESC)
User.objects.order_by("first_name")

Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
User.objects.get(id=3)
a = User.objects.get(id=3)
a.last_name = "Clark"
a.save

Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
b= User.objects.get(id=1)
b.delete()

(optional) 
Ninja:
Find a way to validate the data coming in to the shell.  For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.