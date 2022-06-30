class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        
        for i,n in enumerate(nums):
            w = target-n
            if w in _map:
                return [i,_map[w]]
            if n not in _map :
                _map[n]=i
        
            