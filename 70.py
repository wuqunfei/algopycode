class Solution:
    ### Time Compliticy O(n)
    ### Space Compliticy O(n)
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        states = [1, 1] + [0] * (n + 1)
        for i in range(2, n + 1):
            states[i] = states[i - 1] + states[i - 2]
        return states[n]

    def climbSimple(self, n: int) -> int:
        if n <= 2:
            return n
        pre_previous_step, previous_step = 1, 2
        current = None
        for i in range(2, n + 1):
            current = pre_previous_step + previous_step
            pre_previous_step = previous_step
            previous_step = current
        return current


solution = Solution()
x = solution.climbStairs(5)
print(x)
y = solution.climbSimple(5)
print(x)
