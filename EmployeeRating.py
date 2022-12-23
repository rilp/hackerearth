# Problem title: Employee rating
# URL: https://www.hackerearth.com/problem/algorithm/employee-rating-8cd8dc10/

def solve (N, workload):
    prev = 0
    count = 0
    max_count = 0
    for current in workload:
        if current > 6 and prev > 6:
            count += 1
        elif current > 6 and prev <= 6:
            count = 1
        
        if count > max_count:
            max_count = count
        prev = current
    return max_count
    pass

N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print (out_)