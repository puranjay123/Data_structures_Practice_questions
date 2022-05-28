class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrSize = len(nums)
        
        nums.sort()
#         0 ,1,3
        result=0
        for i in range(arrSize):
            if(nums[i]!=i):
                return i
        return arrSize
            
               
        
                
            
        