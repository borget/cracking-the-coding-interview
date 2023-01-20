from typing import List


class Solution:
    """

    """

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)


        return []

    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            # return

        for candidate in self.get_candidates(state):
            state.add(candidate)
            self.search(state, solutions)
            state.remove(candidate)

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
