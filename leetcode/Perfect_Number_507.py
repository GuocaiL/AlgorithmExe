'''
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

 
示例：
输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14
 
注意:
输入的数字 n 不会超过 100,000,000. (1e8)
'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num>0:
            li=[]
            s=int(math.sqrt(num))
            print(s)
            for i in range(1,s+1):
                if num%i==0:
                    a=num//i
                    if i not in li and i!=num:
                        li.append(i)
                    if a not in li and a!=num:
                        li.append(a)
            print(li)
            return num==sum(li)
        else:
            return False
                
'''
执行用时 : 48 ms, 在Perfect Number的Python3提交中击败了97.95% 的用户
内存消耗 : 13.1 MB, 在Perfect Number的Python3提交中击败了83.47% 的用户
'''