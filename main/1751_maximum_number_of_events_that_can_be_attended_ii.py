"""
Problem: 1751 - Maximum Number of Events That Can Be Attended II
Difficulty: Hard

Link:
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

Time Complexity:
O(n*k)

Space Complexity:
O(n)

Notes:
easy mais la difficulté est de trouver j
c'est aussi le problème 6 du final 2020 :)
"""

import bisect

class Solution(object):
    def maxValue(self, events, K):
        """
        :type events: List[List[int]]
        :type K: int
        :rtype: int
        """
        N = len(events)
        curr = [0] * (N + 1)
        prev = [0] * (N + 1)
        events.sort(key=lambda x: x[1])
        ends = [e[1] for e in events]

        for _ in range(1, K+1):
            for i in range(1, N+1):
                startDay, _, value = events[i - 1] # corresponding event
                j = bisect.bisect_left(ends, startDay, 0, i - 1)

                curr[i] = max(
                    prev[j] + value, # take it
                    curr[i-1] # keep it
                )
            prev, curr = curr, prev
        return prev[N]

def run_tests():
    sol = Solution()

    # Test 1
    events = [[1,2,4],[3,4,3],[2,3,1]]
    k = 2
    assert sol.maxValue(events, k) == 7

    # Test 2
    events = [[1,2,4],[3,4,3],[2,3,10]]
    k = 2
    assert sol.maxValue(events, k) == 10

    # Test 3
    events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    k = 3
    assert sol.maxValue(events, k) == 9

    # Test 4
    events = [[69,83,61],[44,90,19],[26,87,9]]
    k = 3
    assert sol.maxValue(events, k) == 61

    # Test 5
    events = [[11,17,56],[24,40,53],[5,62,67],[66,69,84],[56,89,15]]
    k = 2
    assert sol.maxValue(events, k) == 151
    
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
