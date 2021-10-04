# Implement pow(x, n), which calculates x raised to the power n (i.e., xⁿ). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#  
# 
#  Example 2: 
# 
#  
# Input: x = 2.10000, n = 3
# Output: 9.26100
#  
# 
#  Example 3: 
# 
#  
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2⁻² = 1/2² = 1/4 = 0.25
#  
# 
#  
#  Constraints: 
# 
#  
#  -100.0 < x < 100.0 
#  -2³¹ <= n <= 2³¹-1 
#  -10⁴ <= xⁿ <= 10⁴ 
#  
#  Related Topics Math Recursion 👍 3125 👎 4347


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        return self.half_pow(x, n)

    def half_pow(self, x, n):
        # 1. terminator
        if n == 0:
            return 1.0
        # 2. divide
        data = n // 2
        # 3. conquer
        half = self.half_pow(x, data)
        # 4. combine
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.myPow(2, 4))
