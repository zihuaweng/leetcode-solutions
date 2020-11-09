#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_d = collections.defaultdict(set)
        col_d = collections.defaultdict(set)
        box_d = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                # get row value
                if num in row_d[r]:
                    return False
                else:
                    row_d[r].add(num)

                # get col value
                if num in col_d[c]:
                    return False
                else:
                    col_d[c].add(num)

                # box
                box_x = r // 3
                box_y = c // 3
                if num in box_d[(box_x, box_y)]:
                    return False
                else:
                    box_d[(box_x, box_y)].add(num)

        return True
