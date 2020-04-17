Assignment: Dojo Ninjas
Create a new app called 'dojo_ninjas'. For this project, you're going to need the following tables/models. Please see the following diagram and create the necessary model:

-Dojo
Have it include the name of the dojo and the city and state of each dojo
Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
Have the third dojo be "CodingDojo New York" in "New York", "NY".


-Ninja
Have it include first_name, last_name of each ninja in the dojo.
Each dojo can have multiple ninjas and each ninja belongs to a specific dojo.


-This is what you'll do:

Start a new app (the name of the app should be 'dojo_ninjas')

Create appropriate tables/models that allows you to perform tasks such as (Dojo.objects.first().ninjas.all()) (Ninja.objects.first().dojo)


-Using Django Shell:

Create 3 dojos
Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")

Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
a=Dojo.objects.get(id=1)
a.delete()
b=Dojo.objects.get(id=2)
b.delete()
c=Dojo.objects.get(id=3)
c.delete()

Create 3 additional dojos by using Dojo.objects.create
Dojo.objects.create(name="CodingDojo Chicago", city="Chicago", state="IL")
Dojo.objects.create(name="CodingDojo Iowa City", city="Iowa City", state="IA")
Dojo.objects.create(name="CodingDojo New Orleans", city="New Orleans", state="LA")

Create 3 ninjas that belong to the first dojo you created.
Chicago = Dojo.objects.get(id=4)
Student_One = Ninja.objects.create(first_name="Steve", last_name="Cat", state="IL", location=Chicago)
Student_Four = Ninja.objects.create(first_name="Mo", last_name="Money", state="IL", location=Chicago)
Student_Five = Ninja.objects.create(first_name="Sears", last_name="Tower", state="IL", location=Chicago)

Create 3 more ninjas and have them belong to the second dojo you created.
Iowa_City = Dojo.objects.get(id=5)
Student_Two = Ninja.objects.create(first_name="Sam", last_name="Stoolman", state="IA", location=Iowa_City)
Student_Six = Ninja.objects.create(first_name="Matt", last_name="Stan", state="IA", location=Iowa_City)
Student_Seven = Ninja.objects.create(first_name="Herky", last_name="Hawkeye", state="IA", location=Iowa_City)

Create 3 more ninjas and have them belong to the third dojo you created.
New_Orleans = Dojo.objects.get(id=6)
Student_Three = Ninja.objects.create(first_name="Jay", last_name="Cee", state="LA", location=New_Orleans)
Student_Eight = Ninja.objects.create(first_name="Hurri", last_name="Cane", state="LA", location=New_Orleans)
Student_Nine = Ninja.objects.create(first_name="Lil", last_name="Wayne", state="LA", location=New_Orleans)

Be able to retrieve all ninjas that belong to the first Dojo
Student_One.location.name
Student_Four.location.name
Student_Five.location.name

Be able to retrieve all ninjas that belong to the last Dojo
Student_Three.location.name
Student_Eight.location.name
Student_Nine.location.name

Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.

python manage.py makemigrations
You are trying to add a non-nullable field 'desc' to dojo without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> none
Invalid input: name 'none' is not defined
>>> 3
Migrations for 'first_app':
  apps\first_app\migrations\0003_dojo_desc.py
    - Add field desc to dojo

python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, first_app, sessions
Running migrations:
  Applying first_app.0003_dojo_desc... OK