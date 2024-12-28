class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  next lexicographically greater permutation of current permutation
        
        # first find the pivot
        n = len(nums)
        pivot_index = -1
        for i in range(n-1,0,-1): # backward traverse
            # find the first element which satisfy this condition
            if nums[i] > nums[i-1]:
                pivot_index = i - 1
                break 

        if pivot_index == -1:
            nums.reverse()
            return 

        # Find the rightmost element greater than nums[pivot_index]
        for i in range(n-1,pivot_index,-1):
            if nums[i] > nums[pivot_index]:
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                break

        # now reverse the list just after the pivot_index
        nums[pivot_index+1:] = nums[pivot_index+1:][::-1]