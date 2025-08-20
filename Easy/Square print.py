# https://quera.org/problemset/591

n = int(input())

print("*" * n)

for j in range(n - 2):
    for i in range(n):
        if i == 0:
            print("*", end="")
        elif i == n - 1:
            print("*")
        else:
            print(" ", end="")

print("*" * n)