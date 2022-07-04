#User function Template for python3

class Solution:
    def minVal(self, a, b):
        #code here
        bitsA=bin(a).replace("0b","")
        bitsB=bin(b).replace("0b","")
        b1 =bitsB.count('1')
        a1 =bitsA.count('1')
        diff =abs(a1-b1)
        if diff ==0:return a
        elif a1>b1:
            while diff>0:
                a= a&(a-1)
                diff-=1
        else:
            while diff>0:
                a= a | (a+1)
                diff-=1
        return a
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends