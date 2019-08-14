import math

N = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

Rx = [sorted(X).index(x) for x in X]
Ry = [sorted(Y).index(y) for y in Y]

Dxy = 0
for i in range(N):
    Dxy += ((Rx[i] - Ry[i]) * (Rx[i] - Ry[i]))

spear_rank_corr = 1 - ((6 * Dxy) / (N*(N*N - 1)))

print(round(spear_rank_corr, 3))
