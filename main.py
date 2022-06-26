from argparse import ArgumentParser
from pickle import Pickler

from src.util.loader import load_board

from src.algorithmes import BreathFirstSearch

from datetime import datetime

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    state = load_board(args.filename)

    alg = BreathFirstSearch(state)

    route = alg.solve()
    print(len(route))

    with open(
        f"jar/{state.board.length}x{state.board.length}_{state.board.board_number}_{int(datetime.now().timestamp())}.pickle",
        "wb",
    ) as f:
        p = Pickler(f).dump(route)

    # for state in route:
    #     print(state)
    #     sleep(0.1)
