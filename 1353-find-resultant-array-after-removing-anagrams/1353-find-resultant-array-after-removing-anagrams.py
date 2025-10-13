from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        last_sig = None  # signature (sorted letters) of the last kept word
        
        for w in words:
            sig = ''.join(sorted(w))
            if sig != last_sig:
                res.append(w)
                last_sig = sig
            # else: same signature as previous kept word → skip (delete)
        
        return res
