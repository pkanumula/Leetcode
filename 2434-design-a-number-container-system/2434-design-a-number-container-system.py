import collections
import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_min_heap = collections.defaultdict(list)  # Maps number -> min-heap of indices
        self.valid_entries = collections.defaultdict(set)  # Tracks valid index entries for each number

    def change(self, index: int, number: int) -> None:
        # If the index already has a number, update it
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number == number:
                return  # No need to do anything if the number remains the same
            # Remove the old entry from valid_entries
            self.valid_entries[old_number].discard(index)

        # Update the index with the new number
        self.index_to_number[index] = number
        # Add the index to the new number's heap and mark it as valid
        heapq.heappush(self.number_to_min_heap[number], index)
        self.valid_entries[number].add(index)

    def find(self, number: int) -> int:
        # If the number has no valid indices, return -1
        if number not in self.number_to_min_heap:
            return -1

        # Clean up invalid entries at the top of the heap
        while self.number_to_min_heap[number]:
            smallest_index = self.number_to_min_heap[number][0]
            if smallest_index not in self.valid_entries[number]:
                heapq.heappop(self.number_to_min_heap[number])  # Remove stale entry
            else:
                return smallest_index

        return -1
