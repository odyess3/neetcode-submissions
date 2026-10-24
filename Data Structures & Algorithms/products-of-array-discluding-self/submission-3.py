class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_list=[]
        my_list =nums.copy()

        my_list.insert(0, 1)
        my_list.append(1)

        prefix =[]
        countup = 1
        postfix =[]

        for i in range(len(my_list)-2):
            countup *= my_list[i]
            prefix.append(countup)
        
        countup = 1

        for i in range(len(my_list)-1, 1, -1):
            countup *= my_list[i]
            postfix.append(countup)

        postfix.reverse()

        ans =[]
        

        for i in range(len(prefix)):
            ans.append(prefix[i] * postfix[i])

        

        return ans



#l 1 2 4 6 l
#l 48 24 12 8 l