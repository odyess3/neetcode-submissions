class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        highest = arr[-1]
        arr[-1] = -1

        list1 =[-1 for i in range(len(arr))]


        for r in range(len(arr)-2, -1 , -1):


            highest = max(highest, arr[r+1])
            
            list1[r] = highest
            

            
        

        return list1


            




        