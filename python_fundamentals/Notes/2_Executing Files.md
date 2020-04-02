Creating and Running Python Files
We just learned how to experiment with Python code in the shell, but as soon as we close the shell, we've lost all of our hard work. Now we need a way of saving our code so that we can use it later.

Open your text editor and create a new file called hello_world.py and save it in a directory where you plan on storing the rest of your python assignments. Keeping an organized directory structure will be very important going forward. Right now your file should be empty.

Run your first file:
Open your terminal and change directories into the directory where you saved your new file. Type python hello_world.py

Nothing will output into your terminal because we haven't entered anything in our new file. Read on to see your output in the terminal.

Printing
In your new file add the following line of code:

print "Hello World!"
The print statement tells the Python interpreter to output whatever follows into the terminal. It's a lot like console.log() in JavaScript. Save your document and run the above command again. Your terminal output will look like the following:

If you got an error instead of the expected output, make sure you're in the same directory as the target file and that you've saved your changes. To check if you're in the target location try ls (dir for Windows) to see if your file is in the list.

We can now use a variable to contain any type of information, ask Python to print it, and see that output in our terminal. Try entering the following in your file and run your file again:

x = "Hello Python"
print x
y = 42
print y