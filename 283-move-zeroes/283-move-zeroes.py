import numpy as np
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow=0
        fast=1
        length = len(nums)-1
        while slow<=length and fast<=length:
            if nums[slow] == 0 and nums[fast]!=0:
                nums[slow] = nums[fast]
                nums[fast]=0
            if nums[slow]!=0:
                slow+=1
                
            fast =fast+1
        return nums
            
        """
        Do not return anything, modify nums in-place instead.
        """
    
#         nums = [0,1,0,3,12]
#         l=len(nums)
#         end = nums[l-1]
#         arr1=[]
#         arr2=[]
#         arr3 = [0]*len(nums)
        
#         for i in range(l):
#             if(nums[i]==0):
#                 arr2.append(nums[i])
#             elif(nums[i]!=0):
#                 arr1.append(nums[i])
#         nums=[0]*len(nums)    
#         nums=arr1+arr2
#         # arr3.replace(" ","")
#         print(arr3)
#         return nums
        