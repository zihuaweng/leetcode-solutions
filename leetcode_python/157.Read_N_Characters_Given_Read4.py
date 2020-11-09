#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(1)

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # 存储read4的结果
        temp = [None] * 4
        # buf的指针
        idx = 0
        # 一直走到idx满足n
        while idx < n:
            temp_len = read4(temp)
            # temp的指针
            pointer = 0
            while idx < n and pointer < temp_len:
                buf[idx] = temp[pointer]
                idx += 1
                pointer += 1
            if temp_len < 4:
                break
        return idx

