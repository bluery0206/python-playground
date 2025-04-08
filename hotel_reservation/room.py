"""
Room
"""

class Room:
    """ Room """

    def __init__(self, number:int, capacity:int, date_reservation:str, day_stay:int, price:float, status:str) -> None:
        self._number        = number
        self._capacity           = capacity
        self._date_reservation   = date_reservation
        self._day_stay           = day_stay
        self._price              = price
        self._status             = status # occupied or available

    @property
    def number(self) -> int:
        """ Room Number """
        return self._number

    @number.setter
    def number(self, number:int) -> None:
        self._number = number

    @property
    def capacity(self) -> int:
        """ Room capacity """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity:int) -> None:
        self._capacity = capacity

    @property
    def date_reservation(self) -> int:
        """ Room date_reservation """
        return self._date_reservation

    @date_reservation.setter
    def date_reservation(self, date_reservation:int) -> None:
        self._date_reservation = date_reservation

    @property
    def day_stay(self) -> int:
        """ Room day_stay """
        return self._day_stay

    @day_stay.setter
    def day_stay(self, day_stay:int) -> None:
        self._day_stay = day_stay

    @property
    def price(self) -> int:
        """ Room price """
        return self._price

    @price.setter
    def price(self, price:int) -> None:
        self._price = price

    @property
    def status(self) -> int:
        """ Room status """
        return self._status

    @status.setter
    def status(self, status:int) -> None:
        self._status = status


if __name__ == "__main__":
    room_1 = Room(1, 10, "10-31-25", 2, 12.20, "occupied")
    room_2 = Room(2, 40, "02-21-25", 2, 12.20, "available")
    room_3 = Room(3, 20, "05-23-25", 2, 12.20, "available")
    room_4 = Room(4, 12, "12-31-25", 2, 12.20, "occupied")
    room_5 = Room(5, 15, "09-27-25", 2, 12.20, "available")

    rooms = []

    rooms.append(room_1)
    rooms.append(room_2)
    rooms.append(room_3)
    rooms.append(room_4)
    rooms.append(room_5)

    for room in rooms:
        print(f"Room {room.number}: Capacity={room.capacity}, Date Reservation={room.date_reservation}, Day Stay={room.day_stay}, Price={room.price}")
