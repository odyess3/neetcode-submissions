class Solution:
    def isValid(self, s: str) -> bool:

        dict1 = { ")" : "(",
                  "}" : "{",
                  "]" : "[" }


        if len(s) % 2 != 0:
            return False


        stack = []

        for i in range(len(s)):

            if s[i] in dict1.values():
                stack.append(s[i])

            else:
                if not stack or stack.pop() != dict1[s[i]]:
                    return False
            


        
        return len(stack) == 0


        