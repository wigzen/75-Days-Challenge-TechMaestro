class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        _sum = n*(n+1)/2
        return int(_sum -sum(nums))