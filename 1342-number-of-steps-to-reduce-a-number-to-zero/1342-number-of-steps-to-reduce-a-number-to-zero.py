def rec(num,s):
    if num ==0:
        return int(s)
    if num%2==0:
        return rec(num//2, s+1)
    return rec(num-1,s+1)
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return rec(num, 0)