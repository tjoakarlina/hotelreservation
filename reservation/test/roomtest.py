import unittest
from reservation.hotelroom.room import Room, Booking
import datetime

class TestRoom(unittest.TestCase):

    def test_booking(self):
        r = Room("102", "Deluxe", 300)
        result = r.book(Booking("karlina", datetime.date(2017, 2, 2)))
        self.assertEqual(result, True)
        result = r.book(Booking("anastasia", datetime.date(2017, 2, 2)))
        self.assertEqual(result, False)
    
    def test_cancel_booking(self):
        r = Room("101", "Standard", 200)
        result = r.book(Booking("karlina", datetime.date(2017, 2, 2)))
        self.assertEqual(result, True)
        result = r.cancel(Booking("karlina", datetime.date(2017, 2, 2)))
        self.assertEqual(result, True)
        result = r.cancel(Booking("anastasia",datetime.date(2017, 2, 2)))
        self.assertEqual(result, False)


    def test_get_available_dates(self):
        r = Room("101", "Standard", 200)
        result = r.book(Booking("karlina", datetime.date(2017, 2, 2)))
        self.assertEqual(result, True)
        result = r.book(Booking("karlina", datetime.date(2017, 2, 3)))
        self.assertEqual(result, True)
        dates = r.get_available_dates(datetime.date(2017, 2, 2),4)
        self.assertEqual(len(dates), 2)
        dates = r.get_available_dates(datetime.date(2017, 2, 3),4)
        self.assertEqual(len(dates), 3)

    def test_get_booking(self):
        r = Room("101", "Standard", 200)
        result = r.book(Booking("karlina", datetime.date(2017, 2, 2)))
        self.assertEqual(result, True)
        bookings = r.get_booking("karlina", datetime.date(2017, 2, 2), 10)
        self.assertEqual(len(bookings), 1)
        bookings = r.get_booking("anastasia", datetime.date(2017, 2, 2), 10)
        self.assertEqual(len(bookings), 0)

if __name__ == '__main__':
    unittest.main()
