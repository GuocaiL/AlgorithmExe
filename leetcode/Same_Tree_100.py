'''
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def tree_to_list(self, l):
        list2 = []
        list1 = queue.Queue()
        if l == None:
            return list2
        else:
            list1.put(l)
            while not list1.empty():
                node = list1.get()
                if node != 'null':
                    list2.append(node.val)
                    if node.left != None:
                        list1.put(node.left)
                    else:
                        list1.put('null')
                    if node.right != None:
                        list1.put(node.right)
                    else:
                        list1.put('null')
                else:
                    list2.append('null')
            return list2

    def isSameTree(self, p, q) -> bool:
        l1 = self.tree_to_list(p)
        l2 = self.tree_to_list(q)
        print(l1)
        print(l2)
        return l1 == l2

'''
执行用时 : 52 ms, 在Same Tree的Python3提交中击败了87.16% 的用户
内存消耗 : 13.3 MB, 在Same Tree的Python3提交中击败了8.10% 的用户
'''

#借鉴（碰见树，递归就行）
class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return True
        else:
            return False