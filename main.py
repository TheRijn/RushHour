from argparse import ArgumentParser
from code.classes.board import Board
from code.classes.state import State

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    board = Board(args.filename)
    board.print_state(board.starting_state)
    int_hash = board.starting_state.hash()
    print("int versie", int_hash)
    new_state = State.from_hash(int_hash, board.number_of_cars)
    fake_state = State.from_hash(int_hash + 1, board.number_of_cars)
    print(board.starting_state.cars)
    print(new_state == board.starting_state)
    print((fake_state == board.starting_state))
