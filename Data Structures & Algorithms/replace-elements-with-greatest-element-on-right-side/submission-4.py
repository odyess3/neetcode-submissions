class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        

        for l in range(0,len(arr)-1):
            r = l+1
            highest = 0

            while r < len(arr):
                highest = max(arr[r],highest)
                
                r+=1
            
            arr[l] = highest
            
        
            

        
        arr[-1] = -1

        return arr














# 2 4 5 3 1 2 -> loop thru them
# 2 4 | l=0 r= 1
# since 4 > 2
# 4 4 | l reset to 0, r continues