# https://leetcode.com/problems/permutations/
# ****注意：res.append(temp[:]) 不可以使用 res.append(temp)， 因为这样会后面temp更改，res里面的内容也会被更改！！

# O(n) = n!


# 因为走到后面的数字前面还是有可能需要加进去的，所以我们需要用used记录一下这个数字是否已经使用了
# 另一种做法是直接查找temp里面有没有存在，但是这样查找是O（n）不高效
class Solution:
    def permute(self, nums):
        res = []
        used = [0] * len(nums)
        self.helper(nums, used, [], res)
        return res

    def helper(self, nums, used, temp, res):

        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(used)):
            if used[i] == 0:
                used[i] = 1
                self.helper(nums, used, temp + [nums[i]], res)
                used[i] = 0


# 和上面一样，当时这次不需要存储used，直接swap两个数字，然后加入nums即可
# 节省了空间
class Solution:
    def permute(self, nums):
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, index, res):
        if index == len(nums):
            res.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.helper(nums, index+1, res)
            nums[index], nums[i] = nums[i], nums[index]




# 这个跟上一个基本一样，这是写法不一样，而且存储了temp

# dfs(nums = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(nums = [2, 3] , path = [1] , result = [] )
# |      |___dfs(nums = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path[:])
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)