import math

C = 10551408

s = 0

for i in range(1, int(math.sqrt(C)) + 1):
    if C % i == 0:
        s += i + C // i
print(s)
