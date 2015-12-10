#No.51 http://yukicoder.me/problems/100
import math
w = int(input())
d = int(input())

for i in range(1, d):
    w = w - math.floor(w / (d - i + 1) ** 2)

print(w)
