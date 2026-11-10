#from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        operations = deque(operations)
        counting = []

        while operations:
            print(counting)
            if operations[0] == "C":
                operations.popleft()
                counting.pop()
            
            elif operations[0] == "D":
                operations.popleft()
                double = int(counting[len(counting)-1]) *2
                counting.append(double)
            
            elif operations[0] == "+":
                operations.popleft()
                add = (int(counting[len(counting)-1]) + int(counting[len(counting)-2]))
                counting.append(add)
            
            else:
                value=operations[0]
                operations.popleft()
                counting.append(value)
        
        

        sum1 = 0
        for i in counting:
            sum1 += int(i)

        

        return sum1
        

            



        