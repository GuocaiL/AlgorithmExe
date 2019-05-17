'''
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:
给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。

示例 1:
输入: 5
输出: 2
解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。

示例 2:
输入: 1
输出: 0
解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
'''

class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)
        binary2='0b'
        for i in binary[2:]:
            if i=='0':
                binary2=binary2+'1'
            else :
                binary2=binary2+'0'
        return int(binary2,2)

'''
执行用时 : 52 ms, 在Number Complement的Python3提交中击败了84.16% 的用户
内存消耗 : 13.1 MB, 在Number Complement的Python3提交中击败了61.29% 的用户
'''

class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)