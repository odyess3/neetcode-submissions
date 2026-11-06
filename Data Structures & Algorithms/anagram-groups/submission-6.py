class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic1 = {}

        for i, n in enumerate(strs):
            
            sorted_text = ''.join(sorted(n))
            
            if sorted_text not in dic1:
                dic1[sorted_text] = []

            dic1[sorted_text].append(n)
        
        return list(dic1.values())
        
       

    
        






# 1st loop sorting out the key, but not the values
# e.g dic1["act"] = "act"
# e.g dic1["act"] += cat