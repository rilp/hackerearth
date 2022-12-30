# Problem title: Breakup App
# URL: https://www.hackerearth.com/problem/algorithm/breakup-app/

n = int(input())

calendar = { x:0 for x in range(1,31)}
for _ in range(n):
    msg = input()
    digits = [int(x) for x in msg.split() if x.isdigit()]
    for d in digits:
        if msg[0] == 'G':
            calendar[d] += 2
        elif msg[0] == 'M':
            calendar[d] += 1

max_value = max(calendar.values())
max_keys = [key for key, val in calendar.items() if val == max_value]

if len(max_keys) != 1 or max_keys[0] not in [19, 20]:
    print('No Date')
else:
    print('Date')