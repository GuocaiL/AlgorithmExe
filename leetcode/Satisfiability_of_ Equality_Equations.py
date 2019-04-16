'''
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。
'''

'''
方法：联通分量

思路:
    所有相互等于的变量能组成一个联通分量。举一个例子，如果 a=b, b=c, c=d，那么 a, b, c, d 就在同一个联通分量中，因为它们必须相等。

算法:
    第一步，我们基于给定的等式，用深度优先遍历将每一个变量按照联通分量染色。
    将联通分量染色之后，我们分析形如 a != b 的不等式。如果两个分量有相同的颜色，那么它们一定相等，因此如果说它们不相等的话，就一定无法满足给定的方程组。
    否则，我们的染色就可以看作是一组能满足方程组约束的方案，所以结果是 true。
'''


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        recoder = [[] for _ in range(26)]
        for equa in equations:
            if equa[1] == '=':
                x = ord(equa[0]) - ord('a')
                y = ord(equa[3]) - ord('a')
                recoder[x].append(y)
                recoder[y].append(x)
        color = [None] * 26
        t = 0
        for start in range(26):
            if color[start] is None:
                t = t + 1
                count = [start]
                while count:
                    num = count.pop()
                    for i in recoder[num]:
                        if color[i] is None:
                            color[i] = t
                            count.append(i)
        for end in equations:
            if end[1] == '!':
                if end[0] == end[3]:
                    return False
                elif color[ord(end[0]) - ord('a')] is not None and color[ord(end[0]) - ord('a')] == color[
                    ord(end[3]) - ord('a')]:
                    return False
        return True

'''
复杂度分析
    时间复杂度： O(N)，其中 NN 是方程组 equations 的数量。
    空间复杂度： O(1)，认为字母表的大小是 O(1) 的。
'''