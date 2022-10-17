from hotels import hotel
from flight import flights

import sys
class Home:
    def hpage(self):
        while True:
            print("********WELCOME TO HOME PAGE********")
            print("1.Flight Bookings")
            print("2.Hotel Bookings")
            print("3.EXIT")
            choice = int(input("Press Any Option:"))
            if (choice == 1):
                f=flights()
                f.flight_data()
                break
            elif choice == 2:
                h=hotel()
                h.hotel_data()
                break
            elif choice == 3:
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                sys.exit()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(choice) + "). Try again!")
