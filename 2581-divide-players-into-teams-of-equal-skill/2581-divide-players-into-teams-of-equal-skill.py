class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # Sort the skills to make pairing easier
        skill.sort()

        # Initialize variables
        total_chemistry = 0
        n = len(skill)
        expected_sum = skill[0] + skill[-1]  # the sum that each pair should have

        # Iterate through half the list to form pairs
        for i in range(n // 2):
            # Check if current pair has the correct sum
            if skill[i] + skill[n - 1 - i] != expected_sum:
                return -1  # Return -1 if it's not possible to form valid pairs

            # Add the product of the current pair to the total chemistry
            total_chemistry += skill[i] * skill[n - 1 - i]

        return total_chemistry
