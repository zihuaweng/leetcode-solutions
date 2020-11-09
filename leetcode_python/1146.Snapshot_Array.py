#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(logs)
# Space complexity: O(s)

# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot_id = 0
        self.data = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index].append([self.snapshot_id, val])

    def snap(self) -> int:
        self.snapshot_id += 1
        return self.snapshot_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.data[index], [snap_id+1]) - 1
        return self.data[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)