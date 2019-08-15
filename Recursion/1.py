# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

# Recursive
def tripleStep(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)
print(tripleStep(5))

# Memoized -- > Bottom up Approach
def tripleStep_memo(n):
    if n <= 3:
        return n
    temp = [0]*(n+1)
    temp[0] = 0
    temp[1] = 1
    temp[2] = 2
    temp[3] = 4
    for i in range(4,n+1):
        temp[i] = temp[i-1]+temp[i-2]+temp[i-3]
    return temp[n]
print(tripleStep_memo(5))

# Top Down Approach with memo
memo = {0:0,1:1,2:2,3:4}
def tripleStep_td(n,memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = tripleStep_td(n-1,memo) + tripleStep_td(n-2,memo) + tripleStep_td(n-3,memo)
        return memo[n]
print(tripleStep_td(5,memo))