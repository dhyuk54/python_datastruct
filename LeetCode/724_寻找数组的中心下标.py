from typing import List

"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            # 先求总和S，然后遍历，记左边的和为L，当前的值为V，如果碰到一个值满足2*L+V==Sum，这个就是中点？
            # 记左边和为L，当前值为V，右边和为R，那有L+V+R=S呗，当L和R相等，不就是2L+V=Sum
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        print(n)
        left_sum = [0] * (n + 1)
        print(left_sum)
        right_sum = [0] * (n + 1)
        print(right_sum)
        for i in range(1, n + 1):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]
            print("left_sum", left_sum)
        for i in range(n - 1, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i]
            print("right_sum", right_sum)

        for i in range(n):
            if left_sum[i] == right_sum[i + 1]:
                return i
        return -1


sol = Solution()
result = sol.pivotIndex([1, 2, 3])
print("result:", result)