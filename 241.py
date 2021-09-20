from typing import List


class Solution:

    def __init__(self):
        self.ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i, v in enumerate(expression):
            if v in self.ops:
                left_value = self.diffWaysToCompute(expression[:i])
                right_value = self.diffWaysToCompute(expression[i + 1:])
                for left in left_value:
                    for right in right_value:
                        res.append(self.ops[v](left, right))
        if len(res) == 0:
            res.append(int(expression))
        return res


solution = Solution()
value = solution.diffWaysToCompute('2*3-4*5')
print(value)
