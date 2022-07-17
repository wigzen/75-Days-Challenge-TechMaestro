class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[[1]]
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row =[]
            for j in range(1,len(temp)):
                row.append(temp[j]+temp[j-1])
            res.append(row)
        return res