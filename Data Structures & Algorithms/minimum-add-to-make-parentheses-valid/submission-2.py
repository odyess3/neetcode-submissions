class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        dict1 = {
                ")" : "("
                }
        
        insertion = 0
        count =0


        s = list(s)

        while s:

            if s[-1] == "(":
                insertion +=1
                s.pop()
            
            elif s[-1] == ")":
                while s and s[-1] == ")":
                    insertion +=1
                    count +=1
                    s.pop()
                
                while s and s[-1] == "(" and count > 0:
                    count -=1
                    insertion -=1
                    s.pop()
            
            elif len(s) > 0 and s[-1] == ")" :
                insertion +=1
                s.pop() 
        

        return insertion



