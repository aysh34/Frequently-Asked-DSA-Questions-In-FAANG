class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                p += 1
            return primes

        prime_table = sieve(right)
        primes = [i for i in range(left, right + 1) if prime_table[i]]

        if len(primes) < 2:
            return [-1, -1]

        res = [-1, -1]
        minDiff = float('inf')

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < minDiff:
                minDiff = diff
                res = [primes[i - 1], primes[i]]

        return res
