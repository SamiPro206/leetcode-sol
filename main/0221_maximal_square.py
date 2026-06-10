"""
Problem: 221 - Maximal Square
Difficulty: Medium

Link:
https://leetcode.com/problems/maximal-square/

Time Complexity:
O(n*m)

Space Complexity:
O(n*m)

Notes:
J'ai voulu reprendre l'exemple du maximum subarray mais sans succès :(
C'est aussi le problème 6 du final 2018
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # m = len(matrix)
        # n = len(matrix[0])

        # def find_max_square_crossing():

        #     return 0
        
        # def find_max_square(matrix, lm, rm, ln, rn):
        #     if lm == rm and ln == rn:
        #         return 1 if matrix[lm][ln] == '1' else 0
        #     if lm < rm or ln < rn:
        #         (mm, mn) = ((lm+rm)//2,(ln+rn)//2) # midpoint
        #         maxTopLeft = find_max_square(matrix, lm, mm, ln, mn)
        #         maxTopRight = find_max_square(matrix, lm, mm, mn+1, rn)
        #         maxBottomLeft = find_max_square(matrix, mm+1, rm, ln, mn)
        #         maxBottomRight = find_max_square(matrix, mm+1, rm, mn+1, rn)
        #         maxCrossing = find_max_square_crossing(matrix, lm, rm, mm, mn, ln, rn)
        #         return max(maxTopLeft, maxTopRight, maxBottomLeft, maxBottomRight, maxCrossing)
        #     else:
        #         return 0
        # return find_max_square(matrix, 0, m-1, 0, n-1)

        m = len(matrix)
        n = len(matrix[0])

        best = 0
        r = [[0] * n for _ in range(m)] # max side size when the square ends (bottom right) at (i, j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        r[i][j] = 1
                    else :
                        r[i][j] = min(
                            r[i-1][j], 
                            r[i][j-1], 
                            r[i-1][j-1]
                        ) + 1
                    best = max(best, r[i][j])
        return best**2


def run_tests():
    sol = Solution()

    # Test 2
    matrix = [["0","1"],["1","0"]]
    r = sol.maximalSquare(matrix)
    assert r == 1

    # Test 1
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    r = sol.maximalSquare(matrix)
    assert r == 4

    # Test 3
    matrix = [["0"]]
    assert sol.maximalSquare(matrix) == 0

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
