
# Part 1
with open('Day 1) Calorie Counting\puzzle_input.txt','r') as f:
    data = f.read().split('\n')

elf_calories = []
current_elf = 0
for i in data:
    if (i == ''):
        elf_calories.append(current_elf)
        current_elf = 0
        continue
    current_elf += int(i)
print('Part 1:', max(elf_calories))


# Part 2
elf_calories.sort()
total_3 = 0
for i in elf_calories[-3:]:
    total_3 += i
print('Part 2:', total_3)