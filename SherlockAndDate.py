# Problem title: Sherlock and Date
# URL: https://www.hackerearth.com/problem/algorithm/sherlock-and-date/

from datetime import datetime, timedelta

t = int(input())
for _ in range(t):
    d = datetime.strptime(input(), '%d %B %Y') - timedelta(days=1)
    print( str( d.strftime('%e %B %Y') ).lstrip() )