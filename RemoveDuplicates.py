# Problem title: Remove Duplicates
# URL: https://www.hackerearth.com/problem/algorithm/remove-duplicates-3/

string = input()
uniques = []
for s in string:
    if s not in uniques:
        uniques.append(s)

print(''.join(uniques))