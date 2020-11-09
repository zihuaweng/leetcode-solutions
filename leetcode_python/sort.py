#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


#!/usr/bin/env python3
# coding: utf-8

from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def func_wrapper(cls, *args):
        start = time.monotonic_ns()
        arr = func(cls, *args)
        print(time.monotonic_ns() - start)
        return arr

    return func_wrapper


class SelectionSort:
    # @time_it
    def sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            # Replace the arr.
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


class InsertionSort:
    # @time_it
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Switch the element to the right when the last element is smaller.
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr


class QuickSort:
    def sortArray(self, nums):

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
            print(r, l, p, nums[r], nums[head:tail+1])
            nums[r], nums[p] = nums[p], nums[r]
            quick_sort(head, l - 1)
            quick_sort(r + 1, tail)

        quick_sort(0, len(nums) - 1)
        return nums


class MergeSort:
    ## merge sort
    def sort(self, nums):
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
# Build Max Heap O(n)
# heap sort is O(nlogn)
class Solution:
    def sortArray(self, nums):

        def heapify(i, last):  # O(logn)
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

        for i in range(n - 1, -1, -1):  #Build Max Heap O(n)
            heapify(i, n)

        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)

        return nums



q = QuickSort()
print(q.sortArray([1,8,2,7,9,8,2,4]))