#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # 方法 1， 递归，dfs
    # def connect_two(self, node1, node2):
    #     if not node1 or not node2:
    #         return None
        
    #     node1.next = node2
    #     self.connect_two(node1.left, node1.right)
    #     self.connect_two(node2.left, node2.right)
    #     self.connect_two(node1.right, node2.left)
        
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return None
    #     self.connect_two(root.left, root.right)
    #     return root

    # 方法 2， 逐层遍历
    def connect(self, root):
        if not root: return root

        # 从根结点开始
        leftmost = root

        while leftmost.left:
            # 遍历同一层节点链表
            head = leftmost
            while head:
                # 连接具有统一父节点的两个左右子节点
                head.left.next = head.right
                # 如果两个节点相邻且没有共同父节点，那么可以通过父节点的 next 节点来连接
                if head.next:
                    head.right.next = head.next.left
                # 遍历到下一个节点，能运行到这里说明上一层操作中已经将本层的节点都已经连接好了
                head = head.next
            # 接下来对下一层进行操作
            leftmost = leftmost.left
        return root

# @lc code=end

