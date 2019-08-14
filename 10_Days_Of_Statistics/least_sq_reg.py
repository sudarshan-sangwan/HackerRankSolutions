import math

s1 = list(map(float, input().split()))
s2 = list(map(float, input().split()))
s3 = list(map(float, input().split()))
s4 = list(map(float, input().split()))
s5 = list(map(float, input().split()))

X = [s1[0], s2[0], s3[0], s4[0], s5[0]]
Y = [s1[1], s2[1], s3[1], s4[1], s5[1]]

N = len(X)

mean_x = (sum(x for x in X)/N)
mean_y = (sum(y for y in Y)/N)

sigm_xy = 0
sigma_x = 0
sigm_xx = 0
sigma_y = 0
for i in range(N):
    sigm_xy += (X[i] * Y[i])
    sigma_x += X[i]
    sigm_xx += (X[i] * X[i])
    sigma_y += Y[i]

b = ((N * sigm_xy) - (sigma_x * sigma_y)) / ((N * sigm_xx) - (sigma_x * sigma_x))

a = mean_y - (b * mean_x)

x  = 80

y = a + (b * x)

print(round(y, 3))
