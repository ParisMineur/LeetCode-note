class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            curmin, curmax = curmin*num, curmax*num
            curmin, curmax = min(num, curmin, curmax), max(curmin, curmax, num)
            
            if curmax > res:
                res = curmax
        return res
