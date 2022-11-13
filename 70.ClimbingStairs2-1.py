# 70.ClimbingStairs.py
# memoization
def climbStairs(n):
    def helper(n, memo = None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]
    return helper(n)


print(climbStairs(1)) #1
print(climbStairs(2)) #2
print(climbStairs(3)) #3
print(climbStairs(5)) #8
print(climbStairs(50)) #20365011074