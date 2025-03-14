class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0
        def can_give_candies(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k

        res = 0
        l = 1
        r = max(candies)
        while l <= r :
            mid = (l+r) // 2
            if can_give_candies(mid):
                res = mid
                l = mid + 1 # look for more larger number
            else:
                r = mid - 1
        return res
            
        # max_candies = 0
        # for target in range(1, max(candies) + 1):
        #     count = 0
        #     # Count how many children can get at least `target` candies
        #     for candy in candies:
        #         count += candy // target            
        #     if count >= k:
        #         max_candies = target

        # return max_candies