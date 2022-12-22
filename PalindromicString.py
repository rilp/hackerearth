# Problem Title: Palindromic String
# URL: https://www.hackerearth.com/problem/algorithm/palindrome-check-2/

in_str = input()
back_str = in_str[::-1]
if in_str == back_str:
    print('YES')
else:
    print ('NO')