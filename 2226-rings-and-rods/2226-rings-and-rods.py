class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        # Dictionary to keep track of colors on each rod
        rods = {}

        # Loop through the string two characters at a time
        for i in range(0, len(rings), 2):
            color = rings[i]    # Color of the ring ('R', 'G', 'B')
            rod = rings[i+1]    # Rod number ('0' to '9')

            # If the rod isn't in the dictionary, add it with an empty set
            if rod not in rods:
                rods[rod] = set()

            # Add the color to the set for the rod
            rods[rod].add(color)

        # Count the number of rods that have all three colors
        count = 0
        for colors in rods.values():
            if len(colors) == 3:
                count += 1

        return count
