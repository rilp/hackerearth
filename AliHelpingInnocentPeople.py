# Problem title: Ali and Helping innocent people
# URL: https://www.hackerearth.com/problem/algorithm/cartag-948c2b02/

import sys

tag = input()
vowels = ['A','E','I','O','U','Y']
if tag[2] in vowels:
    print('invalid')
    sys.exit()
    
tests = [(0,1),(3,4),(4,5),(7,8)]
for test in tests:
    if (int(tag[test[0]]) + int(tag[test[1]])) % 2 == 1:
        print('invalid')
        sys.exit()
print('valid')