class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #aPPROACH 2
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
            print(result)
        return result
#         res = []
        
#         subset = []
#         def dfs(i):
#             if i>=len(nums):
#                 res.append(subset.copy())
#                 return
#             # decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i+1)
            
#             #decision NOt to include nums[i]
#             subset.pop()
#             dfs(i+1)
            
#         dfs(0)
#         return res
            
            
            
                
        
        