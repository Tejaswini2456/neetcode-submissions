class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq = self.frequency_count(s)
        t_freq = self.frequency_count(t)
        return s_freq == t_freq
    
    def frequency_count(self,s:str):
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        return freq
        