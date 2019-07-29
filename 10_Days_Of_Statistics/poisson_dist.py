from math import pow, factorial

def poisson_dist(n, m):
    e = 2.71828
    return pow(m, n)*pow(e, -m) / factorial(n)

# # PROBLEM 1
# Input
m = float(input())
n = float(input())

d = poisson_dist(n, m)
print(round(d, 3))


# # PROBLEM 2
# Input
I = list(map(float, input().rstrip().split()))
a = I[0]
b = I[1]

ca = 160 + 40 * (a + pow(a, 2))
cb = 128 + 40 * (b + pow(b, 2))

print(round(ca, 3))
print(round(cb, 3))
