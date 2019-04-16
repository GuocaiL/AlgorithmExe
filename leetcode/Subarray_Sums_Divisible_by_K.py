'''
给定一个整数数组
A，返回其中元素之和可被
K
整除的（连续、非空）子数组的数目。

示例：
输入：A = [4, 5, 0, -2, -3, 1], K = 5
输出：7
解释：
有
7
个子数组满足其元素之和可被
K = 5
整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

提示：
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''


'''
方法一：前缀和与计数
思路:
    通常，涉及连续子数组问题的时候，我们使用前缀和来解决它们。我们令 P[i+1] = A[0] + A[1] + ... + A[i]。
那么，每个连续子数组就可以写成 P[j] - P[i] （其中 j > i） 的形式。因此，我们将 P[j] - P[i] 模 K 等于 0 等
价于 P[i] 与 P[j] 在模 K 的意义下同余。

算法:
    计算所有的 P[i] 在模 K 意义下的值。如果说一共有 C_xCx​个 P[i] \equiv x \pmod{K}P[i]≡x(modK)。那么，
就有 \sum_x \binom{C_x}{2}∑ x( 2C x)个可行的连续子数组。
'''

#实现：
import collections
class Solution:
    def subarraysDivByK(self, A, K) :
        p=[0]
        for num in A:
            p.append((p[-1]+num%K)%K)
        count=collections.Counter(p)
        return int(sum(v*(v-1)/2 for v in count.values()))