#User function Template for python3
def reaching_height (n, arr) : 
    #Complete the function
    v=[]
    if (n == 1):
        v.append(arr[0]);
        return v;
    arr.sort()
    if (arr[0] == arr[n-1]):
        v.append(-1);
        return v;
    hi = n-1;
    lo = 0;
    is_hi = 1;
    while (lo <= hi):
        if (is_hi):
            v.append(arr[hi]);
            hi-=1;
        else:
            v.append(arr[lo]);
            lo+=1;
        is_hi ^= 1;
    return v;


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = reaching_height(n, arr)
    if(len(ans) == 1 and ans[0] == -1):
        print("Not Possible")
    else:
        print(*ans)
# } Driver Code Ends