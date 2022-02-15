class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.res = []
        self.dfs(n, 0, 0, "")
        return self.res
    
    def dfs(self, n, left, right, s):
        if left == n and right == n:
            self.res.append(s)
            return
        if left < n:
            self.dfs(n, left+1, right, s+"(")
        if left > right and right < n:
            self.dfs(n, left, right+1, s+")")
