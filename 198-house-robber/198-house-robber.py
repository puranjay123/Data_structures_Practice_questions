class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2,prev,cur =0,0,0
        for i in nums:
            cur = max(prev,prev2+i)
            prev2 = prev
            prev = cur
        return cur
        # if not nums:
        #     return 0
        # if len(nums) ==1:
        #     return nums[0]
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     dp[i] = max(nums[i] +dp[i-2],dp[i-1])
        # return dp[-1]
        # memo = [-1 for i in range(len(nums))]
        # i=len(nums)-1
        # if (i<0):
        #     return 0
        # if(memo[i]>0):
        #     return memo[i]
        # result= max(self.rob(i-2)+nums[i],self.rob(i-1))
        # memo[i] =result
        # return result
#         take adjust values which are maximum
#  take max value from the left and teh right tree
#  1)find recursive realtion
#  2) Recursive(top-down)
#  3) Recusrive +memo(top-down)
#  4) Iteravtive +memo(bottom-up)
#  5) Iteravtive + N variables(bottom-up)

# rob(i) = math.max(rob(i-2),currentHouseValue,rob(i-1))

