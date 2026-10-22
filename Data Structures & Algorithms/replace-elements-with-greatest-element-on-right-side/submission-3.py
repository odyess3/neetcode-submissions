class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        my_list =[]

        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])

        return arr   