"""
Problem: 207 - Course Schedule
Difficulty: Medium

Link:
https://leetcode.com/problems/course-schedule/

Time Complexity:
O(numCourses * |prerequisites|)

Space Complexity:
O(numCourses * |prerequisites|)

Notes:
cycle detection using dfs states (WHITE, GRAY, BLACK)
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        states = {}

        edges = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            edges[a].append(b)

        def visit(u):
            states[u] = 1
            for v in edges[u]:
                if v in states and states[v] == 1:
                    return False
                if not v in states:
                    if not visit(v):
                        return False
            states[u] = 2
            return True
                

        for u in range(numCourses):
            if not u in states:
                if not visit(u):
                    return False

        return True


def run_tests():
    sol = Solution()

    # Test 1
    numCourses = 2
    prerequisites = [[1,0]]
    assert sol.canFinish(numCourses, prerequisites) == True

    # Test 2
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    assert sol.canFinish(numCourses, prerequisites) == False

    # Test 3
    numCourses = 5
    prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    assert sol.canFinish(numCourses, prerequisites) == True

    # Test 4
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    assert sol.canFinish(numCourses, prerequisites) == False

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
