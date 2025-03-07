class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n < 2:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = []
        for i in range(left, right + 1):
            if is_prime(i):
                primes.append(i)

        res = [-1,-1]
        minDiff = float('inf')
        for i in range(1,len(primes)):
            if primes[i] - primes[i-1] < minDiff:
                minDiff = primes[i] - primes[i-1]
                res[0] = primes[i-1]
                res[1] = primes[i]
        return res 
            

