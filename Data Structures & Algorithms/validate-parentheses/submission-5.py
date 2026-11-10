class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {   ")" : "(",
                    "}" : "{",
                    "]" : "["   }
        
        stack = []

        if len(s) % 2 != 0:
            return False
        


        for i in s:

            if i not in dict1:
                stack.append(i)

            else:
                if not stack or stack.pop() != dict1[i]:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
 
        
        

            
        