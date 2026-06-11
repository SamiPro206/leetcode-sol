"""
Problem: 14 - Longest Common Prefix
Difficulty: Easy

Link:
https://leetcode.com/problems/longest-common-prefix/

Time Complexity:
O(# strings x # length of first string)

Space Complexity:
O(strings)

Notes:
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix = prefix[:-1]
        return prefix


def run_tests():
    sol = Solution()

    # Test 1
    strs = ["flower","flow","flight"]
    assert sol.longestCommonPrefix(strs) == "fl"

    # Test 2
    strs = ["dog","racecar","car"]
    assert sol.longestCommonPrefix(strs) == ""

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
