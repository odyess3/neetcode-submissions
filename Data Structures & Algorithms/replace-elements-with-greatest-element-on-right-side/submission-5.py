class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        highest = arr[len(arr)-1]

        ans = [0] * len(arr)



        for r in range(len(arr)-1, -1, -1):
            ans[r] = highest

            highest = max(highest, arr[r])
            
            


        ans[len(ans)-1] = -1
        
    

        return ans



#  start at the right side -1 ()second last
# compare all the numbers on the right ie right plus highest
# store current in temp



        