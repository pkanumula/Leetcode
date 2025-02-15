class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(sq_str, target, index=0, curr_sum=0):
            if index == len(sq_str):
                return curr_sum == target
            
            num = 0
            for i in range(index, len(sq_str)):
                num = num * 10 + int(sq_str[i])
                if curr_sum + num > target:
                    break
                if can_partition(sq_str, target, i + 1, curr_sum + num):
                    return True
            return False
        
        punishment_sum = 0
        for i in range(1, n + 1):
            sq_str = str(i * i)
            if can_partition(sq_str, i):
                punishment_sum += i * i
        
        return punishment_sum