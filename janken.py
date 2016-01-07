#No.264 じゃんけん
#自分と相手がじゃんけんをする。
#じゃんけんの結果を標準出力に出力してください。
#結果は、自分が勝ったら「Won」、自分が負けたら「Lost」、引き分けなら「Drew」を出力してください。
#ぐー　ちょき　ぱー　をそれぞれ　0 1 2とする

numlist = list(map(int, input().split()))
mine = numlist[0]
enemy = numlist[1]
if mine == enemy:
    print('Drew')
elif enemy == (mine + 1) % 3:
    print('Won')
else:
    print('Lost')
