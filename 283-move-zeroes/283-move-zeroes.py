class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        right = 0
        left = 0

        if n==0 or n==1:
            return nums
        
        while right < n:
            if nums[right]==0:
                right+=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
                left+=1
            