class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqt = {}
        freqs = {}
        for letterS in s:
            if letterS in freqs:
                freqs[letterS] +=1
            else:
                freqs[letterS] = 1


        for letterT in t:
            if letterT in freqt:
                freqt[letterT] +=1
            else:
                freqt[letterT] = 1

        return freqs == freqt


 
   
    
        