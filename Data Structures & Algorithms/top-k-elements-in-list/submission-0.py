class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dor = {}
        
        buckets = [[] for _ in range(len(nums)+1)]

        for i in range(len(nums)):
            dor[nums[i]] = 1 + dor.get(nums[i], 0)

        
        for i , n in dor.items():
            buckets[n].append(i)


        result  = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

            if len(result) == k:
                return result 
        