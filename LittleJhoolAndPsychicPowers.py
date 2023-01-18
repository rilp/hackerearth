# Problme title: Little Jhool and psychic powers
# URL: https://www.hackerearth.com/problem/algorithm/psychic-powers/

s = input()
if s.find('111111') == -1 and s.find('000000') == -1:
    print('Good luck!')
else:
    print('Sorry, sorry!')