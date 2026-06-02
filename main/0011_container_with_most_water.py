"""
Problem: 11 - Container With Most Water
Difficulty: Medium

Link:
https://leetcode.com/problems/container-with-most-water/

Time Complexity:
O(n)

Space Complexity:
O(1)

Notes:
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        best = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            best = max(best, width * current_height)
            
            if height[left] < height[right]: # increase i
                left += 1
            else: # decrease j
                right -= 1
        return best


def run_tests():
    s = Solution()

    # Example 1:
    height = [1,8,6,2,5,4,8,3,7]
    r = s.maxArea(height)
    assert r == 49

    # Example 2:
    height = [1,1]
    r = s.maxArea(height)
    assert r == 1

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()