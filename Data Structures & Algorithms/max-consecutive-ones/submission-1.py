class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt =0
        high = 0

        for i in nums:
            if i == 1:
                cnt +=1
                high = max(high, cnt)
            else:
                cnt = 0
            
        return high
            
        