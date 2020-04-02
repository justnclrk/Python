To git bash or not to git bash?
The decision is up to you! If you're comfortable with command prompt you're less likely to encounter bugs while using it. We recommend you use it, in fact. Commands will be similar to the Linux/Unix commands we typically provide, but if the command doesn't work, the correct one is very simple to find.

If you're more comfortable operating in a Linux-like environment, you can use a bash shell like git bash, which you've probably been using since web fundamentals. If you choose to do so, you may encounter a few strange behaviors when running the Python shell. We'll talk about two of the most common errors so you'll be prepared if you decide to continue to use git bash.

Issue #1: Python Shell hangs on initialization
If you type the python command in git bash and you see your cursor move down a line but nothing else happens, you've encountered a known problem relating to a software dependency called ncurses. The best way to solve this problem is by adding an alias to your .bashrc file. From your bash shell:

cd ~
touch .bashrc
start .bashrc
Now with your file open, add this line:

alias python='winpty python.exe'
Then, restart your Python Shell.

Issue #2: Print statements do not appear
This is a known problem and has yet to be corrected. There are two good workarounds. If you're running python in shell, you'll have to flush the output buffer after each print statement. This line does the trick: sys.stdout.flush(). If you're running the code from a document using the python filename.py just modify this to python -u filename.py.