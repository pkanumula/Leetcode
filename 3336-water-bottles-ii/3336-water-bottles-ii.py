class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        cost = numExchange
        drunk = 0

        while True:
            # Drink all currently full bottles
            if full > 0:
                drunk += full
                empty += full
                full = 0

            # Try to exchange once at the current cost
            if empty >= cost:
                empty -= cost    # spend empties
                full += 1        # get one new full bottle
                cost += 1        # next exchange is more expensive
            else:
                break

        return drunk
