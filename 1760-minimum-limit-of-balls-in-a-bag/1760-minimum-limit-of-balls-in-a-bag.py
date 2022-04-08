class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        
        while l < r:
            mid = l + (r-l) // 2
            count = self.count(mid,nums)
            if count <= maxOperations:
                r = mid
            else:
                l = mid+1
        return r
    
    
    def count(self,n,arr):
        return sum((a-1) // n for a in arr)