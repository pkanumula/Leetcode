class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Combine names and heights into a list of tuples
        people = list(zip(heights, names))
        # Sort the list of tuples by height in descending order
        people.sort(reverse=True, key=lambda x: x[0])
        # Extract and return the names from the sorted list of tuples
        return [name for height, name in people]
