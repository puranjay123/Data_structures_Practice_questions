class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
#         kuch samajh nahi aya
        k=k%len(nums)
        count =0
        start =0
        while count<len(nums):
            current =start
            prev = nums[start]
            
            while True:
                next = (current+k)% len(nums)
                temp = nums[next]
                nums[next]=prev
                prev = temp
                current = next
                count +=1
                if start == current:
                    break
            start +=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # a = [0] * len(nums)
#         for i in range(len(nums)):
#             a[(i+k)% len(nums)] = nums[i]
#         for i in range(len(nums)):
#             nums[i] = a[i]
            
            
#             3%7
#               
