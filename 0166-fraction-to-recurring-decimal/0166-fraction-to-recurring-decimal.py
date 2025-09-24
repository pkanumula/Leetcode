class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        n, d = abs(numerator), abs(denominator)

        # Integer part
        res.append(str(n // d))
        rem = n % d
        if rem == 0:
            return "".join(res)

        # Fractional part
        res.append(".")
        seen = {}  # remainder -> index in res where its digit starts

        while rem != 0:
            if rem in seen:
                # Insert '(' at the first occurrence and append ')'
                insert_at = seen[rem]
                res.insert(insert_at, "(")
                res.append(")")
                break

            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return "".join(res)
