# Problem title: Palindromic Numbers
# URL: https://www.hackerearth.com/problem/algorithm/palindromic-numbers-7/

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b+1):
        s = str(i)
        if s == s[::-1]:
            count += 1
    print(count)