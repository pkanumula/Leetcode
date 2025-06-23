class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def to_base_k(num: int, k: int) -> str:
            if num == 0:
                return "0"
            result = []
            while num > 0:
                result.append(str(num % k))
                num //= k
            return ''.join(reversed(result))

        def generate_palindromes():
            # Generate palindromes with even and odd lengths
            length = 1
            while True:
                # Odd length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # odd-length
                # Even length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])    # even-length
                length += 1

        count = 0
        total = 0
        for num in generate_palindromes():
            base_k = to_base_k(num, k)
            if is_palindrome(base_k):
                total += num
                count += 1
                if count == n:
                    break
        return total
