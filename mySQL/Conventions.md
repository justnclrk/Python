Conventions
We will be following a set of conventions to create our database. We don't have to follow these conventions, but we recommend our students to follow them for the following reasons:

Developers can have a better understanding of your database if you are using a set of industry standards.
Developers can create software to automate a lot of the queries if some assumptions can be made. In later chapters, you will learn about Object Relational Mappers (ORM), which are programs that other developers use to make database queries easier by providing some handy functions. These functions will only work if we have followed conventions that ORM author expects, which are primarily based on set industry standards.
Guidelines
Down the line, you may find yourself working with a company that has set up their database conventions a little bit differently, but these are the guidelines that we feel are best for this course:

make the table name plural and ALL lowercase - make it plural (ex. users, leads, sites, clients, chapters, courses, modules)
use "id" as the primary key - name it id (also make it auto-incremented).
name foreign keys with singular_table_name_id when referencing to a primary key in another table name it [singular name of the table you're referring to]_id (ex. user_id, lead_id, site_id, client_id, chapter_id, course_id, module_id).
use created_at and updated_at as columns for the timestamp in EVERY table you create.
When we do things in ORM or in Ruby on Rails, it becomes extremely important that we follow these naming conventions.