nums = []
for i in range(100):
    nums.append(float(input()))
    if nums[i] <= 10:
        print(f'A[{i}] = {nums[i]:.1f}')
