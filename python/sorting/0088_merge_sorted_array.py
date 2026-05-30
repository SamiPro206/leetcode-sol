"""
Problem: 88 - Merge Sorted Array
Difficulty: Easy

Link:
https://leetcode.com/problems/merge-sorted-array/

Time Complexity:
O(m+n)

Space Complexity:
O(1)

Notes:
- Fill the array from the end
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result_len = m+n

        # case: nums1 does not have enough space
        if len(nums1) < result_len:
            nums1.extend([0]* (result_len-len(nums1)))
        
        k = result_len-1 # points to the max of the final list
        i = m-1 # points to the max of the first list
        j = n-1 # points to the max of the second list

        while(j >= 0):
            if (i >= 0) and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

if __name__ == "__main__":
    s = Solution()

    # Example 1:
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    s.merge(nums1, 3, nums2, 3)
    assert nums1 == [1,2,2,3,5,6]

    # Example 2:
    nums1 = [1]
    nums2 = []
    s.merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

    # Example 3:
    nums1 = []
    nums2 = [1]
    s.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]