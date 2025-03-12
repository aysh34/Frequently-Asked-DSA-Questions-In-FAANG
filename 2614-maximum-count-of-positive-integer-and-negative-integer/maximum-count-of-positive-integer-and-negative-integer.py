class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        def first_pos():
            l = 0
            r = n 
            while l < r:
                m = (l + r) // 2
                if nums[m] > 0:
                    r = m
                else:
                    l = m + 1
            return l

        def first_zero():
            l = 0
            r = n 
            while l < r:
                m = (l + r) // 2
                if nums[m] >= 0:
                    r = m
                else:
                    l = m + 1
            return l

        neg_count = first_zero()
        pos_count = n - first_pos()
        return max(neg_count,pos_count)


        # mx = float('-inf')
        # pos = 0
        # neg = 0

        # for i in nums:
        #     if i < 0:
        #         neg += 1
        #     if i > 0:
        #         pos += 1

        #     mx = max(pos,neg)
        # return mx
