from math import pow

def geo_dist(n, p):
    return p * pow(1-p, n-1)

# Input
I = list(map(int, input().rstrip().split()))
n = int(input())
p = I[0]/I[1]

# # PROBLEM 1
g = geo_dist(n, p)
print(round(g, 3))

# # PROBLEM 2
q = 1 - p

g = 1 - (q ** n)
print(round(g, 3))
