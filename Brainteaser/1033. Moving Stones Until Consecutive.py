class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        temp = [a,b,c]
        temp.sort()
        
        d1, d2 = temp[1] - temp[0], temp[2] - temp[1]
        
        if d1 == 1 and d2 == 1:
            return [0, 0]
        elif d1 == 1 or d2 == 1:
            return [1, max(d1, d2)-1]
        elif d1 == 2 and d2 == 2:
            return [1, 2]
        elif d1 == 2 or d2 == 2:
            return [1, d1+d2-2]
        else:
            return [2, d1+d2-2]
