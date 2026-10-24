class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = list(map(float, nums1 + nums2))
        nums3.sort()
        ans = 0.0
        length = len(nums3)
        # print(length)
        # print(nums3)

        if length%2 == 0:
            ans = (nums3[length//2] + nums3[(length//2)-1])
            ans = ans/2
        else:
            ans = nums3[(length//2)]
        
        return ans

        