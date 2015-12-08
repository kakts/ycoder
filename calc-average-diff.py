#No.21 平均の差

#数字の個数
n = int(input())
k = int(input())

list = []
for i in range(2, n + 2):
    list.append(int(input()))

list = sorted(list)
print(abs(list[0] - list[len(list) - 1]))
