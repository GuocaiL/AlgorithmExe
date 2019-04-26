'''
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

示例 2 :
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。

注意：
s.length 在1到50,000之间。
s 只包含“0”或“1”字符。
'''

#我的解法
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pos=[i for i in range(len(s)) if s.startswith('01',i) or s.startswith('10',i)]
        m=0
        for n in pos:
            k=0
            if n==0 or n==len(s)-2:
                m+=1
            else :
                while n-k>=0 and k+n+1<=len(s)-1:
                    if s[n-k]==s[n] and s[n+1+k]==s[n+1]:
                        m+=1
                        k+=1
                    else:
                        break
        return m
'''
执行用时 : 828 ms, 在Count Binary Substrings的Python3提交中击败了5.30% 的用户
内存消耗 : 14 MB, 在Count Binary Substrings的Python3提交中击败了17.74% 的用户
'''
                        
#一种更简洁的解法
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        preCount = 0
        curCount = 1
        result = 0
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                curCount += 1
            else:
                preCount = curCount
                curCount = 1
            if preCount >= curCount:
                result += 1
        return result

'''
执行用时 : 208 ms, 在Count Binary Substrings的Python3提交中击败了70.15% 的用户
内存消耗 : 13.3 MB, 在Count Binary Substrings的Python3提交中击败了56.45% 的用户
'''

