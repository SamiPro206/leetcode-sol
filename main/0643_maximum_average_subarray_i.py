"""
Problem: 643 - Maximum Average Subarray I
Difficulty: Easy

Link:
https://leetcode.com/problems/maximum-average-subarray-i/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = sum(nums[:k])
        best = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i-k]
            best = max(best, window)

        return best * 1.0 / k

def run_tests():
    sol = Solution()

    # Test 1
    nums = [1,12,-5,-6,50,3]
    k = 4
    assert sol.findMaxAverage(nums, k) == 12.75

    # Test 2
    nums = [5]
    k = 1
    assert sol.findMaxAverage(nums, k) == 5.0

    # Test 3
    nums = [1,12,-5,-6,50,3]
    k = 4
    assert sol.findMaxAverage(nums, k) == 12.75000

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
