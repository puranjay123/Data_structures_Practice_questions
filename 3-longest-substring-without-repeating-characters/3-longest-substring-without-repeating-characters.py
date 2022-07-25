class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = {}
        l =0
        output = 0
        for r in range(len(s)):
            if s[r] not in occur:
                output = max(output,r-l+1)
            else:
                if occur[s[r]]<l:
                    output = max(output,r-l+1)
                else:
                    l = occur[s[r]]+1
            occur[s[r]] = r
        return output
        
        # APproach 1
        # charSet = set()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res,r-l+1)
        # return res
        
#         Approach 2
       
        