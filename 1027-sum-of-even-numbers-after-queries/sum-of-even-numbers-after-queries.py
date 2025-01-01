class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum(n for n in nums if n % 2 == 0)
        res = []

        for val , idx in queries:
            # sbsy phele tu check kro js no pr query lagane bol rha hai nums mei wo even tu nhi hai
            if nums[idx] % 2 == 0:
                sum_even -= nums[idx]

            # ab query lga do uss no pr
            nums[idx] = nums[idx] + val 

            # ab q k nums update hu gya wo phr se even numbers ka sum nikale gai
            # usk liye bs itna dekho k ye new number ju query k bad bna hai ye even hai k odd

            if nums[idx] % 2 == 0:
                sum_even += nums[idx] # add kr do iss no ko
            
            res.append(sum_even)

        return res