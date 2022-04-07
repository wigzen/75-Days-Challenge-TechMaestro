import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min =sys.maxsize
        if len(prices)==0: return 0
        for i in prices:
            if min>i:
                min =i
            elif profit<i-min:
                profit = i-min
        return profit