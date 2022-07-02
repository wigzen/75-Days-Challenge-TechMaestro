class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key =lambda x:x[1],reverse=True)
        count =0
        ans =0
        print(boxTypes)
        for i in range(len(boxTypes)):
            count+=boxTypes[i][0]
            if count<=truckSize:
                ans+= boxTypes[i][0]*boxTypes[i][1]
                
                print(boxTypes[i][0])
            else:
                ans+=(truckSize-(count-boxTypes[i][0]))*boxTypes[i][1]
                
                return ans
        return ans