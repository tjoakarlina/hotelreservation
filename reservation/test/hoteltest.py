import unittest
from reservation.hotelroom.hotel import Hotel
from reservation.hotelroom.room import Room, Booking
import datetime

class TestHotel(unittest.TestCase):

    def test_booking(self):
        h = Hotel("BV", [Room("202", "Superior", 200), Room("101", "Standard", 100)])
        result = h.book_room("102", "karlina", datetime.date(2020, 2, 2), 10)
        self.assertEqual(result, False)
        result = h.book_room("202", "karlina", datetime.date(2020, 2, 2), 10)
        self.assertEqual(result, True)
        bookings = h.get_room_booking("karlina",datetime.date(2020, 2, 2),30)
        self.assertEqual(len(bookings[0][1]), 10)
        result = h.book_room("202", "anastasia", datetime.date(2020, 2, 1), 5)
        self.assertEqual(result, False)
        bookings = h.get_room_booking("anastasia",datetime.date(2020, 2, 2),30)
        self.assertEqual(len(bookings), 0)
    
    def test_cancel_booking(self):
        h = Hotel("BV", [Room("202", "Superior", 200), Room("101", "Standard", 100)])
        result = h.book_room("202", "karlina", datetime.date(2020, 2, 2), 10)
        self.assertEqual(result, True)

        h.cancel_room_booking([("202",[Booking("anastasia", datetime.date(2020, 2, 2))])])
        bookings = h.get_room_booking("karlina",datetime.date(2020, 2, 2),30)
        self.assertEqual(len(bookings[0][1]), 10)

        h.cancel_room_booking([("202",[Booking("karlina", datetime.date(2020, 2, 2))])])
        bookings = h.get_room_booking("karlina",datetime.date(2020, 2, 2),30)
        self.assertEqual(len(bookings[0][1]), 9)

        rooms = h.find_room_available(datetime.date(2020, 2, 2),5, 'ALL')
        self.assertEqual(len(rooms), 1)

if __name__ =='__main__':
    unittest.main()