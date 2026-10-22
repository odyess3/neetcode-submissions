class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        my_list = []
        arr.pop(0)

        for i in range(0,len(arr)):
            
            my_list.append(max(arr))
            arr.pop(0)
        
        my_list.append(-1)

        return my_list