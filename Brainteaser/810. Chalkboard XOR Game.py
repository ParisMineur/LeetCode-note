class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        res = 0
        for i in nums:
            res ^= i
        return res == 0 or len(nums)%2 == 0 
