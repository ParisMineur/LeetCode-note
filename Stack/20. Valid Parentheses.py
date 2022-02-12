class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c not in m:
                stack.append(c)
            elif len(stack) == 0 or m[c] != stack.pop():
                return False
        return stack == []
