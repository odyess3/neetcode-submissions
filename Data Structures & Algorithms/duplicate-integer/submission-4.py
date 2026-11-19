class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict1 = {}

        for i in range(len(nums)):
            dict1[nums[i]] = 1 + dict1.get(nums[i],0)

            if dict1[nums[i]] == 2:
                return True


        return False 
        