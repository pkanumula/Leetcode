class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift_effects = [0] * (n + 1)

        # Apply the shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift_effects[start] += 1
                shift_effects[end + 1] -= 1
            else:
                shift_effects[start] -= 1
                shift_effects[end + 1] += 1

        # Compute the net shifts using prefix sum
        for i in range(1, n):
            shift_effects[i] += shift_effects[i - 1]

        # Apply the net shifts to the string
        result = []
        for i in range(n):
            shift = (ord(s[i]) - ord('a') + shift_effects[i]) % 26
            result.append(chr(shift + ord('a')))

        return ''.join(result)
