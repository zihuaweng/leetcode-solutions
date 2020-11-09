#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/student-attendance-record-ii/
# https://leetcode.com/problems/student-attendance-record-ii/discuss/101638/simple-java-on-solution
# https://www.cnblogs.com/grandyang/p/6866756.html
# 下面这种方法来自 大神 dettier 的帖子，这里面定义了两个数组P和 PorL，其中 P[i] 表示数组前i个数字中1以P结尾的排列个数，PorL[i] 表示数组前i个数字中已P或者L结尾的排列个数。这个解法的精髓是先不考虑字符A的情况，而是先把定义的这个数组先求出来，由于P字符可以再任意字符后面加上，所以 P[i] = PorL[i-1]；而 PorL[i] 由两部分组成，P[i] + L[i]，其中 P[i] 已经更新了，L[i] 只能当前一个字符是P，或者前一个字符是L且再前一个字符是P的时候加上，即为 P[i-1] + P[i-2]，所以 PorL[i] = P[i] + P[i-1] + P[i-2]。
#
# 那么这里就已经把不包含A的情况求出来了，存在了 PorL[n] 中，下面就是要求包含一个A的情况，那么就得去除一个字符，从而给A留出位置。就相当于在数组的任意一个位置上加上A，数组就被分成左右两个部分了，而这两个部分当然就不能再有A了，实际上所有不包含A的情况都已经在数组 PorL 中计算过了，而分成的子数组的长度又不会大于原数组的长度，所以直接在 PorL 中取值就行了，两个子数组的排列个数相乘，然后再把所有分割的情况累加起来就是最终结果啦，参见代码如下：

class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10 ** 9 + 7
        p_l = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = p_l[0] = 1
        p_l[1] = 2
        p[1] = 1

        for i in range(2, n + 1):
            p[i] = p_l[i - 1]
            p_l[i] = (p[i] + p[i - 1] + p[i - 2]) % M

        res = p_l[n]
        for i in range(n):
            res += p_l[i] * p_l[n - i - 1]
            res %= M

        return res

