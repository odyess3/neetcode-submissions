class Solution:

    def encode(self, strs: List[str]) -> str:

        stri = ""

        for i in range(len(strs)):
            length = len(strs[i])

            stri += f"{length}#{strs[i]}"
        

        print(f"encode: {stri}")
        return stri



    def decode(self, s: str) -> List[str]:
        start = 0
        list1 = []
        lengthstr = ""
        l=0
        while start<len(s):
            j = start

            while s[j] != "#":
                j+=1


            length = int (s[start:j])

            start = j+1

            start_length = start+length

            word = s[start:start_length]

            list1.append(word)

            print(start)
            start += length
            print(word)

        return list1

#hello5

#while -> everything
# 1: index 0 = length
# 2: next index always a hash
# 3: move l to hash+1 and up to hash+1 + length
# 4: all over again
