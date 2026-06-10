"""
Problem: 152 - Maximum Product Subarray
Difficulty: Medium

Link:
https://leetcode.com/problems/maximum-product-subarray/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_r = nums[0]
        min_r = nums[0]
        best = nums[0]

        for x in nums[1:]:
            p_max_r = max_r
            p_min_r = min_r
            max_r = max(
                x,
                p_min_r * x,
                p_max_r * x
            )
            min_r = min(
                x,
                p_min_r * x,
                p_max_r * x
            )
            best = max(best, max_r)
        return best


def run_tests():
    sol = Solution()

    # Test 1
    nums = [2,3,-2,4]
    assert sol.maxProduct(nums) == 6

    # Test 2
    nums = [-2,0,-1]
    assert sol.maxProduct(nums) == 0

    # Test 3
    nums = [2,3,-2,4,-1]
    assert sol.maxProduct(nums) == 6*4*2

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
