class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # You always drink the initial bottles
        total_drunk = numBottles
        empty = numBottles
        
        # Keep exchanging while you have enough empty bottles
        while empty >= numExchange:
            # Number of new bottles you can get
            new_full = empty // numExchange
            total_drunk += new_full
            
            # Update empty bottles after drinking the new ones
            empty = empty % numExchange + new_full
        
        return total_drunk
