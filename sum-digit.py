#No.289 数字をすべて足そう
#文字列SSが与えられるので, その中のそれぞれの数字を1桁の数値とみなして, 全ての合計値を求めてください.
#例えば1test23という文字列の数字の合計値は1+2+3=61+2+3=6となる.
#http://yukicoder.me/problems/783

text = input()

sum = 0
for i in text:
    if i.isdigit():
        sum = sum + int(i)

print(sum)
