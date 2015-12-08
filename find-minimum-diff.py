#No.135 http://yukicoder.me/problems/135
#不完全な回答　正式な回答はfind-minimum-diff2.py
n = int(input())

numList = list(map(int, input().split()))
numList = sorted(numList)
ret = None
for i in range(n):
    val = 0
    if (i == n - 1):
        break
    print(numList[i])
    print(numList[i + 1])
    val = abs(numList[i] - numList[i + 1])
    if i == 0:
        ret = val
        continue
    elif (val == 0):
        continue
    elif (ret > val):
        print("changed")
        print(i)
        print(val)
        ret = val

if ret == None:
    ret = 0

print(ret)
