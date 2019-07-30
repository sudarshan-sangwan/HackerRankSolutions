from math import erf

X = list(map(float, input().split()))
Y = float(input())
Z = list(map(float, input().split()))
mn, sd = X[0], X[1]
lr, ur = Z[0], Z[1]

cdf = lambda x: 0.5 * (1 + erf((x - mn) / (sd * (2 ** 0.5))))

# Less than 19.5
print(round(cdf(Y), 3))

# Between 20 and 22
print(round((cdf(ur) - cdf(lr)), 3))
