# 70.ClimbingStairs.py
# tabulation with memory save
def climbStairs(n):
    one = 1
    two = 1
    for _ in range(n - 1):
        temp = two
        two = one + two
        one = temp
    return two


print(climbStairs(1)) #1
print(climbStairs(2)) #2
print(climbStairs(3)) #3
print(climbStairs(5)) #8
print(climbStairs(50)) #20365011074