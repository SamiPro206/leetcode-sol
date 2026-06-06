"""
Problem: 1235 - Maximum Profit in Job Scheduling
Difficulty: Hard

Link:
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

Time Complexity:
O(n log(n))

Space Complexity:
O(n)

Notes:
facile en O(endTime)
mais pour améliorer il faut être astucieux
en prenant les indices endTime par exemple: O(n log(n))
"""


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        n = len(endTime)
        r = [0] * (n + 1)

        # endTime = (real_id, endTime)
        sortedEndTime = sorted(enumerate(endTime), key=lambda x: x[1])

        def searchDicho(startTime_, l=0, r=n): # jobs: endTime <= startTime_
            while l < r:
                s = (l + r + 1) // 2
                if sortedEndTime[s-1][1] <= startTime_:
                    l = s
                else:
                    r = s - 1
            return l
        
        for i, (real_i, _) in enumerate(sortedEndTime):
            # problem: find index: r[j] = max profit before taking job i
            j = searchDicho(startTime[real_i])

            r[i+1] = max(r[j] + profit[real_i], r[i])
        return r[n]


def run_tests():
    s = Solution()

    # Test 1
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    assert s.jobScheduling(startTime, endTime, profit) == 120

    # Test 2
    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    assert s.jobScheduling(startTime, endTime, profit) == 150

    # Test 3
    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]
    assert s.jobScheduling(startTime, endTime, profit) == 6

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
