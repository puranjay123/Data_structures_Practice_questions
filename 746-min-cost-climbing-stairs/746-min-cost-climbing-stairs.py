class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp =[0] *len(cost)
        
        dp[0] = cost[0]
        if len(cost) >=2:
            dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
#         cost.append(0)
#         for i in range(len(cost) -3,-1,-1):
#             cost[i] += min(cost[i+1],cost[i+2])
            
#         return min(cost[0],cost[1])
        
        