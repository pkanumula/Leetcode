MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.seq = []       # stores normalized values
        self.add = 0        # global additive offset
        self.mult = 1       # global multiplicative factor

    def append(self, val: int) -> None:
        # Normalize val so that: stored * mult + add ≡ val (mod MOD)
        # stored = (val - add) * modInverse(mult)
        normalized = (val - self.add) * pow(self.mult, MOD - 2, MOD) % MOD
        self.seq.append(normalized)

    def addAll(self, inc: int) -> None:
        # true_val = v*mult + (add+inc)
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        # true_val = v*(mult*m) + (add*m)
        self.mult = self.mult * m % MOD
        self.add  = self.add  * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % MOD