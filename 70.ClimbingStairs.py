# 70.ClimbingStairs.py
# tabulation
def climbStairs(n):
    tab = [None for _ in range(n + 1)]
    tab[0] = 1
    tab[1] = 1
    #tab[2] = 2
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[n]


print(climbStairs(1)) #1
print(climbStairs(2)) #2
print(climbStairs(3)) #3
print(climbStairs(5)) #8
print(climbStairs(50)) #20365011074