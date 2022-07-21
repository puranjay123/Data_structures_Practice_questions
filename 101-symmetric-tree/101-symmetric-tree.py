# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(L,R):
            if not L and not R: 
                return True
            if L and R and L.val == R.val:
                return isSym(L.left,R.right) and isSym(L.right,R.left)
            return False
        return isSym(root,root)
    #     if not root :
    #         return True
    #     else:
    #         return self.ismirror(root.left,root.right)
    # def ismirror(self,left,right):
    #     if left is None and right is None:
    #         return True
    #     if left is None or right is None:
    #         return False
    #     if left.val == right.val:
    #         outpair = self.ismirror(left.left,right.right)
    #         inpair  = self.ismirror(left.right,right.left) 
    #         return outpair and inpair
    #     else:
    #         return False