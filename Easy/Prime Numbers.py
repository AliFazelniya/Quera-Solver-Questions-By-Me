# https://quera.org/problemset/293

a = int(input())
b = int(input())

if a > b:
    a, b = b, a

is_prime = [True] * (b + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(b**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, b+1, i):
            is_prime[j] = False

for i in range(a, b + 1):
    if is_prime[i]:
        print(i)
