class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length=len(nums)
        low=0
        high=length-1
        
        while(low<high):
            mid=low +(high-low)//2
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid
#             if(nums[mid]>=nums[mid-1] & nums[mid]>=nums[mid+1]):
#                 return mid
#             elif(nums[mid]<nums[mid+1] & nums[mid-1]<nums[mid]):
#                 low=mid+1
#             elif(nums[mid+1]<nums[mid] & nums[mid-1]>nums[mid]):
#                 high=mid-1
        
        return low