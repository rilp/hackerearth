# Problem title: UpUp
# URL: https://www.hackerearth.com/problem/algorithm/upup/

s = input()
prev = ''
for current in s:
    if (prev == '' or prev == ' ') and current != ' ':
        print(current.upper(), end='')
    else:
        print(current, end='')
    prev = current