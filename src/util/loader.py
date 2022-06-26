import re
from csv import DictReader
from typing import Sequence

from src.classes import Board, Car, State


def load_board(filename: str) -> State:
    cars: dict[str, Car] = {}
    car_positions: dict[str, int] = {}

    with open(filename, "r") as f:
        reader = DictReader(f)

        for row in reader:
            if row["orientation"] == "H":  # horizontal
                car_lane = int(row["row"]) - 1
                car_pos = int(row["col"]) - 1
            else:  # vertical
                car_lane = int(row["col"]) - 1
                car_pos = int(row["row"]) - 1

            cars[row["car"]] = Car(
                row["car"], row["orientation"], int(row["length"]), car_lane
            )
            car_positions[row["car"]] = car_pos

    board_size, board_number = extract_from_filename(filename)

    board = Board(cars, int(board_size), int(board_number))

    state = State(board, car_positions)

    return state


def extract_from_filename(filename: str) -> Sequence[str]:
    print(filename)
    p = re.compile(r".*Rushhour(\d+)x\d+_(\d+)\.csv")
    matches = p.match(filename)

    if matches:
        return matches.groups()
    else:
        raise Exception
