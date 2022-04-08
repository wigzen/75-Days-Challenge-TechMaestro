class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end =len(nums)-1
        res =[0]*len(nums)
        index =len(nums)-1
        while index>=0:
            if abs(nums[start]) >abs(nums[end]):
                res[index] = nums[start]**2
                start+=1
                index-=1
            else:
                res[index]=nums[end]**2
                end-=1
                index-=1
        return res
            
            