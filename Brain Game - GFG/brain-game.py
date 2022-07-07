#User function Template for python3

class Solution:
	def brainGame(self, nums):
		def isprime(n):
		    if n<=1:
		        return 0
		    ans=0
		    div =2
		    while n >1:
		        if n%div ==0:
		            ans+=1
		            n//=div
		        else:
		            div+=1
		    return ans -1
	    arr = [isprime(num) for num in nums]
	    s =0
	    for i in arr:
	        s^=i
	    if s !=0 :
	        return True
	    else:
	        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.brainGame(nums)
		if(ans):
			print("A")
		else:
			print("B")

# } Driver Code Ends