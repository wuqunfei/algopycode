from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = list(range(1, N + 1))
        nums.sort(key=lambda x: bin(x)[::-1])
        return nums
