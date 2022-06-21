class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        low=0
        
        high = 0
        while high<len(s):
            if s[high]!=' ':
                high+=1
            elif s[high]== ' ':
                res += s[low:high+1][::-1]
                high +=1
                low = high
        res+=' '
        res +=s[low:high+2][::-1]
        return res[1:]
                