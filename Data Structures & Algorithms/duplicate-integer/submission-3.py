class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dic = {}

        for i, n in enumerate(nums):
            dic[n] = dic.get(n,0) + 1  
            if dic[n] > 1:
                return True
        
        return False

        