def getFizzBuzzString(num):
    arr = []
    for i in range(num):
        cur = i + 1
        if ((cur % 15) == 0):
            arr.append('FizzBuzz')
        elif ((cur % 3) == 0):
            arr.append('Fizz')
        elif ((cur % 5) == 0):
            arr.append('Buzz')
        else:
            arr.append(str(i))
    return ''.join(arr)

input = input()
split_input = input.split()

def test(number):
    return (number / 5 + number / 3) * 2
number = int(split_input[0])
if (1 <= number and number <= 10 ** 18):
  print(test(number))
