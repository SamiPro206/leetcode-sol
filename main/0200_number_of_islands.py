"""
Problem: 200 - Number of Islands
Difficulty: Medium

Link:
https://leetcode.com/problems/number-of-islands/

Time Complexity:
O(m*n)

Space Complexity:
O(m*n)

Notes:
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])


        def getAdj(i, j):
            return [(i+x, j+y) for (x, y) in [(-1,0), (0,-1), (1,0), (0,1)] if 0 <= (i+x) < m and 0 <= (j+y) < n]
        
        unique = 0
        
        def visit(i, j):
            grid[i][j] = "0"
            for (u, v) in getAdj(i, j):
                if grid[u][v] == "1":
                    visit(u, v)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    unique += 1
                    visit(i, j)

        return unique


def run_tests():
    sol = Solution()

    # Test 1
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert sol.numIslands(grid) == 1

    # Test 2
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    assert sol.numIslands(grid) == 3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
