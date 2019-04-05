import sys


def fun(x,y):
    if x<y:
        x,y=y,x
    d=x%y
    while d>0:
        x,y=y,d
        d=x%y
    return y

def getF(n):
    factors = []
    prime = int(2)
    if n == prime:
        factors.append(prime)
    else:
        while (n >= prime):
            k = n % prime
            if (k == 0):
                factors.append(prime)
                n = n / prime
            else:
                prime = prime + 1
    return factors

def solution(n, nums):
    num_factors = {}
    count = 0
    for num in nums:
        num_factors[num] = set(getF(num))
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if len(num_factors[nums[i]] | num_factors[nums[j]]) == len(num_factors[nums[i]]) + len(num_factors[nums[j]])\
                        or len(num_factors[nums[i]] | num_factors[nums[k]]) == len(num_factors[nums[i]]) + len(num_factors[nums[k]])\
                        or len(num_factors[nums[j]] | num_factors[nums[k]]) == len(num_factors[nums[j]]) + len(num_factors[nums[k]]):
                    #print(nums[i], nums[j], nums[k])
                    count += 1
    return count

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
print(solution(n, nums))

org_str = ''
res = ''
for c in org_str:
    res =