# Problem title: Selection of Cities
# URL: https://www.hackerearth.com/problem/algorithm/selection-of-cities-2/

tests = int(input())
for _ in range(tests):
    n = int(input())
    modulus = int(1e9+7)
    print(pow(2, n, modulus) -1)