from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardrows = defaultdict(list)
        numberslist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for j, row in enumerate(board):
            boardrows[j] = set()
            for i in range(len(row)):
                if row[i] == '.':
                    continue

                if row[i] in boardrows[j]:
                    return False
                elif row[i] not in numberslist:
                    continue
                else:
                    boardrows[j].add(row[i])

        columns = list(map(list, zip(*board)))
        boardcols = defaultdict(list)
        for j, row in enumerate(columns):
            boardcols[j] = set()
            for i in range(len(row)):
                if row[i] == '.':
                    continue

                if row[i] in boardcols[j]:
                    return False
                elif row[i] not in numberslist:
                    continue
                else:
                    boardcols[j].add(row[i])

        boardboxes = defaultdict(set)
        for j in range(9):
            for i in range(9):
                val = board[j][i]
                
                if val == '.':
                    continue
                
                box_idx = (j // 3) * 3 + (i // 3)
                
                if val in boardboxes[box_idx]:
                    return False
                elif val not in numberslist:
                    continue
                else:
                    boardboxes[box_idx].add(val)
        return True 
