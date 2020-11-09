#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sort-an-array/
# quick sort
# merge sort
# heap sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        ## quick sort:
        def quick_sort(head, tail):
            if tail <= head:
                return
            l = head
            r = tail
            p = r
            while l < r:
                while l < r and nums[l] < nums[p]:
                    l += 1
                while l < r and nums[r] >= nums[p]:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[r], nums[p] = nums[p], nums[r]
            quick_sort(head, l - 1)
            quick_sort(r + 1, tail)

        quick_sort(0, len(nums) - 1)

        ## merge sort
        def merge_sort(array):
            if len(array) == 1:
                return
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]

            merge_sort(L)
            merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            if i < len(L):
                array[k:] = L[i:]

            if j < len(R):
                array[k:] = R[j:]

        merge_sort(nums)

        return nums

# heap sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def heapify(i, last):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < last and nums[l] > nums[largest]:
                largest = l
            if r < last and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(largest, last)

        n = len(nums)

        for i in range(n - 1, -1, -1):
            heapify(i, n)

        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)

        return nums


