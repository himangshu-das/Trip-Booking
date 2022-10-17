from csv import DictWriter
from csv import DictReader
import mysql.connector
import sys
from register import *
import os
conn = mysql.connector.connect(host='localhost', username='root',password='Pass@123', database='itc')
my_cursor = conn.cursor()
deplo = []
arrlo = []
fli = []

nam = []
ag = []
gen = []
class flights:
    def flight_data(self):
        print("\n********************WELCOME TO FLIGHT BOOKING SYSTEM***********************")
        self.departure=input("Enter your departure: ")
        self.arrival=input("Enter your destination: ")
        query2 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE DEPARTURE = '{}' AND DESTINATION = '{}'".format(self.departure,
                                                                                                          self.arrival)
        deplo.append(self.departure)
        arrlo.append(self.arrival)
        my_cursor.execute(query2)
        print("\n*******YOUR REQUIRED FLIGHTS ARE*******")
        rec = my_cursor.fetchall()
        for row in rec:
            print(row[0])
        fly = input("\nENTER A FLIGHT NAME YOU WANT: ")
        fli.append(fly)
        print("\n******THE DETAILS OF YOUR FLIGHT******")
        query3 = "SELECT * FROM FLIGHTS WHERE AIRLINES_NAME = '{}' AND DEPARTURE = '{}' AND DESTINATION = '{}' ".format(
            fly, self.departure, self.arrival)
        my_cursor.execute(query3)
        rec1 = my_cursor.fetchall()
        for row in rec1:
            print("ID: ", row[0])
            print("NAME: ", row[1])
            print("DEPARTURE: ", row[2])
            print("ARRIVAL: ", row[3])
            print("FLIGHT NO: ", row[4])
            print("DEPARTURE TIME: ", row[5])
            print("ARRIVAL TIME: ", row[6])
            print("BASE PRICE: ", row[7])

        con = input("\nWOULD YOU LIKE TO CONTINUE (Y/N): ")
        while True:
            if con == 'n' or con == 'N' or con == 'no' or con == 'NO':
                f=flights
                f.flight_data()
            else:
                break

        passenger = int(input("\nENTER THE NUMBER OF PASSENGERS: "))



        def pass_data():
            name = input("\nENTER THE NAME OF PASSENGER: ")
            age = int(input(f"\nENTER THE AGE OF {name}: "))
            gender = input("\nMALE/FEMALE: ")
            nam.append(name)
            ag.append(age)
            gen.append(gender)
            with open('userdata.csv', 'a', newline='') as csvfile:
                csvwriter = DictWriter(csvfile, fieldnames=['name', 'age', 'gender'])
                csvwriter.writeheader()
                csvwriter.writerow({'name': name, 'age': age, 'gender': gender})
            return print("\n-------DATA ENTERED SUCCESSFULLY-------")

        for d in range(passenger):
            pass_data()

        def read_csv():
            with open('userdata.csv') as csvreader:
                reader = DictReader(csvreader)
                for row in reader:
                    print(row)
            os.remove(r'userdata.csv')
            #return print("------------------------------------")

        #read_csv()
        #print("\n----CHECK YOUR DETAILS----")
        ch = input("\nDO YOU WANT TO CONTINUE (Y/N): ")

        while True:
            if ch == 'n' or ch == 'N' or ch == 'no' or ch == 'NO':
                for e in range(passenger):
                    pass_data()
                read_csv()
            else:
                break

        print("\nCHOOSE THE CLASS YOU WANT: ")
        print("1.ECONOMY CLASS")
        print("2.BUSINESS CLASS (+20% CHARGES)")
        print("3.FIRST CLASS (+40% CHARGES)")

        flo = []
        tdep = []
        tarr = []

        def fl_nm():
            query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query4)
            for f in my_cursor:
                flo.append(f)

            query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query5)
            for g in my_cursor:
                tdep.append(g)

            query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query6)
            for h in my_cursor:
                tarr.append(h)

        cl = int(input("\nENTER CLASS NO (1/2/3): "))

        payment = []

        if cl == 1:
            fl_nm()
            query15 = "SELECT CHARGES*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query15)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destination = {arrlo}")
            print(f"flight number = {flo}      departure time = {tdep}        arrival time = {tarr}     ")
            print("class = economy class")
            for q in my_cursor:
                payment.append(q)
                print(f"\nYOU HAVE TO PAY {q[0]} RUPEES")

        elif cl == 2:
            fl_nm()
            query16 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query16)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destination = {arrlo}")
            print(f"flight number = {flo}      departure time = {tdep}        arrival time = {tarr}     ")
            print("class = business class")
            for r in my_cursor:
                payment.append(r)
                print(f"\nYOU HAVE TO PAY {r[0]} RUPEES")

        elif cl == 3:
            fl_nm()
            query17 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format(
                passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query17)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destination = {arrlo}")
            print(f"flight number = {flo}      diparture time = {tdep}        arrival time = {tarr}     ")
            print("class = first class")
            for s in my_cursor:
                payment.append(s)
                print(f"\nYOU HAVE TO PAY {s[0]} RUPEES")

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
            pay3 = input("\nTO CONTINUE PAYMENT PRESS (P):-")
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
        print("\n--------THANKS FOR USING FLIGHT BOOKING SYSTEM--------------")
        print("YOUR TICKETS ARE SEND TO YOUR EMAIL")

        print("1. Continue")
        print("2. EXIT")
        inp = input("Enter your option: ")
        if inp == '1':
            f = flights()
            f.flight_data()

        else:
            sys.exit()



        # opening the CSV file
        #with open('flightdetails.csv', mode='r')as file:
            # reading the CSV file
         #   csvFile = csv.DictReader(file)

            # displaying the contents of the CSV file
           # for lines in csvFile:
              #  print(lines['Name'])



