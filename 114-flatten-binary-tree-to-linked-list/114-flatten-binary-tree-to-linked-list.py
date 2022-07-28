# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            leftEnd =  dfs(root.left)
            rightEnd = dfs(root.right)
            if root.left:
                leftEnd.right =root.right
                root.right = root.left
                root.left = None
            
            if rightEnd:
                last = rightEnd
                return last
            if leftEnd:
                last = leftEnd
                return last
            if root:
                last = root
                return last
            
        dfs(root)
            
            

        
        