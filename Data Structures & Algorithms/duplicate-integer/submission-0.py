class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        true_length = len(set(nums)) 
        if true_length != len(nums):
            return True
        
        return False
        