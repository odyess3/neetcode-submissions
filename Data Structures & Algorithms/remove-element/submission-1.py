class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        list1 = []
        j=0
        
        for i in range(len(nums)):

            if nums[i] == val:
                count +=1

            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        

        ans = len(nums) - count
        
        return ans 
        