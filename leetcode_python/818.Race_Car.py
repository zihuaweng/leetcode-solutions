#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# bfs
# 记录下来走过的（速度，距离），不需要重复计算
# 需要有停止的边界
# abs(dist - target) < target  // abs(new_dist - target) < target

class Solution:
    def racecar(self, target: int) -> int:
        self.min_len = float('inf')
        visited = set()
        visited.add((1, 0))

        queue = [(1, 0)]
        length = 0
        while queue:
            new = []
            length += 1
            for q in queue:
                # print(q)
                speed, dist = q

                # for R
                new_speed = -1 if speed > 0 else 1
                if (new_speed, dist) not in visited and abs(dist - target) < target:  # 需要有停止的边界
                    visited.add((new_speed, dist))
                    new.append((new_speed, dist))

                # for A
                new_speed = speed * 2
                new_dist = dist + speed
                if new_dist == target:
                    return length
                if (new_speed, new_dist) not in visited and abs(new_dist - target) < target:  # 需要有停止的边界
                    visited.add((new_speed, new_dist))
                    new.append((new_speed, new_dist))

            queue = new
        return length


