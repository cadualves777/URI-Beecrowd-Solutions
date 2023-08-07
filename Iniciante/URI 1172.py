nums = []
for i in range(10):
    nums.append(int(input()))
    if nums[i] <= 0:
        nums[i] = 1
    print(f'X[{i}] = {nums[i]}')
