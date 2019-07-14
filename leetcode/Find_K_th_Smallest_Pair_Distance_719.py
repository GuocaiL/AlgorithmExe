'''
给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

示例 1:
输入：
nums = [1,3,1]
k = 1
输出：0
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。

提示:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''

#代码如下
class Solution:
    def smallestDistancePair(self, A, K: int) -> int:
        A.sort()
        low, high = 0, A[len(A) - 1] - A[0]
        while low < high:
            m = (high + low) >> 1
            j = count = 0
            for i in range(1, len(A)):
                while A[i] - A[j] > m:
                    j += 1
                count += i - j
            if count < K:
                low = m + 1
            else:
                high = m
        return low

#结果如下
'''
执行结果：通过
显示详情
执行用时 :204 ms, 在所有 Python3 提交中击败了25.93%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了73.33%的用户
'''
