Background
Up to this point, we haven't really discussed the need to secure our data. Internet hackers are notorious for testing websites' security limitations and exploiting insufficiencies. As web developers, we are responsible for keeping our users' data safe. That means storing the data safely as well. Storing passwords as-is is never a good way to keep data secure. Imagine if a user's password was stored as-is on a database somewhere and a hacker got a hold of it. Now imagine if all of your users' passwords were stored as-is in a database.

This is why we mask users' passwords before we put them into our database. Masking passwords is done using a technique you might have heard of called hashing. Cryptography is a complicated and fascinating field of study that is heavily mathematical in nature. That being said, you don't need a Ph.D. to protect your data. You just need to know a few handy tools, including basic md5 hashing and a salt.

Hashing vs Encryption
As mentioned above, the various techniques for masking data in order to keep its contents private are diverse and complex. Although one can spend years learning the topic in depth, it is important to understand two types of data masking, encryption and hashing, on a conceptual level in order to choose the right technique for your program's needs.

In general terms, hashing scrambles data in such a way the process cannot be reversed. Encryption, however scrambles data in a recoverable way. This means that the person who would like to encrypt data does so using a specific technique that can be reversed given the correct information. The sender and the receiver should ideally be the only holders of the necessary information to decrypt the data. This very fact is what makes encryption less secure than hashing.

So why use encryption? Sometimes we will need both to obscure data and maintain its integrity. Credit card numbers are a great example of use-cases for encryption. Although we need to obscure credit card numbers for security purposes we will eventually need to recover that data.

If hashing isn't reversible, how can we match passwords? The key to that question lies in the fact that the same input into a hashing algorithm always produces the same output. In practical terms this means that we can store a hashed password, re-hash a user's input on login and compare the two hashed values in order to authenticate passwords.

Again, remember this is the most basic summary of these concepts. It's important to know a little about major differences in hashing algorithms that exist, but don't hesitate to explore this topic in more depth on your own.

Note: You may hear hashing referred to as non-reversible encryption. This is a misnomer that has persisted due to the need to explain hashing in simple terms to the lay-person. Realize that hashing is what people mean when they speak about non-reversible encryption.

Basic md5 Hashing
One of the most basic hashing algorithms is known as md5. Md5 is an algorithm that takes a value (most likely a password) and returns a hashed string. To see how this works, type the following into a new Python document:

import md5 # imports the md5 module to generate a hash
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!
What you will see is that long string shown above. The md5 function returns a hashed version of the parameter it is passed. The md5 function yields the same value every time it is run with the same argument. That means the value it spits back is not random -- it is hashed. You may ask: why don't hackers just reverse engineer the values? Answer: the md5 algorithm is well known and solvable but it is very strong in the sense that it is not easily reverse engineered. Md5 is too insecure to be the industry standard but it is a good starting point.

How to use md5
When you add your users to the database upon registration, you should save their passwords as an hashed md5 string. Similarly, when they log in, you should hash the input password to make sure it matches with the one saved in the database. Here's the idea:

The user being put into your database:

import md5 # do this at the top of your file where you import modules
@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest()
     insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username,
     :email, :password, NOW(), NOW())"
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)
When your user is trying to log in:

password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>
Salted hashing
While md5 is an easy to implement hashing method, it is not secure enough for even the most basic projects. You can, however, make your data more secure by making the hashing method more random. By random, we mean more unpredictable. As we said before, md5 hashing is the same no matter what computer runs the code. So to make our hashing more powerful, we will add a salt to our hashed string. A salt is a random unique key used to generate a unique password. Example:

salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)
A salt is a string of random characters that will be passed to a hashing method (an md5()) along with the string we are trying to hash (the submitted password) via concatenation. The hashing method that uses the salt is designed in such a way that it takes the salt to compute the hashed string, using the salt as an 'ingredient' in the hashing 'recipe'.

Generating a salt
To generate a salt, you just need to generate a random string of characters. The code below actually uses two different functions to create a random string:

import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
The function called os.urandom() returns a string of bytes. The number of bytes is equal to the parameter provided. This string isn't a normal alphanumeric string, so we turn it into a string using the function b2a_hex(), which will turn the value into a normal alphanumeric string. This new random string will be our salt. The idea is to store this salt during the registration process. Example:

username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
hashed_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at)
     VALUES (:username, :email, :hashed_pw, :salt, NOW(), NOW())"
query_data = { 'username': username, 'email': email, 'hashed_pw': hashed_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)
Now, when we are trying to authenticate a user's login, we do some pretty nifty stuff:

email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
query_data = {'email': email}
user = mysql.query_db(user_query, query_data)
if len(user) != 0:
 encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
 if user[0]['password'] == encrypted_password:
  # this means we have a successful login!
 else:
     # invalid password!
else:
  # invalid email!
copy
Below are hashed passwords generated by concatenating a password ('password' as value) with the salt ( str_shuffle('hello') which we know is very insecure) within the md5 hashing method. Even though we provided very simple values for both password and salt, we still get 5 random hashed values for password in the database:



By adding a salt we have made our passwords slightly more secure. This is to get you started with the idea of password hashing and salt. We'll talk about more secure password storage a little later in the Django section.