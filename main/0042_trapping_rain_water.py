"""
Problem: 42 - Trapping Rain Water
Difficulty: Hard

Link:
https://leetcode.com/problems/trapping-rain-water/

Time Complexity:
O(n)

Space Complexity:
O(1)

Notes:
magique et faisable
à chaque position, savoir qui est le mur max à droite et à gauche et ça se fait tout seul
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxL = maxR = water = 0
        l, r = 0, len(height)-1 # pointers

        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                water += maxL - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                water += maxR - height[r]
                r -= 1
        return water

def run_tests():
    s = Solution()

    # Test 1
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert s.trap(height) == 6

    # Test 2
    height = [4,2,0,3,2,5]
    assert s.trap(height) == 9

    # Test 3
    height = [2,0,3]
    assert s.trap(height) == 2

    # Test 4
    height = [2,0,1]
    assert s.trap(height) == 1

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
