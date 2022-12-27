# Problem title: Roy and Profile Picture
# URL: https://www.hackerearth.com/problem/algorithm/roy-and-profile-picture/

l = int(input())
n = int(input())
for _ in range(n):
    w, h = map(int, input().split())
    if w < l or h < l:
        print('UPLOAD ANOTHER')
        continue
    elif w != h:
        print('CROP IT')
    else:
        print('ACCEPTED')