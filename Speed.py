# Problem title: Speed
# URL: https://www.hackerearth.com/problem/algorithm/speed-7/

t = int(input())
for i in range(t):
    cars = input()
    speeds = list(map(int,input().split()))
    max_speed = float('inf')
    car_count = 0
    for speed in speeds:
        if speed < max_speed:
            car_count += 1
            max_speed = speed
    print(car_count)