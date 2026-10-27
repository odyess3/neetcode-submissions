class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = 0
        total = 0
        tory = {}
        g = []


        for r in range(0, len(nums)):
            comp = target - nums[r]

                      

            if comp in tory:
                g = [tory[comp],r]

            tory[nums[r]] = r
                

        return g


        