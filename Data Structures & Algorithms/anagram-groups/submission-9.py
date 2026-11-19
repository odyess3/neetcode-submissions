class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = {}

        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))

            if string not in dict1:
                dict1[string] = []

            dict1[string].append(strs[i])
        
        
        return list(dict1.values())