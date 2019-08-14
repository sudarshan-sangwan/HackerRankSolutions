s = float(input())
m = float(input())
sd = float(input())
iv = float(input())
z = float (input())

sd_s = sd / (s**0.5)
print(round(m - sd_s*z, 2))
print(round(m + sd_s*z, 2))

