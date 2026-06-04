"""
Problem: 70 - Climbing Stairs
Difficulty: Easy

Link:
https://leetcode.com/problems/climbing-stairs/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        r = [0] * n
        r[0] = 1

        for i in range(1, n):
            if i == 1:
                r[i] = 2
            else:
                r[i] = r[i-1] + r[i-2]
        
        return r[n-1]


def run_tests():
    s = Solution()

    # Test 1
    n = 2
    assert s.climbStairs(n) == 2

    # Test 2
    n = 3
    assert s.climbStairs(n) == 3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
