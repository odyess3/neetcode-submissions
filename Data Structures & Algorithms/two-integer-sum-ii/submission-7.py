class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dct = {}
        my_list = []

        for i, n in enumerate(numbers):
            comp = target - n

            if comp in dct:
                my_list.append(dct[comp] + 1)
                my_list.append(i + 1)
                break
            dct[n] = i 
        return my_list