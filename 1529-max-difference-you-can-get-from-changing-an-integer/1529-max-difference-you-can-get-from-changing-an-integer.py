class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Try all digits x in num to replace with 9 (maximize)
        max_num = num
        for x in set(s):
            if x != '9':
                a = int(s.replace(x, '9'))
                max_num = max(max_num, a)
        
        # Try all digits x in num to replace with smallest digit (minimize)
        min_num = num
        for x in set(s):
            for y in '0123456789':
                if x != y:
                    b_str = s.replace(x, y)
                    if b_str[0] != '0':  # no leading zeros
                        b = int(b_str)
                        min_num = min(min_num, b)
        
        return max_num - min_num
