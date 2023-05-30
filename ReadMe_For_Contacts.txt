The script starts with the import sqlite3 statement. Then we have defined class contact. Instance variables are set to their values. Then comes the method sql_connect definition.
When called this method will make a connection to the SQLite database and fetch all the contacts in rows variable which in turn will be used for appending all contact objects from the database to self.contact_list.Next, we have a definition for a handle_choice method. This method takes appropriate
actions depending on the values of the self. choice variable. Next comes the show_list method
definition which is the first thing you will see after running this script.﻿Next comes the polymorphism concept of OOP. Here we have changed the behavior of 
the default __add__() dunder function. In the Contacts class __add__ method instead of trying to add or concatenate, this method will append the new Contacts object to self.contact_list variable. Next follows the add_contact method definition. In this method a call to the constructor of the Information 
Class is made in line, self + Infomation(). Also, note that the + operator will call the changed version of __add__ dunder method. Then in this method connection to the SQLite database is made again and a new Contact object is added to the table contacts in Database. Next are the show_info()  and display() method declarations.
After that Class Information is defined. The constructor of this class also implements
polymorphism concepts of OOP. The constructor of this class is overloaded. It accepts self and *args as parameters to the init method.
This method behaves differently depending on the constructor call. Whether the constructor is called from the console or in the sql_connect()
method. Finally, the Information Class defines the display() method.

