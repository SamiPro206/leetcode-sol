"""
Problem: 918 - Maximum Sum Circular Subarray
Difficulty: Medium

Link:
https://leetcode.com/problems/maximum-sum-circular-subarray/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
utiliser les propriétés de inclusion/exclusion
s'il faut être circulaire, un autre problème plus simple se crée
trouver le minimum continue
"""


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        best_max = best_min = curr_max = curr_min = nums[0]
        for i in range(1, len(nums)):
            prev_curr_max = curr_max
            prev_curr_min = curr_min

            curr_max = nums[i] + max(0, prev_curr_max, prev_curr_min)
            curr_min = nums[i] + min(0, prev_curr_max, prev_curr_min)

            best_max = max(best_max, curr_max)
            best_min = min(best_min, curr_min)

        if best_max < 0:
            return best_max
        else:
            return max(best_max, total - best_min)


def run_tests():
    sol = Solution()

    # Test 1
    nums = [1,-2,3,-2]
    assert sol.maxSubarraySumCircular(nums) == 3

    # Test 2
    nums = [5,-3,5]
    assert sol.maxSubarraySumCircular(nums) == 10

    # Test 3
    nums = [-3,-2,-3]
    assert sol.maxSubarraySumCircular(nums) == -2

    # Test 4
    nums = [2,-2,2,7,8,0]
    assert sol.maxSubarraySumCircular(nums) == 19

    # Test 5
    nums = [3,1,3,2,6]
    assert sol.maxSubarraySumCircular(nums) == 15

    # Test 6
    nums = [-1,3,-3,9,-6,8,-5,-5,-6,10]
    assert sol.maxSubarraySumCircular(nums) == 20

    print("-"*40)

    # Test 7
    nums = [-1,3,-3,9,-6,8,-5,-5,-6,10][::-1]
    assert sol.maxSubarraySumCircular(nums) == 20

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
