from datetime import datetime
from datetime import timedelta
from reservation.hotelroom.room import Room, Booking

class Hotel():
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = {}
        for a in rooms:
            if isinstance(a, Room):
                self.rooms[a.number] = a

    def __str__(self):
        s = "Hotel {}\nRooms available: \n".format(self.name)
        for r in self.rooms:
            s = s + str(self.rooms[r]) +"\n"
        return s

    def find_room_available(self, date_start, days, type='ALL'):
        available_rooms =[]
        for r in self.rooms:
            if type =='ALL' or self.rooms[r].type ==type:
                if self.rooms[r].is_available(date_start, days):
                    available_rooms.append(self.rooms[r])
        return available_rooms

    def book_room(self, number, custname, date_start, days):
        if number in [room for room in self.rooms]:
            dates = self.generate_dates(date_start, days)
            fail = False
            for da in dates:
                booking = Booking(custname, da)
                if not self.rooms[number].book(booking):
                    fail = True
                    break
            if fail:
                for da in dates:
                    booking = Booking(custname, da)
                    self.rooms[number].cancel(booking)
                return False
            else:
                charges = self.rooms[number].price * len(dates)
                print("Thank you {} for choosing us. The total charges of your {} room booking for {} days is SGD {}".format(custname, self.rooms[number].type, len(dates), charges))
                return True
        else:
            return False

    def cancel_room_booking(self, bookings):
        for b in bookings:
            for bk in b[1]:
                self.rooms[b[0]].cancel(bk)

    def generate_dates(self, date_start, days):
        dates = []
        for i in range(days):
            dt = date_start +timedelta(days=i)
            dates.append(dt)
        return dates

    def get_room_availability_dates(self, date_start, days, type="ALL"):
        for r in self.rooms:
            if type =='ALL' or self.rooms[r].type == type:
                print(self.rooms[r])
                available_dates = (self.rooms[r].get_available_dates(date_start, days))
                for d in available_dates:
                    print(d)

    def get_room_booking(self, custname, date_start, days):
        bookings = []
        for r in self.rooms:
            bs = self.rooms[r].get_booking(custname, date_start, days)
            if len(bs)>0:
                bookings.append((r,bs))
        return bookings