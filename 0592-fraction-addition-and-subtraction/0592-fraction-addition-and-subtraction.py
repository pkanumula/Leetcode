import re

class Solution(object):
    def fractionAddition(self, expression):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        numerator, denominator = 0, 1
        
        for fraction in fractions:
            num, den = map(int, fraction.split('/'))
            denominator = lcm(denominator, den)
        
        for fraction in fractions:
            num, den = map(int, fraction.split('/'))
            numerator += num * (denominator // den)
        
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        return "{}/{}".format(numerator, denominator)