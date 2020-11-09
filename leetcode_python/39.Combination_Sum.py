# https://leetcode.com/problems/combination-sum/
# 同样是递归完成
# 因为出现的词语可以是重复的，所以递归self.helper中，下一步的start 可以就是上一步i
# self.helper(candidates, res, i, target - candidates[i], temp)
# ***注意res.append(temp[:]) 需要深度复制，不能使用res.append(temp)！！！

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(target, candidates, 0, [], res)
        return res

    def helper(self, target, candidates, idx, tmp, res):
        if target == 0:
            res.append(tmp)
            return
        for i in range(idx, len(candidates)):
            c = candidates[i]
            if c <= target:
                self.helper(target - c, candidates, i, tmp + [c], res)

# 第二种就是添加了一个排序，这样如果后面的值比target大的话就可以直接略过去，减少不必要的计算
# Runtime: 56 ms, faster than 99.39% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.1 MB, less than 64.95% of Python3 online submissions for Combination Sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(target, candidates, 0, [], res)
        return res

    def helper(self, target, candidates, idx, tmp, res):
        if target == 0:
            res.append(tmp)
            return
        for i in range(idx, len(candidates)):
            c = candidates[i]
            if c > target:
                return
            self.helper(target - c, candidates, i, tmp + [c], res)

