# Problem title: Largest Balanced String
# URL: https://www.hackerearth.com/problem/algorithm/largest-balanced-string-bf93ce85/

t = 1
tests = [('(',')'), ('{','}'), ('[',']')]
for i in range(t):
    a = '[]{}]]]]]]]]]]]]('
    count = 0
    for test in tests:
        c1 = a.count(test[0])
        c2 = a.count(test[1])
        if c1 == c2:
            count += c1 * 2
        else:
            count += min(c1, c2) * 2 
    print(count)