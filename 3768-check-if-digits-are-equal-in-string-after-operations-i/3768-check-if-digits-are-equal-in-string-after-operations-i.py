class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Continue until only 2 digits remain
        while len(s) > 2:
            new_s = ""
            # For each pair of consecutive digits
            for i in range(len(s) - 1):
                # Compute the sum modulo 10
                new_digit = (int(s[i]) + int(s[i + 1])) % 10
                new_s += str(new_digit)
            s = new_s  # Replace s with the new sequence

        # Return True if the final two digits are the same
        return s[0] == s[1]
