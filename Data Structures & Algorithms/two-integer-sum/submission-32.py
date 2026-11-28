class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = {}

        for i in range(len(nums)):

            comp = target - nums[i]

            if comp in dict1.keys():
                return [dict1[comp],i]
            
            dict1[nums[i]] = i













"""

target = num[i]


dict1 = {}
value    index


loop:

 comp = target - num[i]

 if comp in dict:
    return [comp,num[i]]




"""
        