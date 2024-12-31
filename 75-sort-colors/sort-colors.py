class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ''' simple but tricky solution '''

        i = 0           # denotes 0
        j = 0           # denotes 1
        k = len(nums) - 1 # denotes 2

        while (j<=k):
            if nums[j] == 2:
                nums[k],nums[j] = nums[j],nums[k]
                k -= 1
            elif nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1 # bcz j and i both started at 0
            else:
                j += 1







