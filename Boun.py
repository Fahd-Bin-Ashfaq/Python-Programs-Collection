
input_nums = input("Enter integers separated by space: ")
nums = list(map(int, input_nums.split()))
nums.sort()

max_length = 1
current_length = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        current_length += 1
    elif nums[i] != nums[i - 1]:
        max_length = max(max_length, current_length)
        current_length = 1

max_length = max(max_length, current_length)

print("Longest consecutive sequence length:", max_length)
