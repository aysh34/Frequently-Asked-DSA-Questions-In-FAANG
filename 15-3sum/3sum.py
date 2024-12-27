class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # as we have to return elements so we can sort the array
        # n1 + n2 + n3 = 0 --->  n2 + n3 = -(n1)
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -(nums[i])

            # simple 2sum apply
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([nums[l], nums[r], nums[i]])

                    # check to avoid duplicates after a potential triplet is found
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1 

                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return triplets
