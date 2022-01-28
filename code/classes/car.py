from enum import Enum


class Car:
    def __init__(self, name: str, orientation: str, length: int):
        self.name = name
        self.orientation: Car.Orientation = self.Orientation.direction_off(orientation)
        self.length: int = length

    class Orientation(Enum):
        HORIZONTAL = 0
        VERTICAL = 1

        class InvalidOrientationError(Exception):
            pass

        @classmethod
        def direction_off(cls, orientation: str) -> "Car.Orientation":
            if orientation == "H":
                return cls.HORIZONTAL
            if orientation == "V":
                return cls.VERTICAL
            raise cls.InvalidOrientationError

    def __repr__(self) -> str:
        return f"Car({self.name})"
