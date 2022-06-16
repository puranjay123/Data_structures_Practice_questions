class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length=len(nums)
        square=[]
        
        for i in range(length):
            square.append(nums[i]*nums[i])
        square.sort()
        return square