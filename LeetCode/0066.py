from typing import List
"""
需求:
给定一个由整数数组成的非空数组所表示的非负整数，在该数的基础上加一
最高位数字存放在数组的首位,数组中的每个元素只存储单个数字
你可以假设除了整数 0 之外，这个整数不会以零开

示例1:
输入: digits = [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例2:
输入: digits = [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

示例3:
输入: digits = [0]
输出: [1]
解释: 输入数组表示数字 0。

示例4:
输入: digits = [-1]
输出: [0]
解释: 输入数组表示数字 -1。

示例5:
输入: digits = [9]
输出: [1,0]
解释: 输入数组表示数字 9。

提示:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        print(len(digits)) # 2
        print(digits)  # [0, 9]
        digits[len(digits) - 1] += 1
        print(digits)  # 0 10
        for i in range(len(digits) - 1, 0, -1):

            print(i)  # 1
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                print(digits)
                digits[i - 1] += 1
                print(digits)

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits


solution = Solution()
result = solution.plusOne([-1])
print(f"result: {result}")


