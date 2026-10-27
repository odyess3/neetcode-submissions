class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for stri in strs:
            length = len(stri)
            string += str(length) +"#"+ stri
        
        return string

    def decode(self, s: str) -> List[str]:

        thi = []

        i =0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])

            start = j+1

            word = s[start:start+length]

            thi.append(word)
            
            i = start + length
        return thi