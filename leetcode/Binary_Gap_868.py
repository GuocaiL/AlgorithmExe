'''
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
如果没有两个连续的 1，返回 0 。

示例 1：
输入：22
输出：2
解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。

示例 2：
输入：5
输出：2
解释：
5 的二进制是 0b101 。

示例 3：
输入：6
输出：1
解释：
6 的二进制是 0b110 。

示例 4：
输入：8
输出：0
解释：
8 的二进制是 0b1000 。
在 8 的二进制表示中没有连续的 1，所以返回 0 。

提示：
1 <= N <= 10^9
'''


class Solution:
    def binaryGap(self, N: int) -> int:
        s = str(bin(N))
        value = 0
        bol = False
        s1 = 0
        s2 = 0
        for i in range(len(s)):
            if s[i] == str(1) and not bol:
                s1 = i
                bol = True
            if s[i] == str(1) and bol:
                s2 = i
                if value < s2 - s1:
                    value = s2 - s1
                s1 = s2
        return value

'''
执行用时 : 56 ms, 在Binary Gap的Python3提交中击败了61.00% 的用户
内存消耗 : 13 MB, 在Binary Gap的Python3提交中击败了86.99% 的用户
'''