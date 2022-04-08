class Solution:
    def divide(self, nums1: int, nums2: int) -> int:
            if (nums1 == -2147483648 and nums2 == -1): return 2147483647
            a, b, res = abs(nums1), abs(nums2), 0
            for x in range(32)[::-1]:
                if (a >> x) - b >= 0:
                    res += 1 << x
                    a -= b << x
            return res if (nums1 > 0) == (nums2 > 0) else -res