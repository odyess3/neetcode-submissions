class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = 0
        dic1 = {}

        for r in range(len(nums)):
            
            comp = target - nums[r]

            if comp in dic1 and dic1[comp] != r:
                return [dic1[comp],r]
                break
            dic1[nums[r]] = r
        
        return []
        

      