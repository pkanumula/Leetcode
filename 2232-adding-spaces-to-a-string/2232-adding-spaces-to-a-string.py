class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        prev = 0
        
        # Iterate over the spaces indices and add substrings and spaces to the result list
        for space in spaces:
            result.append(s[prev:space])
            result.append(' ')
            prev = space
        
        # Add the remaining part of the string after the last space
        result.append(s[prev:])
        
        # Join and return the result
        return ''.join(result)
