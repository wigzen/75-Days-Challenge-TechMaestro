#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, sum):
        t_count=0
        m =dict()
        for i in range(n):
            if arr[i] not in m:
                m[arr[i]]=1
            else:
                m[arr[i]]+=1
        # print(m)
        for j in range(n):
            b =sum-arr[j]
            if b in m.keys():
                t_count +=m[b]
            if sum-arr[j]==arr[j]:
                t_count-=1

        return t_count//2
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends