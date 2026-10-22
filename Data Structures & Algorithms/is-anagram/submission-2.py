class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts = {}
        countt = {}

        if len(s) != len(t):
            return False

        for i in range(0,len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)

        for i in counts:
            if counts[i] != countt.get(i,0):
                return False
        return True 