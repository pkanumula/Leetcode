from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def generate_happy_strings(n, chars):
            happy_strings = []
            
            def backtrack(curr):
                if len(curr) == n:
                    happy_strings.append(curr)
                    return
                for ch in chars:
                    if not curr or curr[-1] != ch:
                        backtrack(curr + ch)
            
            backtrack("")
            return happy_strings
        
        happy_strings = generate_happy_strings(n, "abc")
        return happy_strings[k - 1] if k <= len(happy_strings) else ""
