Hidden Inputs
Hidden input fields are form fields that are hidden from the user. Hidden input is used, along with other input elements, to transfer information between different pages.

A hidden input is just an ordinary input element but has a type of "hidden", which means there will be no visual representation in the rendered HTML, but the form element IS usable by the method where the form is sent.

<input type="hidden" name="action" value="register">
Now there are multiple ways we can make use of the hidden input field, but in this tab, we are just going to focus on how to use this field to navigate our submitted forms to its appropriate function or process. Suppose we have two forms within our index page:

<form method="post" action="/process">
    <input type="hidden" name="action" value="register">
    <input type="text" name="first_name">
    <input type="text" name="last_name">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Register">
</form>
<form method="post" action="/process">
    <input type="hidden" name="action" value="login">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>
Notice that both forms submit their data to the POST /process route and have hidden inputs with the same name, but different values. The input  name's value is up to you, but for this demonstration let's just have "action" as the name. 

In the POST /process route, make sure that you have an if statement that checks what form is being submitted

if request.form['action'] == 'register':
  //do registration process
elif request.form['action'] == 'login':
  //do login process
By using the hidden input fields we set up on the index page, we can be sure that only the codes related to the form being submitted are going to be executed.

But know that, even though hidden inputs are invisible to the user, it is actually very visible in the page's source. That means other users can still see and change the values you set in the hidden input. So be very careful in choosing what data you store in there as value, and set appropriate actions if a user tries to change or remove it.