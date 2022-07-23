# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         For the guys struggling with -1, just think of it as returning False. We are only returning -1 because our function returns integers.

# And for those who don't understand why left or right can be -1:
# If abs(left - right) > 1is triggered, this means we have an unbalanced tree at that node, so we would return -1.
# left == -1 occurs when the left subtree of the current root is already unbalanced.
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            
            if left ==-1 or right ==-1 or abs(left-right) >1:
                return -1
            return 1+ max(left,right)
        return check(root) != -1
            
            
        