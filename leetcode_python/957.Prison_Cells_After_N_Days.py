#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {str(cells): N}

        while N:
            cells = [0] + [
                cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)
            ] + [0]
            N -= 1
            if str(cells) in seen:
                N %= seen[str(cells)] - N
            else:
                seen[str(cells)] = N

        return cells


# this is the same idea but more easy to understand
# cause N might be very big, and the pattern might have cycle, so we if there
# is cycle, we don't need to run the next_day again, just do it the other cycle and return values.
# the cycle might not start from index 0, so we need to use N-1 to deduct the staring values.
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        num = 0
        seen = {str(cells): num}
        for num in range(1, N + 1):
            cells = self.next_day(cells)
            key = str(cells)
            if key not in seen:
                seen[key] = num
            else:
                remain = (N - num) % (num - seen[key])
                while remain:
                    cells = self.next_day(cells)
                    remain -= 1
                return cells

        return cells

    def next_day(self, cells):
        temp =  [1 if cells[j-1] == cells[j+1] else 0 for j in range(1, len(cells)-1)]
        temp = [0] + temp + [0]
        return temp