from typing import List, Dict, Tuple
from collections import deque
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.cap = memoryLimit
        self.q = deque()  # stores (source, destination, timestamp) in FIFO
        self.seen = set()  # for duplicate detection: (s, d, t)
        # per-destination: dest -> {"ts": [timestamps...], "start": int}
        self.dest_index: Dict[int, Dict[str, object]] = {}

    def _ensure_dest(self, destination: int):
        if destination not in self.dest_index:
            self.dest_index[destination] = {"ts": [], "start": 0}

    def _compact_if_needed(self, destination: int):
        """Occasionally compact the per-destination timestamp list to avoid unbounded growth."""
        slot = self.dest_index[destination]
        ts = slot["ts"]
        start = slot["start"]
        # Compact if start is large (amortized constant over time)
        if start > 1024 and start > len(ts) // 2:
            slot["ts"] = ts[start:]
            slot["start"] = 0

    def _remove_oldest(self):
        """Remove the global oldest packet from all structures."""
        if not self.q:
            return
        s, d, t = self.q.popleft()
        self.seen.discard((s, d, t))
        slot = self.dest_index.get(d)
        if slot:
            # Oldest packet for destination must be at current 'start'
            slot["start"] += 1
            self._compact_if_needed(d)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False

        # Evict oldest if at capacity
        if len(self.q) == self.cap:
            self._remove_oldest()

        # Insert new packet
        self.q.append(key)
        self.seen.add(key)

        self._ensure_dest(destination)
        slot = self.dest_index[destination]
        # timestamps are non-decreasing in add queries, so append keeps order
        slot["ts"].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.discard((s, d, t))

        slot = self.dest_index.get(d)
        if slot:
            # remove from the logical front
            slot["start"] += 1
            self._compact_if_needed(d)

        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        slot = self.dest_index.get(destination)
        if not slot:
            return 0
        ts = slot["ts"]
        start_idx = slot["start"]
        # binary search within the active slice [start_idx : ]
        lo = bisect.bisect_left(ts, startTime, lo=start_idx)
        hi = bisect.bisect_right(ts, endTime, lo=start_idx)
        return max(0, hi - lo)
