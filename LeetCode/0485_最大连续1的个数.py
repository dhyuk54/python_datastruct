from typing import List
"""
需求:
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

示例1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

示例2:
输入:[1,0,1,1,0,1]
输出:2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        for num in nums:
            if num == 1:
                sum += 1
                ans = max(ans, sum)
            else:
                sum = 0
        return ans


sol = Solution()
result = sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
print("result", result)
