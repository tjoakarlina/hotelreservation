from reservation.hotelroom.hotel import Hotel
from reservation.data.loader import load_hotel_from_file
from datetime import datetime

def initialize_hotel(filename):
    return load_hotel_from_file(filename)

def print_hotel_intro(hotel):
    print("Welcome to our hotel!")
    print(hotel)

def check_available_date(hotel, date, days, type):
    hotel.get_room_availability_dates(date, days, type)

def book_hotel_room(hotel, number, date, days):
    hotel.book_room(number, date, days)

def print_rooms(list_rooms):
    for r in list_rooms:
        print(r)

def ask_customer_which_date():
    dv= False
    sv = False
    tv = False
    while True:
        if not dv:
            d = input("Please enter the from date, you would like to stay in our hotel in format: ")
            try:
                ds = datetime.strptime(d, "%d %m %Y")
            except:
                print("Please enter the date in the correct format e.g. 18 02 2020")
                continue
            else:
                dv = True
        if not sv:
            try:
                s = int(input("Please enter the number of days you would like to stay: "))
            except ValueError:
                print("The number of stays should be integer")
                continue
            else:
                sv = True
        if not tv:
            t = input("Please enter the room type you would like to check (Standard, Superior, Deluxe, ALL): ")
            if t not in ['Standard', 'Superior', 'Deluxe', 'ALL']:
                continue
            else:
                tv = True
                break
    return ds, s, t

def ask_customer_name_and_room_number(list_rooms):
    while True:
        number = input("Please choose the room number you would like to book from the list: {}".format(list_rooms))
        if number not in list_rooms:
            print("The number you choose is not available.")
            continue
        else:
            custname = ask_customer_name()
            return number, custname

def ask_customer_name():
    custname = input("Please enter your name: ")
    return custname

def ask_customer_on_checking_room_availability():
    tv = False
    dv = False
    sv = False
    while True:
        if not tv:
            t = input("Which room type you would like to check (Standard, Superior, Deluxe): ")
            if t not in ["Standard", "Superior", "Deluxe"]:
                print("Your room type is not available, please try again.")
                continue
            else:
                tv = True
                break
    ds, s = ask_customer_for_days_start_and_days()
    return t, ds, s

def ask_customer_for_days_start_and_days():
    date_valid = False
    while True:
        if not date_valid:
            d = input("Please enter the starting date in dd mm YYYY format: ")
            try:
                ds = datetime.strptime(d, "%d %m %Y")
            except:
                print("The date format is incorrect")
                continue
            else:
                date_valid = True
        try:
            s = int(input("Please enter the number of days from the start date: "))
        except:
            print("The number of days must be integer")
        else:
            return ds, s

def print_bookings(bookings):
    if len(bookings)==0:
        print("There is no room booking under the selected query.")
    for b in bookings:
        print("Room {}: ".format(b[0]))
        for i in b[1]:
            print(i)
