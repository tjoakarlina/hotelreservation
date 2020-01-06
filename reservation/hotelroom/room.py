import bisect
from datetime import datetime
from datetime import timedelta

class Room():
    '''
    Room is the super class of various room types
    '''
    
    def __init__(self, number, type, price):
        self.number = number
        self.type = type
        self.price = price
        self.booking_list = []

    def book(self, booking):
        if booking.date not in [booking.date for booking in self.booking_list] :
            bisect.insort(self.booking_list,booking)
            return True
        return False
    
    def cancel(self, booking):
        if booking in self.booking_list:
            del self.booking_list[bisect.bisect_left(self.booking_list, booking)]
            return True
        else:
            return False

    def get_available_dates(self, date, days):
        available_dates =[]
        for i in range(0,days):
            d = date + timedelta(days =i)
            if d not in [booking.date for booking in self.booking_list]:
                available_dates.append(d.strftime("%d %b %Y"))
        return available_dates
    
    def is_available(self, date, days):
        for i in range(0,days):
            d = date + timedelta(days =i)
            if d in [booking.date for booking in self.booking_list]:
                return False
        return True
    
    def __str__(self):
        return ""+ self.type + " room, unit number: "+ self.number + " , daily cost: SGD " + str(self.price)

    def get_booking(self, custname, date_start, days):
        bookings = []
        for d in range (days):
            date = date_start + timedelta(days=d)
            if custname == "ALL":
                booking_list = self.booking_list
            else:
                booking_list = [booking for booking in self.booking_list if booking.custname == custname]
            if date in [booking.date for booking in booking_list]:
                booking = next(booking for booking in booking_list if booking.date ==date)
                bookings.append(booking)
        return bookings

class StandardRoom(Room):
    def __init__(self,number, price = 200):
        Room.__init__(self, number, 'Standard', price)

    def __str__(self):
        return Room.__str__(self)
    

class SuperiorRoom(Room):
    def __init__(self, number, price = 300):
        Room.__init__(self, number, 'Superior', price)

    def __str__(self):
        return Room.__str__(self)


class DeluxeRoom(Room):
    def __init__(self, number, price = 400):
        Room.__init__(self, number, 'Deluxe', price)

    def __str__(self):
        return Room.__str__(self)

class Booking():
    def __init__(self, custname, date):
        self.custname = custname
        self.date = date

    def __lt__(self, other):
        return self.date < other .date
    
    def __str__(self):
        return "Date {}, booked by customer: {}".format(self.date, self.custname)

    def __eq__(self, other):
        return (self.custname == other.custname and self.date == other.date)