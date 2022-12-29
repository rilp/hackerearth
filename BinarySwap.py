# Problem title: Binary Swap
# URL: https://www.hackerearth.com/problem/algorithm/binary-swap-b91d9bef/

s1=input()
s2=input()

dc = { '0':0, '1':0 }
for i in range(0,len(s1)):
   if s1[i] != s2[i]:
       dc[ s2[i] ] += 1

if (dc['0'] == dc['1']):
   print(dc['0'])
else:
   print(-1)
