
import itertools

#构建一个数组，行数如果是4行，那么这个数组应该是：[1,2,3,4,3,2], 未来每一个字符，对应一个行数，行数序列为1,2,3,4,3,2,1,2,3.。。
def lineNum_gen(n):
    lineNums = [x for x in range(1,n+1)]
    mid_Nums = lineNums[1:-1]
    mid_Nums.reverse()
    lineNums = lineNums + mid_Nums
    while True:
        yield lineNums[0]
        x = lineNums.pop(0)
        lineNums.append(x)

g = itertools.islice(lineNum_gen(4), 10)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        gen = itertools.islice(lineNum_gen(numRows), len(s))
        chars_lineNum = [(c, n) for c,n in zip(s, gen)]
        result = []
        for i in range(1, numRows+1):
            result += [char for char,n in chars_lineNum if n == i]
        return ''.join(result)


print(Solution().convert('LEETCODEISHIRING', 3))
