# Problem title: Maximum Sum
# URL: https://www.hackerearth.com/problem/algorithm/maximum-sum-4-f8d12458/

n = input()
nums = list( map(int, input().split()) )
positives = [i for i in nums if i >= 0]
if len(positives) != 0:
    print( sum(positives), len(positives) )
else:
    print( max(nums), 1 )
