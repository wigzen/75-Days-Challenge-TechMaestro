class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count  =collections.Counter(nums)
        #print(len(count.values()))
        return(count.most_common(1)[0][0])
    