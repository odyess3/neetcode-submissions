class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        l  = 0
        count = 0
        length = 1000000

        for r in range(len(nums)):
            
            count += nums[r]

            while count >= target:
                length=min(length,r+1-l)
                count -= nums[l]
                l += 1
            
            

        
        if length == 1000000:
            return 0
        else:
            return length