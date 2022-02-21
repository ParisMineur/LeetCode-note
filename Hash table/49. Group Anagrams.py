class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            d[tuple(count)].append(s)
        
        return d.values()
