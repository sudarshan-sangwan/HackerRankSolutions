# from math import factorial as f

# X = list(map(float, input().rstrip().split()))

# p = X[0]/sum(x for x in X)
# q = X[1]/sum(x for x in X)

# b3 = (f(6)/(f(3)*f(3))) * (p*p*p) * (q*q*q)
# b4 = (f(6)/(f(4)*f(2))) * (p*p*p*p) * (q*q)
# b5 = (f(6)/(f(5)*f(1))) * (p*p*p*p*p) * (q)
# b6 = (f(6)/(f(6)*f(0))) * (p*p*p*p*p*p) * 1

# b = b3+b4+b5+b6

# print(round(b, 3))

from math import factorial, pow

def comb(n, x):
    return (factorial(n) / (factorial(x) * factorial(n-x)))

def bino(n, x, p):
    return comb(n, x) * pow(p, x) * pow(1-p, n-x)

# Input
R = list(map(float, input().rstrip().split()))
p = R[0]/sum(r for r in R)
n = 6
b = 0
for x in range(3,7):
    b += bino(n, x, p)

print(round(b, 3))
