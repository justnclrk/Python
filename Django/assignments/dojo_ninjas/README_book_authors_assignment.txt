Create a new app called 'book_authors' in the same project where you did the previous assignment: Dojo Ninjas.  You'll use this assignment as well as the previous assignment to learn about Ajax.

Please do the following

Create a new model called 'Book' with the information above.
Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the following:
Book.objects.first().authors
Author.objects.first().books
Successfully create and run the migration files
Using the shell...
Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
Book.objects.create(name="C sharp", desc="The Sharpest C")
Book.objects.create(name="Java", desc="Not coffee")
Book.objects.create(name="Python", desc="A Solid Snake")
Book.objects.create(name="PHP", desc="p.i.m.p.")
Book.objects.create(name="Ruby", desc="Red")

Create 5 different authors: Mike, Speros, John, Jadee, Jay
Author.objects.create(first_name="Mike", last_name="LastName", email="mike@gmail.com")
Author.objects.create(first_name="Speros", last_name="LastName", email="speros@gmail.com")
Author.objects.create(first_name="John", last_name="LastName", email="john@gmail.com")
Author.objects.create(first_name="Jadee", last_name="LastName", email="jadee@gmail.com")
Author.objects.create(first_name="Jay", last_name="LastName", email="jay@gmail.com")

Add a new field in the authors table called 'notes'.  Make this a TextField.  Successfully create and run the migration files.
Using the shell...

Change the name of the 5th book to C#
b=Book.objects.get(id=5)
b.name="C#"
b.save()

Change the first_name of the 5th author to Ketul
c=Author.objects.get(id=5)
c.first_name="Ketul"
c.save()

Assign the first author to the first 2 books
mike=Author.objects.get(id=1)
sharp=Book.objects.get(id=1)
java=Book.objects.get(id=2)
mike.books.add(sharp, java)

Assign the second author to the first 3 books
speros=Author.objects.get(id=2)
python=Book.objects.get(id=3)
speros.books.add(sharp, java, python)

Assign the third author to the first 4 books
john=Author.objects.get(id=3)
php=Book.objects.get(id=4)
john.books.add(sharp, java, python, php)

Assign the fourth author to the first 5 books (or in other words, all the books)
jadee=Author.objects.get(id=4)
sharp2=Book.objects.get(id=5)
jadee.books.add(sharp, java, python, php, sharp2)

For the 3rd book, retrieve all the authors
python.authors.all()

For the 3rd book, remove the first author
d=python.authors.first()
d.delete()

For the 2nd book, add the 5th author as one of the authors
java.authors.add(ketul)

Find all the books that the 3rd author is part of
john.books.all()

Find all the books that the 2nd author is part of
speros.books.all()