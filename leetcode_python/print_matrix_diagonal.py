#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def printDiagonalOrder(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        m = len(a)
        n = len(a[0])
        res = [0] * (m*n)
        i = m - 1
        j = n - 1
        for k in range(m*n):
            res[k] = a[i][j]
            print(i,j)
            if i == 0:
                i = j - 1
                j = 0
            elif j == n-1:
                j = i - 1
                i = n - 1
            else:
                i -= 1
                j += 1
        print(res)


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = len(a)
        res = []
        for i in range(n - 1, -1, -1):
            row = n - 1
            col = i
            while (row >= 0 and col < n):
                res.append(a[row][col])
                col += 1
                row -= 1

        for i in range(n - 1, -1, -1):
            row = i
            col = 0
            while (row >= 0 and col < n):
                res.append(a[row][col])
                col += 1
                row -= 1
        print(res)