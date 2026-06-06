"""
Problem: 198 - House Robber
Difficulty: Medium

Link:
https://leetcode.com/problems/house-robber/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
Easy dp problem
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # profit max at pos i : 
        r = [0] * (n+1)
        
        for i in range(1, (n+1)):
            r[i] = max(nums[i-1] + r[i-2], r[i-1])
        return r[n]


def run_tests():
    s = Solution()

    # Test 1
    nums = [1,2,3,1]
    assert s.rob(nums) == 4

    # Test 2
    nums = [2,7,9,3,1]
    assert s.rob(nums) == 12

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
