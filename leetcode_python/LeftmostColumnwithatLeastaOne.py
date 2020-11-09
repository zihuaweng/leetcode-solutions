#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = BinaryMatrix.dimensions(binaryMatrix)
        col = cols - 1
        row = 0
        res = -1
        while row < rows and col >= 0:
            if BinaryMatrix.get(binaryMatrix, row, col) == 1:
                res = col
                col -= 1
            else:
                row += 1
        return res if res != -1 else -1
