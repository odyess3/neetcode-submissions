class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur =0
        max1 = -1000

        for i in range(len(nums)):

            cur = cur + nums[i]
            max1 = max(max1, cur)

            if cur < 0:
                cur = 0
        

        return max1

        