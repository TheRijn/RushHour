from ..src.classes.board import Board
from ..src.classes.state import State


def test_restore_to_hash():
    board = Board("data/Rushhour6x6_1.csv")
    state = board.starting_state
    state_hash = state.hash()
    new_state = State.from_hash(state_hash, board.number_of_cars)

    assert state == new_state
