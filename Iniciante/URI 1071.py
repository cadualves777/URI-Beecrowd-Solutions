x = int(input())
y = int(input())
nums = []
tot = 0
if x > y:
    x, y = y, x
for i in range(x+1, y):
    if not i % 2 == 0:
        nums.append(i)
for n in nums:
    tot += n
print(tot)
