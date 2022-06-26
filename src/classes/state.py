from __future__ import annotations

from xtermcolor import colorize

from src.classes import Board, Car


class State:
    def __init__(self, board: Board, positions: dict[str, int]):
        self.board = board
        self.positions = positions

    @property
    def cars(self) -> dict[str, Car]:
        return self.board.cars

    def possible_moves(self) -> list[tuple[str, int]]:
        moves = []
        board_grid = self.board_as_array()
        board_t = list(zip(*board_grid))

        for car_name, car in self.cars.items():
            position = self.positions[car_name]

            if car.orientation == Car.Orientation.HORIZONTAL:
                lane = board_grid[car.lane]
            else:
                lane = board_t[car.lane]

            # check left or above
            for pos in range(position - 1, -1, -1):
                if lane[pos] is None:
                    moves.append((car_name, pos))
                else:
                    break

            # check right or below
            for pos in range(position + car.length, self.board.length):
                if lane[pos] is None:
                    moves.append((car_name, pos - car.length + 1))
                else:
                    break

        return moves

    def won(self) -> bool:
        return self.positions["X"] == self.board.length - 2

    def board_as_array(self):
        board: list[list[str | None]] = [
            [None] * self.board.length for _ in range(self.board.length)
        ]

        for car_name, car in self.board.cars.items():

            if car.orientation == Car.Orientation.HORIZONTAL:
                for j in range(car.length):
                    board[car.lane][self.positions[car_name] + j] = car.name
            else:
                for j in range(car.length):
                    board[self.positions[car_name] + j][car.lane] = car.name

        return board

    def __str__(self) -> str:
        board_str = ""

        board = self.board_as_array()

        board_str += "╭" + "──" * self.board.length + "─╮" + "\n"

        for line in board:
            # TODO: Fix for double character boards

            better_line = ["│"]
            for pos in line:
                match pos:
                    case "X":
                        color = 196
                    case "A":
                        color = 114
                    case "B":
                        color = 208
                    case "C":
                        color = 39
                    case "D":
                        color = 211
                    case "E":
                        color = 61
                    case "F":
                        color = 29
                    case "G":
                        color = 253
                    case "H":
                        color = 223
                    case "I":
                        color = 227
                    case "J":
                        color = 95
                    case "K":
                        color = 100
                    case "O":
                        color = 220
                    case "P":
                        color = 139
                    case "Q":
                        color = 32
                    case "R":
                        color = 36
                    case _:
                        color = 15


                if pos is not None:
                    better_line.append(colorize(pos, ansi=color))
                elif pos is not None:
                    better_line.append(pos)
                else:
                    better_line.append(" ")
            board_str += " ".join(better_line)

            if "X" not in line:
                board_str += " │"

            board_str += "\n"

        board_str += "╰" + "──" * self.board.length + "─╯"

        return board_str

    def copy_and_change(self, change: tuple[str, int]):
        positions = self.positions.copy()
        positions[change[0]] = change[1]

        return self.__class__(self.board, positions)

    def __eq__(self, other: "State"):
        return self.positions == other.positions

    def __hash__(self):
        return hash(tuple(self.positions.values()))
