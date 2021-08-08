#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 方法 1:
    def flatten(self, root):
        # base case
        if not root:
            return
        # 拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        # 暂存一下左右子树
        left = root.left
        right = root.right

        # 将左子树接到右子树
        root.right = left
        # 将左子树置为 None
        root.left = None

        # 先选取左子树进行操作
        tmp = root
        # 找到左子树的最右子节点
        while tmp.right:
            tmp = tmp.right
        
        # 将左子树的最右子节点连接右子树
        tmp.right = right




    # 方法 2:
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """

    #     def dfs(node):
    #         # base case
    #         if not node: return

    #         # 先把左右子树打平
    #         # 先从整体对左右子树进行迭代的目的：保证后序操作的时候，root 
    #         # 的左右子树都已经被打平
    #         dfs(node.left)
    #         dfs(node.right)

    #         # 从左子树开始打平
    #         if node.left:
    #             # 取该节点的左子树
    #             tmp = node.left

    #             # 取该节点的最右子树 
    #             while tmp.right:
    #                 tmp = tmp.right
                
    #             tmp.right = node.right
    #             node.right = node.left
    #             node.left = None
            
    #     dfs(root)
    #     return root

# @lc code=end

