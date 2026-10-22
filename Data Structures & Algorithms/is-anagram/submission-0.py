class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_strings = ''.join(sorted(s))
        sorted_stringt = ''.join(sorted(t))

        if sorted_strings == sorted_stringt:
            return True
        
        return False


