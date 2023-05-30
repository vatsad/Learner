import sqlite3

import self as self


class Contacts:
    def __init__(self):
        self.view = 'list'
        self.contact_list = []
        self.choice = None
        self.index = None
        self.db = 'contacts.sqlite'


    def sql_connect(self):
        conn = sqlite3.connect('contacts.sqlite')
        cur = conn.cursor()
        cur.execute('select * from contacts')
        rows = cur.fetchall()
        for tup in rows:
            tup = tuple(tup)
            self.contact_list.append(Information(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]))
        conn.close()
    def handle_choice(self):
        if self.choice == 'q':
            self.view = 'quit'
        elif self.choice == 'a' and self.view == 'list':
            self.view = 'add'
        elif self.choice.isnumeric() and self.view == 'list':
            idx = int(self.choice) - 1
            if idx >= 0 and idx < len(self.contact_list):
                self.index = idx
                self.view = 'info'
        elif self.choice == 'c' and self.view == 'info':
            self.view = 'list'
        elif self.choice == 'n' and self.view == 'info':
            self.index = self.index + 1 if self.index + 1 < len(self.contact_list) else 0
        elif self.choice == 'p' and self.view == 'info':
            self.index = self.index - 1 if self.index - 1 >= 0 else len(self.contact_list) - 1

    def show_list(self):
        print()
        if len(self.contact_list) == 0:
            self.choice = self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
        else:
            for idx ,c in enumerate(self.contact_list):
                print("{}, {}, {}".format(idx + 1, c.first_name, c.last_name))
            self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
        self.handle_choice()


    def __add__(self, other):
        self.contact_list.append(other)


    def add_contact(self):
        self + Information()
        x = len(self.contact_list)
        conn = sqlite3.connect('contacts.sqlite')
        cur = conn.cursor()
        tup = (self.contact_list[-1].first_name,self.contact_list[-1].last_name, self.contact_list[-1].personal_phone, self.contact_list[-1].personal_email, self.contact_list[-1].work_phone,
               self.contact_list[-1].work_email, self.contact_list[1].title)
        cmd ='''INSERT INTO contacts (first_name,last_name,personal_phone,personal_email,work_phone,work_email,title) VALUES (?,?,?,?,?,?,?)'''
        cur.execute(cmd, tup)
        conn.commit()
        conn.close()
        self.view = 'list'


    def show_info(self):
        self.contact_list[self.index].display_info()
        self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
        self.handle_choice()

    def display(self):
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'add':
                print()
                self.add_contact()
            elif self.view == 'info':
                self.show_info()

            elif self.view == 'quit':
                val = input("Quit and save changes to Database: yes or no: ").lower()
                if val == 'yes':
                    print('\nClosing the contact list...\n')
                    break



class Information:
    def __init__(self, *args):
        if len(args) == 0:
            self.first_name = input('Enter their first name: ')
            self.last_name = input('Enter their last name: ')
            self.personal_phone = input('Enter their personal phone number: ')
            self.personal_email = input('Enter their personal email address: ')
            self.work_phone = input('Enter their work phone number: ')
            self.work_email = input('Enter their work email address: ')
            self.title = input('Enter their work title: ')
        else:
            self.first_name = args[0]
            self.last_name = args[1]
            self.personal_phone = args[2]
            self.personal_email = args[3]
            self.work_phone = args[4]
            self.work_email = args[5]
            self.title = args[6]


    def display_info(self):
        print(f'\n{self.first_name} {self.last_name}')
        print(f'Personal phone number: {self.personal_phone}')
        print(f'Personal email address: {self.personal_email}')
        print(f'Work title: {self.title}')
        print(f'Work phone number: {self.work_phone}')
        print(f'Work email address: {self.work_email}')
    def greeting(self):
        print("greetings from contacts class file")



test = Contacts()
test.sql_connect()
test.display()
