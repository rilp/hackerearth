# Problem title: Replace the strings
# URL: https://www.hackerearth.com/problem/algorithm/make-them-equal-ac0bab4a/

tc = int(input())
for x in range(tc):
    n = input()
    s1, s2 = input(), input()
    
    s = set(s1 + s2)
    d1 = { c:s1.count(c) for c in s }
    d2 = { c:s2.count(c) for c in s }

    diff = 0
    for i in s:
        if d1[i] != d2[i]:
            diff += abs( d1[i] - d2[i] )

    if diff > 2:
        print('NO')
    else:
        print('YES')