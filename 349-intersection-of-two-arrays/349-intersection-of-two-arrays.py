class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j]>0:
                res.append(j)
                map[j] = 0
        return res
        
        # return list(set(nums1) & set(nums2))
# ****************Approach2***********
#         res = []
        
#         for i in nums1:
#             if i not in res and i in nums2:
#                 res.append(i)
#         return res
