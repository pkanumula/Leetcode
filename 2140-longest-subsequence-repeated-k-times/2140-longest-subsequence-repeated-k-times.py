import collections

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Finds the longest subsequence repeated k times in a string s.
        """
        n = len(s)
        
        # 1. Identify "hot" characters and their maximum allowed counts in the result.
        freq = collections.Counter(s)
        hot_chars_counts = {c: freq[c] // k for c, count in freq.items() if count >= k}
        
        # If no character appears at least k times, no solution is possible.
        if not hot_chars_counts:
            return ""
        
        # Get hot characters sorted alphabetically to build candidates lexicographically.
        hot_chars = "".join(sorted(hot_chars_counts.keys()))

        # 2. Precompute `next_occurrence` table for fast subsequence checking.
        # next_occ[i][j] = index of char `j` at or after index `i` in `s`.
        # `n` is used as a sentinel for "not found".
        next_occ = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                next_occ[i][j] = next_occ[i+1][j]
            next_occ[i][ord(s[i]) - ord('a')] = i
        
        # 3. BFS to build and check candidate subsequences.
        q = collections.deque([""])
        ans = ""
        
        while q:
            curr = q.popleft()
            
            for char_to_append in hot_chars:
                new_seq = curr + char_to_append
                
                # Pruning step: Check if the character composition is valid.
                if new_seq.count(char_to_append) > hot_chars_counts[char_to_append]:
                    continue
                
                # Check if `new_seq` repeated `k` times is a subsequence of `s`.
                is_valid = True
                s_ptr = 0
                for _ in range(k):
                    for char_in_seq in new_seq:
                        char_code = ord(char_in_seq) - ord('a')
                        s_ptr = next_occ[s_ptr][char_code]
                        if s_ptr == n:
                            is_valid = False
                            break
                        s_ptr += 1 # Move to the next position in `s` for the next character.
                    if not is_valid:
                        break
                
                if is_valid:
                    # Found a valid repeated subsequence. Update the answer and enqueue.
                    ans = new_seq
                    q.append(new_seq)
                    
        return ans