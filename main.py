from home import Home
from register import*


import sys
class mains:
    def log(self):
        while True:
            print("********Please Select Your Option********")
            print("1.REGISTER")
            print("2.LOGIN")
            print("3.EXIT")
            choice = int(input("Press Any Option:"))
            if (choice == 1):
                r = registration()
                r.my_func()
                r.checknum()
                r.checkpassword()
                print("Successfully Registered!\n")
                print("*******Please Login to continue*******")
                l = log()
                l.set_email()
                l.set_password()
                h = Home()
                h.hpage()
                break
            elif choice == 2:
                l = log()
                l.set_email()
                l.set_password()
                h=Home()
                h.hpage()
                break
            elif choice == 3:
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                sys.exit()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(choice) + "). Try again!")
ma=mains()
ma.log()