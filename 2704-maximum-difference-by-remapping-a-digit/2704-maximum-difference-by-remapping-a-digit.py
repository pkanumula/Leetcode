class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Generate maximum value
        max_val = num
        for d in set(num_str):
            if d != '9':
                replaced = int(num_str.replace(d, '9'))
                max_val = max(max_val, replaced)
        
        # Generate minimum value
        min_val = num
        for d in set(num_str):
            if d != '0':
                replaced = int(num_str.replace(d, '0'))
                min_val = min(min_val, replaced)
        
        return max_val - min_val
