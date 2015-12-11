#No.56 http://yukicoder.me/problems/111
import math
data = list(map(int, input().split()))
d = data[0]
p = data[1]
print(math.floor(d * (100 + p) / 100))
