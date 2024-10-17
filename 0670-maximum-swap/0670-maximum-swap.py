class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert the number to a list of characters (digits)
        num_list = list(str(num))
        
        # Create a last occurrence dictionary to store the last index of each digit
        last = {int(x): i for i, x in enumerate(num_list)}
        
        # Traverse the list of digits
        for i, x in enumerate(num_list):
            # Check digits from 9 down to current digit + 1 to find a larger digit for swapping
            for d in range(9, int(x), -1):
                # If a larger digit exists later in the number, swap and return result
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int("".join(num_list))
        
        # If no swap was done, return the original number
        return num
