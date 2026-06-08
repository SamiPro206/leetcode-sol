"""
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium

Link:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time Complexity:
O(n)

Space Complexity:
O(n)

Notes:
dp modifié un peu
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        r = [0] * (len(s) + 1)

        for i, c in enumerate(s):
            last = seen.get(c, -1)
            r[i + 1] = min(r[i] + 1, i - last)
            seen[c] = i

        return max(r)


def run_tests():
    sol = Solution()

    # Test 1
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3

    # Test 2
    assert sol.lengthOfLongestSubstring("bbbbb") == 1

    # Test 3
    assert sol.lengthOfLongestSubstring("pwwkew") == 3

    # Test 4
    assert sol.lengthOfLongestSubstring("aab") == 2

    # Test 5
    assert sol.lengthOfLongestSubstring(" ") == 1

    # Test 6
    assert sol.lengthOfLongestSubstring("au") == 2
    
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
