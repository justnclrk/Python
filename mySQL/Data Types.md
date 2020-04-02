Data Types
The following are the data types that you will be using 95% of the time. Although there are quite a few other data types that you can use, focus on these for now.

Simple Data Types:
VARCHAR(number of characters)
Used to store non-numeric values that can be up to 255 characters. It is called a VARCHAR because it can store a variable number of characters and will only use the space required for each record that is stored in the database. VARCHAR should be used for values with different character lengths like an email, first_name, or last_name.
CHAR(number of characters)
Also used to store non-numeric values, however, it will use up all space for the set number of characters regardless of what value is added. For instance, if I set CHAR(15), and I try to store the value "Coding", it will use up the equivalent of 15 characters even though "Coding" is only 6 characters long. Char is good to use for things that will always be a given number of characters. Char would work well for something like a state_abbreviation.
INT
Used to store integers.
The columns that you will find mostly using the INT are things like a unique identifier for each table. The majority of rows in a table will not exceed 2.1 billion records. INT is good to use for most normal number values like a phone_number or a zip_code.
unsigned (positive numbers only) - can store numerical values from 0 up to 4294967295
signed (positive and negative numbers) - can store numerical values from -2147483648 up to 2147483647


BIGINT
BIGINT would be used for columns that would need to store huge numbers. In most cases, you wouldn't need BIGINT, but if you wanted to store something like a Facebook id when using Facebook's API, since they have over a billion users the id will need to be a data type of BIGINT.
unsigned (again positive numbers only) - can store numerical values from 0 up to 18446744073709551615
signed (positive and negative numbers) - can store numerical values from 9223372036854775807 to -9223372036854775808.


TINYINT
TINYINT would be good to use for numbers that will be relatively small. A good example of something that would use a TINYINT is user level identifier (0 - inactive user, 1 - active user, 9 - admin).
unsigned - can store numerical values from 0 up to 255
signed - can store numerical values from -128 up to 127
FLOAT
Used to store floating point numbers (numbers that need to have decimal places). An example column for this would be like an item_cost.
TEXT
Used to store a large amount of text, like a description, message, or comment. Use this for any text that VARCHAR() is too small to handle.
DATETIME
used to store a date and time in the format YYYY-MM-DD hh:mm:ss