'''
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。

进阶：
你能否仅使用O(1) 空间解决问题？

示例 1：
输入：
["a","a","b","b","c","c","c"]
输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]
说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。

示例 2：
输入：
["a"]
输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。
示例 3：

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。
注意：

所有字符都有一个ASCII值在[35, 126]区间内。
1 <= len(chars) <= 1000。
'''

class Solution:
    def compress(self, chars):
        count = 0
        curPos = 0
        stack = []
        a = []
        Pos = 0
        for i in range(len(chars)):
            if chars[i] == chars[curPos]:
                count += 1
            if chars[i] != chars[curPos]:
                if count != 1:
                    while count > 0:
                        stack.append(count % 10)
                        count = count // 10
                    while stack:
                        curPos += 1
                        chars[curPos] = str(stack.pop())
                    curPos += 1
                    chars[curPos] = chars[i]
                    count = 1
                else:
                    curPos += 1
                    chars[curPos] = chars[i]
                    count = 1
            Pos = i
        if Pos == 0:
            a = chars
        if Pos > 0 and Pos == len(chars) - 1:
            if count != 1:
                while count > 0:
                    stack.append(count % 10)
                    count = count // 10
                while stack:
                    curPos += 1
                    chars[curPos] = str(stack.pop())
            a = chars[:curPos + 1]
        return len(a)

'''
执行用时 : 76 ms, 在String Compression的Python3提交中击败了51.90% 的用户
内存消耗 : 13.1 MB, 在String Compression的Python3提交中击败了90.62% 的用户
'''