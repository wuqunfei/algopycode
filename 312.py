from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        sum_coins = 0
        for i, v in enumerate(nums):
            left, right = 1, 1
            if i > 0:
                left = nums[i - 1]
            if i + 1 < len(nums):
                right = nums[i + 1]
            gains = left * nums[i] * right
            mm = nums.copy()
            del mm[i]
            rest = self.maxCoins(mm)
            sum_coins = max(sum_coins, rest + gains)
        return sum_coins

    def __init__(self):
        self.nums_list = []
        self.nums_value = []

    def maxCoinsT2D(self, nums: List[int]) -> int:
        if nums in self.nums_value:
            index = self.nums_list.index(nums)
            return self.nums_value[index]
        else:
            sum_coins = 0
            for i, v in enumerate(nums):
                left, right = 1, 1
                if i > 0:
                    left = nums[i - 1]
                if i + 1 < len(nums):
                    right = nums[i + 1]
                gains = left * nums[i] * right
                mm = nums.copy()
                del mm[i]
                rest = self.maxCoinsT2D(mm)
                sum_coins = max(sum_coins, rest + gains)
                self.nums_list.append(mm)
                self.nums_list.append(sum_coins)
            return sum_coins


    def maxCoinDAC(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        @lru_cache
        def dp(left, right):
            # maximum if we burst all nums[left]...nums[right], inclusive
            if right - left < 0:
                return 0
            result = 0
            # find the last burst one in nums[left]...nums[right]
            for i in range(left, right + 1):
                # nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                # nums[i] is fixed, recursively call left side and right side
                remaining = dp(left, i - 1) + dp(i + 1, right)
                # update the result
                result = max(result, remaining + gain)
            return result

        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)


input = [3, 1, 5, 8]

solution = Solution()
x = solution.maxCoins(input)
print(x)
y = solution.maxCoinsT2D(input)
print(y)
z = solution.maxCoinDAC(input)
print(z)
