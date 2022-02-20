class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        
        index = 1
        num = nums[0]
        
        for i in range(1, l):
            if nums[i] == num:
                continue
                
            num = nums[i]
            nums[index] = nums[i]
            index += 1

        return index
