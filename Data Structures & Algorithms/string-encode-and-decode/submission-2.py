class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # make the encoded string follow format:
                                         # 'len''#''string' 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): 
            j = i
            while s[j] != "#": # search until we hit a # symbol, we then know we are at the string
                j += 1
            length = int(s[i:j]) # when we hit '#' we know everyting before is the length of the string
            i = j+1 # move i to the first char
            j = i + length # move j past the last char 
            res.append(s[i:j]) # append entire string to our result
            i = j # move i to next chunk 
        return res