#No.275 http://yukicoder.me/problems/746
import math
n = int(input())
#入力値を昇順ソートする
numList = sorted(list(map(int, input().split())))

length = len(numList)
if length % 2 == 0:
    #偶数の場合は、中央に近い2値の平均
    low = math.floor(length / 2) - 1
    high = low + 1
    mid = (numList[low] + numList[high]) / 2
else:
    #配列の中央の値を取得
    mid = (numList[math.ceil(length / 2) - 1])
print(mid)
