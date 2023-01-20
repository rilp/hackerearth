# Problem title: Palindromic Cipher
# URL: https://www.hackerearth.com/problem/algorithm/palindromic-ciphers/

t = int(input())
abc = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(t):
    msg = input()
    
    if( msg == msg[::-1] ):
        print('Palindrome')
    else:
        cipher = 1
        for i in msg:
            num = abc.find(i) + 1
            cipher *= num
        print(cipher)