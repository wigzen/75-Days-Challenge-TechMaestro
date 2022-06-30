class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        mini = float("inf")
        profit =0
        for i in range(len(arr)):
            mini =min(mini,arr[i])
            profit =max(profit,arr[i]-mini)
        return profit