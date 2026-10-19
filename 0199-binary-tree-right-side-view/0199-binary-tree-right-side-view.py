# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right

# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
        # res = []

        # if not root:
        #     return res

        # q = collections.deque([root])

        # while q:
        #     size = len(q) #The size of the queue is cached at the beginning of each level to avoid modifying the queue during the loop.

        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if i == size - 1:
        #             res.append(node.val)

        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)

        # return res
        # q = collections.deque()
        # q.append(root)
        # output = []
        # if not root:
        #     return output
        # while q:
        #     lastPos = len(q)-1
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if i == lastPos:
        #             output.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return output


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = collections.deque()
        output = []
        if not root:
            return output
        q.append(root)

        while q:
            right = root
            # level = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(right.val)
        return output







                



