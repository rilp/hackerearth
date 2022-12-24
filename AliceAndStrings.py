# Problem title: Alice and Strings
# URL: https://www.hackerearth.com/problem/algorithm/aliceandstrings-9da62aa7/

a = input()
b = input()

if (len(a)==len(b)):
    for i in range(len(a)):
        if (a[i] > b[i]):
            print('NO')
            break
    else:
        print('YES')
else:
      print('NO')