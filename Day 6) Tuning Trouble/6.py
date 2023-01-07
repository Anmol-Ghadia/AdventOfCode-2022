# load input
with open(r'Day 6) Tuning Trouble\6_puzzle_input.txt','r') as f:
    data = list(f.read())

def unique(chars):
    # List -> Boolean
    check_list = []
    for i in chars:
        if (i in check_list):
            return False
        check_list.append(i)
    return True

# Part One

last_four = data[:4]
count_1 = 4
for packet in data[4:]:
    if (unique(last_four)):
        break
    else:
        last_four.append(packet)
        last_four.pop(0)
    count_1 += 1

print("Part One:", count_1)

# Part Two

last_fourteen = data[:14]
count_2 = 14
for message in data[14:]:
    if (unique(last_fourteen)):
        break
    else:
        last_fourteen.append(message)
        last_fourteen.pop(0)
    count_2 += 1

print("Part Two:", count_2)