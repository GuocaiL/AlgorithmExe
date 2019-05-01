'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for n1 in nums1:
            if n1 in nums2:
                result.append(n1)
                nums2.remove(n1)
        return result

'''
执行用时 : 92 ms, 在Intersection of Two Arrays II的Python3提交中击败了45.16% 的用户
内存消耗 : 12.9 MB, 在Intersection of Two Arrays II的Python3提交中击败了98.43% 的用户
'''

