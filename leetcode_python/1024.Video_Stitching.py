#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# Time O(NlogN), Space O(1)
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        # print(clips)
        if clips[0][0] != 0:
            return -1
        num = 1
        s, e = clips[0]
        for i,j in clips[1:]:
            # print(s,e)
            if i > e or e >= T:
                break
            elif s < i <= e:
                s = e
                num += 1
            e = max(e, j)
        if e < T:
            return -1
        else:
            return num