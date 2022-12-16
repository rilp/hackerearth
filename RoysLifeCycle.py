# Problem title: Roy's Life Cycle
# URL: https://www.hackerearth.com/problem/algorithm/roys-life-cycle/

n = int(input())

year = ''
count = 0
max_len = 0
for x in range(n):
    day = input()
    year += day     # Concatenates the 'days' in a single 'year' string
    
    pointers = [0,0]
    prev = ''
    # Loop through the 'day' to find the max occurrences per day
    for minute in day:
        # If the current minute starts a new coding cycle the count is reset
        if minute == 'C' and prev != 'C':
            count = 1
        # else if the coding continues a minutes is added to the count
        elif minute == 'C':
            count += 1
        
        if count >= max_len:
            max_len = count
        prev = minute

print(max_len, end=' ')

prev = ''
count = 0
max_len = 0
# Loop through the 'year' to find the max coding occurrences
for x in year:
    # If the current minute starts a new coding cycle the count is reset
    if x == 'C' and prev != 'C':
        count = 1
    # else if the coding continues a minutes is added to the count
    elif x == 'C':
        count += 1
        
    if count >= max_len:
        max_len = count
    prev = x

print(max_len)
