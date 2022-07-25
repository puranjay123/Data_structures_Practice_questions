class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        
        result[0] = self.findStaringIndex(nums,target)
        result[1] = self.findEndIndex(nums,target)
        return result
    def findStaringIndex(self,nums,target):
        index = -1
        low,high = 0,len(nums)-1
        
        while low<=high:
            mid = low +(high-low)//2
            if nums[mid] == target:
                index = mid
                high = mid-1
            elif nums[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return index
    def findEndIndex(self,nums,target):
        index = -1
        low,high = 0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2

            if nums[mid]== target:
                index =mid
                low= mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid + 1
        return index
            # def binarySearchLeft(A,x):
#             left,right = 0,len(A)-1
#             while left<=right:
#                 mid = (right+left)//2
#                 if x>A[mid]:
#                     left = mid+1
#                 else:
#                     right = mid-1
#             return left
#         def binarySearchRight(A,x):
#             left,right=0,len(A)-1
#             while left<=right:
#                 mid = (left+right)//2
#                 if x>=A[mid]:
#                     left = mid+1
#                 else:
#                     right = mid-1
#             return right
#         left,right = binarySearchLeft(nums,target),binarySearchRight(nums,target)
#         return(left,right) if left<=right else[-1,-1]
        