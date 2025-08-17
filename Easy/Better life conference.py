# https://quera.org/problemset/10325

c , r = map(int, input().split())

if r > 10:

    direction = "Left"
    print(direction, end=" ")

else:

    direction = "Right"
    print(direction, end=" ")

print(10 - c+1, end=" ")

if direction == "Left":

    print(20 - r + 1)

else:

    print(r)