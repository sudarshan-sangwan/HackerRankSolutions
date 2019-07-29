from statistics import median

n = int(input())
x = list(map(int, input().rstrip().split()))
f = list(map(int, input().rstrip().split()))

s = []
for r in range(n):
    for j in range(f[r]):
        s.append(x[r])

s.sort()

if len(s) % 2 == 1:
    j = len(s)//2
    s1 = [a for a in s[0:j]]
    s3 = [a for a in s[j+1:len(s)]]

if len(s) % 2 == 0:
    j = len(s)//2
    s1 = [a for a in s[0:j]]
    s3 = [a for a in s[j:len(s)]]

Q1 = median(s1)
Q3 = median(s3)

print(float(round(Q3-Q1, 1)))

