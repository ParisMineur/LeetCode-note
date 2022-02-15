class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left)//2
            if mid <= x/mid and (mid+1) > x/(mid+1):
                return mid
            elif mid > x/mid:
                right = mid
            else:
                left = mid
