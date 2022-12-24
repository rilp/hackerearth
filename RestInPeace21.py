# Problem title: Rest in peace - 21-1!
# URL: https://www.hackerearth.com/problem/algorithm/rest-in-peace-21-1/

n = int(input())
for i in range(n):
    l = input()
    if l.find('21') != -1 or eval(l) % 21 == 0:
        print('The streak is broken!')
        continue
    print('The streak lives still in our heart!')