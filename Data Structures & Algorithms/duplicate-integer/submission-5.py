class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        set1 = set()

        for i in range(len(nums)):

            if nums[i] in set1:
                return True
            
            set1.add(nums[i])
    

        return False






#
"""

set()

for i in range (len(nums)):

    if nim[i] in set():
        return true
    set.add(nums[i])


return false 


"""
        