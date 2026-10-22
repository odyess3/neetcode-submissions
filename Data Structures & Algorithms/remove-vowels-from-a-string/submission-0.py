class Solution:
    def removeVowels(self, s: str) -> str:
        if "a" in s:
           s = s.replace("a", "")
        
        if "e" in s:
           s = s.replace("e", "")

        if "i" in s:
           s = s.replace("i", "")

        if "o" in s:
           s = s.replace("o", "")

        
        if "u" in s:
           s = s.replace("u", "")

        
        
        return s
