from typing import List, Dict, Tuple
from collections import defaultdict
import heapq

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # price lookup
        self.price: Dict[Tuple[int, int], int] = {}

        # per-movie heap of available copies: (price, shop)
        self.avail = defaultdict(list)  # movie -> [(price, shop)]
        # track whether a node for (shop, movie) is currently present in avail[movie]
        self.in_avail: Dict[Tuple[int, int], bool] = {}

        # global heap of rented copies with versioning: (price, shop, movie, token)
        self.rented = []
        # whether a (shop, movie) is currently rented
        self.rented_now = set()
        # version token per (shop, movie); increments on every rent
        self.token: Dict[Tuple[int, int], int] = defaultdict(int)

        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            heapq.heappush(self.avail[movie], (p, shop))
            self.in_avail[(shop, movie)] = True

    # --- helpers --------------------------------------------------------------

    def _clean_avail(self, movie: int) -> None:
        """Remove rented copies that bubble to the top (lazy deletion)."""
        h = self.avail[movie]
        while h and ((h[0][1], movie) in self.rented_now):
            p, s = heapq.heappop(h)
            # this node was physically removed
            self.in_avail[(s, movie)] = False

    def _clean_rented(self) -> None:
        """Remove entries that are no longer the active rental (lazy deletion with tokens)."""
        while self.rented:
            p, s, m, t = self.rented[0]
            # valid iff currently rented AND token matches the latest
            if ((s, m) in self.rented_now) and (t == self.token[(s, m)]):
                break
            heapq.heappop(self.rented)

    # --- API ------------------------------------------------------------------

    def search(self, movie: int) -> List[int]:
        res: List[int] = []
        taken: List[Tuple[int, int]] = []
        h = self.avail[movie]

        for _ in range(5):
            self._clean_avail(movie)
            if not h:
                break
            p, s = heapq.heappop(h)  # guaranteed unrented after clean
            res.append(s)
            taken.append((p, s))

        # restore
        for item in taken:
            heapq.heappush(h, item)
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented_now.add((shop, movie))
        self.token[(shop, movie)] += 1
        t = self.token[(shop, movie)]
        p = self.price[(shop, movie)]
        heapq.heappush(self.rented, (p, shop, movie, t))
        # do not touch avail; lazy deletion + in_avail handles it

    def drop(self, shop: int, movie: int) -> None:
        # mark as not rented
        if (shop, movie) in self.rented_now:
            self.rented_now.remove((shop, movie))

        # reinsert into avail only if its node was physically removed earlier
        if not self.in_avail.get((shop, movie), False):
            p = self.price[(shop, movie)]
            heapq.heappush(self.avail[movie], (p, shop))
            self.in_avail[(shop, movie)] = True

    def report(self) -> List[List[int]]:
        res: List[List[int]] = []
        taken: List[Tuple[int, int, int, int]] = []

        while len(res) < 5:
            self._clean_rented()
            if not self.rented:
                break
            p, s, m, t = heapq.heappop(self.rented)
            # after _clean_rented, this is valid
            res.append([s, m])
            taken.append((p, s, m, t))

        for item in taken:
            heapq.heappush(self.rented, item)
        return res
