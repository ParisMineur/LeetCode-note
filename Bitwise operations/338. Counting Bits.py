class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1, n+1):
            count = 0
            while i:
                i = i&(i-1)
                count += 1
            res.append(count)
        
        return res
    
## second solution
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        
        for i in range(1, n+1):
            res[i] = res[i&(i-1)] + 1
            
        return res

'''
