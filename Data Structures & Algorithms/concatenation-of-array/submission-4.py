class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

       list1 = []

       for j in range(2):
            for i in range(len(nums)):
                list1.append(nums[i])


       return list1
        