from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(s: str) -> str:
            s = s.lower()
            return ''.join('*' if ch in vowels else ch for ch in s)
        
        # 1) Exact words (case-sensitive)
        exact = set(wordlist)
        
        # 2) Case-insensitive first occurrence
        ci_first = {}
        # 3) Vowel-error tolerant first occurrence
        ve_first = {}
        
        for w in wordlist:
            lw = w.lower()
            dw = devowel(w)
            # only store the first occurrence to respect precedence
            ci_first.setdefault(lw, w)
            ve_first.setdefault(dw, w)
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)  # exact case-sensitive match returns the query itself
                continue
            
            lq = q.lower()
            dq = devowel(q)
            
            if lq in ci_first:
                ans.append(ci_first[lq])
            elif dq in ve_first:
                ans.append(ve_first[dq])
            else:
                ans.append("")
        
        return ans
