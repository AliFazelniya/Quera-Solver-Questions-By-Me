# https://quera.org/problemset/3414

m_v, m_h, b_v, b_h = map(int, input().split())

if m_v == b_v:

    print("Vertical")

elif m_h == b_h:

    print("Horizontal")

else:
    
    print("Try again")