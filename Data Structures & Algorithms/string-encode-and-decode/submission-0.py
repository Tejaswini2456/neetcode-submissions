class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for word in strs:
            encoded_string += str(len(word))+"#"+word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result=[]
        i =0
        while i < len(s):
            j = i
            while s[j]!='#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            result.append(word)
            i = j+1+length
        return result
    