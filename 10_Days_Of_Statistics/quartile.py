from statistics import median

n = int(input())
x = list(map(int, input().rstrip().split()))
x.sort()

if n % 2 == 1:
    j = n//2
    x1 = [s for s in x[0:j]]
    x3 = [s for s in x[j+1:n]]

if n % 2 == 0:
    j = n//2
    x1 = [s for s in x[0:j]]
    x3 = [s for s in x[j:n]]

print(int(median(x1)))
print(int(median(x)))
print(int(median(x3)))

