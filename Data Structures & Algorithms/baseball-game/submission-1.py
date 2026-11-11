class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stacks = []

        for i in range(len(operations)):

            if operations[i] == "C":
                stacks.pop()
            
            elif operations[i] == "D":
                stacks.append(int(stacks[-1]) * 2)
            
            elif operations[i] == "+":
                stacks.append(int(stacks[-1]) + int(stacks[-2]))
            
            else:
                stacks.append(int(operations[i]))
        
        return sum(stacks)
        