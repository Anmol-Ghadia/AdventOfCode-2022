# load input
with open(r'Day 3) Rucksack Reorganization\3_puzzle_input.txt','r') as f:
    data = f.read().split('\n')

# Part one
# this is O(n^2) but we could have 
total = 0
for item in data:
    mid = int(len(item)/2)
    first_list = item[:mid]
    second_list = item[mid:]
    for ele in first_list:
        if (ele in second_list):
            if (ele.islower()):
                total += ord(ele) - 96
            else:
                total += ord(ele) - 38
            break
    
print('Part One:', total)