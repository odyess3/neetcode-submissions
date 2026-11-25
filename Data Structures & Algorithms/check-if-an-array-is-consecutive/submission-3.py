class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        smallest = min(nums)
        dict1= {}
        print

        for i in range(len(nums)):
            dict1[nums[i]] = nums[i]
            smallest = min(smallest,nums[i])
        

        for i in range(len(nums)):

            if smallest+i not in dict1:
                print(smallest+i)
                return False
        
        return True
            

