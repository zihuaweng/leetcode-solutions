#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        345,665,454,345,452
        
        1. read 3 num once + ['', 'Thousand', 'Million', 'Billion']
            split them into trunk with len == 3
            
        2. 999-100:
            345.  3 +  'Hundred' + 45
            
        3. 99-20: read trucks, len == 2
            44.  Forty + 4
            35.  Thirdty + 5
        
        4. 0-19:
            2 two
            11 Eleven
        
        """
        if num == 0:
            return 'Zero'
        
        thousands = ["", "Thousand", "Million", "Billion"]
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                      "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        res = ''
        i = 0
        while num > 0:
            if num % 1000:   # only Million or only Billion
                res = self.helper(num % 1000) + thousands[i] + ' ' + res
            num //= 1000
            i += 1
            
        return res.strip()
    
    def helper(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.lessThan20[num] + ' '
        if num < 100:
            return self.tens[num//10] + ' ' + self.helper(num%10)
        if num < 1000:
            return self.lessThan20[num//100] + ' Hundred ' + self.helper(num%100)
        