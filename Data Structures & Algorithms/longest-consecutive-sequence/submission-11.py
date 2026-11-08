class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        left = 0
        highest = 1
        count = 1

        nums.sort()

        if len(nums) == 0:
            return 0
        

        for i in range(len(nums)-1):

            numright = nums[i+1]

            if nums[i] == numright:
                continue

            elif nums[i]+1 == numright:
                count +=1

                highest=max(count,highest)
            else:
                count = 1
            


        return highest
            
            

        