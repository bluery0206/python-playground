"""
hotel
"""

from room import Room

class Hotel:
    """ Hotel """

    def __init__(self) -> None:
        self.__room_list = []

    def add_room(self, room:Room) -> None:
        """ Adds room """
        self.__room_list.append(room)

    def display_rooms(self) -> None:
        """ Displays rooms """
        print("===================")
        print("Rooms:")
        print("-------------------")
        for room in self.__room_list:
            print(f"Room number: {room.get_room_number()}, Status: {room.get_status()}")
        print("===================\n")

    def get_room(self, room_number:int) -> Room|None:
        """ Returns the room in the specified room number """
        for room in self.__room_list:
            if room.get_room_number() == room_number:
                return room

        print(f"Room number {room_number} not found.")
        return None

    def reserve(self, room_number:int, date:str, days:int) -> bool:
        """ Reserves a specified room. Return a bool if successful or not """
        room = self.get_room(room_number)

        if room:
            if room.get_status() == "available":
                room.set_status("occupied")
                room.set_date_reservation(date)
                room.set_day_stay(days)
                print(f"Room number {room_number} successfully reserved.")
                return True
            else:
                print(f"Room {room_number} not available.")
                return False
        else:
            return False

    def check_out(self, room_number:int) -> bool:
        """ Checks out the specified room number, resetting its attrs to available """
        room = self.get_room(room_number)

        if room:
            room.set_status("available")
            room.set_date_reservation("")
            room.set_day_stay(0)
            print(f"Room number {room_number} check out successfully.")
            return True
        else:
            return False


if __name__ == "__main__":
    r1 = Room(100, 2, "", 0, 900, "available")
    r2 = Room(101, 2, "", 0, 900, "available")
    r3 = Room(102, 2, "", 0, 900, "available")
    r4 = Room(103, 4, "", 0, 1500, "available")
    r5 = Room(104, 4, "", 0, 1500, "available")

    hotel = Hotel()
    hotel.add_room(r1)
    hotel.add_room(r2)
    hotel.add_room(r3)
    hotel.add_room(r4)
    hotel.add_room(r5)
    hotel.display_rooms()

    print()
    hotel.reserve(100, "05/20/2022", 5)
    hotel.reserve(103, "05/20/2022", 5)
    hotel.display_rooms()

    print()
    hotel.reserve(100, "05/20/2022", 5)
    hotel.check_out(103)
    hotel.display_rooms()
