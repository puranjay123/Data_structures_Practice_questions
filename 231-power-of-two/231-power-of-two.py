class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not(n&n-1)
#         if (n==1):
#             return True
#         if(n%2!=0 or n==0):
#             return False
        
#         return self.isPowerOfTwo(n//2)
            
        
        