# Problem title: Little Jhool and his breakup
# URL: https://www.hackerearth.com/problem/algorithm/little-jhool-and-his-breakup/

s = input()
love = ['l','o','v','e']
for c in love:
    index = s.find(c)

    if index == -1:
        print('Let us breakup!')
        quit()
    s = s[index:]

print('I love you, too!')