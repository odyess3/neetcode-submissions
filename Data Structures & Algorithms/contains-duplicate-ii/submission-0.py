class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dict1 = {}

        for i in range(len(nums)):

            dict1[i] = nums[i]
        

        dict2 = {}

        for i, n in dict1.items():

            if n in dict2:
                comp = i - dict2[n]
                if comp <= k:
                    return True

            dict2[n] = i



        return False
