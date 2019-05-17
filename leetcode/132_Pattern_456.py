'''
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
注意：n 的值小于15000。

示例1:
输入: [1, 2, 3, 4]
输出: False
解释: 序列中不存在132模式的子序列。

示例 2:
输入: [3, 1, 4, 2]
输出: True
解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

示例 3:
输入: [-1, 3, 2, 0]
输出: True
解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
'''

#解法一
import sys
class Solution:
    def find132pattern(nums) -> bool:
        leftmin = sys.maxsize
        for i in range(len(nums)):
            if leftmin > nums[i]:
                leftmin = nums[i]
                for j in range(len(nums) - 1, i + 1, -1):
                    if nums[i] < nums[j]:
                        for k in range(i + 1, j):
                            if nums[k] > nums[i] and nums[k] > nums[j]:
                                return True
        return False

'''
81 / 95 个通过测试用例
状态：超出时间限制
'''

#解法二
class Solution:
    def find132pattern( nums) -> bool:
        _min = float('-inf')
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < _min:
                print("1")
                return True
            while stack and nums[i] > stack[-1]:
                _min = stack.pop()
            stack.append(nums[i])
        print("2")
        return False
'''
执行用时 : 88 ms, 在132 Pattern的Python3提交中击败了60.95% 的用户
内存消耗 : 14.3 MB, 在132 Pattern的Python3提交中击败了53.70% 的用户
'''
a=Solution
a.find132pattern([4,9,3,8])