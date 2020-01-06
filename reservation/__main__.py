import reservation.app as app

if __name__ == "__main__":
    h= app.initialize_hotel("hotel.json")
    app.print_hotel_intro(h)

    while True:
        opt = input("What can I do for you today?\n 1. Book a room\n 2. Check room availability\n 3. Print Room Booking\n 4. Cancel Room Booking\n 5. Quit\n")
        if opt =='1':
            d, s, t = app.ask_customer_which_date()
            print("Let me find you what are the rooms available on {} for {} days, with room type {}".format(d, s, t))
            rooms = h.find_room_available(d, s, t)
            if len(rooms)==0:
                print("Sorry there is no room available")
            else:
                app.print_rooms(rooms)
                number, custname =app.ask_customer_name_and_room_number([item.number for item in rooms])
                h.book_room(number, custname, d, s)
        elif opt=='2':
            t, d, s = app.ask_customer_on_checking_room_availability()
            h.get_room_availability_dates(d, s, t)
        elif opt=='3':
            d, s = app.ask_customer_for_days_start_and_days()
            print("If you want to view for all customer, please type 'ALL'")
            custname= app.ask_customer_name()
            bookings = h.get_room_booking(custname,d, s)
            app.print_bookings(bookings)
        elif opt =='4':
            custname= app.ask_customer_name()
            d, s = app.ask_customer_for_days_start_and_days()
            bookings = h.get_room_booking(custname,d, s)
            app.print_bookings(bookings)
            y = input("Do you want to cancel the bookings above (y/n): ")
            if y =='y':
                h.cancel_room_booking(bookings)
        elif opt =='5':
            break
        else:
            print("You enter incorrect value, please type either '1', or '2' or '3' or '4'")
            continue



