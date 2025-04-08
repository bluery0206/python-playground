import math

class Point():
    def __init__(self, x:int|float, y:int|float) -> None:
        self.x = x
        self.y = y

    def get_distance(self, point:"Point") -> float:
        distance = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

        return distance


if __name__ == "__main__":
    point_a = Point(18, 2)
    point_b = Point(15, 6)

    print(point_a.get_distance(point_b))
