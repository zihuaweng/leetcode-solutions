# https://leetcode.com/problems/rotate-image/
# 这道题直接循环做会很繁琐
# 可以选择对角线互换，互换后再翻转列表。
# 互换的小技巧是左上角互换写起来更容易，这样后面翻转列表需要一个循环。


# 一般做法
# https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


    def rotate2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]

    def rotate3(self, A):
        A[:] = map(list, zip(*A[::-1]))

    def rotate4(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
