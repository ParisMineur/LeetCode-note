class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = []
        count = 0

        for c in s:
            if c == '(':
                res.append(c)
            elif res and c == ')' and res.pop() == '(':
                continue
            elif not res and c == ')':
                count += 1
                
        return len(res) + count
