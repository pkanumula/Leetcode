class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_distances(start: int) -> List[int]:
            dist = [float('inf')] * n
            curr = start
            d = 0
            # Follow the unique outgoing edges until we hit -1 or a visited node
            while curr != -1 and dist[curr] == float('inf'):
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        # Now find the node i minimizing max(dist1[i], dist2[i])
        best_node = -1
        best_dist = float('inf')
        for i in range(n):
            d1, d2 = dist1[i], dist2[i]
            # only consider nodes reachable from both
            if d1 < float('inf') and d2 < float('inf'):
                candidate = max(d1, d2)
                if candidate < best_dist:
                    best_dist = candidate
                    best_node = i
        return best_node
