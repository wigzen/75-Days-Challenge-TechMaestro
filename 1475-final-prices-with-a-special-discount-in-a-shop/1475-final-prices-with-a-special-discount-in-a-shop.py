class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = []
        for i in range(len(prices)):
            item = prices[i]
            for j in range(i+1, len(prices)):
                # discount =0                    
                print(j,prices[j])
                if prices[j]<=item:
                    # print(j,prices[j])
                    item -= prices[j]
                    break
            arr.append(item)
        return arr