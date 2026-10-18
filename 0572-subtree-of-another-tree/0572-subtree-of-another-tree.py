# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
    
    def sameTree(self, r, sr):
        if not r and not sr:
            return True
        if not r or not sr or r.val != sr.val:
            return False
        left = self.sameTree(r.left, sr.left)
        right = self.sameTree(r.right, sr.right)
        return left and right




# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not t:
#             return True
#         if not s:
#             return False

#         return self.sameTree(s,t) or (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))
            
#     #The sameTree method handles the comparisons between nodes, including the cases where either s or t is None. Thus, additional base case conditions are not required in this scenario.

#     def sameTree(self, s, t):
#         if not s and not t:
#             return True
#         if s and t and s.val == t.val:
#             return (self.sameTree(s.left, t.left) and
#             self.sameTree(s.right, t.right))
#         return False