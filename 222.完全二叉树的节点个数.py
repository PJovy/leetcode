#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 经典递归解决

        # 1. 边际条件，当节点为 None，返回 0
        # 2. 1 + 迭代左子树 + 迭代右子树
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
# @lc code=end

