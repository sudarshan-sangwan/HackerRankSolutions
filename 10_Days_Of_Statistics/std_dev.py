import math

N = int(input())
X = list(map(int, input().rstrip().split()))

mean = (sum(x for x in X)/N)

dist = 0
for x in X:
    dist += (x - mean) * (x - mean)

sd = math.sqrt(dist/N)

print(round(sd, 1))

