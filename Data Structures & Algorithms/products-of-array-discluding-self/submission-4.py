class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        left = 1

        for i in range(len(nums)-1):
            value = nums[i]*left
            prefix.append(value)
            left = prefix[i]
        
        right = 1
        postfix = []
        count = 0
        
        for i in range(len(nums)-1, 0,-1):
            value = right*nums[i]
            postfix.append(value)
            right = postfix[count]
            count+=1
        
        prefix.insert(0,1)
        postfix.reverse()
        postfix.append(1)
        
        result = []
        
        for i in range(len(nums)):
            result.append(postfix[i] * prefix[i])
        
        return result