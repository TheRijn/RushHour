from __future__ import annotations

from collections import deque

from ..classes import State


class BreathFirstSearch:
    def __init__(self, start: State):
        self.nodes: deque[State] = deque([start])
        self.archive: dict[State, State | None] = {start: None}

    def next_node(self) -> State:
        return self.nodes.popleft()

    def add_node(self, node: State, prev: State) -> None:
        self.nodes.append(node)
        self.archive[node] = prev

    def solve(self) -> list[State]:
        while self.nodes:
            state = self.next_node()

            for move in state.possible_moves():
                new_state = state.copy_and_change(move)

                if new_state in self.archive:
                    continue

                if new_state.won():
                    return self.backtrack(state) + [new_state]

                self.add_node(new_state, state)

    def backtrack(self, state: State) -> list[State]:
        states = [state]

        while (prev := self.archive[state]) is not None:
            states.append(prev)
            state = prev

        states.reverse()

        return states
