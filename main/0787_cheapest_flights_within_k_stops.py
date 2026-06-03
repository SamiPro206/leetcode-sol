"""
Problem: 787 - Cheapest Flights Within K Stops
Difficulty: Medium

Link:
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Time Complexity:
O(Ek) # edges * iterations

Space Complexity:
O(V) # vertices

Notes:
WOW quel exo!
J'ai commencé avec Dijkstra mais trop compliqué, 
Dijkstra optimise une seule dimension (le coût). 
Dès qu'il y a une deuxième contrainte (ici les stops), un vertex peut avoir plusieurs états valides simultanément
Dijkstra ne peut pas les représenter tous.

Alors que Bellman-Ford fait ça naturellement dans sa boucle...
"""


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        dist = {u: float('inf') for u in range(n)}
        dist[src] = 0

        for _ in range(k+1):
            temp = dict(dist)
            for (u, v, w) in flights:
                if temp[v] > dist[u] + w:
                    temp[v] = dist[u] + w
            dist = temp
        
        return -1 if dist[dst] == float('inf') else dist[dst]


def run_tests():
    s = Solution()

    # Test 1
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 700

    # Test 2
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 200

    # Test 3
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    assert s.findCheapestPrice(n, flights, src, dst, k) == 500

    # Test 4
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 6

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
