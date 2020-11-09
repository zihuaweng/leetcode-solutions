#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(N)
# Space complexity: O(1)

# The easiest way is to first sort and check the diff
# this method is first find out the interval and check they are valid.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val = min(arr)
        max_val = max(arr)
        if (max_val - min_val) % (len(arr) - 1) != 0:
            return False
        interval = (max_val - min_val) // (len(arr) - 1)
        if interval == 0:        # it means all values are equal, return True
            return True

        # This part is to sort the arr, we get the index and put it to the desire location to sort it.
        i = 0
        while i < len(arr):
            if (arr[i] - min_val) % interval != 0:
                return False
            idx = (arr[i] - min_val) // interval  # idx of current value should be in a sorted array
            if idx < i:  # all values before i are valid and sorted, if idx < i, it means current value is invalid.
                return False
            elif idx == i:
                i += 1
            else:
                if arr[i] == arr[idx]:
                    return False
                arr[i], arr[idx] = arr[idx], arr[i]
        return True