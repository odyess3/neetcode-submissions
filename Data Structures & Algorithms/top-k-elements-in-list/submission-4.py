class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict1 = {}

        for i in range(len(nums)):
            dict1[nums[i]] = 1 + dict1.get(nums[i], 0)
        
        
        dict2 = {}

        for i, n in dict1.items():
            
            if n not in dict2:
                dict2[n] = []
                
            dict2[n].append(i)
        
        print(dict2)

        res = []

        while len(res) < k:
            value = max(dict2)

            for num in dict2[value]:
                res.append(num)

                if len(res) == k:
                    return res

            dict2.pop(value)
        




# dic -> freq

# loop key num, value freq

# next loop key freq,  value  num

# max dictorary -> num ||| put it into a list || remove 
