class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         Approach 3
        if len(s)!=len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -=1
            if count[c]<0:
                return False
        return True
        

        
#         appraoch 2
        
        # return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])
#         approach 1 stack

#         a = []
#         for ch in s:
#             a.append(ch)
#             a.sort()
#             print(a)
#         for ca in t:
#             if ca in a:
                
                
#                 a.sort()
#                 a.replace()
#                 print(a)
            
#         if len(a)==0:
#             return True
#         else:
#             return False
        
            
        