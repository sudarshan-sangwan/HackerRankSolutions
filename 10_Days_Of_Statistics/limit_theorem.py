import math

w = int(input())
n = int(input())
m = float(input())
s = float(input())

sum_m = n * m
sum_s = math.sqrt(n) * s

def prob_cal(w, m, s):
    Z = (w - m)/s
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(prob_cal(w, sum_m, sum_s), 4))
