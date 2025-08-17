# https://quera.org/problemset/271649

n = int(input())

sum = 0
for i in range(n):
    if i % 2 != 0:
        sum += i

print(sum)