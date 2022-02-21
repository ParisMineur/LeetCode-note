class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], res)

## second solution
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for item in sorted(nums):
            res += [i+[item] for i in res]
        
        return res
'''
