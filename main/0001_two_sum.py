"""
Problem: 1 - Two Sum
Difficulty: Easy

Link:
https://leetcode.com/problems/two-sum/

Time Complexity:
O(...)

Space Complexity:
O(...)

Notes:
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pass


def run_tests():
    s = Solution()

    # Test 1
    nums = [2,7,11,15]
    target = 9
    assert s.twoSum(nums, target) == [0, 1]

    # Test 2
    nums = [3,2,4]
    target = 6
    assert s.twoSum(nums, target) == [1, 2]

    # Test 3
    nums = [3,3]
    target = 6
    assert s.twoSum(nums, target) == [0, 1]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
