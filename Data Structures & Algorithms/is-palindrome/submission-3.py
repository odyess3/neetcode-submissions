class Solution:
    def isPalindrome(self, s: str) -> bool:

        right = len(s)-1
        left = 0
        ans = True


        while left < right:

            while left < right and not s[left].isalnum() :
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            
            if s[right].lower() != s[left].lower():
                ans = False
            
            left+=1
            right-=1
        
        return ans
            
            
        


        return True



# odd/even  -> abcba
#  left = right 
#       left<right
#       if != abcd -> left+=1, right-=1
        