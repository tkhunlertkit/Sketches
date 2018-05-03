"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        sl = sorted(nums1)
        num_ints = len(sl)
        index = num_ints // 2
        return sl[index] if num_ints % 2 == 1 else (sl[index] + sl[index - 1]) / 2.0


if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    print (Solution().findMedianSortedArrays(nums1, nums2))