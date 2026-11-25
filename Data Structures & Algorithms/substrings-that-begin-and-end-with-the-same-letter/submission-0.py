class Solution:
    def numberOfSubstrings(self, s: str) -> int:


        count = 0


        dict1 = {}

        for i in range(len(s)):
            
            if s[i:i+1] not in dict1:
                dict1[s[i:i+1]] = []
            
            dict1[s[i:i+1]].append(s[i:i+1])




        i = 0

        while dict1 and i < len(s):
            count += len(dict1[s[i:i+1]])
            if dict1[s[i:i+1]] == []:
                i += 1
            else:
                dict1[s[i:i+1]].pop()
        

        return count










#dict[letter] = {[]}
# dict1[lettet] = [postion]
#
# dict1["a"] = [0,3]
# dict1["b"] = [1]
# dict1["c"] = [2]


#dict2["z"] = [0,1,2,3]


# plus len(of dict)
