class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        n = len(operations)
        max_k = k
        lengths = [1] * (n + 1)

        # Step 1: compute lengths after each operation
        for i in range(n):
            lengths[i + 1] = min(max_k, lengths[i] * 2)

        # Step 2: Work backwards to find the source of character at position k
        shifts = 0
        for i in reversed(range(n)):
            if k > lengths[i]:
                # The character came from the second half
                if operations[i] == 1:
                    shifts += 1
                # Either way, move k to its corresponding position in the first half
                k -= lengths[i]
            # else: k is in the first half → do nothing

        # Step 3: After all tracing, the character is originally 'a', apply shifts
        ch = (ord('a') - ord('a') + shifts) % 26
        return chr(ord('a') + ch)
