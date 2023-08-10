s, t, f = map(int, input().split())
h_final = s + t + f
if h_final >= 24:
    h_final -= 24
elif h_final < 0:
    h_final += 24
print(h_final)
