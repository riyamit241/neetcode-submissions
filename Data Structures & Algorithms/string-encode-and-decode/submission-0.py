class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for i in strs:
            new += str(len(i)) + '#' + i

        return new
                

    def decode(self, s: str) -> List[str]:
        new, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])

            word = s[j+1 : j+1+length]
            new.append(word)

            i = j+1+length
        return new