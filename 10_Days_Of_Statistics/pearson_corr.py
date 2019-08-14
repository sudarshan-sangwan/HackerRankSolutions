import math

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mean_x = (sum(x for x in X)/N)
mean_y = (sum(y for y in Y)/N)
print(mean_x, mean_y)

dist_x = 0
for x in X:
    dist_x += (x - mean_x) * (x - mean_x)
sd_x = math.sqrt(dist_x/N)

dist_y = 0
for y in Y:
    dist_y += (y - mean_y) * (y - mean_y)
sd_y = math.sqrt(dist_y/N)

print(sd_x, sd_y)

Sxy = 0
for i in range(N):
    Sxy += ((X[i] - mean_x)*(Y[i] - mean_y))

pear_corr = Sxy/(N * sd_x * sd_y)

print(round(pear_corr, 3))
