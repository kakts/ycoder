#No.207 世界のなんとか
#A以上B以下の整数のうち、3の倍数および3の付く数を、小さい順に出力してください。
#なお、「3の付く数」とは、10進数表記にした時、少なくとも1つの桁が3であるような数のことです。

min, max = map(int, input().split())

for i in range(min, max + 1):
    if i % 3 == 0:
        print(i)
    else:
        #各桁の数値を取り出してリストに入れる
        digits = [int(c) for c in str(i)]
        for digit in digits:
            sum = 0
            if digit == 3:
                print(i)
                break
