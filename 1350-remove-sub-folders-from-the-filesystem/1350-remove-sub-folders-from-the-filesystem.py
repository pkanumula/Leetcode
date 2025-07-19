from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 1. Sort lexicographically so parents come before sub-folders
        folder.sort()
        ans = []
        prev = ""
        
        # 2. Scan sorted list
        for f in folder:
            # If `f` is a sub-folder of `prev`, skip it
            if prev and f.startswith(prev) and f[len(prev)] == '/':
                continue
            # Otherwise, accept `f` as a top-level folder
            ans.append(f)
            prev = f
        
        return ans
