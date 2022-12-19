# Problem title: Non-empty subsets
# URL: https://www.hackerearth.com/problem/algorithm/minor-4-41918cb8/

t = int(input())
for x in range(t):
    n = int(input())
    print(min(list(map(int,input().split()))))