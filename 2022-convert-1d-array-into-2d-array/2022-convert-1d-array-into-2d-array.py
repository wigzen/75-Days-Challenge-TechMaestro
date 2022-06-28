class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        res= []
        for i in range(m):
            temp =[]
            for j in range(n):
                if original:
                    temp.append(original.pop(0))
            res.append(temp)
        return res