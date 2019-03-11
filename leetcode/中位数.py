import bisect
import numpy as np
import cProfile
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        index = 0
        for x in nums2:
            index = bisect.bisect_left(nums1[index:],x)
            nums1.insert(index, x)
        return nums1

nums1 = list(set(np.random.randint(1,1000,1000) ))
nums1.sort()
nums2 = list(set(np.random.randint(50,5000,2000)))
nums2.sort()
cProfile.run('Solution().findMedianSortedArrays(nums1, nums2)')

