'''
    Hotel Reservation System
    by: Karlina
'''
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
        self.booked_date = []

    def book(self, *args):
        for arg in args:
            if arg in self.booked_date:
                return False
        for arg in args:
            bisect.insort(self.booked_date,arg)
        return True

    def get_available_dates(self, date, days):
        available_dates =[]
        for i in range(0,days):
            d = date + timedelta(days =i)
            if d not in self.booked_date:
                available_dates.append(d.strftime("%d %b %Y"))
        return available_dates
    
    def is_available(self, date, days):
        for i in range(0,days):
            d = date + timedelta(days =i)
            if d in self.booked_date:
                return False
        return True
    
    def __str__(self):
        return "{} room, unit number: {}, daily cost: SGD {}".format(self.type, self.number, self.price)

class StandardRoom(Room):
    def __init__(self,number, price = 200):
        Room.__init__(self, number, 'Standard', price)
    

class SuperiorRoom(Room):
    def __init__(self, number, price = 300):
        Room.__init__(self, number, 'Superior', price)


class DeluxeRoom(Room):
    def __init__(self, number, price = 400):
        Room.__init__(self, number, 'Deluxe', price)


class Hotel():
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = {}
        for a in rooms:
            if isinstance(a, Room):
                self.rooms[a.number] = a
        self.booking = {}

    def find_room_available(self, date_start, days, type='ALL'):
        available_rooms =[]
        for r in self.rooms:
            if type =='ALL' or self.rooms[r].type ==type:
                if self.rooms[r].is_available(date_start, days):
                    available_rooms.append(self.rooms[r])
        return available_rooms

    def book_room(self, number, date_start, days):
        dates = []
        for i in range(days):
            dt = date_start + timedelta(days=i)
            dates.append(dt)
        for da in dates:
            self.rooms[number].book(da)
            ds = datetime.strftime(da,"%d %m %Y")
            if ds not in self.booking:
                self.booking[ds]= [self.rooms[number]]
            else:
                self.booking[ds].append(self.rooms[number])
        charges = self.rooms[number].price * len(dates)
        print("The total charges of your {} room booking for {} days is SGD {}".format(self.rooms[number].type, len(dates), charges))

    def get_room_availability_dates(self, date_start, days, type="ALL"):
        for r in self.rooms:
            if type =='ALL' or r.type == type:
                print(self.rooms[r])
                print(self.rooms[r].get_available_dates(date_start, days))


h = Hotel("karlina", [SuperiorRoom('101'), DeluxeRoom('201')])

rooms = h.find_room_available(datetime(2020,1,1), 2, 'Superior')

for i in rooms:
    print(i.number)

h.book_room('101', datetime(2020,1,1), 2)

rooms = h.find_room_available(datetime(2020,1,1), 2, 'Superior')

for i in rooms:
    print(i.number)

h.get_room_availability_dates(datetime(2020, 1, 1), 10)



    


