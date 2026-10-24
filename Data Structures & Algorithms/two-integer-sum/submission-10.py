class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic1 = {}

        for i, n in enumerate(nums):
            comp = target - n
            
            if comp in dic1 and i != dic1[comp]:
                return [dic1[comp], i]
                break
            dic1[n] = i
        
        return []