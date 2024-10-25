class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders in lexicographical order
        folder.sort()
        result = []
        
        # Iterate through the sorted list
        for f in folder:
            # If the list is empty or the current folder is not a sub-folder
            # of the last folder added to the result, add it to the result
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result
