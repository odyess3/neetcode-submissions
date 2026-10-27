class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}


        for i in range(len(strs)):
            huge = [0] * 26

            for char in strs[i]:
                index = ord(char) - ord("a")
                huge[index] += 1
                
            

            key = tuple(huge)

            if key not in group:
                group[key] = []
            

            group[key].append(strs[i])
        

        return list(group.values())


        