'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

#代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    stack = []

    def Iteration(self, root):
        if root != None:
            self.Iteration(root.left)
            self.stack.append(root.val)
            self.Iteration(root.right)

    def inorderTraversal(self, root):
        self.stack.clear()
        self.Iteration(root)
        return self.stack