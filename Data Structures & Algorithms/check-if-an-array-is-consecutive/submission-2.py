class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        output = True
        if len(set(nums)) != len(nums):
            output = False
        
        if max(nums) - min(nums) + 1 != len(nums):
                output = False
        
        return output

        



