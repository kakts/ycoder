#No.135 http://yukicoder.me/problems/135

input()
s = set(map(int, input().split()))
if len(s) > 1:
    #昇順にソートする
    s = list(sorted(s))
    #隣あう要素間の差分野中で最小のものを表示
    print("s", s)
    print([s[i] - s[i - 1] for i in range(1, len(s))])
    print(min([s[i] - s[i - 1] for i in range(1, len(s))]))
else:
    print(0)
