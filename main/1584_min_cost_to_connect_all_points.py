"""
Problem: 1584 - Min Cost to Connect All Points
Difficulty: Medium

Link:
https://leetcode.com/problems/min-cost-to-connect-all-points/

Time Complexity:
O(n²log(n²)) = O(n²log(n))

Space Complexity:
O(n²)

Notes:
askip prim est mieux mais compliqué en python
"""


class Solution(object):
    def distance(self, a, b):
        assert len(a) == 2 and len(b) == 2
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cost = 0
        parent = {v : v for v in range(len(points))} # (vertex, parent)
                 
        def find(u):
            while u != parent[u]:
                u = parent[u]
            return u
        
        def union(u, v):
            parent[find(v)] = find(u)

        # get edges
        G_E = [] # (i, j, distance from point i to point j)
        for i in range(len(points)):
            for j in range (i+1, len(points)):
                G_E.append(
                    (i, j, self.distance(points[i], points[j]))
                )

        # sort in decreasing order
        G_E.sort(key=lambda e: e[2])

        for (i, j, w) in G_E:
            if find(i) != find(j):
                cost += w
                union(i, j)

        return cost

def run_tests():
    s = Solution()

    # Test 1
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert s.minCostConnectPoints(points) == 20

    # Test 2
    points = [[3,12],[-2,5],[-4,1]]
    assert s.minCostConnectPoints(points) == 18

    # Test 3
    points = [[0,0],[1,1],[1,0],[-1,1]]
    assert s.minCostConnectPoints(points) == 4

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
