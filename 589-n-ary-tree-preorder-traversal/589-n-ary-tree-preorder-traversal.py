"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def solve(root,ans):
            if root:
                ans.append(root.val)
                for child in root.children:
                    solve(child,ans)
            return ans
        return solve(root,[])
        