#!/usr/bin/env python3
# coding: utf-8

# hard 题目
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://www.youtube.com/watch?v=ScCg9v921ns

# Time complexity: O(log(min(m, n)))
# Space complexity: O()


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
           l_num1,    r_num1
        x x x     |      x x x x     
        y y  | y y
        l_num2  r_num2
        
        
        xx y y x| [x]yxyxx   odd : 
        
        
        1. find the pivot to split num1 to two parts and num2 to two parts
            10.   5, 5
            11.   5, 6
            
            x x x x | x      5 - 1 = 4
            y| y y y y         1
            0  1
            
            
            x x x | x x      5 - 2 = 3
            y y | y y y         2
            
            l_num2 < r_num1      l_num2 > r_num1:  pivot move left
            l_num1 < r_num2      l_num1 > r_num1:  pivot move right
                
 
            
        2. find the median using l_num1, r_num1, l_num2, r_num2
                10.   5, 5
                x [x] |[x] x x      5 - 1 = 4
                y [y] |[y] y y  
                
                x [x] |[x] x x x      5 - 1 = 4
                y [y] |[y] y y
                
                5, [1], 5 min(x,y)
            
                
        """
        # 首先保证len(nums1) < len(nums2), 因为我们需要定pivot point，从小的入手可以保证另外一个左右两边是平分的，从大的入手有可能剩下的数少于1/2
        x = len(nums1)
        y = len(nums2)
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x

        start = 0
        end = x
        while (start <= end):
            p1 = (end + start) // 2  # nums1 左边元素个数
            p2 = (x + y) // 2 - p1  # nums2 左边元素个数
            max_left_x = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right_x = float('inf') if p1 == x else nums1[p1]
            max_left_y = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right_y = float('inf') if p2 == y else nums2[p2]

            if max_left_x > min_right_y:
                end = p1 - 1
            elif max_left_y > min_right_x:
                start = p1 + 1
            else:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2  # even case
                else:
                    return min(min_right_x, min_right_y)  # odd case



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        k = half 
        The the first k num of two sorted arr
        
        xxxx[i] xxxx
        yyy[j] yyyy
        
        i + j == k
        for x: we get k/2 or k1
        for y: we get k/2 or k2
        if x[k/2] < y[k/2]:
            the median in x[k/2:] and y[0:]
            then we find the first k-k1 in x[k/2:] and y[0:]
        """
        m = len(nums1)
        n = len(nums2)
        
        if (m+n) & 1 == 1:
            return self.find_median(nums1, nums2, (m+n+1)//2)
        else:
            return (self.find_median(nums1, nums2, (m+n)//2) + self.find_median(nums1, nums2, (m+n)//2+1)) / 2
        
    def find_median(self, num1, num2, k):
        m = len(num1)
        n = len(num2)
        
        if m > n:
            return self.find_median(num2, num1, k)
        
        if not num1:
            return num2[k-1]
        
        if k == 1:
            return min(num1[0], num2[0])
        
        k1 = min(k//2, m)
        k2 = k - k1
        
        if num1[k1-1] < num2[k2-1]:
            return self.find_median(num1[k1:], num2, k-k1)
        else:
            return self.find_median(num1, num2[k2:], k-k2)
        