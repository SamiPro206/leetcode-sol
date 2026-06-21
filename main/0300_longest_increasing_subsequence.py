"""
Problem: 300 - Longest Increasing Subsequence
Difficulty: Medium

Link:
https://leetcode.com/problems/longest-increasing-subsequence/

Time Complexity:
O(n²)

Space Complexity:
O(n)

Notes:
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        r = [1] * N
    
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    r[i] = max(r[i], r[j] + 1)

        return max(r)


def run_tests():
    sol = Solution()

    # Test 1
    nums = [10,9,2,5,3,7,101,18]
    assert sol.lengthOfLIS(nums) == 4

    # Test 2
    nums = [0,1,0,3,2,3]
    assert sol.lengthOfLIS(nums) == 4

    # Test 3
    nums = [7,7,7,7,7,7,7]
    assert sol.lengthOfLIS(nums) == 1
    
    # Test 4
    nums = [4,10,4,3,8,9]
    assert sol.lengthOfLIS(nums) == 3

    # Test 5
    nums = [3,1,2]
    assert sol.lengthOfLIS(nums) == 2

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
