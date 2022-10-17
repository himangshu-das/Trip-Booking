import re
import mysql.connector
import sys
import os
conn = mysql.connector.connect(host='localhost', username='root',password='Pass@123', database='itc')
my_cursor = conn.cursor()
data=[]

class registration:
    def __init__(self):
        print("Please Register to Continue...")
    def my_func(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            self.name= input("Enter Name: ")
            self.e_mail = input("Enter email id: ")
            if (re.fullmatch(regex, self.e_mail)):
                data.append(self.e_mail)
                conn.commit()
                break
            else:
                print("Not a valid email")

    def checknum(self):

        while True:
            self.phone = input("Enter phone no: ")
            r = re.fullmatch('[6-9][0-9]{9}', self.phone)
            if r != None:
                data.append(self.phone)
                break
            else:
                print('Not a valid number')

    def checkpassword(self):
        #print("password format:\n   atleast 1  [a-z], 1 [A-Z],1 [!%*$#@],1 [0-9]\n   Minimum 6,max 12 character")
        while True:
            self.password = input("Enter password: ")
            length = True if len(self.password) > 6 and len(self.password) < 12 else False
            spec_char = ['@', '#', '$', '%', '!', '*']
            digit = any(char.isdigit() for char in self.password)
            is_upper = any(char.isupper() for char in self.password)
            is_lower = any(char.islower() for char in self.password)
            is_spec_char = any(char in spec_char for char in self.password)
            isValid = all([length, digit, is_upper, is_lower, is_spec_char])
            if isValid:
                data.append(self.password)

                break
            else:
                print("Enter a Valid Password....Min 6 characters, 1 Uppercase, 1 Lowercase and 1 special character")

        query3 = ("INSERT INTO CUSTOMER1 (C_NAME, E_MAIL, PHONE, PASS) VALUES ('{}','{}','{}','{}')".format(self.name,self.e_mail,self.phone,self.password))
        my_cursor.execute(query3)
        conn.commit()

class log():

    def set_email(self):

            self.email = input("Enter email: ")
            query2 = "SELECT E_MAIL FROM CUSTOMER1"
            my_cursor.execute(query2)
            records = my_cursor.fetchall()
            for row in records:
                if self.email==row[0]:

                    break
                else:
                    print("Please enter a registered email!")
                    call = log()
                    call.set_email()

    def set_password(self):

            password = input("Enter password: ")
            query5 = "SELECT PASS FROM CUSTOMER1 WHERE E_MAIL = '{}'".format(
                self.email)
            my_cursor.execute(query5)
            rec = my_cursor.fetchall()
            for row in rec:
                if password == row[0]:

                    break
                else:
                    print("Unmatched password")
                    ca = log()
                    ca.set_password()
