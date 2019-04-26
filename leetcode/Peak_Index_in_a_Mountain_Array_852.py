'''
我们把符合下列属性的数组 A 称作山脉：

A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

示例 1：
输入：[0,1,0]
输出：1

示例 2：
输入：[0,2,1,0]
输出：1

提示：
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A 是如上定义的山脉
'''

#自己的解答
class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return i
'''
执行用时 : 60 ms, 在Peak Index in a Mountain Array的Python3提交中击败了52.10% 的用户
内存消耗 : 14.2 MB, 在Peak Index in a Mountain Array的Python3提交中击败了41.88% 的用户
'''

#更简洁的解法
class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        return A.index(max(A))
'''
执行用时 : 64 ms, 在Peak Index in a Mountain Array的Python3提交中击败了35.47% 的用户
内存消耗 : 14.2 MB, 在Peak Index in a Mountain Array的Python3提交中击败了41.88% 的用户
'''

#更高效的解法（二分查找）
class Solution:
    def peakIndexInMountainArray(self, A) -> int:
        left = 0
        right = len(A) - 1
        while right - left + 1 > 3:
            mid = (left + right) // 2
            if A[mid] > A[mid - 1] and A[mid + 1] > A[mid]:
                left = mid
            if A[mid] < A[mid - 1] and A[mid + 1] < A[mid]:
                right = mid
            if A[mid] > A[mid - 1] and A[mid + 1] < A[mid]:
                return mid
        return (left + right) // 2

''''
执行用时 : 56 ms, 在Peak Index in a Mountain Array的Python3提交中击败了81.54% 的用户
内存消耗 : 14.1 MB, 在Peak Index in a Mountain Array的Python3提交中击败了78.34% 的用户
'''
