# Problem title: Sorted String
# URL: https://www.hackerearth.com/problem/algorithm/sorted-string/

t = int(input())
for i in range(t):
    s = input()
    uniques = set(s)
    d = {}
    # Move the string elements into a dictionary with the keys as the char counts
    for u in uniques:
        try:
            if d[s.count(u)]:
                d[s.count(u)].append(u)
        except KeyError:
            d[s.count(u)] = []
            d[s.count(u)].append(u)

    sorted_keys = sorted(list(d.keys())) # Sort keys to loop from the lowest
    for key in sorted_keys:
        d[key] = sorted(d[key])
        for val in d[key]:
            print(val * key, end='')
    print()
