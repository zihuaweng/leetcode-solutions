#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 一个机器人在一条长的线段原点上可以左移动/右移动/不动，问有多少种情况可以在k步以内回到原点
# 三种情况
# 左移动/右移动/不动


#  0  0  0  0  0  0  0  0  0
#  i
#  | (dis = 0, k-1)
#     | (dis =1, k-1)
#
#     |
#     | (dis=1, k-1)
# | (dis=0, k-1)
#
# base case:
# k == 0:    idx == 0:  count +1
#
# check : idx > k / 2 || idx < 0

class Solution:

    def move(self, n, k):
        self.count = 0
        self.dfs(n, 0, k)
        return self.count

    def dfs(self, n, idx, k):
        if idx > k / 2 or idx < 0 or idx >= n:
            return
        if k == 0 and idx == 0:
            self.count += 1
        for i in [-1, 1, 0]:
            self.dfs(n, idx + i, k - 1)


# dp 方法

# k = 3
# len = 5
#    0  0  0  0  0
# dp = k +2
#
# 推导公式：
# dp_new = dp[i-1] + dp[i] + dp[i+1]
# 意思是上一次   左边 -> 右移
#             右边 -> 左移动
#             当前位置 -> 不动
# 这三种情况都可以得到下一次当前位置的结果
# 每个槽表示落到该地方的次数
# 0  1  0  0  0  0  0 (k=0)
# 0  1  1  0  0  0  0 (k=1) 只走一步回到原点只能说是选择不动，及1种可能
# 0  2  2  1  0  0  0 (k=3) 走两步
# 0  4  5  3  1  0  0 (k=4) 走三步


class Solution2:
    def move(self, n, k):
        dp = [0] * (k + 2)  # 前面多一位，后面多一位，避免了区间问题
        dp[1] = 1
        for i in range(k):
            temp = [0] * (k + 2)
            for j in range(1, min(n + 1, k + 1)):
                temp[i] = dp[i - 1] + dp[i] + dp[i - 1]

            dp = temp
        return dp[1]
