"""
Problem: 329 - Longest Increasing Path in a Matrix
Difficulty: Hard

Link:
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Time Complexity:
O(m * n)

Space Complexity:
O(m * n)

Notes:
"""


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        
        r = [[0] * n for _ in range(m)]
        visited = set()

        def visit(i, j):
            if r[i][j] != 0:
                return
            visited.add((i, j))

            potentialPaths = [(i+dx,j+dy) for (dx,dy) in [(-1,0), (1,0), (0,-1), (0,1)] 
                              if (m > i+dx >= 0 and n > j+dy >= 0) and (matrix[i][j] < matrix[i+dx][j+dy])]
            
            for (u, v) in potentialPaths:
                if not (u, v) in visited:
                    visit(u, v)
                
            r[i][j] = 1 + max([0] + [r[u][v] for (u, v) in potentialPaths])

        for i in range(m):
            for j in range(n):
                if not (i,j) in visited:
                    visit(i, j)

        return max(r[i][j] for i in range(m) for j in range(n))


def run_tests():
    s = Solution()

    # Test 1
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    assert s.longestIncreasingPath(matrix) == 4

    # Test 2
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    assert s.longestIncreasingPath(matrix) == 4

    # Test 3
    matrix = [[1]]
    assert s.longestIncreasingPath(matrix) == 1

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
