class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 in (1,2,3)
