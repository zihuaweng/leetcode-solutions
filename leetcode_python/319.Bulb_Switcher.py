#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://blog.csdn.net/baidu_23318869/article/details/50386323

# 那么最后我们发现五次遍历后，只有1号和4号灯泡是亮的，而且很巧的是它们都是平方数，是巧合吗，还是其中有什么玄机。我们仔细想想，对于第n个灯泡，
# 只有当次数是n的因子的之后，才能改变灯泡的状态，即n能被当前次数整除，比如当n为36时，它的因数有(1,36), (2,18), (3,12), (4,9), (6,6),
# 可以看到前四个括号里成对出现的因数各不相同，括号中前面的数改变了灯泡状态，后面的数又变回去了，等于灯泡的状态没有发生变化，只有最后那个(6,6)，
# 在次数6的时候改变了一次状态，没有对应其它的状态能将其变回去了，所以灯泡就一直是点亮状态的。所以所有平方数都有这么一个相等的因数对，即所有平
# 方数的灯泡都将会是点亮的状态。 那么问题就简化为了求1到n之间完全平方数的个数，我们可以用force brute来比较从1开始的完全平方数和n的大小，


class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while (i + 1) * (i + 1) <= n:
            i += 1
        return i


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
