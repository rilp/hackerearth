# Problem title: Count Divisors
# URL: https://www.hackerearth.com/problem/algorithm/count-divisors/

l, r, k = map(int, input().split())
n = 0
for x in range(l, r + 1):
    if x % k == 0:
        n += 1

print(n)