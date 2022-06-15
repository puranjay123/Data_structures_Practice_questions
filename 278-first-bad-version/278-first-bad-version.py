# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersion(self, n: int) -> int:
        low=0
        high=n-1
        version=n
        while(low<=high):
            mid=low+(high-low)//2
            if isBadVersion(mid):
                version=mid
                high=mid-1
            else:
                low=mid+1
        return version
        
#         isbadversion retrun karega ki bad verison hai ya nahi
#  if is bad version is true to bad version hai else false
#         result=0
#         for i in range(n):
#             if(isBadVersion(i)):
            
#                 return i
#         return n
        
             
            
        
        