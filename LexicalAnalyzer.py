# Problem title: Lexical Analyzer
# URL: https://www.hackerearth.com/problem/algorithm/lexical-analyzer-3/

n = int(input())

vars = set()
for _ in range(n):
    line = input()
    if '=' in line:
        vars.add( line[0:line.index('=')] )
print(len(vars))