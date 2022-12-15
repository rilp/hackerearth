# Problem title: Zoos
# URL: https://www.hackerearth.com/problem/algorithm/is-zoo-f6f309e7

zoo = input() 
z = zoo.count('z')
o = zoo.count('o')

if z * 2 == o and len(zoo) <= 20:
    print('Yes')
else:
    print('No')