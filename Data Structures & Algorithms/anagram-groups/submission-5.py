class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tory = {}
        

        for i in range(len(strs)):
            lis = [0] * 26


            for char in strs[i]:

                one = ord(char) - ord("a")
                lis[one] +=  1
            

            uniq = tuple(lis)

            if uniq not in tory:
                tory[uniq] = []


            tory[uniq].append(strs[i])
            
        return list(tory.values())