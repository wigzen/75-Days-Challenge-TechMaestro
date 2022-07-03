from collections import Counter  
class Solution:
    def wordBreak(self, n, dict, s):
        def _help(dic,st,arr,ans):
            if st ==len(s):
                ans.append(arr[:])
            for string in dic:
                if s[st:st+len(string)]==string:
                    arr.append(string)
                    _help(dic,st+len(string),arr,ans)
                    arr.pop()
        ans =[]
        _help(dict,0,[],ans)
        ans=[" ".join(j) for j in ans]
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dict = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dict, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends