from .car import Car


class Board:
    def __init__(self, cars: dict[str, Car], board_size: int, board_number: int):
        self.cars = cars
        self.length = board_size
        self.board_number = board_number

    def __eq__(self, other: object) -> bool:
        return False

    def __len__(self):
        return self.length
