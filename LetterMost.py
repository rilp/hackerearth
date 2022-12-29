# Problem title: Letter most
# URL: https://www.hackerearth.com/problem/algorithm/letter-most-fb72d803/

n = int(input())
s = input()
counts = [s.count(c) for c in set(s)]
print(max(counts))