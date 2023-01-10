# Problem title: A Special Number
# URL: https://www.hackerearth.com/problem/algorithm/special-number-9-a0cda359/

t = int(input())
for _ in range(t):
    num = input()
    for i in range(eval(num), 10**4 ):
        nums = sum(map(int, list(str(i))))
        if nums % 4 == 0:
            print(i)
            break