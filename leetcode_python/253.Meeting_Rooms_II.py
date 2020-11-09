#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/meeting-rooms-ii/

# Time complexity: O(nlogn) (因为排序了)
# Space complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = s = 0 # 记录当前开始和终止指针位置
        numRooms = available = 0
        while s < len(starts):
            # 如果每个间断开始都比第一个结束的要早，这些都需要用新的房间
            # 如果available（之前腾空的房间），就从里面扣除
            if starts[s] < ends[e]:
                s += 1
                if available:
                    available -= 1
                else:
                    numRooms += 1
            else:
                # 证明有一个房间用完了，加进去available
                # 更新终止时间
                # 注意：但是这个start其实还没有开始房间去房间，所以start还是当前指针！！！！
                available += 1
                e += 1

        return numRooms


class Solution:
    def minMeetingRooms(self, intervals):
        e = ret = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)

        for s in range(len(start)):
            if start[s] < end[e]:
                ret += 1
            else:
                e += 1
        return ret

#  模版
# https://leetcode.com/problems/car-pooling/
# https://leetcode.com/problems/meeting-rooms-ii/discuss/322622/Simple-Python-solutions

class Solution:
    def minMeetingRooms(self, intervals):
        """
        0.            30
          5 10
                15 20
        """
        lst = []
        for start, end in intervals:
            lst.append((start, 1))
            lst.append((end, -1))
        lst.sort()
        res = 0
        cur = 0
        for time, num in lst:
            cur += num
            res = max(res, cur)
        return res

