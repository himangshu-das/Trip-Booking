from csv import DictWriter
from csv import DictReader
import mysql.connector
import sys
import os
conn = mysql.connector.connect(host='localhost', username='root',password='Pass@123', database='itc')
my_cursor = conn.cursor()

loc = []
ht=[]

nam = []
ag = []
gen = []
class hotel:
    def hotel_data(self):
        print("\n********************WELCOME TO HOTEL BOOKING SYSTEM***********************")
        self.location = input("Enter your location: ")
        query2 = "SELECT HOTEL_NAME FROM HOTELS WHERE LOCATION = '{}'".format(
            self.location)
        loc.append(self.location)
        my_cursor.execute(query2)
        print("\n********YOUR REQUIRED HOTELS********")
        rec = my_cursor.fetchall()
        for row in rec:
            print(row[0])

        htl = input("\nENTER A HOTEL NAME YOU WANT: ")
        ht.append(htl)
        print("\n********THE DETAILS OF YOUR HOTEL********")
        query3 = "SELECT * FROM HOTELS WHERE HOTEL_NAME = '{}' AND LOCATION = '{}'".format(
            htl, self.location)
        my_cursor.execute(query3)
        rec1 = my_cursor.fetchall()
        for row in rec1:
            print("Id = ", row[0] )
            print("Name = ", row[1])
            print("Location  = ", row[2])
            print("Base Price  = ", row[3])

        inp = input("\nWOULD YOU LIKE TO CONTINUE (Y/N): ")
        while True:
            if inp == 'n' or inp == 'N' or inp == 'no' or inp == 'NO':
                h=hotel()
                h.hotel_data()
            else:
                break

        guest = int(input("\nENTER THE NUMBER OF GUESTS: "))

        def guest_data():
            name = input("\nENTER THE NAME OF GUEST: ")
            age = int(input(f"\nENTER THE AGE OF {name}: "))
            gender = input("\nMALE/FEMALE: ")
            nam.append(name)
            ag.append(age)
            gen.append(gender)
            with open('userdata.csv', 'a', newline='') as csvfile:
                csvwriter = DictWriter(csvfile, fieldnames=['name', 'age', 'gender'])
                csvwriter.writeheader()
                csvwriter.writerow({'name': name, 'age': age, 'gender': gender})
            return print("\n******DATA ENTERED SUCCESSFULLY******")

        for d in range(guest):
            guest_data()

        def read_csv():
            with open('userdata.csv') as csvreader:
                reader = DictReader(csvreader)
                for row in reader:
                    print(row)
            os.remove(r'userdata.csv')
            return print("------------------------------------")

        #read_csv()
        #print("\n----CHECK YOUR DETAILS----")
        ch = input("\nDO YOU WANT TO CONTINUE (Y/N): ")

        while True:
            if ch == 'n' or ch == 'N' or ch == 'no' or ch == 'NO':
                for e in range(guest):
                    guest_data()
                read_csv()
            else:
                break

        print("\nCHOOSE THE ROOM YOU WANT: ")
        print("1.SINGLE BED ROOM")
        print("2.DOUBLE BED ROOM (+20% CHARGES)")

        cl = int(input("\nENTER ROOM CLASS (1/2): "))

        payment = []

        if cl == 1:
            query15 = "SELECT CHARGES*{} FROM HOTELS WHERE hotel_name = '{}' and LOCATION = '{}' ".format(
                guest, ht[0], loc[0])
            my_cursor.execute(query15)
            print(f"\nName = {nam}               Age = {ag}           Gender = {gen}")
            print(f"Hotel name = {ht}         Location = {loc}")
            print("Type = Single Bed")
            for q in my_cursor:
                payment.append(q)
                print(f"\nYOU HAVE TO PAY {q[0]} RUPEES")

        elif cl == 2:
            query16 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM HOTELS WHERE HOTEL_name = '{}' and LOCATION = '{}'".format(
                guest, ht[0], loc[0])
            my_cursor.execute(query16)
            print(f"\nName = {nam}               Age = {ag}           Gender = {gen}")
            print(f"Hotel name = {ht}         Location = {loc}")
            print("Type = Double Bed")
            for r in my_cursor:
                payment.append(r)
                print(f"\nYOU HAVE TO PAY {r[0]} RUPEES")
        pay = input("\nTO PAY PRESS (P): ")

        if pay == 'p' or pay == 'P':
            print("\nHOW YOU WANT TO PAY ?")
            print("1.UPI PAYMENT")
            print("2.CREDIT CARD")
            print("3.DEBIT CARD")

        pay2 = int(input("\nENTER YOUR PAYMENT METHOD (1/2/3): "))

        if pay2 == 1:
            print("\n-------------------UPI PAYMENT---------------------------")
            print(F"PAY {payment[0]} RUPEES")
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P): ")
            ott = int(input("\nENTER A OTP SENT TO YOUR PHONE NO AND EMAIL:-"))
            print("\nTRANSACTION SUCCESSFUL------------")
            print("\n**********THANK YOU***********")

        elif pay2 == 2 or pay2 == 3:
            print("\n-------------------CARD payment---------------------------")
            print(F"PAY {payment[0]} RUPEES")
            c_no = input("\nENTER YOUR CARD NO:-")
            cvv = input("\nENTER YOUR CVV:-")
            ott2 = (input("\nENTER A OTP SEND TO YOUR NUMBER:-"))
            print("\nTRANSACTION SUCCESSFUL------------")
            print("**********THANK YOU***********")
        else:
            print("Invalid Option....")
        print("\n--------THANKS FOR USING HOTEL BOOKING SYSTEM--------------")
        print("YOUR TICKETS ARE SEND TO YOUR EMAIL")

        print("1. Continue")
        print("2. EXIT")
        inp=input("Enter your option: ")
        if inp=='1':
            h=hotel()
            h.hotel_data()

        else:
            sys.exit()


