#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 方法 1: 递归
    # def helper(self, root, res):
    #     if root:
    #         self.helper(root.left, res)
    #         res.append(root.val)
            # self.helper(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # self.helper(root, res)
        # return res

        # 方法 2，使用栈遍历
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            if node.val:
                res.append(node.val)
            root = node.right
    

# @lc code=end

