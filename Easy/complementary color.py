# https://quera.org/problemset/244098

n = int(input())

for i in range(n):

    hex_string = input().strip("#")

    red_hex_string = hex_string[0:2]
    green_hex_string = hex_string[2:4]
    blue_hex_string = hex_string[4:6]

    red_value = int(red_hex_string, 16)
    green_value = int(green_hex_string, 16)
    blue_value = int(blue_hex_string, 16)    

    complementary_red_value = 255 - red_value
    complementary_green_value = 255 - green_value
    complementary_blue_value = 255 - blue_value

    complementary_hex_string = f"#{complementary_red_value:02X}{complementary_green_value:02X}{complementary_blue_value:02X}"


    print(complementary_hex_string.upper())