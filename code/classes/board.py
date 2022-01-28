import re
from csv import DictReader
from typing import Sequence

from .car import Car
from .state import State


class Board:
    def __init__(self, filepath: str):
        self.filename: str = filepath.split("/")[-1]
        self.cars: list[Car] = [Car("X", "H", 2)]
        self.number_of_cars = 0
        self.starting_state: State = self.read_file(filepath)

        board_size, board_number = self.extract_from_filename()
        self.board_size = int(board_size)
        self.board_number = int(board_number)

    def read_file(self, filepath: str) -> State:
        state_list = [(0, 0)]

        with open(filepath, "r") as f:
            reader = DictReader(f)

            for row in reader:
                if row["car"] == "X":
                    state_list[0] = (int(row["col"]) - 1, int(row["row"]) - 1)

                else:
                    state_list.append((int(row["col"]) - 1, int(row["row"]) - 1))
                    self.cars.append(
                        Car(row["car"], row["orientation"], int(row["length"]))
                    )

        self.number_of_cars = len(state_list)
        return State(tuple(state_list))

    def extract_from_filename(self) -> Sequence[str]:
        p = re.compile(r"Rushhour(\d+)x\d+_(\d+)\.csv")
        matches = p.match(self.filename)

        if matches:
            return matches.groups()
        else:
            raise Exception

    def print_state(self, state: State) -> None:
        board = [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
        print(self.cars)

        for i, pos in enumerate(state.cars):
            car = self.cars[i]

            if car.orientation == Car.Orientation.HORIZONTAL:
                for j in range(car.length):
                    board[pos[1]][pos[0] + j] = car.name
            else:
                for j in range(car.length):
                    board[pos[1] + j][pos[0]] = car.name

        print("╭" + "──" * self.board_size + "╮")

        for line in board:
            # TODO: Fix for double character boards
            print("│" + " ".join(line), end="")
            if "X" not in line:
                print(" │")
            else:
                print()

        print("╰" + "──" * self.board_size + "╯")

    def __eq__(self, other: object) -> bool:
        return False
