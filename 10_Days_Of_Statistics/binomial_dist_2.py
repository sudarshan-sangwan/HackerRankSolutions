from math import factorial, pow

def comb(n, x):
    return (factorial(n) / (factorial(x) * factorial(n-x)))

def bino(n, x, p):
    return comb(n, x) * pow(p, x) * pow(1-p, n-x)

# Inputs
I = list(map(int, input().rstrip().split()))

n = I[1]
p = I[0]/100
b = 0
 # For no more than 2
for x in range(0,3):
    b += bino(n, x, p)

print(round(b, 3))

# For at least two
b = 1 - bino(n, 0, p) - bino(n, 1, p)

print(round(b, 3))

