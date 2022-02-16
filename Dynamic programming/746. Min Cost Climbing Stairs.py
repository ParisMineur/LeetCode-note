class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        
        if l == 2:
            return min(cost)
        
        res = [0] * (l)
        
        for i in range(2, l):
            res[i] = min(cost[i-1] + res[i-1], res[i-2] + cost[i-2])
        
        return min(res[l-1] + cost[l-1], res[l-2] + cost[l-2])
