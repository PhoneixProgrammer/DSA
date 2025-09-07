from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and list of empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r,c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + c//3].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True  # solved

            r, c = empties[idx]
            b = (r//3)*3 + c//3
            for num in map(str, range(1,10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(idx + 1):
                        return True

                    # Undo / backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)
            return False

        backtrack()
