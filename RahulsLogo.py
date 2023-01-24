# Problme title: Rahul's Logo
# URL: https://www.hackerearth.com/problem/algorithm/rahuls-logo/

def print_line(symbol, n):
    for j in range(n):
        if j % 2 == 0:
            print(symbol, end='')
        else:
            print(' ', end='')
    return


n = int(3)

for i in range(n):
    print( ' '*(n-i-1), end='' )
    print_line('/', i + 1)

    if i % 2 != 0:
        print(' ', end='')
    print_line('\\', i + 1)
    print()

for i in range(n,0,-1):
    print( ' '*(n-i+2), end='' )
    print_line('\\', i)

    if i % 2 == 0:
        print(' ', end='')
    print_line('/', i)
    print()


n += 1
for i in range(n):
    print( ' '*(n-i-1), end='' )
    print_line('/', i + 1)

    if i % 2 != 0:
        print(' ', end='')
    print_line('\\', i + 1)
    print()

for i in range(n,0,-1):
    print( ' '*(n-i+2), end='' )
    print_line('\\', i)

    if i % 2 == 0:
        print(' ', end='')
    print_line('/', i)
    print()