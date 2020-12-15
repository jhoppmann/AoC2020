import datetime

with open('input.txt') as file:
    input_text = file.read().splitlines()[0]

numbers = [int(x) for x in input_text.split(',')]
previous_nums = {}
for pos, number in enumerate(numbers):
    previous_nums[number] = (1, pos + 1, pos+1)
target = 30_000_000

for i in range(len(numbers)-1, target):
    if i % 10000 == 0:
        print(i)
    old_number = numbers[len(numbers) - 1]
    if old_number in previous_nums and previous_nums[old_number][0] == 1:
        numbers.append(0)
        previous_nums[0] = (previous_nums[0][0] + 1, i + 2, previous_nums[0][1])
    else:
        current_index = i + 2
        new_number = previous_nums[old_number][1] - previous_nums[old_number][2]
        if new_number not in previous_nums:
            previous_nums[new_number] = (0, 0, 0)
        previous_nums[new_number] = (previous_nums[new_number][0] + 1, current_index, previous_nums[new_number][1])
        numbers.append(new_number)
print(numbers[:10])
print(numbers[target - 1])