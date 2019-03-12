class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
Solution().merge(nums1,m, nums2, n)
print(nums1)

