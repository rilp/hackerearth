# Problme title: The best Internet Browser
# URL: https://www.hackerearth.com/problem/algorithm/the-best-internet-browser-3/

vowels = {'a', 'e', 'i', 'o', 'u'}

for _ in range(int(input())):
    url = input()
    best_url = url[4:-4]
    for vowel in vowels:
        best_url = best_url.replace(vowel, '')
    
    print( f'{len(best_url)}/{len(url)}' )