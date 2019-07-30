from math import erf

X = list(map(float, input().split()))
Y = float(input())
Z = float(input())
mn, sd = X[0], X[1]

cdf = lambda x: 0.5 * (1 + erf((x - mn) / (sd * (2 ** 0.5))))

# Greater than 80
print(round((1-cdf(80))*100, 2))

# Passed (>60)
print(round((1-cdf(60))*100, 2))

# Failed (<60)
print(round((cdf(60))*100, 2))
