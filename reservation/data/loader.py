import json
import sys
from reservation.hotelroom.hotel import Hotel
from reservation.hotelroom.room import Room, StandardRoom, SuperiorRoom, DeluxeRoom
import os


def load_hotel_from_file(filename):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, filename)
    with open(abs_file_path) as json_file:
        data = json.load(json_file)
        rooms = []
        for r in data["rooms"]:
            if r["type"] =='Standard':
                rooms.append(StandardRoom(r["number"],r["price"]))
            elif r["type"] =='Superior':
                rooms.append(SuperiorRoom(r["number"], r["price"]))
            elif r["type"] =='Deluxe':
                rooms.append(DeluxeRoom(r["number"], r["price"]))
        return Hotel(data["hotelName"], rooms)