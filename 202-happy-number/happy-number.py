import math
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_digits(n):
            sum_of_squares = 0  
            while n > 0:
                dig = n % 10
                sum_of_squares += dig ** 2
                n = n // 10
            return sum_of_squares
        
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = sum_of_squares_of_digits(n)
        
        return False


        
        
        