# load input
with open(r'Day 3) Rucksack Reorganization\3_puzzle_input.txt','r') as f:
    data = f.read().split('\n')

# Part One
total_1 = 0
for item in data:
    mid = int(len(item)/2)
    first_list = item[:mid]
    second_list = item[mid:]
    for ele in first_list:
        if (ele in second_list):
            if (ele.islower()):
                total_1 += ord(ele) - 96
            else:
                total_1 += ord(ele) - 38
            break

print('Part One:', total_1)

# Part Two

def common(grp):
    # grp: list with 3 lists, each with 1 string
    l1,l2,l3 = grp
    for item in l1:
        if (item in l2 and item in l3):
            if (item.islower()):
                return ord(item) - 96
            else:
                return ord(item) - 38
            

total_2 = 0
skip_count = 2
current_group = []
for rs in data:
    if skip_count == 0:
        # end of group, start new group
        # and add to total
        current_group.append(rs)
        total_2 += common(current_group)
        current_group = []
        skip_count = 2
    else:
        current_group.append(rs)
        skip_count -= 1

print('Part Two:', total_2)