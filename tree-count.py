
l = int(input())
num = int(input())

blockList = list(map(int, input().split()))
blockList = sorted(blockList)

blockCount = 0
blockLen = 0
for i in blockList:
    if (blockLen + i <= l):
        blockLen += i
        blockCount += 1
    else:
        break
print(blockCount)
