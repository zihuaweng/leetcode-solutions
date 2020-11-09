#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/text-justification/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        1. for each work, calculate the char length to cur_sum until the next one will excess the maxWidth, get the subarr
            1. for each word, we need to add one more to the cur_sum which is for the space
            ["This", "is", "an", "example", "of", "text", "justification."]

            ["This","is", "an", "example"]
            4 + 1 + 2 + 1 + 2  + 1+7
            10

            subarr: [the first one]   -> cur_sum
            next = 2
            while cur_sum + 1 + len(next) <= maxWidth:
                subarr += next
                next += 1

        2. calculate the space and add them to the subarr, round robin logic 
            1. 0- (16 - sum(subarr)) % max(1, (len(subarr) - 1))
            ["What","must","be"]   10, space=6, 010101
            ["What   ","must   ","be"]   => ''.join()

            ["acknowledgment"]  14 space=2,  (len(subarr) - 1)==0: space % 1  00
            ["acknowledgment  "]    => ''.join()

            if it is the end subarr, then we only need to add one space for each (except the last one), add the remaining space to the end
            ["shall","be"]   7 space = 9, 9 - (len(subarr)-1) = 8
            ["shall ","be        "]  => ''.join()
            
        time O(n)*O(k)
        space O(n)
        
        n = the length of string
        k = length of subarr
        """
        res = []
        temp = []
        word_length = 0
        for w in words:
            if word_length + len(w) + len(temp) <= maxWidth:
                temp.append(w)
                word_length += len(w)
            else:
                # 分配所有的空格，round robin logic
                space = maxWidth - word_length
                # 有可能这一行是只有一个元素，length=0， 那么%报错，length or 1 会自动选择1
                length = max(len(temp) - 1, 1) 
                for i in range(space):
                    temp[i % length] += " "
                res.append(''.join(temp))
                # 新的一个循环
                temp = [w]
                word_length = len(w)
        # 最后一行：
        res.append(' '.join(temp).ljust(maxWidth))

        return res




