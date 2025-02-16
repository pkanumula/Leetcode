from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)
        
        def backtrack(index: int) -> bool:
            if index == length:
                return True
            if result[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    result[index] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[num] = False
                else:
                    if index + num < length and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        result[index] = result[index + num] = 0
                        used[num] = False
            return False
        
        backtrack(0)
        return result
