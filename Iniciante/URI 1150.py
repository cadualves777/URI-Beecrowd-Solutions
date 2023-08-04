x = int(input())
y = int(input())

while x >= y:
    y = int(input())

c = 1
tot = x

while tot < y:
    x += 1
    tot += x
    c += 1
print(c)
