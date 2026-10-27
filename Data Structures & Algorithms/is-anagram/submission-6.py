class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tory = {}
        tory2 = {}
        hi = False

        if len(s) == len(t):
            for i in range(len(s)):
                tory[s[i]] = 1 + tory.get(s[i], 0)
                tory2[t[i]] = 1 + tory2.get(t[i], 0)
        
            if tory == tory2:
                hi = True
        
        return hi

        