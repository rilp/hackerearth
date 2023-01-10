# Problem title: Finding Vaccines
# URL: https://www.hackerearth.com/problem/algorithm/find-the-vaccine-a60e06ee/

vaccines_no = int(input())
input()
virus = list(input())
virus_guanine = virus.count('G')
virus_cytosine = virus.count('C')

best = 0
best_interaction = 0
for i in range(1, vaccines_no + 1):
    input()
    vaccine = list(input())
    vaccine_guanine = vaccine.count('G')
    vaccine_cytosine = vaccine.count('C')
    if virus_guanine * vaccine_cytosine + virus_cytosine * vaccine_guanine > best_interaction:
        best_interaction = virus_guanine * vaccine_cytosine + virus_cytosine * vaccine_guanine
        best = i

print(best)