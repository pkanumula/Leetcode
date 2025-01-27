from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize a reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Set direct prerequisites as reachable
        for a, b in prerequisites:
            reachable[a][b] = True

        # Apply Floyd-Warshall algorithm to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True

        # Answer each query based on the reachability matrix
        return [reachable[u][v] for u, v in queries]