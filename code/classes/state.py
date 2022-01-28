from copy import copy

Position = tuple[int, int]


class State:
    def __init__(self, cars: tuple[Position, ...]):
        self._cars = cars

    @classmethod
    def from_hash(cls, hash: int, n_cars: int) -> "State":
        state_list: list[Position] = []
        hex_str = [int(x, base=16) for x in "%x" % hash]

        if (diff := n_cars * 2 - len(hex_str)) != 0:
            hex_str = diff * [0] + hex_str

        for i in range(0, len(hex_str), 2):
            state_list.append(tuple(hex_str[i : i + 2]))

        return State(tuple(state_list))

    @property
    def cars(self) -> tuple[Position, ...]:
        return copy(self._cars)

    def move_car(self) -> "State":
        # check if can be moves
        pass

    def __hash__(self) -> int:
        return hash(self._cars)

    def hash(self) -> int:
        new_hash = ""

        for col, row in self._cars:
            new_hash += "%x%x" % (col, row)

        return int(new_hash, base=16)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, State):
            return NotImplemented

        return hash(self) == hash(other)

    def __repr__(self) -> str:
        return f"State({self._cars})"
