import cProfile
import numpy as np
import bisect
from collections import OrderedDict

class Solution:
    def maxArea(self, height)->  int:#嵌套循环，n^2的时间复杂度，太慢了！
        xis = [(x,i) for x,i in zip(height, range(1, len(height)+1))]
        result = 0
        for x,i in xis:
            for y,j in xis:
                l = j - i if j>i else i-j
                h = min(x,y)
                result = l * h if l*h> result else result
        return result

    def maxArea2(self, height) -> int:#先对数字进行排序，从小打到，依次查找最大的距离
        max_sum = 0
        xis = [(x,i) for x,i in zip(height, range(1, len(height)+1))]
        axis = [i for i in range(1, len(height)+1)]
        xis.sort(key=lambda x:x[0])
        for x,i in xis:
            a = i - axis[0]
            b = axis[len(axis)-1] - i
            temp = x * (a if a>b else b)
            max_sum = temp if max_sum<temp else max_sum
            axis.pop(axis.index(i))
        return max_sum

    def maxArea3(self, height) -> int:#相比第二个方案，使用二分查找有序列表
        max_sum = 0
        xis = [(x,i) for x,i in zip(height, range(1, len(height)+1))]
        axis = [i for i in range(1, len(height)+1)]
        xis.sort(key=lambda x:x[0])
        for x,i in xis:
            a = i - axis[0]
            b = axis[len(axis)-1] - i
            temp = x * (a if a>b else b)
            max_sum = temp if max_sum<temp else max_sum
            axis.pop(bisect.bisect_left(axis, i))
        return max_sum


nums = np.random.randint(100,7895,10000)
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea2([1,8,6,2,5,4,8,3,7]))

#cProfile.run('Solution().maxArea(nums)')

cProfile.run('Solution().maxArea2(nums)')
cProfile.run('Solution().maxArea3(nums)')