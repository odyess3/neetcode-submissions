class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        mini = str(min(nums))

        sum =0
        for i in mini:
            sum+=int(i)
        
        if sum % 2 == 0:
            return 1
        
        else:
            return 0





