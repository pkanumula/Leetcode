from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:
        n = len(source)
        INF = 10**18

        # -------- 1) Build per-length graphs over unique strings --------
        # For each length L:
        #   - map string -> node id
        #   - edges u->v with minimal cost
        len_id = defaultdict(dict)          # L -> {string: id}
        nodes_by_len = defaultdict(list)    # L -> [string]
        edge_cost = defaultdict(dict)       # L -> {(u,v): w_min}

        def get_id(L: int, s: str) -> int:
            mp = len_id[L]
            if s in mp:
                return mp[s]
            idx = len(nodes_by_len[L])
            mp[s] = idx
            nodes_by_len[L].append(s)
            return idx

        for o, c, w in zip(original, changed, cost):
            L = len(o)
            u = get_id(L, o)
            v = get_id(L, c)
            key = (u, v)
            prev = edge_cost[L].get(key)
            if prev is None or w < prev:
                edge_cost[L][key] = w

        # -------- 2) All-pairs shortest paths per length (Dijkstra from each node) --------
        dist_by_len = {}  # L -> dist[m][m]
        for L, nodes in nodes_by_len.items():
            m = len(nodes)
            adj = [[] for _ in range(m)]
            for (u, v), w in edge_cost[L].items():
                adj[u].append((v, w))

            dist = [[INF] * m for _ in range(m)]
            for s in range(m):
                dist[s][s] = 0
                pq = [(0, s)]
                while pq:
                    d, u = heappop(pq)
                    if d != dist[s][u]:
                        continue
                    for v, w in adj[u]:
                        nd = d + w
                        if nd < dist[s][v]:
                            dist[s][v] = nd
                            heappush(pq, (nd, v))
            dist_by_len[L] = dist

        # -------- 3) Trie of all graph strings (original + changed, grouped by length IDs) --------
        # Each terminal stores (length, id_in_that_length_graph)
        children = [{}]     # list of dict(char -> next_node)
        terminal = [None]   # list of Optional[(L, id)]

        def trie_insert(s: str, L: int, idx: int) -> None:
            cur = 0
            for ch in s:
                nxt = children[cur].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[cur][ch] = nxt
                    children.append({})
                    terminal.append(None)
                cur = nxt
            terminal[cur] = (L, idx)

        for L, mp in len_id.items():
            for s, idx in mp.items():
                trie_insert(s, L, idx)

        def matches_at(text: str, start: int) -> dict:
            """
            Return dict: end_index -> node_id (for the matched string of length end-start).
            Only includes strings that exist in our graphs (union of originals/changed).
            """
            res = {}
            cur = 0
            j = start
            while j < n:
                ch = text[j]
                nxt = children[cur].get(ch)
                if nxt is None:
                    break
                cur = nxt
                j += 1
                if terminal[cur] is not None:
                    # (L, id) but L == j-start; keep id, length known from indices
                    _, idx = terminal[cur]
                    res[j] = idx
            return res

        # -------- 4) DP over positions (disjoint segments) --------
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] >= INF:
                continue

            # Option: do nothing on this single char if already equal
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]

            # Option: convert a whole segment starting at i using rules
            ms = matches_at(source, i)  # end -> idS
            mt = matches_at(target, i)  # end -> idT
            if not ms or not mt:
                continue

            # Iterate smaller dict for intersection by end index
            if len(ms) <= len(mt):
                items, other, s_is_source = ms.items(), mt, True
            else:
                items, other, s_is_source = mt.items(), ms, False

            for end, idA in items:
                idB = other.get(end)
                if idB is None:
                    continue
                L = end - i
                if L not in dist_by_len:
                    continue
                if s_is_source:
                    u, v = idA, idB
                else:
                    u, v = idB, idA

                seg_cost = dist_by_len[L][u][v]
                if seg_cost < INF:
                    nd = dp[i] + seg_cost
                    if nd < dp[end]:
                        dp[end] = nd

        return -1 if dp[n] >= INF else dp[n]
