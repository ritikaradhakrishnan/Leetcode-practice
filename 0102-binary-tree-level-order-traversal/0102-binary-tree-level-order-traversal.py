# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Lot of edge cases where val can be None 
        #TC ans SC: O(n), regular BFS implementation 
        q = deque()
        outerlist = []
        if root: #innerlist.append(node.val) kar rahe hai toh atleast value value hona chaiye q mein append karne
            q.append(root)
        while q:
            innerlist = []
            for i in range(len(q)):
                node = q.popleft()
                innerlist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            outerlist.append(innerlist) #Ek iteration hone ke baad saare values list mein aa jate hai tabhi outerlist mein append karna
        return outerlist #q empty hone ke baad outer list return karna


#         q = collections.deque()
#         q.append(root)
#         result = []
#         if not root:
#             return result
#         while q:
#             innerList = []
#             for i in range(len(q)):
#                 node = q.popleft()
#                 innerList.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             result.append(innerList)
#         return result


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         def dfs(node, level):
#             if not node:
#                 return
#             if level >= len(result):
#                 result.append([])
#             result[level].append(node.val)
#             dfs(node.left, level + 1)
#             dfs(node.right, level + 1)
            
#         result = []
#         dfs(root, 0)
#         return result

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        result = []
        if not root:
            return result
        while q:
            level = []
            for i in range(len(q)):
                popped = q.popleft()
                level.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            result.append(level)
        return result
                
                
