# Problem title: Excursion
# URL: https://www.hackerearth.com/problem/algorithm/excursion-2d080f3a/

from math import ceil

t = int(input())
for _ in range(t):
    boys, girls, capacity = map(int, input().split())
    print( ceil( boys/capacity ) + ceil( girls/capacity ))